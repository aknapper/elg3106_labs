from math import pi, degrees, asin, cos, sqrt, radians
import matplotlib.pyplot as plt
import csv

def cosd(angle):
    return cos(radians(angle))

permeability_free_space = 4e-7*pi
permittivity_free_space = 8.854e-12
permittivity_medium_1 = 1
permittivity_medium_2 = 8

transmitted_angle = degrees(asin(1/sqrt(permittivity_medium_2)))
incident_angle = list(range(0,91))

def perpendicular_reflectivity(x):
    return pow(   \
               ((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_2))*cosd(x))-     \
               (sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_1))*cosd(transmitted_angle)))/   \
               ((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_2))*cosd(x))+   \
               (sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_1))*cosd(transmitted_angle)))
              ,2)

def perpendicular_transmissivity(x):
    return pow(
               ((2*(sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_2))*cosd(x)))/     \
               (((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_2))*cosd(x)))+     \
               ((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_1))*cosd(transmitted_angle))))),2)*  \
           ((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_1))*cosd(transmitted_angle)))/     \
           ((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_2))*cosd(x)))

def parallel_reflectivity(x):
    return pow(   \
               ((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_2))*cosd(transmitted_angle))-     \
               (sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_1))*cosd(x)))/   \
               ((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_2))*cosd(transmitted_angle))+   \
               (sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_1))*cosd(x)))
              ,2)

def parallel_transmissivity(x):
    return pow(
               ((2*(sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_2))*cosd(x)))/     \
               (((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_2))*cosd(transmitted_angle)))+     \
               ((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_1))*cosd(x))))),2)*  \
            ((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_1))*cosd(transmitted_angle)))/     \
            ((sqrt(permeability_free_space/(permittivity_free_space*permittivity_medium_2))*cosd(x)))

te_reflect_incident = []
te_transmissivity_incident = []
tm_reflectivity_incident = []
tm_transmissivity_incident = []
te_reflectivity = []
te_transmissivity = []
tm_reflectivity = []
tm_transmissivity = []
for angle in incident_angle:
    te_reflectivity.append(perpendicular_reflectivity(angle))
    te_reflect_incident.append([angle,perpendicular_reflectivity(angle)])

    te_transmissivity.append(perpendicular_transmissivity(angle))
    te_transmissivity_incident.append([angle,perpendicular_transmissivity(angle)])

    tm_reflectivity.append(parallel_reflectivity(angle))
    tm_reflectivity_incident.append([angle, parallel_reflectivity(angle)])

    tm_transmissivity.append(parallel_transmissivity(angle))
    tm_transmissivity_incident.append([angle,parallel_transmissivity(angle)])

#generate plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(incident_angle, te_reflectivity, label='TE Reflectivity')
ax.plot(incident_angle, te_transmissivity, label='TE Transmissivity')
ax.plot(incident_angle, tm_reflectivity, label='TM Reflectivity')
ax.plot(incident_angle, tm_transmissivity, label='TM Transmissivity')

ax.set_xlim([0,90])
ax.set_ylim([0,1])

plt.xlabel('Incident Angle (Degrees)')

ax.set_title('Reflectivity and Transmissivity as a function of the Incident Angle')
ax.legend()
plt.show()

# generate table
file = open('table.csv', 'w', newline='\n')

with file:
    write = csv.writer(file)
    #ugly formatting, still needs to write to multiple columns
    write.writerows([angle] for angle in incident_angle)
    write.writerows([value] for value in te_reflectivity)
    write.writerows([value] for value in te_transmissivity)
    write.writerows([value] for value in tm_reflectivity)
    write.writerows([value] for value in tm_transmissivity)