#Write a program to print the lyrics for ten verses of "The Ants Go March­ ing. " A couple of sample verses are given below. You may choose your own activity for the "little one" in each verse, but be sure to choose something that makes the rhyme work (or almost work) .
#The ants go marching one by one, hurrah! hurrah! The ants go marching one by one, hurrah! hurrah! The ants go marching one by one,
#The little one stops to suck his thumb,
#And they all go marching down... In the ground...
#To get out....
#Of the rain.
#Boom! Boom! Boom!
#The ants go marching two by two, hurrah! hurrah! The ants go marching two by two, hurrah! hurrah! The ants go marching two by two,
#The little one stops to tie his shoe,
#And they all go marching down... In the ground...
#To get out...
#Of the rain.
#Boom! Boom! Boom!



def sangen():
    song()
    songP2()
    song()
    songP2() 

    
def song():
    print("The ants go marching one by one, hurrah! hurrah")
    print("The ants go marching one by one, hurrah! hurrah")
    print("The ants go marching one by one, hurrah! hurrah")
    print("The ants go marching one by one.")

def songP2():
    print("The little one stops to suck his thumb,")
    print("And they all go marching down...")
    print("In the ground...")
    print("To get out....")
    print("Of the rain.")
    print("Boom! Boom! Boom!")

def main():
 
# Input the number of songs showed from the user
    n = int(input("Indtast det antal gange sangen skal ses: "))

# Print the requested number of songs with Functions
    for i in range(1, n + 1):
        sangen()
        print("Nummer: ", i)
        print(" ")
main()
       

        
    ######Færdig    


    