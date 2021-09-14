from .models import *

# change all these before run
# n u l l  =  None
# t r u e  =  True
# f a l s e  =  False
# change all img field with image location (location must be in media folder)

QuizQue=[
  {
    "Question": "⚽ What is xyz's favorite sport?",
    "category": "friends",
    "part1": "⚽ What is",
    "part2": "s favorite sport?",
    "optionA": "🏏 Cricket",
    "optionB": "🎲 Ludo",
    "optionC": "📱 PUBG",
    "optionD": "📱 Subway Surfers"
  },
  {
    "Question": "If xyz could be a superhero for a day, who would it be?",
    "category": "friends",
    "part1": "If",
    "part2": "could be a superhero for a day, who would it be?",
    "optionA": "Ironman",
    "optionB": "Superman",
    "optionC": "Thor",
    "optionD": "Captain America"
  },
  {
    "Question": "�� What is the best gift xyz has received?",
    "category": "friends",
    "part1": "🎁 What is the best gift",
    "part2": "has received?",
    "optionA": "📱 A phone",
    "optionB": "🧳 A surprise trip",
    "optionC": "😘 A kiss from his crush",
    "optionD": "🐻 A pet"
  },
  {
    "Question": "💰 If xyz has one hour to spend 1 million, where do you think he/she'd go first?",
    "category": "friends",
    "part1": "💰 If",
    "part2": "has one hour to spend 1 million, where do you think he/she'd go first?",
    "optionA": "🚗 A luxury car dealership",
    "optionB": "🍲 A luxury restaurant",
    "optionC": "👚 A designer store",
    "optionD": "🗺️ World tour"
  },
  {
    "Question": "��️ What does xyz prefer?",
    "category": "friends",
    "part1": "🗯️ What does",
    "part2": "prefer?",
    "optionA": "💬 Text Message",
    "optionB": "📞 Call",
    "optionC": "💾 Voice mail",
    "optionD": "🤳 Video Chat"
  },
  {
    "Question": "�� Which pet does xyz have?",
    "category": "friends",
    "part1": "🐻 Which pet does",
    "part2": "have?",
    "optionA": "🐕 Dog",
    "optionB": "🐈 Cat",
    "optionC": "🐿️ Squirrel",
    "optionD": "Nothing"
  },
  {
    "Question": "Which device does xyz mostly use?",
    "category": "friends",
    "part1": "Which device does",
    "part2": "mostly use?",
    "optionA": "📱 Mobile",
    "optionB": "💻 Laptop",
    "optionC": "📱 Tablets",
    "optionD": "Nothing"
  },
  {
    "Question": "�� What kind of Ice Cream does xyz prefer to eat?",
    "category": "friends",
    "part1": "🍨 What kind of Ice Cream does",
    "part2": "prefer to eat?",
    "optionA": "Vanilla",
    "optionB": "🍫 Chocolate",
    "optionC": "🍓 Strawberry",
    "optionD": "Bubble Gum"
  },
  {
    "Question": "�� What would xyz rather drink?",
    "category": "friends",
    "part1": "🥛 What would",
    "part2": "rather drink?",
    "optionA": "🍵 Tea",
    "optionB": "☕ Hot Coffee",
    "optionC": "🥤 Cold Coffee",
    "optionD": "🥤 Cold Drink"
  },
  {
    "Question": "Which season is xyz's favorite?",
    "category": "friends",
    "part1": "Which season is",
    "part2": "s favorite?",
    "optionA": "🌧️ Monsoon",
    "optionB": "☀️ Summer",
    "optionC": "🌥️ Spring",
    "optionD": "☃️ Winter"
  },
  {
    "Question": "✈️ If xyz could go anywhere, it would be...",
    "category": "friends",
    "part1": "✈️ If",
    "part2": "could go anywhere, it would be...",
    "optionA": "Paris",
    "optionB": "New York",
    "optionC": "London",
    "optionD": "California"
  },
  {
    "Question": "❌ xyz has never ever...",
    "category": "friends",
    "part1": "❌",
    "part2": "has never ever...",
    "optionA": "🦴 Broken a bone",
    "optionB": "📱🚽 Dropped his/her cellphone in the toilet",
    "optionC": "🥱 Stayed up for more than 24 hours",
    "optionD": "🍕 Ate a whole pizza by himself/herself"
  },
  {
    "Question": "�� What is xyz's favorite color?",
    "category": "friends",
    "part1": "🌈 What is",
    "part2": "s favorite color?",
    "optionA": "Pink",
    "optionB": "🟦 Blue",
    "optionC": "Red",
    "optionD": "Purple"
  },
  {
    "Question": "⛅ What does xyz do first thing in the morning?",
    "category": "friends",
    "part1": "⛅ What does",
    "part2": "do first thing in the morning?",
    "optionA": "🏐 Sport",
    "optionB": "🛀 Showers",
    "optionC": "📱 look at smartphone",
    "optionD": "🤳 Take Selfie"
  },
  {
    "Question": "Which would xyz choose?",
    "category": "friends",
    "part1": "Which would",
    "part2": "choose?",
    "optionA": "⛰️ Mountains",
    "optionB": "🏖️ Beach",
    "optionC": "🧊 Glacier",
    "optionD": "🌲 Jungle"
  },
  {
    "Question": "What is important for xyz?",
    "category": "friends",
    "part1": "What is important for",
    "part2": "?",
    "optionA": "💸 Money",
    "optionB": "😎 Success",
    "optionC": "🏥 Health",
    "optionD": "👩‍❤️‍👨 Love"
  },
  {
    "Question": "�� How does xyz sleep?",
    "category": "friends",
    "part1": "😴 How does",
    "part2": "sleep?",
    "optionA": "on the stomach",
    "optionB": "on the back",
    "optionC": "on the side",
    "optionD": "in sitting position"
  },
  {
    "Question": "�� What food does xyz hate?",
    "category": "friends",
    "part1": "🤢 What food does",
    "part2": "hate?",
    "optionA": "Broccoli",
    "optionB": "Tomatoes",
    "optionC": "🧀 Cheese",
    "optionD": "Spinach"
  },
  {
    "Question": "�� What is the most exciting animal to see at the zoo for xyz?",
    "category": "friends",
    "part1": "🐻 What is the most exciting animal to see at the zoo for",
    "part2": "?",
    "optionA": "🐒 Monkey",
    "optionB": "🐅 Tiger",
    "optionC": "🦒 Giraffe",
    "optionD": "🦜 Parrot"
  },
  {
    "Question": "😔 When sad or upset, what is the best way to comfort xyz?",
    "category": "friends",
    "part1": "😔 When sad or upset, what is the best way to comfort",
    "part2": "?",
    "optionA": "☕ Talking over a cup of coffee",
    "optionB": "🛒 Going shopping",
    "optionC": "🍷 Going for a drink",
    "optionD": "🎥 Watching a movie"
  },
  {
    "Question": "�� What would xyz dare to try?",
    "category": "friends",
    "part1": "😎 What would",
    "part2": "dare to try?",
    "optionA": "Bungee jump",
    "optionB": "Balloon flight",
    "optionC": "Parachute jump",
    "optionD": "Wild roller coaster"
  },
  {
    "Question": "What app does xyz use most often?",
    "category": "friends",
    "part1": "What app does",
    "part2": "use most often?",
    "optionA": "Instagram",
    "optionB": "WhatsApp",
    "optionC": "Facebook",
    "optionD": "Snapchat"
  },
  {
    "Question": "�� During which month is xyz's birthday?",
    "category": "friends",
    "part1": "🎂 During which month is",
    "part2": "s birthday?",
    "optionA": "January, February, or March",
    "optionB": "April, May, or June",
    "optionC": "July, August, or September",
    "optionD": "October, November, or December"
  },
  {
    "Question": "�� What can xyz cook?",
    "category": "friends",
    "part1": "🍲 What can",
    "part2": "cook?",
    "optionA": "Some sophisticated dish I don't even know the name of",
    "optionB": "Pasta",
    "optionC": "Anything you'll ask for!",
    "optionD": "Tea maybe..."
  },
  {
    "Question": "�� What is xyz's biggest fear?",
    "category": "friends",
    "part1": "😨 What is",
    "part2": "s biggest fear?",
    "optionA": "cockroach",
    "optionB": "Snake",
    "optionC": "Blood",
    "optionD": "Flying"
  },
  {
    "Question": "�� What would xyz spend money from the lottery most likely on?",
    "category": "friends",
    "part1": "💰 What would",
    "part2": "spend money from the lottery most likely on?",
    "optionA": "Traveling",
    "optionB": "Food",
    "optionC": "Designer clothes",
    "optionD": "No spending, just investing"
  },
  {
    "Question": "�� What's the perfect birthday celebration for xyz?",
    "category": "friends",
    "part1": "🥳 What's the perfect birthday celebration for",
    "part2": "?",
    "optionA": "Big house party",
    "optionB": "A night out with friends",
    "optionC": "Surprise party",
    "optionD": "Candlelight dinner with a boyfriend/girlfriend"
  },
  {
    "Question": "��‍♂️ What kind of addiction xyz might fall into one day?",
    "category": "friends",
    "part1": "🤦‍♂️ What kind of addiction",
    "part2": "might fall into one day?",
    "optionA": "Alcohol",
    "optionB": "Gaming",
    "optionC": "Shopping",
    "optionD": "Gambling"
  },
  {
    "Question": "�� What talent does xyz have?",
    "category": "friends",
    "part1": "😎 What talent does",
    "part2": "have?",
    "optionA": "Drawing",
    "optionB": "Dancing",
    "optionC": "Singing",
    "optionD": "making people fool"
  },
  {
    "Question": "⏲️ If xyz got a time machine, where he go first?",
    "category": "friends",
    "part1": "⏲️ If",
    "part2": "got a time machine, where he go first?",
    "optionA": "Future",
    "optionB": "Past",
    "optionC": "don't use it",
    "optionD": "give it to you"
  },
  {
    "Question": "�� What magical power would xyz like to possess?",
    "category": "friends",
    "part1": "💪 What magical power would",
    "part2": "like to possess?",
    "optionA": "Time Control",
    "optionB": "Mind reading",
    "optionC": "teleportation",
    "optionD": "hypnotize"
  },
  {
    "Question": "�� What type of movies does xyz like?",
    "category": "friends",
    "part1": "🎥 What type of movies does",
    "part2": "like?",
    "optionA": "Horror",
    "optionB": "Romance",
    "optionC": "Comedy",
    "optionD": "Thriller"
  },
  {
    "Question": "�� What matters most in your life?",
    "category": "friends",
    "part1": "🤨 What is",
    "part2": "s favorite slang term in electronic communications?",
    "optionA": "Money",
    "optionB": "Family",
    "optionC": "Friendship",
    "optionD": "Health"
  },
  {
    "Question": "�� What is xyz's favorite slang term in electronic communications?",
    "category": "friends",
    "part1": "🎥 Who is",
    "part2": "s favorite Bollywood actor?",
    "optionA": "OMG",
    "optionB": "IDK",
    "optionC": "WTF?",
    "optionD": "LOL"
  },
  {
    "Question": "�� Who is xyz's favorite Bollywood actor?",
    "category": "friends",
    "part1": "🎥 Who is",
    "part2": "s favorite Bollywood actress?",
    "optionA": "Shah Rukh Khan",
    "optionB": "Hrithik Roshan",
    "optionC": "Amir khan",
    "optionD": "Kartik Aaryan"
  },
  {
    "Question": "�� Who is xyz's favorite Bollywood actress?",
    "category": "friends",
    "part1": "🎥 If",
    "part2": "s life was a movie, which movie would you choose?",
    "optionA": "Disha Patani",
    "optionB": "Kareena Kapoor",
    "optionC": "Katrina Kaif",
    "optionD": "Kriti Sanon"
  },
  {
    "Question": "🎥 If xyz's life was a movie, which movie would you choose?",
    "category": "friends",
    "part1": "🏫 How many schools has",
    "part2": "gone to?",
    "optionA": "Dil Wale Dulhaniya Le Jayenge",
    "optionB": "Gangs of Wasseypur",
    "optionC": "Shershaah",
    "optionD": "Kabir Singh"
  },
  {
    "Question": "�� How many schools has xyz gone to?",
    "category": "friends",
    "part1": "💀 If",
    "part2": "could be a cartoon character for a day, who would it be?",
    "optionA": 1,
    "optionB": 2,
    "optionC": 3,
    "optionD": 4
  },
  {
    "Question": "💀 If xyz could be a cartoon character for a day, who would it be?",
    "category": "friends",
    "part1": "🍲 If",
    "part2": "had to eat the same food for dinner every day, what would he pick?",
    "optionA": "Tom Cat",
    "optionB": "Jerry Mouse",
    "optionC": "Daffy Duck",
    "optionD": "Mickey Mouse"
  },
  {
    "Question": "🍲 If xyz had to eat the same food for dinner every day, what would he pick?",
    "category": "friends",
    "part1": "🧑‍🤝‍🧑",
    "part2": "is?",
    "optionA": "Burger",
    "optionB": "Sushi",
    "optionC": "Pizza",
    "optionD": "Burrito"
  },
  {
    "Question": "��‍🤝‍🧑 xyz is?",
    "category": "friends",
    "part1": "🎃 Is",
    "part2": "a ?",
    "optionA": "Single",
    "optionB": "Taken",
    "optionC": "heartbroken",
    "optionD": "playboy"
  },
  {
    "Question": "�� Is xyz a ?",
    "category": "friends",
    "part1": "🧛‍♂️ If",
    "part2": "meets a genie, what would be sadfasfd's wish?",
    "optionA": "Morning Person",
    "optionB": "NightOwl",
    "optionC": "Both",
    "optionD": "None"
  },
  {
    "Question": "🧛‍♂️ If xyz meets a genie, what would be sadfasfd's wish?",
    "category": "friends",
    "part1": "🧑‍🤝‍🧑 Does",
    "part2": "want his/her wife/husband to be the Hottest or the Smartest?",
    "optionA": "💸 Rs100 crore",
    "optionB": "💑 Beautiful wife/Handsome Husband",
    "optionC": "👑 To be the king of the world",
    "optionD": "Reduce his age upto 20 years"
  },
  {
    "Question": "��‍🤝‍🧑 Does xyz want his/her wife/husband to be the Hottest or the Smartest?",
    "category": "friends",
    "part1": "✈️ Where would",
    "part2": "like to go with his/her life partner?",
    "optionA": "💖 The Hottest",
    "optionB": "😏 The Smartest",
    "optionC": "Beauty Queen",
    "optionD": "Average"
  },
  {
    "Question": "✈️ Where would xyz like to go with his/her life partner?",
    "category": "friends",
    "part1": "🧑‍🤝‍🧑 Where would",
    "part2": "like to go with",
    "optionA": "🏂 Manali",
    "optionB": "🏖 Goa",
    "optionC": "🏔 Leh and Ladakh",
    "optionD": "⛄ Shimla"
  },
  {
    "Question": "��‍🤝‍🧑 Where would xyz like to go with xyz's soulmate?",
    "category": "friends",
    "part1": "like to go with",
    "part2": "s soulmate?",
    "optionA": "🗼 Paris",
    "optionB": "🏝 Bali",
    "optionC": "🏞 Maldives",
    "optionD": "🌉 Venice"
  },
  {
    "Question": "�� What xyz likes about himself/herself?",
    "category": "friends",
    "part1": "🙃 What",
    "part2": "likes about himself/herself?",
    "optionA": "Looks",
    "optionB": "Attitude",
    "optionC": "Height",
    "optionD": "Beard"
  },
  {
    "Question": "��️ Which website xyz often visit?",
    "category": "friends",
    "part1": "🖥️ Which website",
    "part2": "often visit?",
    "optionA": "Socal media sites",
    "optionB": "Google",
    "optionC": "Dating sites",
    "optionD": "Porn Sites"
  },
  {
    "Question": "How often xyz watch porn",
    "category": "friends",
    "part1": "How often",
    "part2": "watch porn",
    "optionA": "daily",
    "optionB": "weekly",
    "optionC": "twice a day",
    "optionD": "never"
  },
  {
    "Question": "how many Ex xyz have",
    "category": "friends",
    "part1": "how many Ex",
    "part2": "have",
    "optionA": "Zero",
    "optionB": "one",
    "optionC": "two",
    "optionD": "three"
  },
  {
    "Question": "last time when xyz have deram about you",
    "category": "friends",
    "part1": "last time when",
    "part2": "have deram about you",
    "optionA": "last night",
    "optionB": "today",
    "optionC": "week ago",
    "optionD": "month ago"
  },
  {
    "Question": "when last time xyz say sorry to you",
    "category": "friends",
    "part1": "when last time",
    "part2": "say sorry to you",
    "optionA": "in this week",
    "optionB": "in this month",
    "optionC": "today",
    "optionD": "never"
  },
  {
    "Question": "At what age did xyz lose virginity?",
    "category": "friends",
    "part1": "At what age did",
    "part2": "lose virginity?",
    "optionA": "16 years",
    "optionB": "20 years",
    "optionC": "20+ years",
    "optionD": "still a virgin"
  },
  {
    "Question": "How many people have xyz slept with?",
    "category": "friends",
    "part1": "How many people have",
    "part2": "slept with?",
    "optionA": "only with you",
    "optionB": "5+",
    "optionC": 2,
    "optionD": "no one"
  },
  {
    "Question": "What must a perfect evening have?",
    "category": "friends",
    "part1": "What must a perfect evening have?",
    "part2": "",
    "optionA": "🕺 Visit a club",
    "optionB": "🎥 Watch a movie with friends",
    "optionC": "Watch Sports on TV",
    "optionD": "🍽️ Candlelight dinner"
  },
  {
    "Question": "Who is most important?",
    "category": "friends",
    "part1": "Who is most important?",
    "part2": "",
    "optionA": "👪 Family",
    "optionB": "🧑‍🤝‍🧑 Friends",
    "optionC": "👫 Partner",
    "optionD": "Someone else"
  },
  {
    "Question": "⚽ What is xyz's favorite sport?",
    "category": "siblings",
    "part1": "⚽ What is",
    "part2": "s favorite sport?",
    "optionA": "🏏 Cricket",
    "optionB": "🎲 Ludo",
    "optionC": "📱 PUBG",
    "optionD": "📱 Subway Surfers"
  },
  {
    "Question": "If xyz could be a superhero for a day, who would it be?",
    "category": "siblings",
    "part1": "If",
    "part2": "could be a superhero for a day, who would it be?",
    "optionA": "Ironman",
    "optionB": "Superman",
    "optionC": "Thor",
    "optionD": "Captain America"
  },
  {
    "Question": "�� What is the best gift xyz has received?",
    "category": "siblings",
    "part1": "🎁 What is the best gift",
    "part2": "has received?",
    "optionA": "📱 A phone",
    "optionB": "🧳 A surprise trip",
    "optionC": "😘 A kiss from his crush",
    "optionD": "🐻 A pet"
  },
  {
    "Question": "💰 If xyz has one hour to spend 1 million, where do you think he/she'd go first?",
    "category": "siblings",
    "part1": "💰 If",
    "part2": "has one hour to spend 1 million, where do you think he/she'd go first?",
    "optionA": "🚗 A luxury car dealership",
    "optionB": "🍲 A luxury restaurant",
    "optionC": "👚 A designer store",
    "optionD": "🗺️ World tour"
  },
  {
    "Question": "��️ What does xyz prefer?",
    "category": "siblings",
    "part1": "🗯️ What does",
    "part2": "prefer?",
    "optionA": "💬 Text Message",
    "optionB": "📞 Call",
    "optionC": "💾 Voice mail",
    "optionD": "🤳 Video Chat"
  },
  {
    "Question": "�� Which pet does xyz have?",
    "category": "siblings",
    "part1": "🐻 Which pet does",
    "part2": "have?",
    "optionA": "🐕 Dog",
    "optionB": "🐈 Cat",
    "optionC": "🐿️ Squirrel",
    "optionD": "Nothing"
  },
  {
    "Question": "Which device does xyz mostly use?",
    "category": "siblings",
    "part1": "Which device does",
    "part2": "mostly use?",
    "optionA": "📱 Mobile",
    "optionB": "💻 Laptop",
    "optionC": "📱 Tablets",
    "optionD": "Nothing"
  },
  {
    "Question": "�� What kind of Ice Cream does xyz prefer to eat?",
    "category": "siblings",
    "part1": "🍨 What kind of Ice Cream does",
    "part2": "prefer to eat?",
    "optionA": "Vanilla",
    "optionB": "🍫 Chocolate",
    "optionC": "🍓 Strawberry",
    "optionD": "Bubble Gum"
  },
  {
    "Question": "�� What would xyz rather drink?",
    "category": "siblings",
    "part1": "🥛 What would",
    "part2": "rather drink?",
    "optionA": "🍵 Tea",
    "optionB": "☕ Hot Coffee",
    "optionC": "🥤 Cold Coffee",
    "optionD": "🥤 Cold Drink"
  },
  {
    "Question": "Which season is xyz's favorite?",
    "category": "siblings",
    "part1": "Which season is",
    "part2": "s favorite?",
    "optionA": "🌧️ Monsoon",
    "optionB": "☀️ Summer",
    "optionC": "🌥️ Spring",
    "optionD": "☃️ Winter"
  },
  {
    "Question": "✈️ If xyz could go anywhere, it would be...",
    "category": "siblings",
    "part1": "✈️ If",
    "part2": "could go anywhere, it would be...",
    "optionA": "Paris",
    "optionB": "New York",
    "optionC": "London",
    "optionD": "California"
  },
  {
    "Question": "❌ xyz has never ever...",
    "category": "siblings",
    "part1": "❌",
    "part2": "has never ever...",
    "optionA": "🦴 Broken a bone",
    "optionB": "📱🚽 Dropped his/her cellphone in the toilet",
    "optionC": "🥱 Stayed up for more than 24 hours",
    "optionD": "🍕 Ate a whole pizza by himself/herself"
  },
  {
    "Question": "�� What is xyz's favorite color?",
    "category": "siblings",
    "part1": "🌈 What is",
    "part2": "s favorite color?",
    "optionA": "Pink",
    "optionB": "🟦 Blue",
    "optionC": "Red",
    "optionD": "Purple"
  },
  {
    "Question": "⛅ What does xyz do first thing in the morning?",
    "category": "siblings",
    "part1": "⛅ What does",
    "part2": "do first thing in the morning?",
    "optionA": "🏐 Sport",
    "optionB": "🛀 Showers",
    "optionC": "📱 look at smartphone",
    "optionD": "🤳 Take Selfie"
  },
  {
    "Question": "Which would xyz choose?",
    "category": "siblings",
    "part1": "Which would",
    "part2": "choose?",
    "optionA": "⛰️ Mountains",
    "optionB": "🏖️ Beach",
    "optionC": "🧊 Glacier",
    "optionD": "🌲 Jungle"
  },
  {
    "Question": "What is important for xyz?",
    "category": "siblings",
    "part1": "What is important for",
    "part2": "?",
    "optionA": "💸 Money",
    "optionB": "😎 Success",
    "optionC": "🏥 Health",
    "optionD": "👩‍❤️‍👨 Love"
  },
  {
    "Question": "�� How does xyz sleep?",
    "category": "siblings",
    "part1": "😴 How does",
    "part2": "sleep?",
    "optionA": "on the stomach",
    "optionB": "on the back",
    "optionC": "on the side",
    "optionD": "in sitting position"
  },
  {
    "Question": "�� What food does xyz hate?",
    "category": "siblings",
    "part1": "🤢 What food does",
    "part2": "hate?",
    "optionA": "Broccoli",
    "optionB": "Tomatoes",
    "optionC": "🧀 Cheese",
    "optionD": "Spinach"
  },
  {
    "Question": "�� What is the most exciting animal to see at the zoo for xyz?",
    "category": "siblings",
    "part1": "🐻 What is the most exciting animal to see at the zoo for",
    "part2": "?",
    "optionA": "🐒 Monkey",
    "optionB": "🐅 Tiger",
    "optionC": "🦒 Giraffe",
    "optionD": "🦜 Parrot"
  },
  {
    "Question": "😔 When sad or upset, what is the best way to comfort xyz?",
    "category": "siblings",
    "part1": "😔 When sad or upset, what is the best way to comfort",
    "part2": "?",
    "optionA": "☕ Talking over a cup of coffee",
    "optionB": "🛒 Going shopping",
    "optionC": "🍷 Going for a drink",
    "optionD": "🎥 Watching a movie"
  },
  {
    "Question": "�� What would xyz dare to try?",
    "category": "siblings",
    "part1": "😎 What would",
    "part2": "dare to try?",
    "optionA": "Bungee jump",
    "optionB": "Balloon flight",
    "optionC": "Parachute jump",
    "optionD": "Wild roller coaster"
  },
  {
    "Question": "What app does xyz use most often?",
    "category": "siblings",
    "part1": "What app does",
    "part2": "use most often?",
    "optionA": "Instagram",
    "optionB": "WhatsApp",
    "optionC": "Facebook",
    "optionD": "Snapchat"
  },
  {
    "Question": "�� During which month is xyz's birthday?",
    "category": "siblings",
    "part1": "🎂 During which month is",
    "part2": "s birthday?",
    "optionA": "January, February, or March",
    "optionB": "April, May, or June",
    "optionC": "July, August, or September",
    "optionD": "October, November, or December"
  },
  {
    "Question": "�� What can xyz cook?",
    "category": "siblings",
    "part1": "🍲 What can",
    "part2": "cook?",
    "optionA": "Some sophisticated dish I don't even know the name of",
    "optionB": "Pasta",
    "optionC": "Anything you'll ask for!",
    "optionD": "Tea maybe..."
  },
  {
    "Question": "�� What is xyz's biggest fear?",
    "category": "siblings",
    "part1": "😨 What is",
    "part2": "s biggest fear?",
    "optionA": "cockroach",
    "optionB": "Snake",
    "optionC": "Blood",
    "optionD": "Flying"
  },
  {
    "Question": "�� What would xyz spend money from the lottery most likely on?",
    "category": "siblings",
    "part1": "💰 What would",
    "part2": "spend money from the lottery most likely on?",
    "optionA": "Traveling",
    "optionB": "Food",
    "optionC": "Designer clothes",
    "optionD": "No spending, just investing"
  },
  {
    "Question": "�� What's the perfect birthday celebration for xyz?",
    "category": "siblings",
    "part1": "🥳 What's the perfect birthday celebration for",
    "part2": "?",
    "optionA": "Big house party",
    "optionB": "A night out with friends",
    "optionC": "Surprise party",
    "optionD": "Candlelight dinner with a boyfriend/girlfriend"
  },
  {
    "Question": "��‍♂️ What kind of addiction xyz might fall into one day?",
    "category": "siblings",
    "part1": "🤦‍♂️ What kind of addiction",
    "part2": "might fall into one day?",
    "optionA": "Alcohol",
    "optionB": "Gaming",
    "optionC": "Shopping",
    "optionD": "Gambling"
  },
  {
    "Question": "�� What talent does xyz have?",
    "category": "siblings",
    "part1": "😎 What talent does",
    "part2": "have?",
    "optionA": "Drawing",
    "optionB": "Dancing",
    "optionC": "Singing",
    "optionD": "making people fool"
  },
  {
    "Question": "⏲️ If xyz got a time machine, where he go first?",
    "category": "siblings",
    "part1": "⏲️ If",
    "part2": "got a time machine, where he go first?",
    "optionA": "Future",
    "optionB": "Past",
    "optionC": "don't use it",
    "optionD": "give it to you"
  },
  {
    "Question": "�� What magical power would xyz like to possess?",
    "category": "siblings",
    "part1": "💪 What magical power would",
    "part2": "like to possess?",
    "optionA": "Time Control",
    "optionB": "Mind reading",
    "optionC": "teleportation",
    "optionD": "hypnotize"
  },
  {
    "Question": "�� What type of movies does xyz like?",
    "category": "siblings",
    "part1": "🎥 What type of movies does",
    "part2": "like?",
    "optionA": "Horror",
    "optionB": "Romance",
    "optionC": "Comedy",
    "optionD": "Thriller"
  },
  {
    "Question": "�� What matters most in your life?",
    "category": "siblings",
    "part1": "🤨 What is",
    "part2": "s favorite slang term in electronic communications?",
    "optionA": "Money",
    "optionB": "Family",
    "optionC": "Friendship",
    "optionD": "Health"
  },
  {
    "Question": "�� What is xyz's favorite slang term in electronic communications?",
    "category": "siblings",
    "part1": "🎥 Who is",
    "part2": "s favorite Bollywood actor?",
    "optionA": "OMG",
    "optionB": "IDK",
    "optionC": "WTF?",
    "optionD": "LOL"
  },
  {
    "Question": "�� Who is xyz's favorite Bollywood actor?",
    "category": "siblings",
    "part1": "🎥 Who is",
    "part2": "s favorite Bollywood actress?",
    "optionA": "Shah Rukh Khan",
    "optionB": "Hrithik Roshan",
    "optionC": "Amir khan",
    "optionD": "Kartik Aaryan"
  },
  {
    "Question": "�� Who is xyz's favorite Bollywood actress?",
    "category": "siblings",
    "part1": "🎥 If",
    "part2": "s life was a movie, which movie would you choose?",
    "optionA": "Disha Patani",
    "optionB": "Kareena Kapoor",
    "optionC": "Katrina Kaif",
    "optionD": "Kriti Sanon"
  },
  {
    "Question": "🎥 If xyz's life was a movie, which movie would you choose?",
    "category": "siblings",
    "part1": "🏫 How many schools has",
    "part2": "gone to?",
    "optionA": "Dil Wale Dulhaniya Le Jayenge",
    "optionB": "Gangs of Wasseypur",
    "optionC": "Shershaah",
    "optionD": "Kabir Singh"
  },
  {
    "Question": "�� How many schools has xyz gone to?",
    "category": "siblings",
    "part1": "💀 If",
    "part2": "could be a cartoon character for a day, who would it be?",
    "optionA": 1,
    "optionB": 2,
    "optionC": 3,
    "optionD": 4
  },
  {
    "Question": "💀 If xyz could be a cartoon character for a day, who would it be?",
    "category": "siblings",
    "part1": "🍲 If",
    "part2": "had to eat the same food for dinner every day, what would he pick?",
    "optionA": "Tom Cat",
    "optionB": "Jerry Mouse",
    "optionC": "Daffy Duck",
    "optionD": "Mickey Mouse"
  },
  {
    "Question": "🍲 If xyz had to eat the same food for dinner every day, what would he pick?",
    "category": "siblings",
    "part1": "🧑‍🤝‍🧑",
    "part2": "is?",
    "optionA": "Burger",
    "optionB": "Sushi",
    "optionC": "Pizza",
    "optionD": "Burrito"
  },
  {
    "Question": "��‍🤝‍🧑 xyz is?",
    "category": "siblings",
    "part1": "🎃 Is",
    "part2": "a ?",
    "optionA": "Single",
    "optionB": "Taken",
    "optionC": "heartbroken",
    "optionD": "playboy"
  },
  {
    "Question": "�� Is xyz a ?",
    "category": "siblings",
    "part1": "🧛‍♂️ If",
    "part2": "meets a genie, what would be sadfasfd's wish?",
    "optionA": "Morning Person",
    "optionB": "NightOwl",
    "optionC": "Both",
    "optionD": "None"
  },
  {
    "Question": "🧛‍♂️ If xyz meets a genie, what would be sadfasfd's wish?",
    "category": "siblings",
    "part1": "🧑‍🤝‍🧑 Does",
    "part2": "want his/her wife/husband to be the Hottest or the Smartest?",
    "optionA": "💸 Rs100 crore",
    "optionB": "💑 Beautiful wife/Handsome Husband",
    "optionC": "👑 To be the king of the world",
    "optionD": "Reduce his age upto 20 years"
  },
  {
    "Question": "��‍🤝‍🧑 Does xyz want his/her wife/husband to be the Hottest or the Smartest?",
    "category": "siblings",
    "part1": "✈️ Where would",
    "part2": "like to go with his/her life partner?",
    "optionA": "💖 The Hottest",
    "optionB": "😏 The Smartest",
    "optionC": "Beauty Queen",
    "optionD": "Average"
  },
  {
    "Question": "✈️ Where would xyz like to go with his/her life partner?",
    "category": "siblings",
    "part1": "🧑‍🤝‍🧑 Where would",
    "part2": "like to go with",
    "optionA": "🏂 Manali",
    "optionB": "🏖 Goa",
    "optionC": "🏔 Leh and Ladakh",
    "optionD": "⛄ Shimla"
  },
  {
    "Question": "��‍🤝‍🧑 Where would xyz like to go with xyz's soulmate?",
    "category": "siblings",
    "part1": "like to go with",
    "part2": "s soulmate?",
    "optionA": "🗼 Paris",
    "optionB": "🏝 Bali",
    "optionC": "🏞 Maldives",
    "optionD": "🌉 Venice"
  },
  {
    "Question": "�� What xyz likes about himself/herself?",
    "category": "siblings",
    "part1": "🙃 What",
    "part2": "likes about himself/herself?",
    "optionA": "Looks",
    "optionB": "Attitude",
    "optionC": "Height",
    "optionD": "Beard"
  },
  {
    "Question": "��️ Which website xyz often visit?",
    "category": "siblings",
    "part1": "🖥️ Which website",
    "part2": "often visit?",
    "optionA": "Socal media sites",
    "optionB": "Google",
    "optionC": "Dating sites",
    "optionD": "Porn Sites"
  },
  {
    "Question": "How often xyz watch porn",
    "category": "siblings",
    "part1": "How often",
    "part2": "watch porn",
    "optionA": "daily",
    "optionB": "weekly",
    "optionC": "twice a day",
    "optionD": "never"
  },
  {
    "Question": "how many Ex xyz have",
    "category": "siblings",
    "part1": "how many Ex",
    "part2": "have",
    "optionA": "Zero",
    "optionB": "one",
    "optionC": "two",
    "optionD": "three"
  },
  {
    "Question": "last time when xyz have deram about you",
    "category": "siblings",
    "part1": "last time when",
    "part2": "have deram about you",
    "optionA": "last night",
    "optionB": "today",
    "optionC": "week ago",
    "optionD": "month ago"
  },
  {
    "Question": "when last time xyz say sorry to you",
    "category": "siblings",
    "part1": "when last time",
    "part2": "say sorry to you",
    "optionA": "in this week",
    "optionB": "in this month",
    "optionC": "today",
    "optionD": "never"
  },
  {
    "Question": "At what age did xyz lose virginity?",
    "category": "siblings",
    "part1": "At what age did",
    "part2": "lose virginity?",
    "optionA": "16 years",
    "optionB": "20 years",
    "optionC": "20+ years",
    "optionD": "still a virgin"
  },
  {
    "Question": "How many people have xyz slept with?",
    "category": "siblings",
    "part1": "How many people have",
    "part2": "slept with?",
    "optionA": "only with you",
    "optionB": "5+",
    "optionC": 2,
    "optionD": "no one"
  },
  {
    "Question": "What must a perfect evening have?",
    "category": "siblings",
    "part1": "What must a perfect evening have?",
    "part2": "",
    "optionA": "🕺 Visit a club",
    "optionB": "🎥 Watch a movie with friends",
    "optionC": "Watch Sports on TV",
    "optionD": "🍽️ Candlelight dinner"
  },
  {
    "Question": "Who is most important?",
    "category": "siblings",
    "part1": "Who is most important?",
    "part2": "",
    "optionA": "👪 Family",
    "optionB": "🧑‍🤝‍🧑 Friends",
    "optionC": "👫 Partner",
    "optionD": "Someone else"
  },
  {
    "Question": "⚽ What is xyz's favorite sport?",
    "category": "couple",
    "part1": "⚽ What is",
    "part2": "s favorite sport?",
    "optionA": "🏏 Cricket",
    "optionB": "🎲 Ludo",
    "optionC": "📱 PUBG",
    "optionD": "📱 Subway Surfers"
  },
  {
    "Question": "If xyz could be a superhero for a day, who would it be?",
    "category": "couple",
    "part1": "If",
    "part2": "could be a superhero for a day, who would it be?",
    "optionA": "Ironman",
    "optionB": "Superman",
    "optionC": "Thor",
    "optionD": "Captain America"
  },
  {
    "Question": "�� What is the best gift xyz has received?",
    "category": "couple",
    "part1": "🎁 What is the best gift",
    "part2": "has received?",
    "optionA": "📱 A phone",
    "optionB": "🧳 A surprise trip",
    "optionC": "😘 A kiss from his crush",
    "optionD": "🐻 A pet"
  },
  {
    "Question": "💰 If xyz has one hour to spend 1 million, where do you think he/she'd go first?",
    "category": "couple",
    "part1": "💰 If",
    "part2": "has one hour to spend 1 million, where do you think he/she'd go first?",
    "optionA": "🚗 A luxury car dealership",
    "optionB": "🍲 A luxury restaurant",
    "optionC": "👚 A designer store",
    "optionD": "🗺️ World tour"
  },
  {
    "Question": "��️ What does xyz prefer?",
    "category": "couple",
    "part1": "🗯️ What does",
    "part2": "prefer?",
    "optionA": "💬 Text Message",
    "optionB": "📞 Call",
    "optionC": "💾 Voice mail",
    "optionD": "🤳 Video Chat"
  },
  {
    "Question": "�� Which pet does xyz have?",
    "category": "couple",
    "part1": "🐻 Which pet does",
    "part2": "have?",
    "optionA": "🐕 Dog",
    "optionB": "🐈 Cat",
    "optionC": "🐿️ Squirrel",
    "optionD": "Nothing"
  },
  {
    "Question": "Which device does xyz mostly use?",
    "category": "couple",
    "part1": "Which device does",
    "part2": "mostly use?",
    "optionA": "📱 Mobile",
    "optionB": "💻 Laptop",
    "optionC": "📱 Tablets",
    "optionD": "Nothing"
  },
  {
    "Question": "�� What kind of Ice Cream does xyz prefer to eat?",
    "category": "couple",
    "part1": "🍨 What kind of Ice Cream does",
    "part2": "prefer to eat?",
    "optionA": "Vanilla",
    "optionB": "🍫 Chocolate",
    "optionC": "🍓 Strawberry",
    "optionD": "Bubble Gum"
  },
  {
    "Question": "�� What would xyz rather drink?",
    "category": "couple",
    "part1": "🥛 What would",
    "part2": "rather drink?",
    "optionA": "🍵 Tea",
    "optionB": "☕ Hot Coffee",
    "optionC": "🥤 Cold Coffee",
    "optionD": "🥤 Cold Drink"
  },
  {
    "Question": "Which season is xyz's favorite?",
    "category": "couple",
    "part1": "Which season is",
    "part2": "s favorite?",
    "optionA": "🌧️ Monsoon",
    "optionB": "☀️ Summer",
    "optionC": "🌥️ Spring",
    "optionD": "☃️ Winter"
  },
  {
    "Question": "✈️ If xyz could go anywhere, it would be...",
    "category": "couple",
    "part1": "✈️ If",
    "part2": "could go anywhere, it would be...",
    "optionA": "Paris",
    "optionB": "New York",
    "optionC": "London",
    "optionD": "California"
  },
  {
    "Question": "❌ xyz has never ever...",
    "category": "couple",
    "part1": "❌",
    "part2": "has never ever...",
    "optionA": "🦴 Broken a bone",
    "optionB": "📱🚽 Dropped his/her cellphone in the toilet",
    "optionC": "🥱 Stayed up for more than 24 hours",
    "optionD": "🍕 Ate a whole pizza by himself/herself"
  },
  {
    "Question": "�� What is xyz's favorite color?",
    "category": "couple",
    "part1": "🌈 What is",
    "part2": "s favorite color?",
    "optionA": "Pink",
    "optionB": "🟦 Blue",
    "optionC": "Red",
    "optionD": "Purple"
  },
  {
    "Question": "⛅ What does xyz do first thing in the morning?",
    "category": "couple",
    "part1": "⛅ What does",
    "part2": "do first thing in the morning?",
    "optionA": "🏐 Sport",
    "optionB": "🛀 Showers",
    "optionC": "📱 look at smartphone",
    "optionD": "🤳 Take Selfie"
  },
  {
    "Question": "Which would xyz choose?",
    "category": "couple",
    "part1": "Which would",
    "part2": "choose?",
    "optionA": "⛰️ Mountains",
    "optionB": "🏖️ Beach",
    "optionC": "🧊 Glacier",
    "optionD": "🌲 Jungle"
  },
  {
    "Question": "What is important for xyz?",
    "category": "couple",
    "part1": "What is important for",
    "part2": "?",
    "optionA": "💸 Money",
    "optionB": "😎 Success",
    "optionC": "🏥 Health",
    "optionD": "👩‍❤️‍👨 Love"
  },
  {
    "Question": "�� How does xyz sleep?",
    "category": "couple",
    "part1": "😴 How does",
    "part2": "sleep?",
    "optionA": "on the stomach",
    "optionB": "on the back",
    "optionC": "on the side",
    "optionD": "in sitting position"
  },
  {
    "Question": "�� What food does xyz hate?",
    "category": "couple",
    "part1": "🤢 What food does",
    "part2": "hate?",
    "optionA": "Broccoli",
    "optionB": "Tomatoes",
    "optionC": "🧀 Cheese",
    "optionD": "Spinach"
  },
  {
    "Question": "�� What is the most exciting animal to see at the zoo for xyz?",
    "category": "couple",
    "part1": "🐻 What is the most exciting animal to see at the zoo for",
    "part2": "?",
    "optionA": "🐒 Monkey",
    "optionB": "🐅 Tiger",
    "optionC": "🦒 Giraffe",
    "optionD": "🦜 Parrot"
  },
  {
    "Question": "😔 When sad or upset, what is the best way to comfort xyz?",
    "category": "couple",
    "part1": "😔 When sad or upset, what is the best way to comfort",
    "part2": "?",
    "optionA": "☕ Talking over a cup of coffee",
    "optionB": "🛒 Going shopping",
    "optionC": "🍷 Going for a drink",
    "optionD": "🎥 Watching a movie"
  },
  {
    "Question": "�� What would xyz dare to try?",
    "category": "couple",
    "part1": "😎 What would",
    "part2": "dare to try?",
    "optionA": "Bungee jump",
    "optionB": "Balloon flight",
    "optionC": "Parachute jump",
    "optionD": "Wild roller coaster"
  },
  {
    "Question": "What app does xyz use most often?",
    "category": "couple",
    "part1": "What app does",
    "part2": "use most often?",
    "optionA": "Instagram",
    "optionB": "WhatsApp",
    "optionC": "Facebook",
    "optionD": "Snapchat"
  },
  {
    "Question": "�� During which month is xyz's birthday?",
    "category": "couple",
    "part1": "🎂 During which month is",
    "part2": "s birthday?",
    "optionA": "January, February, or March",
    "optionB": "April, May, or June",
    "optionC": "July, August, or September",
    "optionD": "October, November, or December"
  },
  {
    "Question": "�� What can xyz cook?",
    "category": "couple",
    "part1": "🍲 What can",
    "part2": "cook?",
    "optionA": "Some sophisticated dish I don't even know the name of",
    "optionB": "Pasta",
    "optionC": "Anything you'll ask for!",
    "optionD": "Tea maybe..."
  },
  {
    "Question": "�� What is xyz's biggest fear?",
    "category": "couple",
    "part1": "😨 What is",
    "part2": "s biggest fear?",
    "optionA": "cockroach",
    "optionB": "Snake",
    "optionC": "Blood",
    "optionD": "Flying"
  },
  {
    "Question": "�� What would xyz spend money from the lottery most likely on?",
    "category": "couple",
    "part1": "💰 What would",
    "part2": "spend money from the lottery most likely on?",
    "optionA": "Traveling",
    "optionB": "Food",
    "optionC": "Designer clothes",
    "optionD": "No spending, just investing"
  },
  {
    "Question": "�� What's the perfect birthday celebration for xyz?",
    "category": "couple",
    "part1": "🥳 What's the perfect birthday celebration for",
    "part2": "?",
    "optionA": "Big house party",
    "optionB": "A night out with friends",
    "optionC": "Surprise party",
    "optionD": "Candlelight dinner with a boyfriend/girlfriend"
  },
  {
    "Question": "��‍♂️ What kind of addiction xyz might fall into one day?",
    "category": "couple",
    "part1": "🤦‍♂️ What kind of addiction",
    "part2": "might fall into one day?",
    "optionA": "Alcohol",
    "optionB": "Gaming",
    "optionC": "Shopping",
    "optionD": "Gambling"
  },
  {
    "Question": "�� What talent does xyz have?",
    "category": "couple",
    "part1": "😎 What talent does",
    "part2": "have?",
    "optionA": "Drawing",
    "optionB": "Dancing",
    "optionC": "Singing",
    "optionD": "making people fool"
  },
  {
    "Question": "⏲️ If xyz got a time machine, where he go first?",
    "category": "couple",
    "part1": "⏲️ If",
    "part2": "got a time machine, where he go first?",
    "optionA": "Future",
    "optionB": "Past",
    "optionC": "don't use it",
    "optionD": "give it to you"
  },
  {
    "Question": "�� What magical power would xyz like to possess?",
    "category": "couple",
    "part1": "💪 What magical power would",
    "part2": "like to possess?",
    "optionA": "Time Control",
    "optionB": "Mind reading",
    "optionC": "teleportation",
    "optionD": "hypnotize"
  },
  {
    "Question": "�� What type of movies does xyz like?",
    "category": "couple",
    "part1": "🎥 What type of movies does",
    "part2": "like?",
    "optionA": "Horror",
    "optionB": "Romance",
    "optionC": "Comedy",
    "optionD": "Thriller"
  },
  {
    "Question": "�� What matters most in your life?",
    "category": "couple",
    "part1": "🤨 What is",
    "part2": "s favorite slang term in electronic communications?",
    "optionA": "Money",
    "optionB": "Family",
    "optionC": "Friendship",
    "optionD": "Health"
  },
  {
    "Question": "�� What is xyz's favorite slang term in electronic communications?",
    "category": "couple",
    "part1": "🎥 Who is",
    "part2": "s favorite Bollywood actor?",
    "optionA": "OMG",
    "optionB": "IDK",
    "optionC": "WTF?",
    "optionD": "LOL"
  },
  {
    "Question": "�� Who is xyz's favorite Bollywood actor?",
    "category": "couple",
    "part1": "🎥 Who is",
    "part2": "s favorite Bollywood actress?",
    "optionA": "Shah Rukh Khan",
    "optionB": "Hrithik Roshan",
    "optionC": "Amir khan",
    "optionD": "Kartik Aaryan"
  },
  {
    "Question": "�� Who is xyz's favorite Bollywood actress?",
    "category": "couple",
    "part1": "🎥 If",
    "part2": "s life was a movie, which movie would you choose?",
    "optionA": "Disha Patani",
    "optionB": "Kareena Kapoor",
    "optionC": "Katrina Kaif",
    "optionD": "Kriti Sanon"
  },
  {
    "Question": "🎥 If xyz's life was a movie, which movie would you choose?",
    "category": "couple",
    "part1": "🏫 How many schools has",
    "part2": "gone to?",
    "optionA": "Dil Wale Dulhaniya Le Jayenge",
    "optionB": "Gangs of Wasseypur",
    "optionC": "Shershaah",
    "optionD": "Kabir Singh"
  },
  {
    "Question": "�� How many schools has xyz gone to?",
    "category": "couple",
    "part1": "💀 If",
    "part2": "could be a cartoon character for a day, who would it be?",
    "optionA": 1,
    "optionB": 2,
    "optionC": 3,
    "optionD": 4
  },
  {
    "Question": "💀 If xyz could be a cartoon character for a day, who would it be?",
    "category": "couple",
    "part1": "🍲 If",
    "part2": "had to eat the same food for dinner every day, what would he pick?",
    "optionA": "Tom Cat",
    "optionB": "Jerry Mouse",
    "optionC": "Daffy Duck",
    "optionD": "Mickey Mouse"
  },
  {
    "Question": "🍲 If xyz had to eat the same food for dinner every day, what would he pick?",
    "category": "couple",
    "part1": "🧑‍🤝‍🧑",
    "part2": "is?",
    "optionA": "Burger",
    "optionB": "Sushi",
    "optionC": "Pizza",
    "optionD": "Burrito"
  },
  {
    "Question": "��‍🤝‍🧑 xyz is?",
    "category": "couple",
    "part1": "🎃 Is",
    "part2": "a ?",
    "optionA": "Single",
    "optionB": "Taken",
    "optionC": "heartbroken",
    "optionD": "playboy"
  },
  {
    "Question": "�� Is xyz a ?",
    "category": "couple",
    "part1": "🧛‍♂️ If",
    "part2": "meets a genie, what would be sadfasfd's wish?",
    "optionA": "Morning Person",
    "optionB": "NightOwl",
    "optionC": "Both",
    "optionD": "None"
  },
  {
    "Question": "🧛‍♂️ If xyz meets a genie, what would be sadfasfd's wish?",
    "category": "couple",
    "part1": "🧑‍🤝‍🧑 Does",
    "part2": "want his/her wife/husband to be the Hottest or the Smartest?",
    "optionA": "💸 Rs100 crore",
    "optionB": "💑 Beautiful wife/Handsome Husband",
    "optionC": "👑 To be the king of the world",
    "optionD": "Reduce his age upto 20 years"
  },
  {
    "Question": "��‍🤝‍🧑 Does xyz want his/her wife/husband to be the Hottest or the Smartest?",
    "category": "couple",
    "part1": "✈️ Where would",
    "part2": "like to go with his/her life partner?",
    "optionA": "💖 The Hottest",
    "optionB": "😏 The Smartest",
    "optionC": "Beauty Queen",
    "optionD": "Average"
  },
  {
    "Question": "✈️ Where would xyz like to go with his/her life partner?",
    "category": "couple",
    "part1": "🧑‍🤝‍🧑 Where would",
    "part2": "like to go with",
    "optionA": "🏂 Manali",
    "optionB": "🏖 Goa",
    "optionC": "🏔 Leh and Ladakh",
    "optionD": "⛄ Shimla"
  },
  {
    "Question": "��‍🤝‍🧑 Where would xyz like to go with xyz's soulmate?",
    "category": "couple",
    "part1": "like to go with",
    "part2": "s soulmate?",
    "optionA": "🗼 Paris",
    "optionB": "🏝 Bali",
    "optionC": "🏞 Maldives",
    "optionD": "🌉 Venice"
  },
  {
    "Question": "�� What xyz likes about himself/herself?",
    "category": "couple",
    "part1": "🙃 What",
    "part2": "likes about himself/herself?",
    "optionA": "Looks",
    "optionB": "Attitude",
    "optionC": "Height",
    "optionD": "Beard"
  },
  {
    "Question": "��️ Which website xyz often visit?",
    "category": "couple",
    "part1": "🖥️ Which website",
    "part2": "often visit?",
    "optionA": "Socal media sites",
    "optionB": "Google",
    "optionC": "Dating sites",
    "optionD": "Porn Sites"
  },
  {
    "Question": "How often xyz watch porn",
    "category": "couple",
    "part1": "How often",
    "part2": "watch porn",
    "optionA": "daily",
    "optionB": "weekly",
    "optionC": "twice a day",
    "optionD": "never"
  },
  {
    "Question": "which part of your body xyz likes more",
    "category": "couple",
    "part1": "which part of your body",
    "part2": "likes more",
    "optionA": "face",
    "optionB": "chest",
    "optionC": "back",
    "optionD": "legs"
  },
  {
    "Question": "how many Ex xyz have",
    "category": "couple",
    "part1": "how many Ex",
    "part2": "have",
    "optionA": "Zero",
    "optionB": "one",
    "optionC": "two",
    "optionD": "three"
  },
  {
    "Question": "acording to xyz what is the best place for sex",
    "category": "couple",
    "part1": "acording to",
    "part2": "what is the best place for sex",
    "optionA": "Bedroom",
    "optionB": "bathroom",
    "optionC": "kitchen",
    "optionD": "public place"
  },
  {
    "Question": "last time when xyz have deram about you",
    "category": "couple",
    "part1": "last time when",
    "part2": "have deram about you",
    "optionA": "last night",
    "optionB": "today",
    "optionC": "week ago",
    "optionD": "month ago"
  },
  {
    "Question": "what xyz most want form you",
    "category": "couple",
    "part1": "what",
    "part2": "most want form you",
    "optionA": "romance",
    "optionB": "sex",
    "optionC": "friendship",
    "optionD": "money"
  },
  {
    "Question": "when last time xyz say sorry to you",
    "category": "couple",
    "part1": "when last time",
    "part2": "say sorry to you",
    "optionA": "in this week",
    "optionB": "in this month",
    "optionC": "today",
    "optionD": "never"
  },
  {
    "Question": "Where is xyz favorite spot to be kissed?",
    "category": "couple",
    "part1": "Where is",
    "part2": "favorite spot to be kissed?",
    "optionA": "forehead",
    "optionB": "lips",
    "optionC": "hand",
    "optionD": "boobs"
  },
  {
    "Question": "Where is xyz favorite spot to kiss?",
    "category": "couple",
    "part1": "Where is",
    "part2": "favorite spot to kiss?",
    "optionA": "forehead",
    "optionB": "lips",
    "optionC": "hand",
    "optionD": "boobs"
  },
  {
    "Question": "when did xyz realie he/she likes you",
    "category": "couple",
    "part1": "when did",
    "part2": "realie he/she likes you",
    "optionA": "six month ago",
    "optionB": "a year ago",
    "optionC": "first time he/she saw you",
    "optionD": "not remember"
  },
  {
    "Question": "At what age did xyz lose virginity?",
    "category": "couple",
    "part1": "At what age did",
    "part2": "lose virginity?",
    "optionA": "16 years",
    "optionB": "20 years",
    "optionC": "20+ years",
    "optionD": "still a virgin"
  },
  {
    "Question": "How many people have xyz slept with?",
    "category": "couple",
    "part1": "How many people have",
    "part2": "slept with?",
    "optionA": "only with you",
    "optionB": "5+",
    "optionC": 2,
    "optionD": "no one"
  },
  {
    "Question": "What must a perfect evening have?",
    "category": "couple",
    "part1": "What must a perfect evening have?",
    "part2": "",
    "optionA": "🕺 Visit a club",
    "optionB": "🎥 Watch a movie with friends",
    "optionC": "Watch Sports on TV",
    "optionD": "🍽️ Candlelight dinner"
  },
  {
    "Question": "Who is most important?",
    "category": "couple",
    "part1": "Who is most important?",
    "part2": "",
    "optionA": "👪 Family",
    "optionB": "🧑‍🤝‍🧑 Friends",
    "optionC": "👫 Partner",
    "optionD": "Someone else"
  },
  {
    "Question": "If we could be together anywhere right now, where would it be?",
    "category": "couple",
    "part1": "If we could be together anywhere right now, where would it be?",
    "part2": "",
    "optionA": "Your place",
    "optionB": "mountain",
    "optionC": "OYO",
    "optionD": "beach"
  }
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



def add_data():
    print("Quiz")
    add_quizque()
