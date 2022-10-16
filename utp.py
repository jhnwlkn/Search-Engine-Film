import os
import time

def mainMenu():
    print("\t\tBumflix\n")
    print("1. 365 Days")
    print("2. Sex Education") 
    print("3. Bridgerton")
    print("4. Kung-fu Panda")
    print("5. Marriage Story")
    print("6. The Platform")
    print("7. Lalaland")
    print("8. Stranger Things")
    print("9. Money Heist")
    menu = int(input("Choose your film\t : "))
    os.system("cls")
    loading()
    return menu

def loading():
    for i in range(3):
        print("loading")
        time.sleep(0.3)
        os.system("cls")
        print("loading.")
        time.sleep(0.3)
        os.system("cls")
        print("loading..")
        time.sleep(0.3)
        os.system("cls")
        print("loading...")
        time.sleep(0.3)
        os.system("cls")
       
mainMenu()