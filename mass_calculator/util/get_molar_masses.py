import csv

def read_molar_masses(filename):
    molar_masses = {}
    with open(filename, mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            element, molar_mass = row
            molar_masses[element.strip()] = float(molar_mass.strip())
    return molar_masses
