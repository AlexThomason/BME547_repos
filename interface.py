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
   
   
def hdl_input():
    hdl_value = int(input(("Enter HDL Value: ")))
    return hdl_value


interface()