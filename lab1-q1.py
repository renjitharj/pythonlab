from datetime import date
name=input("enter name")
age=int(input("enter age"))
today=date.today()
dob=today.year-age
year=dob+100

print("Hello "+name)
print("You will turn 100 on" ,year) 