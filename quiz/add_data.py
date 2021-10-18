from .models import *

# change all these before run
# n u l l  =  None
# t r u e  =  True
# f a l s e  =  False
# change all img field with image location (location must be in media folder)

QuizQue=[
  {
    "Question": "�� What game xyz like the most?",
    "part1": "🎮 What game",
    "part2": "like the most?",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "🏏 Cricket",
    "OptionB": "🎲 Ludo",
    "OptionC": "📱 PUBG",
    "OptionD": "🕹️ Play station"
  },
  {
    "Question": "🧜‍♂️ If xyz could be a superhero for a day, who would it be?",
    "part1": "🧜‍♂️ If",
    "part2": "could be a superhero for a day, who would it be?",
    "Friends": 1,
    "Couple": 1,
    "siblings": 1,
    "OptionA": "🎭 Ironman",
    "OptionB": "🎭 Wonder woman",
    "OptionC": "🎭 Thor",
    "OptionD": "🎭 Captain Marvel"
  },
  {
    "Question": "�� What is the best gift xyz has received?",
    "part1": "🎁 What is the best gift",
    "part2": "has received?",
    "Friends": "",
    "Couple": 1,
    "siblings": 1,
    "OptionA": "📱 A phone",
    "OptionB": "🧳 A surprise trip",
    "OptionC": "😘Kiss from  crush",
    "OptionD": "🐻 A pet"
  },
  {
    "Question": "💰 If xyz has one hour to spend 1 million, where do you think he/she'd go first?",
    "part1": "💰 If",
    "part2": "has one hour to spend 1 million, where do you think he/she'd go first?",
    "Friends": 1,
    "Couple": 1,
    "siblings": 1,
    "OptionA": "🚗 A luxury car dealership",
    "OptionB": "🍲 A luxury restaurant",
    "OptionC": "👚 A designer store",
    "OptionD": "🗺️ World tour"
  },
  {
    "Question": "��️ What does xyz prefer?",
    "part1": "🗯️ What does",
    "part2": "prefer?",
    "Friends": 1,
    "Couple": 1,
    "siblings": 1,
    "OptionA": "💬 Text Message",
    "OptionB": "📞 Call",
    "OptionC": "🗣️ Voice mail",
    "OptionD": "🤳 Video Chat"
  },
  {
    "Question": "�� Which pet does xyz like?",
    "part1": "🐻 Which pet does",
    "part2": "like?",
    "Friends": "",
    "Couple": "",
    "siblings": 1,
    "OptionA": "🐕 Dog",
    "OptionB": "🐈 Cat",
    "OptionC": "🐿️ Squirrel",
    "OptionD": "🚫 Nothing"
  },
  {
    "Question": "�� Which pet does xyz like?",
    "part1": "🐻 Which pet does",
    "part2": "like?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "😎 You",
    "OptionB": "🐕 Dog",
    "OptionC": "🐈 Cat",
    "OptionD": "🐿️ Squirrel"
  },
  {
    "Question": "�� Which device does xyz mostly use?",
    "part1": "🧏 Which device does",
    "part2": "mostly use?",
    "Friends": 1,
    "Couple": 1,
    "siblings": 1,
    "OptionA": "📱 Mobile",
    "OptionB": "💻 Laptop",
    "OptionC": "📱 Tablets",
    "OptionD": "🚫 Nothing"
  },
  {
    "Question": "�� What kind of Ice Cream does xyz prefer to eat?",
    "part1": "🍨 What kind of Ice Cream does",
    "part2": "prefer to eat?",
    "Friends": 1,
    "Couple": 1,
    "siblings": "",
    "OptionA": "🍧 Vanilla",
    "OptionB": "🍫 Chocolate",
    "OptionC": "🍓 Strawberry",
    "OptionD": "🍧 ButterScotch"
  },
  {
    "Question": "�� What would xyz rather drink?",
    "part1": "🥛 What would",
    "part2": "rather drink?",
    "Friends": "",
    "Couple": "",
    "siblings": 1,
    "OptionA": "🍵 Tea",
    "OptionB": "☕ Coffee",
    "OptionC": "🍺Beer",
    "OptionD": "🥤 Cold Drink"
  },
  {
    "Question": "�� What would xyz rather drink?",
    "part1": "🥛 What would",
    "part2": "rather drink?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "💞 Your Blood",
    "OptionB": "🍵 Tea",
    "OptionC": "☕ Coffee",
    "OptionD": "🍺Beer"
  },
  {
    "Question": "�� Which season is xyz's favorite?",
    "part1": "🌏 Which season is",
    "part2": "s favorite?",
    "Friends": 1,
    "Couple": 1,
    "siblings": "",
    "OptionA": "🌧️ Monsoon",
    "OptionB": "☀️ Summer",
    "OptionC": "🌥️ Spring",
    "OptionD": "☃️ Winter"
  },
  {
    "Question": "✈️ If xyz could go anywhere, it would be...",
    "part1": "✈️ If",
    "part2": "could go anywhere, it would be...",
    "Friends": 1,
    "Couple": 1,
    "siblings": 1,
    "OptionA": "🗼 Paris",
    "OptionB": "🏝 Bali",
    "OptionC": "🏞 Maldives",
    "OptionD": "🌉 Venice"
  },
  {
    "Question": "�� xyz has never ever...",
    "part1": "🚫",
    "part2": "has never ever...",
    "Friends": 1,
    "Couple": "",
    "siblings": "",
    "OptionA": "🦴 Broken a bone",
    "OptionB": "📱🚽 Dropped his/her cellphone in the toilet",
    "OptionC": "🥱 Stayed up for more than 24 hours",
    "OptionD": "🍕 Ate a whole pizza by himself/herself"
  },
  {
    "Question": "�� xyz has never ever...",
    "part1": "🚫",
    "part2": "has never ever...",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "🦴 Broken a bone",
    "OptionB": "💋 Kissed you on lips",
    "OptionC": "🤳 Made a Insta reel",
    "OptionD": "🍕 Ate a whole pizza by himself/herself"
  },
  {
    "Question": "�� What is xyz's favorite color?",
    "part1": "🌈 What is",
    "part2": "s favorite color?",
    "Friends": "",
    "Couple": "",
    "siblings": "",
    "OptionA": "🟨 Yellow",
    "OptionB": "🟦 Blue",
    "OptionC": "🟥 Red",
    "OptionD": "🟦 Purple"
  },
  {
    "Question": "⛅ What does xyz do first thing in the morning?",
    "part1": "⛅ What does",
    "part2": "do first thing in the morning?",
    "Friends": 1,
    "Couple": "",
    "siblings": "",
    "OptionA": "🏋️‍♀️ Exercise",
    "OptionB": "🛀 Showers",
    "OptionC": "📱 Look at smartphone",
    "OptionD": "🤳 Take Selfie"
  },
  {
    "Question": "⛅ What does xyz do first thing in the morning?",
    "part1": "⛅ What does",
    "part2": "do first thing in the morning?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "💬 Text You",
    "OptionB": "🛀 Showers",
    "OptionC": "🏋️‍♀️ Exercise",
    "OptionD": "🤳 Take Selfie"
  },
  {
    "Question": "�� Which would xyz choose?",
    "part1": "🌏 Which would",
    "part2": "choose?",
    "Friends": "",
    "Couple": "",
    "siblings": 1,
    "OptionA": "⛰️ Mountains",
    "OptionB": "🏖️ Beach",
    "OptionC": "🧊 Glacier",
    "OptionD": "🌲 Jungle"
  },
  {
    "Question": "�� How does xyz sleep?",
    "part1": "😴 How does",
    "part2": "sleep?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "🛌 On the stomach",
    "OptionB": "🛌 On the back",
    "OptionC": "🛌 On the side",
    "OptionD": "🙇‍♀️ In sitting position"
  },
  {
    "Question": "�� What food does xyz hate?",
    "part1": "🤢 What food does",
    "part2": "hate?",
    "Friends": 1,
    "Couple": 1,
    "siblings": "",
    "OptionA": "🍛 Broccoli",
    "OptionB": "🥔 Tomatoes",
    "OptionC": "🧀 Cheese",
    "OptionD": "🍲 Spinach"
  },
  {
    "Question": "�� What is the most exciting animal to see at the zoo for xyz?",
    "part1": "🐻 What is the most exciting animal to see at the zoo for",
    "part2": "?",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "🐒 Monkey",
    "OptionB": "🐅 Tiger",
    "OptionC": "🦒 Giraffe",
    "OptionD": "🐍 Snake"
  },
  {
    "Question": "😔 When sad or upset, what xyz wants most?",
    "part1": "😔 When sad or upset, what",
    "part2": "wants most?",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "☕ Talking over a cup of coffee",
    "OptionB": "😴 Sleep",
    "OptionC": "🗣️ Talk to someone",
    "OptionD": "🎥 Watching a movie"
  },
  {
    "Question": "😔 When sad or upset, what xyz wants most?",
    "part1": "😔 When sad or upset, what",
    "part2": "wants most?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "☕ Talking over a cup of coffee",
    "OptionB": "🛒 Going shopping",
    "OptionC": "🗣️ Talk to you",
    "OptionD": "🎥 Watching a movie"
  },
  {
    "Question": "�� What would xyz dare to try?",
    "part1": "😎 What would",
    "part2": "dare to try?",
    "Friends": 1,
    "Couple": 1,
    "siblings": 1,
    "OptionA": "😨 Bungee jump",
    "OptionB": "😱 Balloon flight",
    "OptionC": "😨 Parachute jump",
    "OptionD": "🎢 Wild roller coaster"
  },
  {
    "Question": "�� What app does xyz use most often?",
    "part1": "📱 What app does",
    "part2": "use most often?",
    "Friends": 1,
    "Couple": 1,
    "siblings": 1,
    "OptionA": "📱 Instagram",
    "OptionB": "📱 WhatsApp",
    "OptionC": "📱 Facebook",
    "OptionD": "📱 Snapchat"
  },
  {
    "Question": "�� What can xyz cook?",
    "part1": "🍲 What can",
    "part2": "cook?",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "🍘 Some sophisticated dish I don't even know the name of",
    "OptionB": "🍲 Pasta",
    "OptionC": "🍱 Anything you'll ask for!",
    "OptionD": "☕ Tea maybe..."
  },
  {
    "Question": "�� What can xyz cook for you?",
    "part1": "🍲 What can",
    "part2": "cook for you?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "🍘 Some sophisticated dish I don't even know the name of",
    "OptionB": "🍱 Anything you'll ask for!",
    "OptionC": "☕ Tea maybe...",
    "OptionD": "🚫 Nothing"
  },
  {
    "Question": "�� What is xyz's biggest fear?",
    "part1": "😨 What is",
    "part2": "s biggest fear?",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "🦗 Cockroach",
    "OptionB": "🐍 Snake",
    "OptionC": "🩸 Blood",
    "OptionD": "🐕 Dog"
  },
  {
    "Question": "�� What is xyz's biggest fear?",
    "part1": "😨 What is",
    "part2": "s biggest fear?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "💞 You",
    "OptionB": "🦗 Cockroach",
    "OptionC": "🐍 Snake",
    "OptionD": "🐕 Dog"
  },
  {
    "Question": "�� Where would xyz spend money from the lottery most likely on?",
    "part1": "🎰 Where would",
    "part2": "spend money from the lottery most likely on?",
    "Friends": 1,
    "Couple": 1,
    "siblings": 1,
    "OptionA": "✈️ Traveling",
    "OptionB": "🍲 Food",
    "OptionC": "👗 Designer clothes",
    "OptionD": "🏦 No spending, just investing"
  },
  {
    "Question": "�� What's the perfect birthday celebration for xyz?",
    "part1": "🥳 What's the perfect birthday celebration for",
    "part2": "?",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "🏤 Big house party",
    "OptionB": "🌚 A night out with friends",
    "OptionC": "🎷 Surprise party",
    "OptionD": "🥳 A small party with close friends"
  },
  {
    "Question": "�� What's the perfect birthday celebration for xyz?",
    "part1": "🥳 What's the perfect birthday celebration for",
    "part2": "?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "🏤 Big house party",
    "OptionB": "🌚 A night out with you",
    "OptionC": "🤤 Spending quality night with you",
    "OptionD": "🕯️ 🍽️ Candlelight dinner with you"
  },
  {
    "Question": "��‍♂️ What kind of addiction xyz might fall into one day?",
    "part1": "🤦‍♂️ What kind of addiction",
    "part2": "might fall into one day?",
    "Friends": 1,
    "Couple": 1,
    "siblings": 1,
    "OptionA": "🥃 Alcohol",
    "OptionB": "🎮 Gaming",
    "OptionC": "🛒 Shopping",
    "OptionD": "♣️ Gambling"
  },
  {
    "Question": "�� What talent does xyz have?",
    "part1": "😎 What talent does",
    "part2": "have?",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "🎴 Drawing",
    "OptionB": "💃 Dancing",
    "OptionC": "🎻 Singing",
    "OptionD": "🤹🏻‍♂️ Making people fool"
  },
  {
    "Question": "⏲️ If xyz got a time machine, what will he/she do first?",
    "part1": "⏲️ If",
    "part2": "got a time machine, what will he/she do first?",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "⏭️ Future",
    "OptionB": "⏮️ Past",
    "OptionC": "©️ Patent it",
    "OptionD": "🚫 Don't use it"
  },
  {
    "Question": "�� What magical power would xyz like to possess?",
    "part1": "💪 What magical power would",
    "part2": "like to possess?",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "🕐 Time Control",
    "OptionB": "🧠 Mind reading",
    "OptionC": "💺 Teleportation",
    "OptionD": "🙅‍♀️ Object Control"
  },
  {
    "Question": "�� What matters most in xyz life?",
    "part1": "😎 What matters most in",
    "part2": "life?",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "💸 Money",
    "OptionB": "👨‍👩‍👧‍👦 Family",
    "OptionC": "🤝 Friendship",
    "OptionD": "🩺 Health"
  },
  {
    "Question": "�� What matters most in xyz life?",
    "part1": "😎 What matters most in",
    "part2": "life?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "💸 Money",
    "OptionB": "👨‍👩‍👧‍👦 Family",
    "OptionC": "🤝 Friendship",
    "OptionD": "💗 You"
  },
  {
    "Question": "�� What is more important for xyz than you?",
    "part1": "😎 What is more important for",
    "part2": "than you?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "💸 Money",
    "OptionB": "👨‍👩‍👧‍👦 Family",
    "OptionC": "🤝 Friendship",
    "OptionD": "🩺 Health"
  },
  {
    "Question": "�� What is more important for xyz than you?",
    "part1": "😎 What is more important for",
    "part2": "than you?",
    "Friends": 1,
    "Couple": "",
    "siblings": "",
    "OptionA": "💸 Money",
    "OptionB": "👨‍👩‍👧‍👦 Family",
    "OptionC": "🤝 Love",
    "OptionD": "🩺 Health"
  },
  {
    "Question": "�� What is xyz favorite slang term in electronic communications?",
    "part1": "🤨 What is",
    "part2": "favorite slang term in electronic communications?",
    "Friends": 1,
    "Couple": 1,
    "siblings": 1,
    "OptionA": "🙆‍♀️ OMG",
    "OptionB": "🤷‍♀️ IDK",
    "OptionC": "🤬 WTF?",
    "OptionD": "🤦‍♀️ LOL"
  },
  {
    "Question": "�� Who is xyz's favorite Bollywood actor?",
    "part1": "🎥 Who is",
    "part2": "s favorite Bollywood actor?",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "👱‍♂️ Shah Rukh Khan",
    "OptionB": "👱‍♂️ Hrithik Roshan",
    "OptionC": "👱‍♂️ Amir khan",
    "OptionD": "👱‍♂️ Kartik Aaryan"
  },
  {
    "Question": "�� Who is xyz's favorite Bollywood actress?",
    "part1": "🎥 Who is",
    "part2": "s favorite Bollywood actress?",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "👱‍♀️ Disha Patani",
    "OptionB": "👱‍♀️ Kareena Kapoor",
    "OptionC": "👱‍♀️ Katrina Kaif",
    "OptionD": "👱‍♀️ Kriti Sanon"
  },
  {
    "Question": "🎥 If xyz's life was a movie, which movie would You choose?",
    "part1": "🎥 If",
    "part2": "s life was a movie, which movie would You choose?",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "👰‍♀ Dil Wale Dulhaniya Le Jayenge",
    "OptionB": "🧔 Gangs of Wasseypur",
    "OptionC": "👮‍♂️ Shershaah",
    "OptionD": "🧑‍⚕️ Kabir Singh"
  },
  {
    "Question": "�� How many schools has xyz gone to?",
    "part1": "🏫 How many schools has",
    "part2": "gone to?",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "1️⃣ One",
    "OptionB": "2️⃣ Two",
    "OptionC": "3️⃣ Three",
    "OptionD": "4️⃣ Four"
  },
  {
    "Question": "💀 If xyz could be a cartoon character for a day, who would it be?",
    "part1": "💀 If",
    "part2": "could be a cartoon character for a day, who would it be?",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "😎 Johny Bravo",
    "OptionB": "🤓 Minion",
    "OptionC": "🦝 Smurf",
    "OptionD": "❄️ Elsa (Frozen)"
  },
  {
    "Question": "🍲 If xyz had to eat the same food for dinner every day, what would he pick?",
    "part1": "🍲 If",
    "part2": "had to eat the same food for dinner every day, what would he pick?",
    "Friends": 1,
    "Couple": 1,
    "siblings": 1,
    "OptionA": "🍔 Burger",
    "OptionB": "🍲 Sushi",
    "OptionC": "🍕 Pizza",
    "OptionD": "🍗 Chicken"
  },
  {
    "Question": "��‍🤝‍🧑 xyz is?",
    "part1": "🧑‍🤝‍🧑",
    "part2": "is?",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "🧍‍♀️ Single",
    "OptionB": "👫 Taken",
    "OptionC": "💔 Heartbroken",
    "OptionD": "🧍‍♂️🤤 Playboy/ 🧍‍♀️🤤 Playgirl"
  },
  {
    "Question": "�� Is xyz a?",
    "part1": "🎃 Is",
    "part2": "a?",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "🌝 Morning Person",
    "OptionB": "🌚 NightOwl",
    "OptionC": "🌗 Both",
    "OptionD": "🌗 None"
  },
  {
    "Question": "🧛‍♂️ If xyz meets a genie, what would he/she wish?",
    "part1": "🧛‍♂️ If",
    "part2": "meets a genie, what would he/she wish?",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "💸 Rs100 crore",
    "OptionB": "💑 Beautiful wife/Handsome Husband",
    "OptionC": "👑 To be the king of the world",
    "OptionD": "👶 Reduce his age upto 20 years"
  },
  {
    "Question": "��‍🤝‍🧑 Does xyz want his/her wife/husband to be the Hottest or the Smartest?",
    "part1": "🧑‍🤝‍🧑 Does",
    "part2": "want his/her wife/husband to be the Hottest or the Smartest?",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "😎 The Hottest",
    "OptionB": "👩‍💼 The Smartest",
    "OptionC": "👸 Beauty Queen/ 🤴 King",
    "OptionD": "👩‍⚕️ Doctor"
  },
  {
    "Question": "✈️ Where would xyz like to go with his/her life partner?",
    "part1": "✈️ Where would",
    "part2": "like to go with his/her life partner?",
    "Friends": 1,
    "Couple": "",
    "siblings": "",
    "OptionA": "🏂 Manali",
    "OptionB": "🏖 Goa",
    "OptionC": "🏝 Bali",
    "OptionD": "🗼 Paris"
  },
  {
    "Question": "✈️ Where would xyz like to go with you?",
    "part1": "✈️ Where would",
    "part2": "like to go with you?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "🏂 Manali",
    "OptionB": "🏖 Goa",
    "OptionC": "🏝 Bali",
    "OptionD": "🗼 Paris"
  },
  {
    "Question": "��️ Which website xyz often visit?",
    "part1": "🖥️ Which website",
    "part2": "often visit?",
    "Friends": 1,
    "Couple": 1,
    "siblings": "",
    "OptionA": "💬 Social media sites",
    "OptionB": "🔍 Google",
    "OptionC": "💗 Dating sites",
    "OptionD": "🔞 Porn Sites"
  },
  {
    "Question": "✊ How often xyz watch porn?",
    "part1": "✊ How often",
    "part2": "watch porn?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "🤤 Daily",
    "OptionB": "🤤 Weekly",
    "OptionC": "🤤 Twice a day",
    "OptionD": "🚫 Never"
  },
  {
    "Question": "��‍♀️ Which part of your body xyz likes more?",
    "part1": "🧍‍♀️ Which part of your body",
    "part2": "likes more?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "👤 Face",
    "OptionB": "👙 Chest",
    "OptionC": "🍑 Ass",
    "OptionD": "👀 Eye"
  },
  {
    "Question": "�� How many Ex xyz had?",
    "part1": "💔 How many Ex",
    "part2": "had?",
    "Friends": 1,
    "Couple": 1,
    "siblings": 1,
    "OptionA": "0️⃣ Zero",
    "OptionB": "1️⃣ One",
    "OptionC": "2️⃣ Two",
    "OptionD": "3️⃣ Three"
  },
  {
    "Question": "�� According to xyz what is the best place for sex?",
    "part1": "👫 According to",
    "part2": "what is the best place for sex?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "🛋️ Couch",
    "OptionB": "🚿 Bathroom",
    "OptionC": "🥘 Kitchen",
    "OptionD": "🅿️ Parking"
  },
  {
    "Question": "�� The last time when xyz have dreamed about you?",
    "part1": "💭 The last time when",
    "part2": "have dreamed about you?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "🕚 Last night",
    "OptionB": "📅 Today",
    "OptionC": "🗓️ Week ago",
    "OptionD": "🗓️ Month ago"
  },
  {
    "Question": "�� What xyz most want from you?",
    "part1": "😝 What",
    "part2": "most want from you?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "👩‍❤️‍💋‍👨 Romance",
    "OptionB": "🤤 Sex",
    "OptionC": "🕐 Time",
    "OptionD": "💸 Life-time commitment"
  },
  {
    "Question": "��‍♀️ When last time xyz say sorry to you?",
    "part1": "🙇‍♀️ When last time",
    "part2": "say sorry to you?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "🗓️ In this week",
    "OptionB": "🗓️ In this month",
    "OptionC": "📅 Today",
    "OptionD": "🚫 Never"
  },
  {
    "Question": "�� Where is xyz favorite spot to be kissed?",
    "part1": "💋 Where is",
    "part2": "favorite spot to be kissed?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "👱‍♀️ Forehead",
    "OptionB": "👄 lips",
    "OptionC": "💪 Hand",
    "OptionD": "(.)(.) Boobs"
  },
  {
    "Question": "�� Where is xyz favorite spot to kiss?",
    "part1": "💋 Where is",
    "part2": "favorite spot to kiss?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "👱‍♀️ Forehead",
    "OptionB": "👄 lips",
    "OptionC": "💪 Hand",
    "OptionD": "(.)(.) Boobs"
  },
  {
    "Question": "��‍❤️‍💋‍👨 When did xyz realize he/she likes you?",
    "part1": "👩‍❤️‍💋‍👨 When did",
    "part2": "realize he/she likes you?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "6️⃣ Six months ago",
    "OptionB": "1️⃣2️⃣ A year ago",
    "OptionC": "▶️ Love at first site",
    "OptionD": "🤔 Not remember"
  },
  {
    "Question": "�� At what age did xyz lose virginity?",
    "part1": "🤤 At what age did",
    "part2": "lose virginity?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "1️⃣6️⃣ 16 years",
    "OptionB": "2️⃣0️⃣ 20 years",
    "OptionC": "2️⃣0️⃣➕ 20+ years",
    "OptionD": "❌ Still a virgin"
  },
  {
    "Question": "�� How many people have xyz slept with?",
    "part1": "🛌 How many people have",
    "part2": "slept with?",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "❌ No one",
    "OptionB": "⏹️ Only with you",
    "OptionC": "2️⃣ Two",
    "OptionD": "5️⃣➕ 5+"
  },
  {
    "Question": "�� How many people have xyz slept with?",
    "part1": "🛌 How many people have",
    "part2": "slept with?",
    "Friends": 1,
    "Couple": "",
    "siblings": "",
    "OptionA": "0️⃣ Zero",
    "OptionB": "1️⃣ One",
    "OptionC": "2️⃣ Two",
    "OptionD": "3️⃣ Three"
  },
  {
    "Question": "🌏 If we could be together anywhere right now, where would it be?",
    "part1": "🌏 If we could be together anywhere right now, where would it be?",
    "part2": "",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "🗼 Top of Eiffel tower",
    "OptionB": "🏕️ Hillside",
    "OptionC": "🏪 OYO",
    "OptionD": "🏖️ Beach"
  },
  {
    "Question": "�� What must a perfect Evening have?",
    "part1": "🌚 What must a perfect Evening have?",
    "part2": "",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "👩‍❤️‍💋‍👨 A good date",
    "OptionB": "🌅 Romantic evening at beach",
    "OptionC": "🚘 Long drive with you",
    "OptionD": "🕯️🍽️ Candlelight dinner"
  },
  {
    "Question": "�� What must a perfect Evening have?",
    "part1": "🌚 What must a perfect Evening have?",
    "part2": "",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "🕺 Visit a club",
    "OptionB": "🎥 Watch a movie with friends",
    "OptionC": "👩‍❤️‍💋‍👨 A good date",
    "OptionD": "🕯️🍽️ Candlelight dinner"
  },
  {
    "Question": "�� What must a perfect Night have?",
    "part1": "🌚 What must a perfect Night have?",
    "part2": "",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "🏩 Awesome sex",
    "OptionB": "🎥 Watch a movie with you",
    "OptionC": "👩‍❤️‍💋‍👨 Spending quality time with you",
    "OptionD": "🕯️🍽️ Candlelight dinner"
  },
  {
    "Question": "�� What must a perfect Night have?",
    "part1": "🌚 What must a perfect Night have?",
    "part2": "",
    "Friends": 1,
    "Couple": "",
    "siblings": 1,
    "OptionA": "🕺 Visit a nightclub",
    "OptionB": "🎥 Watch a movie",
    "OptionC": "🎉 Party at restaurant",
    "OptionD": "🌚 Night out"
  },
  {
    "Question": "👥 If your body swap with opposite gender, what will be first thing you do?",
    "part1": "👥 If your body swap with opposite gender, what will be first thing you do?",
    "part2": "",
    "Friends": 1,
    "Couple": 1,
    "siblings": "",
    "OptionA": "💦 Self love",
    "OptionB": "🧏‍♀️ Flirt with other",
    "OptionC": "👊 Involve in fights",
    "OptionD": "Check their phone📱 and social media account🔒"
  },
  {
    "Question": "🕥 If you can send a message or a thing to yourself, 2 yr in past .What is it?",
    "part1": "🕥 If you can send a message or a thing to yourself, 2 yr in past .What is it?",
    "part2": "",
    "Friends": 1,
    "Couple": 1,
    "siblings": 1,
    "OptionA": "📈 Stock Market Data",
    "OptionB": "📝 List of your mistakes",
    "OptionC": "📊 Betting results",
    "OptionD": "📑 Question Paper"
  },
  {
    "Question": "👫 If you could only touch me in one place, where would it be",
    "part1": "👫 If you could only touch me in one place, where would it be",
    "part2": "",
    "Friends": "",
    "Couple": 1,
    "siblings": "",
    "OptionA": "👩 Face",
    "OptionB": "(.)(.) Chest",
    "OptionC": "🦵 Thighs",
    "OptionD": "🍑 Ass"
  }
]



