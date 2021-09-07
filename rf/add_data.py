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
    {
        "que": "sample question 1", 
        "category": "friends"
    },
    {
        "que": "sample question 2", 
        "category": "friends"
    },
    {
        "que": "sample question 3", 
        "category": "friends"
    },
    {
        "que": "sample question 4", 
        "category": "friends"
    },
    {
        "que": "sample question 5", 
        "category": "friends"
    },



    {
        "que": "couples What is your's favorite sport?", 
        "category": "couples"
    },
    {
        "que": "couples If you could be a superhero for a day, who would it be?", 
        "category": "couples"
    },
    {
        "que": "couples What is the best gift you has received?", 
        "category": "couples"
    },
    {
        "que": "couples Which messages do you prefer?", 
        "category": "couples"
    },
    {
        "que": "couples Which pet would you choose?", 
        "category": "couples"
    },
    {
        "que": "couples sample question 1", 
        "category": "couples"
    },
    {
        "que": "couples sample question 2", 
        "category": "couples"
    },
    {
        "que": "couples sample question 3", 
        "category": "couples"
    },
    {
        "que": "couples sample question 4", 
        "category": "couples"
    },
    {
        "que": "couples sample question 5", 
        "category": "couples"
    },




    {
        "que": "bff What is your's favorite sport?", 
        "category": "bff"
    },
    {
        "que": "bff If you could be a superhero for a day, who would it be?", 
        "category": "bff"
    },
    {
        "que": "bff What is the best gift you has received?", 
        "category": "bff"
    },
    {
        "que": "bff Which messages do you prefer?", 
        "category": "bff"
    },
    {
        "que": "bff Which pet would you choose?", 
        "category": "bff"
    },
    {
        "que": "bff sample question 1", 
        "category": "bff"
    },
    {
        "que": "bff sample question 2", 
        "category": "bff"
    },
    {
        "que": "bff sample question 3", 
        "category": "bff"
    },
    {
        "que": "bff sample question 4", 
        "category": "bff"
    },
    {
        "que": "bff sample question 5", 
        "category": "bff"
    },
]


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
    print("rf")
    add_rfque()

