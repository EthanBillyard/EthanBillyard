#allows use of time functions
import time

#Explains purpose of the program
print("--This program will gather your sleep data, and suggest corrections to your sleep schedule.--")
print("-Sleep debt occurs when you sleep fewer hours than your body needs. Doctors recommend that an adult should sleep 8 hours per night.-\n")

#Asks the user for their first and last name
#If user input isn't alphabetical then it asks to input again, before asking for next input
firstName = input("Enter your first name: ")
while firstName.isalpha() < 1:
    firstName = input("Enter your first name (only use alphabet): ")

lastName = input("Enter your last name: ")
while lastName.isalpha() < 1:
    lastName = input("Enter your last name (only use alphabet): ")

#Asks user to input age
userAge = input("Enter your age: ")
#Use isnumeric to check if input is a whole number
#Allows user to re-enter data until a whole number is entered using while loop
while userAge.isnumeric() < 1:
    userAge = input("Enter your age (using whole numbers): ")

#Creates a list storing the seven days of sleep data
#Asks user for amount of sleep each day and adds it to the list
sleepList = []
for day in range (0,7):
    dayCount = day + 1
    #.format(dayCount) allows the program to ask how much sleep for the specific day without multiple input statements
    #will create an error if user enters non-numeric answer, solution not covered in class yet
    sleepPerDay = (float(input("How much sleep did you get on day {}: ".format(dayCount)))) 
    sleepList.append(sleepPerDay)

#Calculates sleep debt for each day and display it
#Uses a loop to calculate all 7 values and store in a new list
sleepDebtList = []
for day in range (0,7):
    dayCount = day + 1
    sleepDebt = sleepList[day] - 8
    sleepDebtList.append(sleepDebt)
    print("Sleep debt for day {}: %.1f".format(dayCount) % sleepDebtList[day])  #Formatted output to only show one decimal point
    time.sleep(0.5)                                                             #pauses for a bit to let user read results easier

#Initialize variable
totalSleepDebt = 0
#Add sleep debt to total for each day
for day in range (0,7):
    totalSleepDebt = totalSleepDebt + sleepDebtList[day]
#Calculates the average per day from total
averageSleepDebt = totalSleepDebt / 7

#Print the report
print("\n\n---YOUR SLEEP DEBT REPORT---")
time.sleep(0.5)

#Print todays date
from datetime import date
today = date.today()
print("Date:", today)
time.sleep(0.5)

#Print the full name of the user
print("Name:",firstName, lastName)
time.sleep(0.5)
#Print the age of the user
print("Age: ",userAge)
time.sleep(0.5)

print("\nYour sleep correction suggestion:")
time.sleep(0.5)
#Triggers event if user need more sleep
    #Suggests user sleeps more
if averageSleepDebt < -0.1:
    print("You should sleep more")
    #Formats value to be positive and one decimal point
    print("Adjust sleep by %.1f" % (averageSleepDebt * (-1)),"hours")
#Triggers event if user needs less sleep
    #Suggests user sleeps less
elif averageSleepDebt > 0.1:
    print("You should sleep less")
    print("Adjust sleep by %.1f" % averageSleepDebt,"hours")
#Acknowledge if they already have a good sleeping habit
else:
    print("Your sleep habits are excellent")    

time.sleep(2)
print("\n\nThank you for using this sleep debt calulator.")