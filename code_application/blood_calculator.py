# returns.py
# Author Alex Thomason

print("This is the interface.py module")
print("It's name is {}".format(__name__))

def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("My Program")
        print("Options:")
        print("0 = Quit")
        print("1 = HDL Analysis")
        print("2 = LDL Analysis")
        print("3 = Cholesterol Analysis")
        choice = int(input("Make a choice: "))
        print(type(choice))
        
        if choice == 0:
            keep_running = False
        elif choice == 1:
            HDL_Driver()
        elif choice == 2:
            LDL_Driver()
        elif choice == 3:
            cholesterol_Driver()
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

def LDL_Driver():
    LDL_value = LDL_input()
    LDL_character = check_LDL(LDL_value)
    HDL_output(LDL_value,LDL_character)

def check_LDL(value):
    if value < 130:
        return "Normal"
    elif 130 <= value <= 159:
        return "Borderline High"
    elif 160 <= value <= 189:
        return "High"
    else:
        return "High"

def LDL_output(value, character) :
    print("Your LDL level is {}".format(value))
    print("This LDL level is {}".format(character))


# Cholesterol Check Functions
# Stevan would have done this so much better

def cholesterol_input():
    cholesterol_value = int(input(("Enter Cholesterol Value: ")))
    return cholesterol_value

def cholesterol_Driver():
    cholesterol_value = cholesterol_input()
    cholesterol_character = check_cholesterol(cholesterol_value)
    cholesterol_output(cholesterol_value,cholesterol_character)

def check_cholesterol(value):
    if value < 200:
        return "Normal"
    elif 200 <= value <= 239:
        return "Borderline High"
    else :
        return "High"

def cholesterol_output(value, character) :
    print("Your cholesterol level is {}".format(value))
    print("This cholesterol level is {}".format(character))




if __name__ == "__main__":
    interface()