def add_friend_quizque():
	print("add_friend_quizque")
	try:
		if len(QuizQuestionBank.objects.all().filter(category='friends')):
			print("add_friend_quizque already have que")
			return 0

		for data in QuizQue:
			if data['Friends']==1:
				print("add_friend_quizque added")
				QuizQuestionBank.objects.create(
					category = 'friends',
					part1 = data["part1"],
					part2 = data["part2"],
					optionA = data["OptionA"],
					optionB = data["OptionB"],
					optionC = data["OptionC"],
					optionD = data["OptionD"],
				)
		print("try add_friend_quizque complete")
	except:
		print("except in add_friend_quizque")
		pass


def add_couple_quizque():
	print("add_couple_quizque")
	try:
		if len(QuizQuestionBank.objects.all().filter(category='couple')):
			print("add_couple_quizque already have que")
			return 0

		for data in QuizQue:
			if data['Couple']==1:
				print("add_couple_quizque added")
				QuizQuestionBank.objects.create(
					category = 'couple',
					part1 = data["part1"],
					part2 = data["part2"],
					optionA = data["OptionA"],
					optionB = data["OptionB"],
					optionC = data["OptionC"],
					optionD = data["OptionD"],
				)
		print("try add_couple_quizque complete")
	except:
		print("except in add_couple_quizque")
		pass


def add_siblings_quizque():
	print("add_siblings_quizque")
	try:
		if len(QuizQuestionBank.objects.all().filter(category='siblings')):
			print("add_siblings_quizque already have que")
			return 0

		for data in QuizQue:
			if data['siblings']==1:
				print("add_siblings_quizque added")
				QuizQuestionBank.objects.create(
					category = 'siblings',
					part1 = data["part1"],
					part2 = data["part2"],
					optionA = data["OptionA"],
					optionB = data["OptionB"],
					optionC = data["OptionC"],
					optionD = data["OptionD"],
				)
		print("try add_siblings_quizque complete")
	except:
		print("except in add_siblings_quizque")
		pass


def add_data():
    print("\nQuiz")
    add_friend_quizque()
    add_couple_quizque()
    add_siblings_quizque()
