#Interactive Molarity Calculator

#Required Inputs

molecular_mass = float(input ("Enter molecular mass of compound (g/mol):"))

volume_ml = float(input("Enter the volume of the solution you want to create (mL):"))

concentration = float(input("Enter the desired concentration (M):"))

#Convert mL to L for the following formula

volume_l = volume_ml / 1000 

#Formula to calculate mass(g)

mass = concentration * volume_l * molecular_mass 

#Display the result

print ("Based on molecular mass:", molecular_mass, "g/mol and the desired concentration of", concentration, "M in a volume of", volume_l, "L, the mass of compound required is:", mass, "g")
