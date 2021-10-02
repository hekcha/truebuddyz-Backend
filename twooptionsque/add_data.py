from .models import *


ThisOrThat_que=[
  {
    "category": "students",
    "optionA": 'Start assignments immediately',
    "optionB": 'Wait until the last minute',
  },
  {
    "category":'students',
    "optionA":'English',
    "optionB":'Math',
  },
  {
    "category":'students',
    "optionA":'Gym',
    "optionB":'Art',
  },
  {
    "category":'students',
    "optionA":'Science',
    "optionB":'History',
  },
  {
    "category":'students',
    "optionA":'Group work',
    "optionB":'solo work',
  },
  {
    "category":'students',
    "optionA":'Art projects',
    "optionB":'science projects',
  },
  {
    "category":'students',
    "optionA":'Forget your pencil',
    "optionB":'forget a notebook',
  },
  {
    "category":'students',
    "optionA":'Teacher reads your text message aloud',
    "optionB":'teacher tells the whole class your grade',
  },
  {
    "category":'students',
    "optionA":'Drive to school',
    "optionB":'take the bus',
  },
  {
    'category':'friends',
    'optionA':'Call first thing in the morning',
    'optionB':'call in the middle of the night',
  },
  {
    'category':'friends',
    'optionA':'Board games',
    'optionB':'video games',
  },
  {
    'category':'friends',
    'optionA':'Photos',
    'optionB':'videos',
  },
  {
    'category':'friends',
    'optionA':'Social media message',
    'optionB':'text message',
  },
  {
    'category':'friends',
    'optionA':'Take a friend on your family vacation',
    'optionB':'join a friend on their family vacation',
  },
  {
    'category':'friends',
    'optionA':'Group hangout',
    'optionB':'one-on-one hangout',
  },
  {
    'category':'friends',
    'optionA':'French fries',
    'optionB':'onion rings',
  },
  {
    'category':'friends',
    'optionA':'Share food',
    'optionB':'don’t share food',
  },
  {
    'category':'friends',
    'optionA':'Give a ride',
    'optionB':'hitch a ride',
  },
]

WouldYouRather_que=[
  {
    "category": "students",
    "optionA": 'this 1',
    "optionB": 'that 1',
  },
  {
    "category": "students",
    "optionA": 'this 2',
    "optionB": 'that 2',
  },
  {
    "category": "students",
    "optionA": 'this 3',
    "optionB": 'that 3',
  },
  {
    "category": "students",
    "optionA": 'this 4',
    "optionB": 'that 4',
  },
  {
    "category": "students",
    "optionA": 'this 5',
    "optionB": 'that 5',
  },
  {
    "category": "students",
    "optionA": 'this 6',
    "optionB": 'that 6',
  },
  {
    "category": "students",
    "optionA": 'this 7',
    "optionB": 'that 7',
  },
  {
    "category": "students",
    "optionA": 'this 8',
    "optionB": 'that 8',
  },
  {
    "category": "students",
    "optionA": 'this 9',
    "optionB": 'that 9',
  },
  {
    "category": "students",
    "optionA": 'this 10',
    "optionB": 'that 10',
  },
  {
    "category": "friends",
    "optionA": 'this 1',
    "optionB": 'that 1',
  },
  {
    "category": "friends",
    "optionA": 'this 2',
    "optionB": 'that 2',
  },
  {
    "category": "friends",
    "optionA": 'this 3',
    "optionB": 'that 3',
  },
  {
    "category": "friends",
    "optionA": 'this 4',
    "optionB": 'that 4',
  },
  {
    "category": "friends",
    "optionA": 'this 5',
    "optionB": 'that 5',
  },
  {
    "category": "friends",
    "optionA": 'this 6',
    "optionB": 'that 6',
  },
  {
    "category": "friends",
    "optionA": 'this 7',
    "optionB": 'that 7',
  },
  {
    "category": "friends",
    "optionA": 'this 8',
    "optionB": 'that 8',
  },
  {
    "category": "friends",
    "optionA": 'this 9',
    "optionB": 'that 9',
  },
  {
    "category": "friends",
    "optionA": 'this 10',
    "optionB": 'that 10',
  },

]


def add_ThisOrThat():
    try:
        print("try ThisOrThat que")
        if len(ThisOrThat.objects.all()):
            print("ThisOrThat que already have que")
            return 0

        for data in ThisOrThat_que:
            print("ThisOrThat que added")
            ThisOrThat.objects.create(
                category = data["category"],
                optionA = data["optionA"],
                optionB = data["optionB"],
            )
        print("try ThisOrThat que complete")
    except:
        print("except in ThisOrThat que")
        pass

def add_WouldYouRather():
    try:
        print("try WouldYouRather que")
        if len(WouldYouRather.objects.all()):
            print("WouldYouRather que already have que")
            return 0

        for data in WouldYouRather_que:
            print("WouldYouRather que added")
            WouldYouRather.objects.create(
                category = data["category"],
                optionA = data["optionA"],
                optionB = data["optionB"],
            )
        print("try WouldYouRather que complete")
    except:
        print("except in WouldYouRather que")
        pass


def add_data():
    print("Two Options Que")
    add_ThisOrThat()
    add_WouldYouRather()

