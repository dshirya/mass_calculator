import re

def get_parsed_formula(formula):
    pattern = r"([A-Z][a-z]*)(\d*\.?\d*)"
    elements = re.findall(pattern, formula)
    ratios = {}
    for element, coefficient in elements:
        ratio = float(coefficient) if coefficient else 1
        ratios[element] = ratio
    return ratios
