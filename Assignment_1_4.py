#program to find if sum of the first 2 numbers and multiplied by the 3rd number is greater than 100
num1,num2,num3=map(int,input("Enter the 3 numbers(given space between them): ").split())
res=(num1+num2)*num3
if (res >100):
    print("Great than 100")
elif res==100:
    print("The result is equal to 100")
else:
    print("Less than 100")