#The speeding ticket fine policy in Podunksville is $50 plus $5 for each mph over the limit plus a penalty of $200
# for any speed over 90 mph. Write a program that accepts a speed limit and a clocked speed and either prints a message 
# indicating the speed was legal or prints the amount of the fine, if the speed is illegal.

#Din fartbøde generator

fart = int(input("Indtast din hastighed: "))

if fart > 90 :
    forseelse = (fart - 90) * 5
    bøde = forseelse + 200
    print("Din bøde for at køre ", fart, "er:", bøde)
else:
    print("Du har ikke kørt for stærkt")