# Task 1: Create a Dictionary of Student Marks

dict={'Rahul':'37', 'John':'30', 'Kamal':'46', 'Rohit':'52','Sachin':'28'}
try:
    a=input("Enter the Student's Name: ")
    print(f"{a}'s Number is: ", dict[a])
except KeyError:
    print(f"Student '{a}' not found !")



