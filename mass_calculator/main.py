import click
import os
from util import get_molar_masses, formula_parser, mass_calculator
import util.batch_processing as bp

def list_files_by_extension(extension):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return [f for f in os.listdir(current_directory) if f.endswith(extension)]

def finish_calculation():
    choice = click.prompt("Do you want to finish the calculation? (Y/N)", type=str).strip().lower()
    return choice == 'y'

@click.command()
@click.option('--filename', default='Periodic Table of Elements.csv', help='CSV file containing element molar masses.')
def main(filename):
    while True:
        click.echo("Choose an input method:")
        click.echo("1. Enter the chemical formula")
        click.echo("2. Paste column of text with formulas")
        click.echo("3. Read from txt file with formulas")
        click.echo("4. Read from Excel file with formulas")

        choice = click.prompt("Enter your choice", type=int)

        if choice == 1:
            formula = click.prompt("Enter the chemical formula of the mixture", type=str)
            total_mass = click.prompt("Enter the total mass of the mixture in grams", type=float)

            ratios = formula_parser.get_parsed_formula(formula)
            molar_masses = get_molar_masses.read_molar_masses(filename)
            masses = mass_calculator.calculate_masses(ratios, total_mass, molar_masses)

            click.echo("Element masses:")
            for element, mass in masses.items():
                click.echo(f"{element}: {mass:.4f} g")

        elif choice == 2:
            formulas = bp.read_formulas_from_text()
            bp.process_formulas(formulas, filename)

        elif choice == 3:
            txt_files = list_files_by_extension('.txt')
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
            bp.process_formulas(formulas, filename)

        elif choice == 4:
            xlsx_files = list_files_by_extension('.xlsx')
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
            bp.process_formulas(formulas, filename)

        else:
            click.echo("Invalid choice. Please restart the program and choose a valid option.")
            continue

        if finish_calculation():
            break

if __name__ == '__main__':
    main()
