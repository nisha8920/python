print("----------welcome to python------------")
print("hello world")
############Conditional Statements#############
print("Conditional statements are used for decision making")
print("----------if Statement-----")
"""Syntax
if condition:     statement """
print("----Example----")
age = 20
if age >= 18:
    print("Eligible for Voting")
"""Syntax 
if condition:     statement else:     statement Example """
age = 15
if age >= 18:
      print("Adult")
else:
       print("Minor")
#############if-elif-else Statement Used for multiple conditions###########
print("------if-elif-else Statement Used for multiple conditions.-------")
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
 print("Grade C") 

print("-----------Nested if------------")
age = 25
if age >= 18:
    if age <= 60:
        print("Working Age")

print("----------Ternary Operator-----------")
age = 20
result = "Adult" \
    if age >= 18 else "Minor"
print(result)

