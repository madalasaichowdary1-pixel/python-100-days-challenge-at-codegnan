addmin_managment.py
# number of student in the class\
n= int(input("enter numberr of students in the class:"))
present_count = 0
absent_count = 0
for rool_number in range(1,n+1):
    print("enter ", rollno," is present or absent and")
    status = input("enter selcet folliwing option 1or 2 \n 1. present \n 2. absent")
    ststus = input()
    
    # check status
if   status == '1':
        prasent_count += 1
elif status == '2':
        absent_count += 1
else:
        print("please select either 1 or 2 options")
print("totel student in the class:",n)
print("number of student present:", present_count)
print("number of student absent:", absent_count)
percentage = (perrsent_count / n) * 100
print("attendence report:", percentage)




addmin_managment.py
# number of student in the class\
n= int(input("enter numberr of students in the class:"))
present_count = 0
absent_count = 0
rollno = 1 # initilization
while rollno <= n: # condition
    print("enter ", rollno," is present or absent and")
    status = input("enter selcet folliwing option 1or 2 \n 1. present \n 2. absent")
    ststus = input()
    
    # check status
if   status == '1':
        prasent_count += 1
        rollno +=1 # increment
elif status == '2':
         rollno +=1 # increment
         absent_count += 1
else:
        print("please select either 1 or 2 options")
print("totel student in the class:",n)
print("number of student present:", present_count)
print("number of student absent:", absent_count)
percentage = (perrsent_count / n) * 100
print("attendence report:", percentage)
