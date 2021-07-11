from .models import *

# change all these before run
# n u l l  =  None
# t r u e  =  True
# f a l s e  =  False
# change all img field with image location (location must be in media folder)

QuizQue = [
    {
        "id": 1,
        "part1": "What is",
        "part2": "'s favorite sport?",
        "optionA": "Cricket",
        "imgA": "https://source.unsplash.com/collection/1390381/250x250",
        "optionB": "Ludo",
        "imgB": "https://source.unsplash.com/collection/DEgfFe0PZlQ/250x250",
        "optionC": "PUBG",
        "imgC": "https://source.unsplash.com/collection/209138/250x250",
        "optionD": "Subway Surfers",
        "imgD": "https://source.unsplash.com/collection/1199299/250x250"
    },
    {
        "id": 2,
        "part1": "If",
        "part2": "could be a superhero for a day, who would it be?",
        "optionA": "Ironman",
        "imgA": "https://source.unsplash.com/collection/1390381/250x250",
        "optionB": "Superman",
        "imgB": "https://source.unsplash.com/collection/DEgfFe0PZlQ/250x250",
        "optionC": "Thor",
        "imgC": "https://source.unsplash.com/collection/209138/250x250",
        "optionD": "Captain America",
        "imgD": "https://source.unsplash.com/collection/1199299/250x250"
    },
    {
        "id": 3,
        "part1": "What is the best gift",
        "part2": "has received?",
        "optionA": "Mobile",
        "imgA": "https://source.unsplash.com/collection/1390381/250x250",
        "optionB": "Crush Mobile No.",
        "imgB": "https://source.unsplash.com/collection/DEgfFe0PZlQ/250x250",
        "optionC": "Bike",
        "imgC": "https://source.unsplash.com/collection/209138/250x250",
        "optionD": "",
        "imgD": "https://source.unsplash.com/collection/1199299/250x250"
    },
    {
        "id": 4,
        "part1": "How many kids will",
        "part2": "have?",
        "optionA": "2",
        "imgA": "https://source.unsplash.com/collection/1390381/250x250",
        "optionB": "3",
        "imgB": "https://source.unsplash.com/collection/DEgfFe0PZlQ/250x250",
        "optionC": "4",
        "imgC": "https://source.unsplash.com/collection/209138/250x250",
        "optionD": "11",
        "imgD": "https://source.unsplash.com/collection/1199299/250x250"
    },
    {
        "id": 5,
        "part1": "Which messages do",
        "part2": "prefer?",
        "optionA": "Text Message",
        "imgA": "https://source.unsplash.com/collection/1390381/250x250",
        "optionB": "Call",
        "imgB": "https://source.unsplash.com/collection/DEgfFe0PZlQ/250x250",
        "optionC": "Voice mail",
        "imgC": "https://source.unsplash.com/collection/209138/250x250",
        "optionD": "Video Chat",
        "imgD": "https://source.unsplash.com/collection/1199299/250x250"
    },
    {
        "id": 6,
        "part1": "Which pet would",
        "part2": "choose?",
        "optionA": "Dog",
        "imgA": "https://source.unsplash.com/collection/1390381/250x250",
        "optionB": "Cat",
        "imgB": "https://source.unsplash.com/collection/DEgfFe0PZlQ/250x250",
        "optionC": "Squirrel",
        "imgC": "https://source.unsplash.com/collection/209138/250x250",
        "optionD": "Nothing",
        "imgD": "https://source.unsplash.com/collection/1199299/250x250"
    },
    {
        "id": 7,
        "part1": "Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "imgA": "https://source.unsplash.com/collection/1390381/250x250",
        "optionB": "Laptop",
        "imgB": "https://source.unsplash.com/collection/DEgfFe0PZlQ/250x250",
        "optionC": "Tablets",
        "imgC": "https://source.unsplash.com/collection/209138/250x250",
        "optionD": "Nothing",
        "imgD": "https://source.unsplash.com/collection/1199299/250x250"
    },
    {
        "id": 7,
        "part1": "Copied 2 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "imgA": "https://source.unsplash.com/collection/1390381/250x250",
        "optionB": "Laptop",
        "imgB": "https://source.unsplash.com/collection/DEgfFe0PZlQ/250x250",
        "optionC": "Tablets",
        "imgC": "https://source.unsplash.com/collection/209138/250x250",
        "optionD": "Nothing",
        "imgD": "https://source.unsplash.com/collection/1199299/250x250"
    },
    {
        "id": 7,
        "part1": "Copied 2 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "imgA": "https://source.unsplash.com/collection/1390381/250x250",
        "optionB": "Laptop",
        "imgB": "https://source.unsplash.com/collection/DEgfFe0PZlQ/250x250",
        "optionC": "Tablets",
        "imgC": "https://source.unsplash.com/collection/209138/250x250",
        "optionD": "Nothing",
        "imgD": "https://source.unsplash.com/collection/1199299/250x250"
    },
    {
        "id": 7,
        "part1": "Copied 3 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "imgA": "https://source.unsplash.com/collection/1390381/250x250",
        "optionB": "Laptop",
        "imgB": "https://source.unsplash.com/collection/DEgfFe0PZlQ/250x250",
        "optionC": "Tablets",
        "imgC": "https://source.unsplash.com/collection/209138/250x250",
        "optionD": "Nothing",
        "imgD": "https://source.unsplash.com/collection/1199299/250x250"
    },
    {
        "id": 7,
        "part1": "Copied 4 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "imgA": "https://source.unsplash.com/collection/1390381/250x250",
        "optionB": "Laptop",
        "imgB": "https://source.unsplash.com/collection/DEgfFe0PZlQ/250x250",
        "optionC": "Tablets",
        "imgC": "https://source.unsplash.com/collection/209138/250x250",
        "optionD": "Nothing",
        "imgD": "https://source.unsplash.com/collection/1199299/250x250"
    },
    {
        "id": 7,
        "part1": "Copied 5 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "imgA": "https://source.unsplash.com/collection/1390381/250x250",
        "optionB": "Laptop",
        "imgB": "https://source.unsplash.com/collection/DEgfFe0PZlQ/250x250",
        "optionC": "Tablets",
        "imgC": "https://source.unsplash.com/collection/209138/250x250",
        "optionD": "Nothing",
        "imgD": "https://source.unsplash.com/collection/1199299/250x250"
    },
    {
        "id": 7,
        "part1": "Copied 6 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "imgA": "https://source.unsplash.com/collection/1390381/250x250",
        "optionB": "Laptop",
        "imgB": "https://source.unsplash.com/collection/DEgfFe0PZlQ/250x250",
        "optionC": "Tablets",
        "imgC": "https://source.unsplash.com/collection/209138/250x250",
        "optionD": "Nothing",
        "imgD": "https://source.unsplash.com/collection/1199299/250x250"
    },
    {
        "id": 7,
        "part1": "Copied 7 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "imgA": "https://source.unsplash.com/collection/1390381/250x250",
        "optionB": "Laptop",
        "imgB": "https://source.unsplash.com/collection/DEgfFe0PZlQ/250x250",
        "optionC": "Tablets",
        "imgC": "https://source.unsplash.com/collection/209138/250x250",
        "optionD": "Nothing",
        "imgD": "https://source.unsplash.com/collection/1199299/250x250"
    },
    {
        "id": 7,
        "part1": "Copied 8 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "imgA": "https://source.unsplash.com/collection/1390381/250x250",
        "optionB": "Laptop",
        "imgB": "https://source.unsplash.com/collection/DEgfFe0PZlQ/250x250",
        "optionC": "Tablets",
        "imgC": "https://source.unsplash.com/collection/209138/250x250",
        "optionD": "Nothing",
        "imgD": "https://source.unsplash.com/collection/1199299/250x250"
    },
]


def add_data():
    print("add_data")
    try:
        print("try quiz")
        if len(QuizQuestionBank.objects.all()):
            print("quiz already have que")
            return 0

        for data in QuizQue:
            print("added")
            QuizQuestionBank.objects.create(
                part1=data["part1"],
                part2=data["part2"],
                optionA=data["optionA"],
                # imgA = data["imgA"],
                optionB=data["optionB"],
                # imgB = data["imgB"],
                optionC=data["optionC"],
                # imgC = data["imgC"],
                optionD=data["optionD"],
                # imgD = data["imgD"]
            )
        print("try quiz complete")
    except:
        print("except quiz")
        pass
