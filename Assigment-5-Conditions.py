# assignment No 5 

# Using conditional statements, check if the number is:
#  1- Even or Odd.
#  2- Positive, Negative, or Zero.
#  3- Whether it is divisible by both 2 and 3 or anyone of them or not divisible by both check all the cases and print statement for each case.
#  4- Take the user age.
#   -- If the age is 18 or above:
#   -- Ask if they have a nationality of "Pakistani".
#     ---If yes, print "You are eligible to vote."
#     ---If no, print "Please obtain a valid ID to vote."
#  5- Write a program that takes the age of a person as input and determines whether they are a child (0-12 years), teenager (13-19 years), adult (20-59 years), or senior citizen (60 years and above)
#  6- Enter a month (as a number between 1 and 12). Print the number of days in that month. Assume a non-leap year.
#  7- Check if a year is a leap year or not.

print("1- Even or Odd.")

def evenOdd(num1):
    if num1 % 2 == 0:
        return f"{num1} is Even"
    else:
        return f"{num1} is Odd"

try:
    num1 = int(input("Enter a number: "))
    result = evenOdd(num1)
    print(result)
except ValueError:
    print("Please enter a valid Number.")


print("2- Positive, Negative, or Zero.")

def check_num(num1):
    if num1 > 0:
        return f"{num1} is Positive"
    elif num1 < 0:
        return f"{num1} is Negative"
    else:
        return f"{num1} is Zero"

try:
    num = float(input("Enter a number: "))
    result = check_num(num)
    print(result)
except ValueError:
    print("Please enter a valid number.")

print("3- Whether it is divisible by both 2 and 3 or anyone of them or not divisible by both check all the cases and print statement for each case.")
def check_divisibility(number):
    if number % 2 == 0 and number % 3 == 0:
        return f"{number} is divisible by both 2 and 3."
    elif number % 2 == 0:
        return f"{number} is divisible by 2 but not by 3."
    elif number % 3 == 0:
        return f"{number} is divisible by 3 but not by 2."
    else:
        return f"{number} is not divisible by either 2 or 3."

try:
    num = int(input("Enter a number: "))
    result = check_divisibility(num)
    print(result)
except ValueError:
    print("Please enter a valid integer.")

print("""
4- Take the user age.
#   -- If the age is 18 or above:
#   -- Ask if they have a nationality of "Pakistani".
#     ---If yes, print "You are eligible to vote."
#     ---If no, print "Please obtain a valid ID to vote." """) 

def check_voting_eligibility(age, nationality):
    if age >= 18:
        if nationality.lower() == "pakistani":
            return "You are eligible to vote."
        else:
            return "Please obtain a valid ID to vote."
    else:
        return "You are not eligible to vote yet."


try:
    age = int(input("Enter your age: "))
    
    if age >= 18:
        nationality = input("Do you have Pakistani nationality? (Y/N): ").strip().lower()
        if nationality == "y":
            print("You are eligible to vote.")
        else:
            print("Please obtain a valid ID to vote.")
    else:
        print("You are not eligible to vote yet.")
except ValueError:
    print("Please enter a valid age.")    

print("Write a program that takes the age of a person as input and determines whether they are a child (0-12 years), teenager (13-19 years), adult (20-59 years), or senior citizen (60 years and above)")

def categorize_age(age):
    if 0 <= age <= 12:
        return "You are a Child."
    elif 13 <= age <= 19:
        return "You are a Teenager."
    elif 20 <= age <= 59:
        return "You are an Adult."
    elif age >= 60:
        return "You are a Senior Citizen."
    else:
        return "Invalid age entered."

try:
    age = int(input("Enter your age: "))
    result = categorize_age(age)
    print(result)
except ValueError:
    print("Please enter a valid number.")   

print("6- Enter a month (as a number between 1 and 12). Print the number of days in that month. Assume a non-leap year.")   

def days_in_month(x):
    monthname ="January","February","March","April","May","june","July","Aug","September","October","Novemver","December"
    if x == 2:        
        return (f"{monthname[x-1]} hax 29 Days")
    elif x in [4, 6, 9, 11]:
        return (f"{monthname[x-1]} has 30 days.")
    elif x in [1, 3, 5, 7, 8, 10, 12]:
        return (f"{monthname[x-1]} has 31 days.")
    else:
        return "Invalid month. Please enter a number between 1 and 12."

try:
    month = int(input("Enter the month as a number (1-12): "))
    result = days_in_month(month)
    print(result)
except ValueError:
    print("Please enter a valid number between 1 and 12.")

print("7- Check if a year is a leap year or not.")

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a leap year."
    else:
        return f"{year} is not a leap year."

# Input from user
year = int(input("Enter a year: "))
print(is_leap_year(year))   