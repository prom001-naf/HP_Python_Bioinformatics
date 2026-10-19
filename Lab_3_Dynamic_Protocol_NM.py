"""
Instruct user how to prepare a 3 ml solution of
10 mM NaCl and 0.5 mM MgCl2, given stock solutions
of 1 M NaCl and 0.1 M MgCl2.
""" 

from builtins import print


try:
    final_vol = float(input("Please enter the final volume of the solution (ml): "))  # use ml volumes throughout the program
except:
    # Handling the ValueError for non-numeric input
    print("Invalid input. Please enter a numeric value.")
    final_vol = float(input("Please enter the final volume of the solution (ml): "))

# NaCl
nacl_stock = float(input("Please enter the NaCl stock (mM): "))  # use mM concentrations throughout the program
nacl_final = float(input("Please enter the NaCl final (mM): "))  # use mM concentrations throughout the program

try:
    step1 = "Add " + str(final_vol * (nacl_final / nacl_stock)) + " ml NaCl\n"
except:
    # Handling the ZeroDivisionError for zero stock concentration
    print("Invalid input. Stock concentration cannot be zero.")
    nacl_stock = float(input("Please enter the NaCl stock (mM): "))  
    step1 = "Add " + str(final_vol * (nacl_final / nacl_stock)) + " ml NaCl\n"

# MgCl2
mg_stock = float(input("Please enter the MgCl2 stock (mM): "))  # use mM concentrations throughout the program
mg_final = float(input("Please enter the MgCl2 final (mM): "))  # use mM concentrations throughout the program

try:
    step2 = "Add " + str(final_vol * (mg_final / mg_stock)) + " ml MgCl2\n"
except:
    # Handling the ZeroDivisionError for zero stock concentration
    print("Invalid input. Stock concentration cannot be zero.")
    mg_stock = float(input("Please enter the MgCl2 stock (mM): "))  
    step2 = "Add " + str(final_vol * (mg_final / mg_stock)) + " ml MgCl2\n"

# Water
step3 = "Add water to a final volume of " + str(final_vol) + " ml and mix"

# Print protocol
print(step1 + step2 + step3)
