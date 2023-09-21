# ExitExceoption
# Heritage: exception
class ExitException(Exception):
    pass


# calculator function
# input :   int_first, integer, the first number for the calculator
#           str_op, string, the operation for the calculator
#           int_second, integer, the second number for the calculator
# output : result from the calculator, NaN for errors
# exception :  division by zero
def calculator(int_first=0, str_op="+", int_second=0):
    str_rtn = "" 
    if str_op == "+":
        str_rtn =  str(int_first + int_second)
    elif str_op == "-":
        str_rtn =  str(int_first - int_second)
    elif str_op == "*":
        str_rtn = str(int_first * int_second)
    elif str_op == "/":
        try:
            str_rtn = str(int_first / int_second)
        except ZeroDivisionError:
            print("Kan ikke divider med nul")
            str_rtn = "NaN"    
    return str_rtn


# get_input
# input: str_input, string, the original input from terminal
# output:   int_op, integer, the index of the operation
#           str_input, string, the input string from terminal
# exception ExitException
def get_input(str_input=""):
    list_op = ["-", "+", "/", "*"]
    int_next = 0
    int_op = str_input.find(list_op[int_next])
    while int_op == -1:
        try:
            int_op = str_input.find(list_op[int_next])
            int_next += 1
        except IndexError:
            int_next = 0
            print("Ikke Valid operation!!")
            str_input = input("Hvilket regne stykke skal jeg lave? ")
            if str_input.lower() == "exit":
                raise ExitException("Lommeregner afslutter nu - tak for denne gang")
    return int_op, str_input


# main function
# input :   str_input, string, original input string
# output : 
# exception :  ExitException
def main(str_input):
    if str_input.lower() == "exit":
        raise ExitException("Lommeregner afslutter nu - tak for denne gang")
    int_op, str_input = get_input(str_input=str_input)
    str_op = str_input[int_op].strip()
    try:
        int_first = int(str_input[:int_op].strip())
        int_second = int(str_input[int_op + 1:].strip())
        str_result = calculator(int_first=int_first, str_op=str_op, int_second=int_second)
        print("Resulatet af " + str_input + " = " + str_result)
    except ValueError:
        print("Jeg tager kun imod tal!!!")

    str_input = input("Hvilket regne stykke skal jeg lave? ")
    main(str_input)


if __name__ == "__main__":
    str_input = ""
    print("Velkommen til lommeregner")
    print("Skriv exit, hvis du vil afslutte.")

    str_input = input("Hvilket regne stykke skal jeg lave? ")
    try: 
        main(str_input)
    except ExitException as e:
        print(e)