from math import pi, degrees, asin, cos, sqrt, radians

def cosd(angle):

    return cos(radians(angle))

permeability_free_space = 4e-7*pi
permittivity_free_space = 8.854e-12
permittivity_medium_1 = 1
permittivity_medium_2 = 8

transmitted_angle = degrees(asin(1/sqrt(permittivity_medium_2)))
incident_angle = list(range(0,90))

perpendicular_reflectivity = pow(   \
                                 ((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_2))*cosd(45))-     \
                                 (sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_1))*cosd(transmitted_angle)))/   \
                                 ((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_2))*cosd(45))+   \
                                 (sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_1))*cosd(transmitted_angle)))
                                 ,2)

print('TE R: ',perpendicular_reflectivity)

perpendicular_transmissivity = pow(
                                   ((2*(sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_2))*cosd(45)))/     \
                                   (((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_2))*cosd(45)))+     \
                                   ((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_1))*cosd(transmitted_angle))))),2)*  \
                               ((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_1))*cosd(transmitted_angle)))/     \
                               ((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_2))*cosd(45)))

print('TE T: ', perpendicular_transmissivity)

parallel_reflectivity = pow(   \
                                 ((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_2))*cosd(transmitted_angle))-     \
                                 (sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_1))*cosd(45)))/   \
                                 ((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_2))*cosd(transmitted_angle))+   \
                                 (sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_1))*cosd(45)))
                                 ,2)

print('TM R: ',parallel_reflectivity)

parallel_transmissivity = pow(
                                   ((2*(sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_2))*cosd(45)))/     \
                                   (((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_2))*cosd(transmitted_angle)))+     \
                                   ((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_1))*cosd(45))))),2)*  \
                               ((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_1))*cosd(transmitted_angle)))/     \
                               ((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_2))*cosd(45)))

print('TM T: ', parallel_transmissivity)