# returns.py
# Author Alex Thomason


def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("My Program")
        print("Options:")
        print("9 = Quit")
        choice = int(input("Make a choice: "))
        print(type(choice))
        
        if choice == 9:
            keep_running = False

    return choice
   

def HDL_input():
    HDL_value = int(input(("Enter HDL Value: ")))
    return HDL_value

def check_HDL():
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline Low"
    else:
        return "Low"

interface()