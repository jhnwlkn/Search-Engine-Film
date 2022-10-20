import os
import time

def mainMenu():
    loading()
    os.system('cls')
    print('\t\t>>>> IMDB <<<<\n\n')
    print('1. Search Film')
    print('2. Detail film')
    print('3. Bookmark')
    print('4. Exit')
    menu = int(input('Choose menu\t : '))
    if menu == 1:
        search()
    elif menu == 2:

        detail()
    elif menu == 3:
        bookmark()
    else:
        os.system("cls")
        print('\n\n\t\t\t\t\t\t\tThank you for coming!\n\n')
        os._exit(0)

while True:
    os.system('cls')
    print('\n\n\n\t\t\t\t\t\t\t\t\t>>>> IMDB <<<<')
    ip = input('\t\t\t\t\t\t\t\t\tclick start to \n\n')
    mainMenu()

    def loading():
    for i in range(3):
        os.system('cls')
        print('loading.')
        time.sleep(0.3)
        os.system('cls')
        print('loading..')
        time.sleep(0.3)
        os.system('cls')
        print('loading')
        time.sleep(0.3)
        os.system('cls')

def bookmark():
    favFilm = ()
    fM = list(favFilm)
    os.system('cls')
    print('\tAdd your favorite Film!')
    choose = 'y'
    while choose == 'y':
        fav = input('Film : ')
        fM.append(fav)
        favFilm = tuple(fM)
        choose = input('Add more? (y/n)')
    os.system('cls')
    print('\tBookmark\n')
    print(favFilm)
    menu = input('Main menu (y/n)')
    if menu == 'y':
        mainMenu()
    else:
        os._exit(0)
