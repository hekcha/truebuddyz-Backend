from .models import *

# change all these before run
# n u l l  =  None
# t r u e  =  True
# f a l s e  =  False
# change all img field with image location (location must be in media folder)

Trnding=[
    {
        'rank':'2',
        'is_active':'True',
        'link':'/rapidfire/friends',
        'text':"Friend's RapidFire",
        'image':"https://i.ibb.co/pQRgQ16/rf-friends.jpg" ,
    },
    {
        'rank':'1',
        'is_active':'True',
        'link':'/quiz/friends',
        'text':"Friend's Quiz",
        'image':"https://i.ibb.co/C5GnQJB/quiz-friends.jpg",
    },
    {
        'rank':'3',
        'is_active':'True',
        'link':'/quiz/couples',
        'text':"Couple's Quiz",
        'image':"https://i.ibb.co/3zKmfNK/quiz-couples.jpg",
    },
]

def add_Trending():
    try:
        print("try Trending que")
        if len(Trending.objects.all()):
            print("Trending que already have que")
            return 0

        for data in Trnding:
            print("Trending que added")
            Trending.objects.create(
                rank = data["rank"],
                is_active = data["is_active"],
                is_GradientCard = False,
                link = data["link"],
                image = data["image"],
                text = data["text"],
            )
        print("try Trending que complete")
    except:
        print("except in Trending que")
        pass


def add_NewGame():
    try:
        print("try NewGames que")
        if len(NewGames.objects.all()):
            print("NewGames que already have que")
            return 0

        for data in Trnding:
            print("NewGames que added")
            NewGames.objects.create(
                rank = data["rank"],
                is_active = data["is_active"],
                is_GradientCard = False,
                link = data["link"],
                image = data["image"],
                text = data["text"],
            )
        print("try NewGames que complete")
    except:
        print("except in NewGames que")
        pass


def add_data():
    print("Trnding")
    add_Trending()
    add_NewGame()

