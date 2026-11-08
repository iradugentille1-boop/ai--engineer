print("Hello, AI Engineer!")
print("My name is Gentille")
print("I am learning AI Engineering")
print(10 + 5)
print(20 - 7)
print(4 * 5)
print(20 / 4)
name = "Gentille"
age = 26
country = "Germany"
future_age = age + 5
print(future_age)

print(name)
print(age)
print(country)

print(age + 5)
name = "Gentille"
age = 26
height = 1.65

print(type(name))
print(type(age))
print(type(height))
name = "Gentille"
age = 26
country = "Germany"

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"I live in {country}.")
name = input("What is your name? ")
age = input("How old are you? ")
country = input("which country do you live in? ")
job= input("what job would you like to have in the future? ")

print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"I live in {country}.")
print(f"I want to become {job}.")
age = int(input("How old are you? "))

future_age = age + 5

print(f"In five years, you will be {future_age} years old.")
age = int(input("How old are you? "))
if age < 13:
    print("you are a child.")
elif age >=  13 and age < 18:
    print("you are a teenager.")
else:
    print("you are an adult.")
for number in range(1, 6): 
    print("the numbers from 1 to 5")       
for number in range(5):
    print("I am learning AI Engineering")
number = 2 
while number <= 10 :
    print(number)
    number = number + 2    
languages = ["java", "c++", "Javascript"]   
languages .append("python") 
print(languages)
fruits = ["Apple", "Banana", "Mango", "Orange"]
for fruit in fruits :
    print(f"I like {fruit}")
def calculate_future_age(age):
    return age 
result = calculate_future_age (26)
print (result + 5)
job = {
    "title": "Data Analyst",
    "location": "Frankfurt",
    "salary": 40000
}
job["location"] = "Berlin"
job["remote"] = True
print(job)
applicants = [
    {"name": "Anna", "age": 25, "job": "Warehouse Worker"},
    {"name": "John", "age": 30, "job": "Data Analyst"},
    {"name": "Mary", "age": 22, "job": "Hotel Assistant"}
]

for applicant in applicants :
    if applicant["job"] == "Data Analyst":
       print(applicant["name"])

try:
    first = float(input("Enter first number: "))
    second = float(input("Enter second number: "))

    if second == 0:
        print("You cannot divide by zero.")
    else:
        result = first / second
        print(f"Result: {result}")

except ValueError:
    print("Invalid input. Please enter a valid number.")
