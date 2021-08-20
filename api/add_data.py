from .models import *

# change all these before run
# n u l l  =  None
# t r u e  =  True
# f a l s e  =  False
# change all img field with image location (location must be in media folder)

RfQue=[
    {
        "que": "What is your's favorite sport?", 
        "category": "friends"
    },

    {
        "que": "If you could be a superhero for a day, who would it be?", 
        "category": "friends"
    },

    {
        "que": "What is the best gift you has received?", 
        "category": "friends"
    },

    {
        "que": "Which messages do you prefer?", 
        "category": "friends"
    },

    {
        "que": "Which pet would you choose?", 
        "category": "friends"
    },

]

QuizQue=[
    {
        "id": 1,
        "category": "friends",
        "part1": "What is",
        "part2": "'s favorite sport?",
        "optionA": "Cricket",
        "optionB": "Ludo",
        "optionC": "PUBG",
        "optionD": "Subway Surfers",
    },
    {
        "id": 2,
        "category": "friends",
        "part1": "If",
        "part2": "could be a superhero for a day, who would it be?",
        "optionA": "Ironman",
        "optionB": "Superman",
        "optionC": "Thor",
        "optionD": "Captain America",
    },
    {
        "id": 3,
        "category": "friends",
        "part1": "What is the best gift",
        "part2": "has received?",
        "optionA": "Mobile",
        "optionB": "Crush Mobile No.",
        "optionC": "Bike",
        "optionD": "",
    },
    {
        "id": 4,
        "category": "friends",
        "part1": "How many kids will",
        "part2": "have?",
        "optionA": "2",
        "optionB": "3",
        "optionC": "4",
        "optionD": "11",
    },
    {
        "id": 5,
        "category": "friends",
        "part1": "Which messages do",
        "part2": "prefer?",
        "optionA": "Text Message",
        "optionB": "Call",
        "optionC": "Voice mail",
        "optionD": "Video Chat",
    },
    {
        "id": 6,
        "category": "friends",
        "part1": "Which pet would",
        "part2": "choose?",
        "optionA": "Dog",
        "optionB": "Cat",
        "optionC": "Squirrel",
        "optionD": "Nothing",
    },
    {
        "id": 7,
        "category": "friends",
        "part1": "Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "id": 7,
        "category": "friends",
        "part1": "Copied 2 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "id": 7,
        "category": "friends",
        "part1": "Copied 2 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "id": 7,
        "category": "friends",
        "part1": "Copied 3 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "id": 7,
        "category": "friends",
        "part1": "Copied 4 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "id": 7,
        "category": "friends",
        "part1": "Copied 5 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "id": 7,
        "category": "friends",
        "part1": "Copied 6 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "id": 7,
        "category": "friends",
        "part1": "Copied 7 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "id": 7,
        "category": "friends",
        "part1": "Copied 8 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
]

def add_quizque():
    try:
        print("try quiz que")
        if len(QuizQuestionBank.objects.all()):
            print("quiz que already have que")
            return 0

        for data in QuizQue:
            print("quiz que added")
            QuizQuestionBank.objects.create(
                category = data["category"],
                part1 = data["part1"],
                part2 = data["part2"],
                optionA = data["optionA"],
                optionB = data["optionB"],
                optionC = data["optionC"],
                optionD = data["optionD"],
            )
        print("try quiz que complete")
    except:
        print("except in quiz que")
        pass


def add_rfque():
    try:
        print("try rf que")
        if len(RfQuestionBank.objects.all()):
            print("rf que already have que")
            return 0

        for data in RfQue:
            print("rf que added")
            RfQuestionBank.objects.create(que = data["que"],category = data["category"])
        print("try rf que complete")
    except:
        print("except in rf que")
        pass


def add_data():
    print("add_data")
    add_quizque()
    add_rfque()

