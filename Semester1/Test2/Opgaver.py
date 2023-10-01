
 
def file_oprettelse():
    # navne input fra bruger
    filename = input("Indtast navn på file, som skal oprettes, som følgende: (e.g., example.txt): ")

    # Her oprettes filen i ("w" mode)
    with open(filename, "w") as file:
        print("File", filename, "er oprettet.\n\n")
        valg = input(print("Vil du tilføje indhold til filen? ja eller nej \n"))
        if valg.lower() == "ja":
            print("errer")
            add_indhold_file(filename)
        else:
            print("Test 22222")
#            break



def add_indhold_file():
#
             # Her skrives/tilføjes indholdet i filen
        indholdet = input(print("Tilføj WWWW her indholdet i filen: www \n"))
          # Her tilføjes indholdet fra variablen
        file.write(indholdet)

def count_word_file():
    print("Tæller ord heeer")


def Count_lines_file():
    print("Tæller linier heer")


# def word_count(filename):#
#    try:
#        with open(filename, "r+") as file:
#            lines = file.readlines()
#            num_lines = len(lines)
#            num_words = sum(len(line.split()) for line in lines)
#            num_chars = sum(len(line) for line in lines)#
#
#        print("Antal linier:", num_lines)
#        print("Antal ord:", num_words)
#        print("Antal anslag:", num_chars)
#
#    except FileNotFoundError:
#        print(f"Error: Filen", filename, "er ikke fundet.")
#    except Exception as e:
#        print(f"En exceptions opstået:", str(e))


# def main():
# Input the filename from the user
#    print("Ønsker du at oprette en file og indtaste indhold: y eller n")
#    ny_file = input(print("Ønsker du at oprette en file og indtaste indhold? (Ja/Nej): \n"))
#   if ny_file.lower() != "ja":
#    elif ny_file.lower() != "ja":
#   else
#   break

while True:
    print("\n\n")
    print("Dette program behandler filer\n")
    print("Vælg hvilken operation du vil bruge.\n")
    print("1. Oprette en tekst file og angiv navn")
    print("2. Tilføje indhold til eksisterende file")
    print("3. Tælle ord i file")
    print("4. Tælle linier i file")
    print("5. Afslut\n")

    valg_file = input("Skriv dit valg 1/2/3/4/5: ")
    if valg_file == '5':
        print("Farvel! :D")
        print("Farvel! :D fff")
        break

    if valg_file in ('1', '2', '3', '4', '5'):
        #               try:
        #                       tal1 = int(input("Skriv dit første nummer: "))
        #                       tal2 = int(input("Skriv dit andet nummer: "))

        if valg_file == '1':
            file_oprettelse()
            print("test 1")
        elif valg_file == '2':
            add_indhold_file()
            print("test 2")
        elif valg_file == '3':
            count_word_file
            print("test 3")
        elif valg_file == '4':
            Count_lines_file()
            print("test 4")
#               except ValueError:
#                       print("ugylidt tal, brug kun heltal. prøv igen")
#       else:
#       print("Ugyldigt tal. Vælg imellem 1/2/3/4/5 \n")


# Kalder WC funktionen
# word_count(filename)

# main()
#   word_count(fwc)