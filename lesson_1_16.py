
with open("applicant.txt", "w") as file:
    file.write("Name: Gentille\n")
    file.write("Job: Al engineer intern\n")
    file.write("Skill: python beginner\n")

print("Applicant information saved!")

with open("applicant.txt", "r") as file:
    information = file.read()

print("Saved applicant information:")
print(information)

