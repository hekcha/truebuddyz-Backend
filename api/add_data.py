from .models.quiz import *
from .models.entertainment import *
from .models.howwelluknow import *
from .models.other import *

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

Entertainment_data=[
    {
        "category": "anime",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",

        "que1": "anime sample question1",
        "option1A": "sample option A",
        "option1B": "sample option B",
        "option1C": "sample option C",
        "option1D": "sample option D",
        
        "que2": "anime sample question2",
        "option2A": "sample option A",
        "option2B": "sample option B",
        "option2C": "sample option C",
        "option2D": "sample option D",

        "que3": "anime sample question3",
        "option3A": "sample option A",
        "option3B": "sample option B",
        "option3C": "sample option C",
        "option3D": "sample option D",

        "que4": "anime sample question4",
        "option4A": "sample option A",
        "option4B": "sample option B",
        "option4C": "sample option C",
        "option4D": "sample option D",
    },
    {
        "category": "dog",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",

        "que1": "dog sample question1",
        "option1A": "sample option A",
        "option1B": "sample option B",
        "option1C": "sample option C",
        "option1D": "sample option D",
        
        "que2": "dog sample question2",
        "option2A": "sample option A",
        "option2B": "sample option B",
        "option2C": "sample option C",
        "option2D": "sample option D",

        "que3": "dog sample question3",
        "option3A": "sample option A",
        "option3B": "sample option B",
        "option3C": "sample option C",
        "option3D": "sample option D",

        "que4": "dog sample question4",
        "option4A": "sample option A",
        "option4B": "sample option B",
        "option4C": "sample option C",
        "option4D": "sample option D",
    },
]

