# Conditional Statements (Used to execute a block of code based on a certain condition)


#if Statement (Used to execute a block of code if a certain condition is true)
age = 20
if age >= 18:
    print("You are an adult.")  

    # Note :Indentation is important in Python. Identation is a space at the beginning of a line.


 #-------------------------------------------------------------   

# Else Statement (Used to execute a block of code if the condition is false)

age = 16
if age >= 18:
    print("You can vote.")
else:
    print("You can't vote.")

#-------------------------------------------------------------------    

# Elif Statement (Used to check multiple conditions)

age = 16
if age >= 18:
    print("You can drive.")
elif age >= 14:
    print("You are a teenage but you can learn driving.")
else:
    print("You can't drive.")



# practise get marks and print the grade

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A+")
elif marks >= 80:       
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
elif marks >= 40:
    print("Grade E")   
else:
    print("Grade F") 

