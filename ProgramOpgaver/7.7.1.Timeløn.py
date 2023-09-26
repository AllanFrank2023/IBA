#Many companies pay time-and-a-half for any hours worked above 40 in a given week. 
#Write a program to input the number of hours worked 
#and the hourly rate and calculate the total wages for the week.

#TimeSkema

print("Velkommen til dit ugen time-beregner")

timer = float(input("Indtast timeantal :  "))
timeLøn = float(input("Indtast din timeløn: "))

if timer > 40.0:
    overtid = timer - 40
    overtidsløn = (overtid * (1.5 * timeLøn))
    løn = timeLøn * 40
    print("Din overtid er:", overtid, " udbetaling af overtid i denne uge er (timeløn 300kr) ", overtidsløn, "din alm løn: ", løn, "I alt:", (løn + overtidsløn))
else: 
        print("Du har ingen overtid i denne her uge")



