# num = int(input("inter your num:"))
# if num >0:
#     print("Number is positive")
# elif num < 0 :
#     print("Number is negative")
# else :
#     print("Number is zero")

# name = input("inter your name:")
# print (f"HELLO {name}, how are you today")
# print ("HELLO" + name)
# friends = ["ALI", "mohamed", "same", "lolo"]
# print(friends[0])
# friends.sort()
# friends.append("BILAL")
# friends.sort()
# print (friends)
# dic_friends = {"key01":"ahmad","key02":"fater"}
# print (dic_friends("key01"))
# for i in friends[3]:
#     print (i)
name = input("inter your name: ")
year  = int(input("inter your age: "))
weight= int(input("inter your weight in Kg: "))
height= int(input("inter your height in Cm: "))/100
# age = 2021-
person= (f"your name is {name},and age is {2021-year}")
calc = weight/(height*height)
print(format(calc, ".2f"))
if (calc < 18.5 and calc > 0):
    {print ( f" {person} you are Underweight")}
elif(calc > 18.5 and calc < 24.9):
    {print (f" {person} you are Normal weight ")}
elif(calc > 25 and calc < 29.9):
    {print (f" {person} you are Overweight")}
else:
    {print (f" {person} you are Obesity ")}
# print(person)
# print (calc)

