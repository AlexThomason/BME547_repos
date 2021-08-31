# returns.py
# Author Alex Thomason


def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("My Program")
        print("Options:")
        print("0 = Quit")
        print("1 = HDL Analysis")
        print("2 = LDL Analysis")
        choice = int(input("Make a choice: "))
        print(type(choice))
        
        if choice == 0:
            keep_running = False
        elif choice == 1:
            HDL_Driver()
        elif choice == 2:
            LDL_Driver()
        else :
            print ("Not an option - Please try again")    

    return choice
   

# HDL Functions

def HDL_input():
    HDL_value = int(input(("Enter HDL Value: ")))
    return HDL_value

def HDL_Driver():
    HDL_value = HDL_input()
    HDL_character = check_HDL(HDL_value)
    HDL_output(HDL_value,HDL_character)

def check_HDL(value):
    if value >= 60:
        return "Normal"
    elif 40 <= value < 60:
        return "Borderline Low"
    else:
        return "Low"

def HDL_output(value, character) :
    print("Your HDL level is {}".format(value))
    print("This HDL level is {}".format(character))



# LDL Functions

def LDL_input():
    LDL_value = int(input(("Enter LDL Value: ")))
    return LDL_value

def HDL_Driver():
    LDL_value = LDL_input()
    LDL_character = check_HDL(LDL_value)
    HDL_output(LDL_value,LDL_character)

def check_HDL(value):
    if value < 130:
        return "Normal"
    elif 130 <= value <= 159:
        return "Borderline High"
    elif 160 <= value <= 189:
        return "High"
    else:
        return "High"

def HDL_output(value, character) :
    print("Your HDL level is {}".format(value))
    print("This HDL level is {}".format(character))

interface()