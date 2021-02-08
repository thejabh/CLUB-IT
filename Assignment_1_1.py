 #program to find if the given age is eligible to vote

age=int(input("Enter your age:"))
if age<18:
    print("Not Eligible for vote wait for {} years.".format(18-age))
else:
    print("Eligible to vote!")