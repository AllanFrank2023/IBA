#The days of the year are 
# often numbered from 1 through 365 (or 366). This number can be computed in three steps using int arithmetic:
#(a)dayNum= 31(month- 1)+day
#(b) if the month is after February subtract (4(month) + 23)//10
#(c) if it's a leap year and after February 29, add 1
#Write a program that accepts a date as month/day/year, verifies that it is a valid date 
# (see previous problem), and then calculates the corresponding day number.

#Dato verificering

date_input = input("Indtast måned/dag/år (ex 5/15/2023): ")
# Splitter input op i måned, dag og år
month, day, year = map(int, date_input.split('/'))

# Dage antal over 28 (ikke skudår)
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #[3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]

#Skudår
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) and month > 2:
    skuddag = 1
    print(year, "er skudår.")
    
else:
    print( year, "er ikke skudår.")
    skuddag = 0

# Valider input
if month < 1 or month > 12 or day < 1 or day > days_in_month[month - 1] or year < 1:
    print("Ikke gyldig format -  Prøv venligst igen.")
else:


     # Beregner dagen
    ########fejl
    day_num = (28 * (month -1)) + day 
    for i in range(month - 1):
     #day_num += days_in_month[i]
     #day_num = days_in_month(month)
     day_num = day_num + skuddag + day
    
    #Beregner Opgave B
if month > 3:
    day_num2 = day_num - ((4 * (month) + 23)//10)
else:
        print("Opgave B : ", day_num)
    # Display the result
print("#########################")
print("Spørgsmål A & C : Dagen er nummer:", day_num)
print("Skudag er lagt til: ", skuddag)
print("Opgave B løsning:", day_num2)
   
#############################################
