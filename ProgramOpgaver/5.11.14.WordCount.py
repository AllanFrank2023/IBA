#Word Count. A common utility on UniX/Linux systems is a small program called ''wc." 
# This program analyzes a file to determine the number of lines, words, and characters contained therein. 
# Write your own version of we. The program should accept a file name as input and then
# print three numbers showing the count of lines, words, and characters in the file.
#


def file_oprettelse():
    # navne input fra bruger
    filename = input("Indtast navn på file, som skal oprettes, som følgende: (e.g., example.txt): ")

    # Her oprettes filen i ("w" mode)
    with open(filename, "w") as file:
        print("File", filename, "er oprettet.\n\n")
    valg = input("Vil du tilføje indhold til filen? ja eller nej \n")
    if valg == "ja":
        add_indhold_file()
    else:
            print("Test 22222")
#    break



def add_indhold_file():
        # Spørg brugeren om filnavnet
        filename = input("Indtast filnavn (inklusive sti .txt): ")

        try:
        #Åbn filen i tilføjelses-tilstand ("a" mode) eller opret den, hvis den ikke findes
            with open(filename, "a") as file:
            #Spørg brugeren om tekst, der skal tilføjes
                tekst_at_add = input("Indtast tekst, der skal tilføjes til filen:\n")

                #Tilføj teksten til filen
                file.write(tekst_at_add + "\n")

                print("Tekst er tilføjet til filen ", filename)

        except FileNotFoundError:
                print("Fejl: Filen", filename, "blev ikke fundet.")
        except Exception as e:
                print("En fejl opstod:", str(e))


#def read_file():
    # Åbn filen "example.txt" i læsetilstand ("r" mode)
 #   with open("example.txt", "r") as file:
        # Læs hele indholdet af filen på én gang
 #       file_contents = file.read()

    # Filen lukkes automatisk, når 'with' -blokken er afsluttet

    # Udskriv indholdet
 #1   print(file_contents)


def count_word_file():
    print("Tæller ord heeer")
    filename = input("Indtast filnavn (inklusive sti .txt): ")
    try:
        with open(filename, "r+") as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)#

        print("Antal linier:", num_lines)
        print("Antal ord:", num_words)
        print("Antal anslag:", num_chars)

    except FileNotFoundError:
        print(f"Error: Filen", filename, "er ikke fundet.")
    except Exception as e:
        print(f"En undtagelse opstået:", str(e))


#def Count_lines_file():

#    filename = input("Indtast filnavn (inklusive sti .txt): ")
#    try:
#        with open(filename, "r+") as file:
#            lines = file.readlines()
#            num_lines = len(lines)
#            num_words = sum(len(line.split()) for line in lines)
#            num_chars = sum(len(line) for line in lines)#

#        print("Antal linier:\n", num_lines)
#        print("Antal ord:\n", num_words)
#        print("Antal anslag:\n", num_chars)

#    except FileNotFoundError:
#        print(f"Error: Filen", filename, "er ikke fundet.")
#    except Exception as e:
#        print(f"En undtagelse opstået:", str(e))

def main():

        while True:
            print("\n\n")
            print("Dette program behandler filer\n")
            print("Vælg hvilken operation du vil bruge.\n")
            print("1. Oprette en tekst file og angiv navn")
            print("2. Tilføje indhold til eksisterende file")
            print("3. Tælle ord, linier og anslag i file")
            print("4. Afslut\n")

            valg_file = input("Skriv dit valg 1/2/3/4: ")
            if valg_file == '4':
                print("Farvel! :D")
                break

            if valg_file in ('1', '2', '3', '4'):
              try:
                if valg_file == '1':
                   file_oprettelse()
                   #print("Farvel")
                elif valg_file == '2':
                   add_indhold_file()
                   #print("test 2")
                elif valg_file == '3':
                    count_word_file()
                #print("test 3")

              except ValueError:
                       print("ugylidt tal, brug kun heltal. prøv igen")
            else:
                print("Ugyldigt tal. Vælg imellem 1/2/3/4/5 \n")
main()
########Færdig