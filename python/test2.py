import sys

try:
    opration = input("inter you opration: ")
    num1 = int(input("inter your 1st mun: "))
    num2 = int(input("inter your 2nd mun: "))
except ValueError:
    print("inter anumber ")
    sys.exit(1)

# print (f" your result is {num1+opration+num2s}")
# def sum (num1,num2):
#     return = num1+num2

# def min (num1,num2):
#     return num1-num2
    

# def mult (num1,num2):
#     return num1*num2

    
# def dev (num1,num2):
#     return num1/num2 
#     num1 > 0 and num2 > 0
if (opration == "+"):
    result = num1+num2
    print(f"your result is: {result}")
    
elif (opration == "-"):
    result = num1-num2
    print(f"your result is: {result}"  )
            
elif (opration == "*"):
    result = num1*num2
    print(f"your result is: {result}" )

elif  (opration == "/"):
    try:
        result = num1/num2
        print(f"your result is:{result} " )
    except ZeroDivisionError:
        print("you cant divine on zero")
else:
    print("inter valied opration")
# except:
#     print("you have to insert number")
# try if (opration == "+"):
#         result = num1+num2
#         print(f"your result is: {result}")
#     print("your result is good")
    
# except:
#     print("An exception occurred")

