# BasicMechanicPhysics Start ----------------------------------------------------------------------------------
def BasicMechanicPhysics() :
    close = "n"
    while not close == "y" :
        print("\nEquation : v = s/t")
        try :
            s = float(input("s : "))
            t = float(input("t : "))
        except :
            print("\nPlz put only number")
        v = s/t
        print("v : %.2f"%v)
        try :
            close = input("Do you want to Exit? (y/n) : ")
        except :
            print("\nPlz type only 'y' or 'n'")
# BasicMechanicPhysics End ----------------------------------------------------------------------------------
# Main Start ------------------------------------------------------------------------------------------------
def Main():
    choice = -1
    while not choice == 0 :
        print("\n0 : Exit")
        print("1 : Basic mechanic physics")
        try :
            choice = int(input("Choose your choice : "))
            if choice == 1 : BasicMechanicPhysics()
        except :
            print("\nPlz type number")        
# Main End ---------------------------------------------------------------------------------------------------
# Start ------------------------------------------------------------------------------------------------------
def Start() :
    close = "n"
    while not close == "y" :
        Main()
        try :
            close = input("\nDo you want to Exit? (y/n) : ")
        except :
            print("\nPlz type only 'y' or 'n'")
    print("End Program")

Start()