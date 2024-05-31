def calculate_masses(ratios, total_mass, molar_masses):
    total_molar_mass = sum(ratios[element] * molar_masses[element] for element in ratios)
    
    masses = {}
    for element in ratios:
        element_mass_fraction = (ratios[element] * molar_masses[element]) / total_molar_mass
        masses[element] = element_mass_fraction * total_mass
    return masses
