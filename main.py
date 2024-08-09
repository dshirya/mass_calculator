import click
import os
from util import get_molar_masses, formula_parser, mass_calculator
import util.batch_processing as bp

def list_files_by_extension(extension, exclude=[]):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return [f for f in os.listdir(current_directory) if f.endswith(extension) and f not in exclude]

def finish_calculation():
    bold_text = "\033[1mDo you want to finish?\033[0m"
    return click.confirm(bold_text, default=True)

@click.command()
@click.option('--filename', default='Periodic Table of Elements.csv', help='CSV file containing element molar masses.')
def main(filename):
    while True:
        click.echo("Choose an input method:")
        click.echo("1. Enter the chemical formula")
        click.echo("2. Paste column of text with formulas")
        click.echo("3. Read from txt file with formulas")
        click.echo("4. Read from Excel file with formulas")
        click.echo("5. Calculate masses based on the known mass of one element")

        choice = click.prompt("Enter your choice", type=int)

        molar_masses = get_molar_masses.read_molar_masses(filename)

        if choice == 1:
            formula = click.prompt("Enter the chemical formula of the mixture (e.g., CdCu4Ho, DyCo2)", type=str)
            try:
                ratios = formula_parser.get_parsed_formula(formula)
                wrong_elements = [element for element in ratios if element not in molar_masses]

                if wrong_elements:
                    click.echo(f"The formula you entered is wrong. Wrong elements: {', '.join(wrong_elements)}")
                else:
                    total_mass = click.prompt("Enter the total mass of the mixture in grams", type=float)
                    masses = mass_calculator.calculate_masses(ratios, total_mass, molar_masses)
                    click.echo("Element masses:")
                    for element, mass in masses.items():
                        click.echo(f"{element}: {mass:.4f} g")
                    click.echo(f"Total mass: {total_mass} g")
            except Exception as e:
                click.echo(f"An error occurred: {e}")

        elif choice == 2:
            formulas = bp.read_formulas_from_text()
            valid_formulas = []

            for formula in formulas:
                try:
                    ratios = formula_parser.get_parsed_formula(formula)
                    wrong_elements = [element for element in ratios if element not in molar_masses]

                    if wrong_elements:
                        click.echo(f"The formula '{formula}' is wrong. Wrong elements: {', '.join(wrong_elements)}")
                    else:
                        valid_formulas.append(formula)
                except Exception as e:
                    click.echo(f"An error occurred while processing '{formula}': {e}")

            if valid_formulas:
                bp.process_formulas(valid_formulas, filename)

        elif choice == 3:
            txt_files = list_files_by_extension('.txt', exclude=['README.txt'])
            if not txt_files:
                click.echo("No .txt files found in the current directory.")
                continue
            
            click.echo("Available .txt files:")
            for i, file in enumerate(txt_files, 1):
                click.echo(f"{i}. {file}")

            file_choice = click.prompt("Choose a .txt file by number", type=int)
            if file_choice < 1 or file_choice > len(txt_files):
                click.echo("Invalid choice.")
                continue
            
            filepath = txt_files[file_choice - 1]
            formulas = bp.read_formulas_from_txt_file(filepath)
            valid_formulas = []

            for formula in formulas:
                try:
                    ratios = formula_parser.get_parsed_formula(formula)
                    wrong_elements = [element for element in ratios if element not in molar_masses]

                    if wrong_elements:
                        click.echo(f"The formula '{formula}' is wrong. Wrong elements: {', '.join(wrong_elements)}")
                    else:
                        valid_formulas.append(formula)
                except Exception as e:
                    click.echo(f"An error occurred while processing '{formula}': {e}")

            if valid_formulas:
                bp.process_formulas(valid_formulas, filename)

        elif choice == 4:
            xlsx_files = list_files_by_extension('.xlsx', exclude=[f"calculated_{n}.xlsx" for n in range(1, 1001)])
            if not xlsx_files:
                click.echo("No .xlsx files found in the current directory.")
                continue
            
            click.echo("Available .xlsx files:")
            for i, file in enumerate(xlsx_files, 1):
                click.echo(f"{i}. {file}")

            file_choice = click.prompt("Choose an .xlsx file by number", type=int)
            if file_choice < 1 or file_choice > len(xlsx_files):
                click.echo("Invalid choice.")
                continue
            
            filepath = xlsx_files[file_choice - 1]
            formulas = bp.read_formulas_from_excel(filepath)
            valid_formulas = []

            for formula in formulas:
                try:
                    ratios = formula_parser.get_parsed_formula(formula)
                    wrong_elements = [element for element in ratios if element not in molar_masses]

                    if wrong_elements:
                        click.echo(f"The formula '{formula}' is wrong. Wrong elements: {', '.join(wrong_elements)}")
                    else:
                        valid_formulas.append(formula)
                except Exception as e:
                    click.echo(f"An error occurred while processing '{formula}': {e}")

            if valid_formulas:
                bp.process_formulas(valid_formulas, filename)

        
        elif choice == 5:
            while True:  # Outer loop to allow changing the element
                known_element = click.prompt("Enter the element with known mass (e.g., Os)", type=str)
                
                while True:  # Inner loop to allow changing the formula or mass
                    formula = click.prompt("Enter the chemical formula of the mixture (e.g., GdOsIn)", type=str)
                    known_mass = click.prompt(f"Enter the known mass of {known_element} in grams", type=float)
    
                    try:
                        ratios = formula_parser.get_parsed_formula(formula)
                        wrong_elements = [element for element in ratios if element not in molar_masses]
    
                        if wrong_elements:
                            click.echo(f"The formula you entered is wrong. Wrong elements: {', '.join(wrong_elements)}")
                        elif known_element not in ratios:
                            click.echo(f"The element '{known_element}' is not present in the formula.")
                        else:
                            masses = mass_calculator.calculate_masses_with_known_element(
                                ratios, known_element, known_mass, molar_masses
                            )
                            click.echo("Element masses:")
                            for element, mass in masses.items():
                                click.echo(f"{element}: {mass:.4f} g")
                            
                    except Exception as e:
                        click.echo(f"An error occurred: {e}")
    
                    # Ask if the user wants to change the formula/mass or continue with a new element
                    if click.confirm("Do you want to change the element or finish?", default=True):
                        break  # Exit inner loop to change element
                        
                # Ask if the user wants to continue with a new element or finish the entire calculation
                if click.confirm("Finish?", default=True):
                    break  # Exit outer loop to finish the process

        else:
            click.echo("Invalid choice. Please restart the program and choose a valid option.")
            continue 
        
        if finish_calculation():
            break

if __name__ == '__main__':
    main()
