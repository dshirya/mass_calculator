def calculate_masses(ratios, total_mass, molar_masses):
    total_molar_mass = sum(ratios[element] * molar_masses[element] for element in ratios)
    
    masses = {}
    for element in ratios:
        element_mass_fraction = (ratios[element] * molar_masses[element]) / total_molar_mass
        masses[element] = element_mass_fraction * total_mass
    return masses

def calculate_masses_with_known_element(ratios, known_element, known_mass, molar_masses):
    # Calculate the molar mass of the entire compound
    total_molar_mass = sum(ratios[element] * molar_masses[element] for element in ratios)
    
    # Calculate the molar mass of the known element in the compound
    known_element_molar_mass = ratios[known_element] * molar_masses[known_element]
    
    # Calculate the scaling factor based on the known mass
    scaling_factor = known_mass / known_element_molar_mass
    
    # Calculate the masses of each element based on the scaling factor
    masses = {}
    for element in ratios:
        masses[element] = scaling_factor * ratios[element] * molar_masses[element]
    
    return masses