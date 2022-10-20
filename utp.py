import imdb
import pynput
import os
import time

moviesdb = imdb.IMDb()

def search():
    movie = input('Search\t: ')
    items = moviesdb.search_movie(movie)
    for i in items:
        print(i)
    choose = input('Do you want more information about the film? (y/n)')
    if choose == 'y':
        detail()
    else:
        os.system("cls")
        print('\n\n\t\t\t\t\t\t\tThank you for coming!\n\n')
        os._exit(0)

def detail():
    movie = input('Detail\t: ')
    items = moviesdb.search_movie(movie)
    id = items[0].getID()
    movie = moviesdb.get_movie(id)

    title = movie['title']
    year = movie['year']
    rating = movie['rating']
    directors = movie['directors']
    casting = movie['cast']

    print('Movie info :\n')
    print(f'{title} - {year}\n')
    print(f'Rating: {rating}')

    direcStr = ' '.join(map(str,directors))
    print(f'Directors: {direcStr}')

    actors = ',\n '.join(map(str, casting))
    print(f'Actors: {actors}')

    menu = input('Wanna add to your bookmark? (y/n)')
    if menu == 'y':
        bookmark()
    else :
        os._exit(0)

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
    favFilm = []
    os.system('cls')
    print('\tAdd your favorite Film!')
    choose = 'y'
    while choose == 'y':
        fav = input('Film : ')
        favFilm.append(fav)
        choose = input('Add more? (y/n)')
    os.system('cls')
    print('\tBookmark\n')
    print(favFilm)
    menu = input('Main menu (y/n)')
    if menu == 'y':
        mainMenu()
    else:
        os._exit(0)

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

os.system('cls')
print('\n\n\n\t\t\t\t\t\t\t\t\t>>>> IMDB <<<<')
ip = input('\t\t\t\t\t\t\t\t\tclick start to \n\n')
mainMenu()
