#
#
# name = input("What name are you sending letter to?")
# content = ''
# with open("C:/Users/HROlaide/PycharmProjects/day-16-start/day24/inputs/letters/letter.txt") as data:
#     content += data.read()
#     if content.__contains__("[Name]"):
#         content.replace("[Name]", name)
#         print(content)
#     with open("C:/Users/HROlaide/PycharmProjects/day-16-start/day24/output/ready_to_send"+name+".txt", "w") as new_letter:
#         new_file = new_letter.write(content)
#
#     with open("C:/Users/HROlaide/PycharmProjects/day-16-start/day24/inputs/names/names.txt", "w") as new_name:
#         name_add = new_name.write(f"\n{name}")

name = input("What name are you sending the letter to? ")

# Read the base letter template
with open("C:/Users/HROlaide/PycharmProjects/day-16-start/day24/inputs/letters/letter.txt") as letter_file:
    content = letter_file.read()

# Replace [Name] with the actual name
content = content.replace("[Name]", name)

# Print the modified letter for confirmation
print(content)

# Save the new letter into the output folder with a unique filename
output_path = f"C:/Users/HROlaide/PycharmProjects/day-16-start/day24/output/ready_to_send/{name}_letter.txt"
with open(output_path, "w") as new_letter:
    new_letter.write(content)

# Append the name to names.txt (if needed)
with open("C:/Users/HROlaide/PycharmProjects/day-16-start/day24/inputs/names/names.txt", "a") as new_name_file:
    new_name_file.write(f"\n{name}")

print(f"Letter successfully created for {name} at: {output_path}")
