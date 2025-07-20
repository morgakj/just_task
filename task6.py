

# class task on comparism operators
first_number =8
second_number= 90

print(first_number > second_number)

print("__________________________________")
# using if else statement
pass_mark = 45
Tom_exam_score = float(input('total secore='))
if Tom_exam_score > pass_mark:
            print("pass")
else:
    print("fail")
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
# instagram bio data password
password =input("Enter user character")
first_five = password[:5]
last_five = password[-5:]

print(F"the password is :{first_five}")
print(f" the password is :{last_five}")
print(f"the lenth of the password entered is :{len(password)}")

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
#bill program
total_bill= float(input("Enter the total bil\n>>>>"))
friends = float(input("enter the number of friends\n>>"))
total=total_bill / friends
print(f"Each person  would pay :{total:.2f}")

print("*****************************************************")
# movie titile using split method, upper method
movie_title = input(" Enter your favorite movie title\n")
first_word = movie_title.split()[0].upper()
last_word = movie_title.split()[1].title()
print(f"my favorite movie title: {first_word}")
print(f"my last movie word title is:{last_word}")
print(" i have  watch the movie ten times")

print("_&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
step1 = int(input(" enter the number of first step\n"))
step2= int(input("enter the number of second step\n"))
step3 = int(input("enter the number of third steps\n"))
total = step1 + step2 + step3

total_average =total/3
print(f"the total steps is: {total:,.2f}")
print(f"the average is : {total_average:,.2f}")

print("=======================================================")
password = input("enter the your password\n")

first_letter= password[0]
last_letter= password[-1]
length = len(password)
stars = "*" * (length -2)
print(f" the password is:{first_letter}{stars}{last_letter}")
print(f" the lenth of the password is:{length}")


