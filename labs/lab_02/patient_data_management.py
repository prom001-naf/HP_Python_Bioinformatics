# Patient Data Management Lab, first creat a list to store the names of four patients: Jane Doe, John Smith, Emily White, and Michael Brown.

patient_list = [
    "Jane Doe", 
    "John Smith", 
    "Emily White", 
    "Michael Brown"
]



# Part 1: Print the name of the second patient in the list
print(patient_list[1])



# Part 2: New patient arrives to the hospital: Sarah Miller. Add her to the end of the list
patient_list.append("Sarah Miller")
print(patient_list)



# Part 3: Third patient's name was misspelled. It should be Williams instead of White. Update the patient's name to reflect the correct one.

patient_list[2] = "Emily Williams"
print(patient_list)



# Part 4: Clinic is merging with another healthcare provider, which means patient records from both institutions must consolidate into a single list:

# Part 4A: Create a new list containing the names Alejandro Ramirez, Chloe Mitchell, Sofia Vargas and Liam Sullivan.

new_patient_list = [
    "Alejandro Ramirez", 
    "Chloe Mitchell", 
    "Sofia Vargas", 
    "Liam Sullivan"
]

print(new_patient_list)

# Part 4B: Combine both patient lists into one and print the new list.

combined_patient_list = patient_list + new_patient_list
print(combined_patient_list)



# Part 5: Modify the script to ask the user for a name, and check if it exists in the list of patients. Output the verification as a boolean value (True or False).

user_name = input("Enter a patient's name to check: ")

is_patient = user_name in combined_patient_list
print(is_patient)



# Part 6: Modify the script to ask the user for multiple patient names (separated by commas) and and index, and then insert the new names into the list, starting at the index/position given by the user.
user_input = input("Enter multiple patient names separated by commas: ")

# Convert entered names into a list
new_names = [name.strip() for name in user_input.split(",")]

# Ask the user for the starting index
index = int(input("Enter the index where you want to insert the new names: "))

# Insert all the new names starting at the given index
combined_patient_list[index:index] = new_names

print(combined_patient_list)