QuizQue=[
    {
        "category": "friends",
        "part1": "What is",
        "part2": "'s favorite sport?",
        "optionA": "Cricket",
        "optionB": "Ludo",
        "optionC": "PUBG",
        "optionD": "Subway Surfers",
    },
    {
        "category": "friends",
        "part1": "If",
        "part2": "could be a superhero for a day, who would it be?",
        "optionA": "Ironman",
        "optionB": "Superman",
        "optionC": "Thor",
        "optionD": "Captain America",
    },
    {
        "category": "friends",
        "part1": "What is the best gift",
        "part2": "has received?",
        "optionA": "Mobile",
        "optionB": "Crush Mobile No.",
        "optionC": "Bike",
        "optionD": "",
    },
    {
        "category": "friends",
        "part1": "How many kids will",
        "part2": "have?",
        "optionA": "2",
        "optionB": "3",
        "optionC": "4",
        "optionD": "11",
    },
    {
        "category": "friends",
        "part1": "Which messages do",
        "part2": "prefer?",
        "optionA": "Text Message",
        "optionB": "Call",
        "optionC": "Voice mail",
        "optionD": "Video Chat",
    },
    {
        "category": "friends",
        "part1": "Which pet would",
        "part2": "choose?",
        "optionA": "Dog",
        "optionB": "Cat",
        "optionC": "Squirrel",
        "optionD": "Nothing",
    },
    {
        "category": "friends",
        "part1": "Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "friends",
        "part1": "Copied 2 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "friends",
        "part1": "Copied 2 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "friends",
        "part1": "Copied 3 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "friends",
        "part1": "Copied 4 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "friends",
        "part1": "Copied 5 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "friends",
        "part1": "Copied 6 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "friends",
        "part1": "Copied 7 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "friends",
        "part1": "Copied 8 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },



    {
        "category": "couples",
        "part1": "couples What is",
        "part2": "'s favorite sport?",
        "optionA": "Cricket",
        "optionB": "Ludo",
        "optionC": "PUBG",
        "optionD": "Subway Surfers",
    },
    {
        "category": "couples",
        "part1": "couples If",
        "part2": "could be a superhero for a day, who would it be?",
        "optionA": "Ironman",
        "optionB": "Superman",
        "optionC": "Thor",
        "optionD": "Captain America",
    },
    {
        "category": "couples",
        "part1": "couples What is the best gift",
        "part2": "has received?",
        "optionA": "Mobile",
        "optionB": "Crush Mobile No.",
        "optionC": "Bike",
        "optionD": "",
    },
    {
        "category": "couples",
        "part1": "couples How many kids will",
        "part2": "have?",
        "optionA": "2",
        "optionB": "3",
        "optionC": "4",
        "optionD": "11",
    },
    {
        "category": "couples",
        "part1": "couples Which messages do",
        "part2": "prefer?",
        "optionA": "Text Message",
        "optionB": "Call",
        "optionC": "Voice mail",
        "optionD": "Video Chat",
    },
    {
        "category": "couples",
        "part1": "couples Which pet would",
        "part2": "choose?",
        "optionA": "Dog",
        "optionB": "Cat",
        "optionC": "Squirrel",
        "optionD": "Nothing",
    },
    {
        "category": "couples",
        "part1": "couples Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "couples",
        "part1": "couples Copied 2 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "couples",
        "part1": "couples Copied 2 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "couples",
        "part1": "couples Copied 3 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "couples",
        "part1": "couples Copied 4 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "couples",
        "part1": "couples Copied 5 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "couples",
        "part1": "couples Copied 6 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "couples",
        "part1": "couples Copied 7 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "couples",
        "part1": "couples Copied 8 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },



    {
        "category": "bff",
        "part1": "bff What is",
        "part2": "'s favorite sport?",
        "optionA": "Cricket",
        "optionB": "Ludo",
        "optionC": "PUBG",
        "optionD": "Subway Surfers",
    },
    {
        "category": "bff",
        "part1": "bff If",
        "part2": "could be a superhero for a day, who would it be?",
        "optionA": "Ironman",
        "optionB": "Superman",
        "optionC": "Thor",
        "optionD": "Captain America",
    },
    {
        "category": "bff",
        "part1": "bff What is the best gift",
        "part2": "has received?",
        "optionA": "Mobile",
        "optionB": "Crush Mobile No.",
        "optionC": "Bike",
        "optionD": "",
    },
    {
        "category": "bff",
        "part1": "bff How many kids will",
        "part2": "have?",
        "optionA": "2",
        "optionB": "3",
        "optionC": "4",
        "optionD": "11",
    },
    {
        "category": "bff",
        "part1": "bff Which messages do",
        "part2": "prefer?",
        "optionA": "Text Message",
        "optionB": "Call",
        "optionC": "Voice mail",
        "optionD": "Video Chat",
    },
    {
        "category": "bff",
        "part1": "bff Which pet would",
        "part2": "choose?",
        "optionA": "Dog",
        "optionB": "Cat",
        "optionC": "Squirrel",
        "optionD": "Nothing",
    },
    {
        "category": "bff",
        "part1": "bff Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "bff",
        "part1": "bff Copied 2 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "bff",
        "part1": "bff Copied 2 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "bff",
        "part1": "bff Copied 3 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "bff",
        "part1": "bff Copied 4 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "bff",
        "part1": "bff Copied 5 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "bff",
        "part1": "bff Copied 6 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "bff",
        "part1": "bff Copied 7 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },
    {
        "category": "bff",
        "part1": "bff Copied 8 Which device",
        "part2": "mostly use?",
        "optionA": "Mobile",
        "optionB": "Laptop",
        "optionC": "Tablets",
        "optionD": "Nothing",
    },


    {
        "category": "anime",
        "part1": "anime random que 2",
        "part2": "", 
        "optionA": "anime random option 2",
        "optionB": "anime random option 2",
        "optionC": "anime random option 2",
        "optionD": "anime random option 2",
    },
    {
        "category": "anime",
        "part1": "anime random que 3",
        "part2": "", 
        "optionA": "anime random option 3",
        "optionB": "anime random option 3",
        "optionC": "anime random option 3",
        "optionD": "anime random option 3",
    },
    {
        "category": "anime",
        "part1": "anime random que 4",
        "part2": "", 
        "optionA": "anime random option 4",
        "optionB": "anime random option 4",
        "optionC": "anime random option 4",
        "optionD": "anime random option 4",
    },
    {
        "category": "anime",
        "part1": "anime random que 5",
        "part2": "", 
        "optionA": "anime random option 5",
        "optionB": "anime random option 5",
        "optionC": "anime random option 5",
        "optionD": "anime random option 5",
    },
    {
        "category": "anime",
        "part1": "anime random que 6",
        "part2": "", 
        "optionA": "anime random option 6",
        "optionB": "anime random option 6",
        "optionC": "anime random option 6",
        "optionD": "anime random option 6",
    },
    {
        "category": "anime",
        "part1": "anime random que 7",
        "part2": "", 
        "optionA": "anime random option 7",
        "optionB": "anime random option 7",
        "optionC": "anime random option 7",
        "optionD": "anime random option 7",
    },
    {
        "category": "anime",
        "part1": "anime random que 8",
        "part2": "", 
        "optionA": "anime random option 8",
        "optionB": "anime random option 8",
        "optionC": "anime random option 8",
        "optionD": "anime random option 8",
    },
    {
        "category": "anime",
        "part1": "anime random que 9",
        "part2": "", 
        "optionA": "anime random option 9",
        "optionB": "anime random option 9",
        "optionC": "anime random option 9",
        "optionD": "anime random option 9",
    },
    {
        "category": "anime",
        "part1": "anime random que 10",
        "part2": "", 
        "optionA": "anime random option 10",
        "optionB": "anime random option 10",
        "optionC": "anime random option 10",
        "optionD": "anime random option 10",
    },
    {
        "category": "anime",
        "part1": "anime random que 1",
        "part2": "", 
        "optionA": "anime random option 1",
        "optionB": "anime random option 1",
        "optionC": "anime random option 1",
        "optionD": "anime random option 1",
    },

    {
        "category": "dog",
        "part1": "dog random que 2",
        "part2": "", 
        "optionA": "dog random option 2",
        "optionB": "dog random option 2",
        "optionC": "dog random option 2",
        "optionD": "dog random option 2",
    },
    {
        "category": "dog",
        "part1": "dog random que 3",
        "part2": "", 
        "optionA": "dog random option 3",
        "optionB": "dog random option 3",
        "optionC": "dog random option 3",
        "optionD": "dog random option 3",
    },
    {
        "category": "dog",
        "part1": "dog random que 4",
        "part2": "", 
        "optionA": "dog random option 4",
        "optionB": "dog random option 4",
        "optionC": "dog random option 4",
        "optionD": "dog random option 4",
    },
    {
        "category": "dog",
        "part1": "dog random que 5",
        "part2": "", 
        "optionA": "dog random option 5",
        "optionB": "dog random option 5",
        "optionC": "dog random option 5",
        "optionD": "dog random option 5",
    },
    {
        "category": "dog",
        "part1": "dog random que 6",
        "part2": "", 
        "optionA": "dog random option 6",
        "optionB": "dog random option 6",
        "optionC": "dog random option 6",
        "optionD": "dog random option 6",
    },
    {
        "category": "dog",
        "part1": "dog random que 7",
        "part2": "", 
        "optionA": "dog random option 7",
        "optionB": "dog random option 7",
        "optionC": "dog random option 7",
        "optionD": "dog random option 7",
    },
    {
        "category": "dog",
        "part1": "dog random que 8",
        "part2": "", 
        "optionA": "dog random option 8",
        "optionB": "dog random option 8",
        "optionC": "dog random option 8",
        "optionD": "dog random option 8",
    },
    {
        "category": "dog",
        "part1": "dog random que 9",
        "part2": "", 
        "optionA": "dog random option 9",
        "optionB": "dog random option 9",
        "optionC": "dog random option 9",
        "optionD": "dog random option 9",
    },
    {
        "category": "dog",
        "part1": "dog random que 10",
        "part2": "", 
        "optionA": "dog random option 10",
        "optionB": "dog random option 10",
        "optionC": "dog random option 10",
        "optionD": "dog random option 10",
    },
    {
        "category": "dog",
        "part1": "dog random que 1",
        "part2": "", 
        "optionA": "dog random option 1",
        "optionB": "dog random option 1",
        "optionC": "dog random option 1",
        "optionD": "dog random option 1",
    },
]

Entertainment_result=[
    {
        "category": "anime",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1111 anime mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1111",
    },
    {
        "category": "anime",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1112 anime mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1112",
    },
    {
        "category": "anime",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1113 anime mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1113",
    },
    {
        "category": "anime",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1114 anime mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1114",
    },
    {
        "category": "anime",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1121 anime mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1121",
    },
    {
        "category": "anime",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1122 anime mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1122",
    },
    {
        "category": "anime",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1123 anime mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1123",
    },
    {
        "category": "anime",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1124 anime mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1124",
    },
    {
        "category": "anime",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1131 anime mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1131",
    },
    {
        "category": "anime",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1132 anime mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1132",
    },
    {
        "category": "anime",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1133 anime mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1133",
    },
    {
        "category": "anime",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1134 anime mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1134",
    },


    {
        "category": "dog",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1111 dog mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1111",
    },
    {
        "category": "dog",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1112 dog mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1112",
    },
    {
        "category": "dog",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1113 dog mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1113",
    },
    {
        "category": "dog",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1114 dog mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1114",
    },
    {
        "category": "dog",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1121 dog mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1121",
    },
    {
        "category": "dog",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1122 dog mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1122",
    },
    {
        "category": "dog",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1123 dog mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1123",
    },
    {
        "category": "dog",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1124 dog mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1124",
    },
    {
        "category": "dog",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1131 dog mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1131",
    },
    {
        "category": "dog",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1132 dog mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1132",
    },
    {
        "category": "dog",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1133 dog mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1133",
    },
    {
        "category": "dog",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
        "text": "1134 dog mtlb aisa bilkul immediate nahi soche hain but....sochenge",
        "code": "1134",
    },
]

HowWellUKnow_que=[
    {
        "category": "marvel",
        "que": "MARVEL sample question 1",
        "optionA": "MARVEL sample optionA",
        "optionB": "MARVEL sample optionB",
        "optionC": "MARVEL sample optionC",
        "optionD": "MARVEL sample optionD",
        "ans": "2",
    },
    {
        "category": "marvel",
        "que": "MARVEL sample question 2",
        "optionA": "MARVEL sample optionA",
        "optionB": "MARVEL sample optionB",
        "optionC": "MARVEL sample optionC",
        "optionD": "MARVEL sample optionD",
        "ans": "2",
    },
    {
        "category": "marvel",
        "que": "MARVEL sample question 3",
        "optionA": "MARVEL sample optionA",
        "optionB": "MARVEL sample optionB",
        "optionC": "MARVEL sample optionC",
        "optionD": "MARVEL sample optionD",
        "ans": "2",
    },
    {
        "category": "marvel",
        "que": "MARVEL sample question 4",
        "optionA": "MARVEL sample optionA",
        "optionB": "MARVEL sample optionB",
        "optionC": "MARVEL sample optionC",
        "optionD": "MARVEL sample optionD",
        "ans": "2",
    },
    {
        "category": "marvel",
        "que": "MARVEL sample question 5",
        "optionA": "MARVEL sample optionA",
        "optionB": "MARVEL sample optionB",
        "optionC": "MARVEL sample optionC",
        "optionD": "MARVEL sample optionD",
        "ans": "2",
    },
    {
        "category": "marvel",
        "que": "MARVEL sample question 6",
        "optionA": "MARVEL sample optionA",
        "optionB": "MARVEL sample optionB",
        "optionC": "MARVEL sample optionC",
        "optionD": "MARVEL sample optionD",
        "ans": "2",
    },
    {
        "category": "marvel",
        "que": "MARVEL sample question 7",
        "optionA": "MARVEL sample optionA",
        "optionB": "MARVEL sample optionB",
        "optionC": "MARVEL sample optionC",
        "optionD": "MARVEL sample optionD",
        "ans": "2",
    },
    {
        "category": "marvel",
        "que": "MARVEL sample question 8",
        "optionA": "MARVEL sample optionA",
        "optionB": "MARVEL sample optionB",
        "optionC": "MARVEL sample optionC",
        "optionD": "MARVEL sample optionD",
        "ans": "2",
    },
    {
        "category": "marvel",
        "que": "MARVEL sample question 9",
        "optionA": "MARVEL sample optionA",
        "optionB": "MARVEL sample optionB",
        "optionC": "MARVEL sample optionC",
        "optionD": "MARVEL sample optionD",
        "ans": "2",
    },
    {
        "category": "marvel",
        "que": "MARVEL sample question 10",
        "optionA": "MARVEL sample optionA",
        "optionB": "MARVEL sample optionB",
        "optionC": "MARVEL sample optionC",
        "optionD": "MARVEL sample optionD",
        "ans": "2",
    },
    {
        "category": "marvel",
        "que": "MARVEL sample question 11",
        "optionA": "MARVEL sample optionA",
        "optionB": "MARVEL sample optionB",
        "optionC": "MARVEL sample optionC",
        "optionD": "MARVEL sample optionD",
        "ans": "2",
    },
    {
        "category": "marvel",
        "que": "MARVEL sample question 12",
        "optionA": "MARVEL sample optionA",
        "optionB": "MARVEL sample optionB",
        "optionC": "MARVEL sample optionC",
        "optionD": "MARVEL sample optionD",
        "ans": "2",
    },
    {
        "category": "marvel",
        "que": "MARVEL sample question 13",
        "optionA": "MARVEL sample optionA",
        "optionB": "MARVEL sample optionB",
        "optionC": "MARVEL sample optionC",
        "optionD": "MARVEL sample optionD",
        "ans": "2",
    },
    {
        "category": "marvel",
        "que": "MARVEL sample question 14",
        "optionA": "MARVEL sample optionA",
        "optionB": "MARVEL sample optionB",
        "optionC": "MARVEL sample optionC",
        "optionD": "MARVEL sample optionD",
        "ans": "2",
    },
    {
        "category": "marvel",
        "que": "MARVEL sample question 15",
        "optionA": "MARVEL sample optionA",
        "optionB": "MARVEL sample optionB",
        "optionC": "MARVEL sample optionC",
        "optionD": "MARVEL sample optionD",
        "ans": "2",
    },
    {
        "category": "bollywood",
        "que": "BOLLYWOOD sample question 1",
        "optionA": "BOLLYWOOD sample optionA",
        "optionB": "BOLLYWOOD sample optionB",
        "optionC": "BOLLYWOOD sample optionC",
        "optionD": "BOLLYWOOD sample optionD",
        "ans": "2",
    },
    {
        "category": "bollywood",
        "que": "BOLLYWOOD sample question 2",
        "optionA": "BOLLYWOOD sample optionA",
        "optionB": "BOLLYWOOD sample optionB",
        "optionC": "BOLLYWOOD sample optionC",
        "optionD": "BOLLYWOOD sample optionD",
        "ans": "2",
    },
    {
        "category": "bollywood",
        "que": "BOLLYWOOD sample question 3",
        "optionA": "BOLLYWOOD sample optionA",
        "optionB": "BOLLYWOOD sample optionB",
        "optionC": "BOLLYWOOD sample optionC",
        "optionD": "BOLLYWOOD sample optionD",
        "ans": "2",
    },
    {
        "category": "bollywood",
        "que": "BOLLYWOOD sample question 4",
        "optionA": "BOLLYWOOD sample optionA",
        "optionB": "BOLLYWOOD sample optionB",
        "optionC": "BOLLYWOOD sample optionC",
        "optionD": "BOLLYWOOD sample optionD",
        "ans": "2",
    },
    {
        "category": "bollywood",
        "que": "BOLLYWOOD sample question 5",
        "optionA": "BOLLYWOOD sample optionA",
        "optionB": "BOLLYWOOD sample optionB",
        "optionC": "BOLLYWOOD sample optionC",
        "optionD": "BOLLYWOOD sample optionD",
        "ans": "2",
    },
    {
        "category": "bollywood",
        "que": "BOLLYWOOD sample question 6",
        "optionA": "BOLLYWOOD sample optionA",
        "optionB": "BOLLYWOOD sample optionB",
        "optionC": "BOLLYWOOD sample optionC",
        "optionD": "BOLLYWOOD sample optionD",
        "ans": "2",
    },
    {
        "category": "bollywood",
        "que": "BOLLYWOOD sample question 7",
        "optionA": "BOLLYWOOD sample optionA",
        "optionB": "BOLLYWOOD sample optionB",
        "optionC": "BOLLYWOOD sample optionC",
        "optionD": "BOLLYWOOD sample optionD",
        "ans": "2",
    },
    {
        "category": "bollywood",
        "que": "BOLLYWOOD sample question 8",
        "optionA": "BOLLYWOOD sample optionA",
        "optionB": "BOLLYWOOD sample optionB",
        "optionC": "BOLLYWOOD sample optionC",
        "optionD": "BOLLYWOOD sample optionD",
        "ans": "2",
    },
    {
        "category": "bollywood",
        "que": "BOLLYWOOD sample question 9",
        "optionA": "BOLLYWOOD sample optionA",
        "optionB": "BOLLYWOOD sample optionB",
        "optionC": "BOLLYWOOD sample optionC",
        "optionD": "BOLLYWOOD sample optionD",
        "ans": "2",
    },
    {
        "category": "bollywood",
        "que": "BOLLYWOOD sample question 10",
        "optionA": "BOLLYWOOD sample optionA",
        "optionB": "BOLLYWOOD sample optionB",
        "optionC": "BOLLYWOOD sample optionC",
        "optionD": "BOLLYWOOD sample optionD",
        "ans": "2",
    },
    {
        "category": "bollywood",
        "que": "BOLLYWOOD sample question 11",
        "optionA": "BOLLYWOOD sample optionA",
        "optionB": "BOLLYWOOD sample optionB",
        "optionC": "BOLLYWOOD sample optionC",
        "optionD": "BOLLYWOOD sample optionD",
        "ans": "2",
    },
    {
        "category": "bollywood",
        "que": "BOLLYWOOD sample question 12",
        "optionA": "BOLLYWOOD sample optionA",
        "optionB": "BOLLYWOOD sample optionB",
        "optionC": "BOLLYWOOD sample optionC",
        "optionD": "BOLLYWOOD sample optionD",
        "ans": "2",
    },
    {
        "category": "bollywood",
        "que": "BOLLYWOOD sample question 13",
        "optionA": "BOLLYWOOD sample optionA",
        "optionB": "BOLLYWOOD sample optionB",
        "optionC": "BOLLYWOOD sample optionC",
        "optionD": "BOLLYWOOD sample optionD",
        "ans": "2",
    },
    {
        "category": "bollywood",
        "que": "BOLLYWOOD sample question 14",
        "optionA": "BOLLYWOOD sample optionA",
        "optionB": "BOLLYWOOD sample optionB",
        "optionC": "BOLLYWOOD sample optionC",
        "optionD": "BOLLYWOOD sample optionD",
        "ans": "2",
    },
    {
        "category": "bollywood",
        "que": "BOLLYWOOD sample question 15",
        "optionA": "BOLLYWOOD sample optionA",
        "optionB": "BOLLYWOOD sample optionB",
        "optionC": "BOLLYWOOD sample optionC",
        "optionD": "BOLLYWOOD sample optionD",
        "ans": "2",
    },
]

HowWellUKnowScore_ans=[
    {
        "category": "marvel",
        "score": "0",
        "message": "MARVEL dub ke mr jo bc your score is 0",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "marvel",
        "score": "1",
        "message": "MARVEL your score is 1",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "marvel",
        "score": "2",
        "message": "MARVEL your score is 2",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "marvel",
        "score": "3",
        "message": "MARVEL your score is 3",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "marvel",
        "score": "4",
        "message": "MARVEL your score is 4",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "marvel",
        "score": "5",
        "message": "MARVEL your score is 5",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "marvel",
        "score": "6",
        "message": "MARVEL your score is 6",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "marvel",
        "score": "7",
        "message": "MARVEL your score is 7",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "marvel",
        "score": "8",
        "message": "MARVEL your score is 8",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "marvel",
        "score": "9",
        "message": "MARVEL your score is 9",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "marvel",
        "score": "10",
        "message": "MARVEL congrats your score is 10",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "bollywood",
        "score": "0",
        "message": "BOLLYWOOD dub ke mr jo bc your score is 0",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "bollywood",
        "score": "1",
        "message": "BOLLYWOOD your score is 1",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "bollywood",
        "score": "2",
        "message": "BOLLYWOOD your score is 2",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "bollywood",
        "score": "3",
        "message": "BOLLYWOOD your score is 3",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "bollywood",
        "score": "4",
        "message": "BOLLYWOOD your score is 4",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "bollywood",
        "score": "5",
        "message": "BOLLYWOOD your score is 5",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "bollywood",
        "score": "6",
        "message": "BOLLYWOOD your score is 6",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "bollywood",
        "score": "7",
        "message": "BOLLYWOOD your score is 7",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "bollywood",
        "score": "8",
        "message": "BOLLYWOOD your score is 8",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "bollywood",
        "score": "9",
        "message": "BOLLYWOOD your score is 9",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
    {
        "category": "bollywood",
        "score": "10",
        "message": "BOLLYWOOD congrats your score is 10",
        "image": "https://i.ibb.co/WsBTZ79/download.jpg",
    },
]

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
                link = data["link"],
                image = data["image"],
                text = data["text"],
            )
        print("try Trending que complete")
    except:
        print("except in Trending que")
        pass

def add_HowWellUKnowScore():
    try:
        print("try HowWellUKnowScore que")
        if len(HowWellUKnowScore.objects.all()):
            print("HowWellUKnowScore que already have que")
            return 0

        for data in HowWellUKnowScore_ans:
            print("HowWellUKnowScore que added")
            HowWellUKnowScore.objects.create(
                category = data["category"],
                score = data["score"],
                message = data["message"],
                image = data["image"],
            )
        print("try HowWellUKnowScore que complete")
    except:
        print("except in HowWellUKnowScore que")
        pass


def add_HowWellUKnow():
    try:
        print("try HowWellUKnow que")
        if len(HowWellUKnow.objects.all()):
            print("HowWellUKnow que already have que")
            return 0

        for data in HowWellUKnow_que:
            print("HowWellUKnow que added")
            HowWellUKnow.objects.create(
                category = data["category"],
                que = data["que"],
                ans = data["ans"],
                optionA = data["optionA"],
                optionB = data["optionB"],
                optionC = data["optionC"],
                optionD = data["optionD"],
            )
        print("try HowWellUKnow que complete")
    except:
        print("except in HowWellUKnow que")
        pass


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

def add_entertainment():
    try:
        print("try entertainment que")
        if len(Entertainment.objects.all()):
            print("entertainment already have que")
            return 0

        for data in Entertainment_data:
            print("entertainment que added")
            Entertainment.objects.create(
                category = data["category"],
                image = data["image"],
                que1 = data["que1"],
                option1A = data["option1A"],
                option1B = data["option1B"],
                option1C = data["option1C"],
                option1D = data["option1D"],

                que2 = data["que2"],
                option2A = data["option2A"],
                option2B = data["option2B"],
                option2C = data["option2C"],
                option2D = data["option2D"],

                que3 = data["que3"],
                option3A = data["option3A"],
                option3B = data["option3B"],
                option3C = data["option3C"],
                option3D = data["option3D"],

                que4 = data["que4"],
                option4A = data["option4A"],
                option4B = data["option4B"],
                option4C = data["option4C"],
                option4D = data["option4D"],
            )
        print("try entertainment que complete")
    except:
        print("except in entertainment que")
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

def add_entertainment_result():
    try:
        print("try entertainment_result que")
        if len(EntertainmentResult.objects.all()):
            print("entertainment_result already have que")
            return 0

        for data in Entertainment_result:
            print("entertainment_result que added")
            EntertainmentResult.objects.create(
                image = data["image"],
                category = data["category"],
                code = data["code"],
                text = data["text"],
                )
        print("try entertainment_result que complete")
    except:
        print("except in entertainment_result que")
        pass


def add_data():
    print("add_data")
    add_quizque()
    add_rfque()
    add_entertainment()
    add_entertainment_result()
    add_HowWellUKnow()
    add_HowWellUKnowScore()
    add_Trending()

