import pandas as pd
from openpyxl import Workbook
from util import get_molar_masses, formula_parser, mass_calculator


def process_formulas(formulas, filename, total_masses=[0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50]):  #change total mass here if needed
    molar_masses = get_molar_masses.read_molar_masses(filename)
    wb = Workbook()
    
    for total_mass in total_masses:
        ws = wb.create_sheet(title=f"{total_mass:.2f}")
        max_elements = max(len(formula_parser.get_parsed_formula(formula)) for formula in formulas)
        headers = ['Formula', 'Total Mass']
        for i in range(max_elements):
            headers.extend([f'Element{i+1}', f'Mass{i+1}'])
        ws.append(headers)
        
        for formula in formulas:
            ratios = formula_parser.get_parsed_formula(formula)
            masses = mass_calculator.calculate_masses(ratios, total_mass, molar_masses)
            row = [formula, total_mass]
            for element, mass in masses.items():
                row.extend([element, mass])
            ws.append(row)
    
    wb.remove(wb['Sheet'])
    wb.save('calculated.xlsx')


def read_formulas_from_text():
    formulas = []
    print("Paste the formulas (one per line), and type 'done' when finished:")
    while True:
        line = input()
        if line.lower() == 'done':
            break
        formulas.append(line.strip())
    return formulas

def read_formulas_from_txt_file(filepath):
    with open(filepath, 'r') as file:
        formulas = [line.strip() for line in file.readlines()]
    return formulas

def read_formulas_from_excel(filepath):
    df = pd.read_excel(filepath, header=None)
    return df[0].tolist()
