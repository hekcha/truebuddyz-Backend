from .models import *

# change all these before run
# n u l l  =  None
# t r u e  =  True
# f a l s e  =  False
# change all img field with image location (location must be in media folder)

QuizQue = [
 {
  "Question": "🧜‍♂️ If xyz could be a superhero for a day, who would it be?",
  "part1": "🧜‍♂️ If",
  "part2": "could be a superhero for a day, who would it be?",
  "Friends": 1,
  "Couple": 1,
  "siblings": 1,
  "OptionA": "🎭 Ironman",
  "OptionB": "🎭 Superman",
  "OptionC": "🎭 Thor",
  "OptionD": " 🎭 Captain America"
 },
 {
  "Question": "🎁 What is the best gift xyz has received?",
  "part1": "🎁 What is the best gift",
  "part2": "has received?",
  "Friends": 0,
  "Couple": 0,
  "siblings": 0,
  "OptionA": "📱 A phone",
  "OptionB": "🧳 A surprise trip",
  "OptionC": "😘 Kiss from his crush",
  "OptionD": "🐻 A pet"
 },
 {
  "Question": "💰 If xyz has one hour to spend 1 million, where do you think he\/she'd go first?",
  "part1": "💰 If",
  "part2": "has one hour to spend 1 million, where do you think he\/she'd go first?",
  "Friends": 1,
  "Couple": 1,
  "siblings": 1,
  "OptionA": "🚗 A luxury car dealership",
  "OptionB": "🍲 A luxury restaurant",
  "OptionC": "👚 A designer store",
  "OptionD": "🗺️ World tour"
 },
 {
  "Question": "🗯️ What does xyz prefer?",
  "part1": "🗯️ What does",
  "part2": "prefer?",
  "Friends": 0,
  "Couple": 0,
  "siblings": 0,
  "OptionA": "💬 Text Message",
  "OptionB": "📞 Call",
  "OptionC": "🗣️ Voice mail",
  "OptionD": "🤳 Video Chat"
 },
 {
  "Question": "🐻 Which pet does xyz like?",
  "part1": "🐻 Which pet does",
  "part2": "like?",
  "Friends": 0,
  "Couple": 0,
  "siblings": 1,
  "OptionA": "🐕 Dog",
  "OptionB": "🐈 Cat",
  "OptionC": "🐿️ Squirrel",
  "OptionD": "🚫 Nothing"
 },
 {
  "Question": "🐻 Which pet does xyz like?",
  "part1": "🐻 Which pet does",
  "part2": "like?",
  "Friends": 0,
  "Couple": 1,
  "siblings": 0,
  "OptionA": "😎 You",
  "OptionB": "🐕 Dog",
  "OptionC": "🐈 Cat",
  "OptionD": "🐿️ Squirrel"
 },
 {
  "Question": "🧏 Which device does xyz mostly use?",
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
  "Question": "🥛 What would xyz rather drink?",
  "part1": "🥛 What would",
  "part2": "rather drink?",
  "Friends": 0,
  "Couple": 0,
  "siblings": 1,
  "OptionA": "🍵 Tea",
  "OptionB": "☕ Hot Coffee",
  "OptionC": "🥤 Cold Coffee",
  "OptionD": "🥤 Cold Drink"
 },
 {
  "Question": "🌏 Which season is xyz's favorite?",
  "part1": "🌏 Which season is",
  "part2": "'s favorite?",
  "Friends": 1,
  "Couple": 1,
  "siblings": 0,
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
  "Question": "🚫 xyz has never ever...",
  "part1": "🚫",
  "part2": "has never ever...",
  "Friends": 1,
  "Couple": 0,
  "siblings": 0,
  "OptionA": "🦴 Broken a bone",
  "OptionB": "📱🚽 Dropped his\/her cellphone in the toilet",
  "OptionC": "🥱 Stayed up for more than 24 hours",
  "OptionD": "🍕 Ate a whole pizza by himself\/herself"
 },
 {
  "Question": "🌈 What is xyz's favorite color?",
  "part1": "🌈 What is",
  "part2": "'s favorite color?",
  "Friends": 0,
  "Couple": 0,
  "siblings": 0,
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
  "Couple": 0,
  "siblings": 0,
  "OptionA": "🏋️‍♀️ Exercise",
  "OptionB": "🛀 Showers",
  "OptionC": "📱 Look at smartphone",
  "OptionD": "🤳 Take Selfie"
 },
 {
  "Question": "⛅ What does xyz do first thing in the morning?",
  "part1": "⛅ What does",
  "part2": "do first thing in the morning?",
  "Friends": 0,
  "Couple": 1,
  "siblings": 0,
  "OptionA": "💬 Text You",
  "OptionB": "🛀 Showers",
  "OptionC": "🏋️‍♀️ Exercise",
  "OptionD": "🤳 Take Selfie"
 },
 {
  "Question": "😴 How does xyz sleep?",
  "part1": "😴 How does",
  "part2": "sleep?",
  "Friends": 0,
  "Couple": 1,
  "siblings": 0,
  "OptionA": "🛌 On the stomach",
  "OptionB": "🛌 On the back",
  "OptionC": "🛌 On the side",
  "OptionD": "🙇‍♀️ In sitting position"
 },
 {
  "Question": "🤢 What food does xyz hate?",
  "part1": "🤢 What food does",
  "part2": "hate?",
  "Friends": 1,
  "Couple": 1,
  "siblings": 0,
  "OptionA": "🍛 Broccoli",
  "OptionB": "🥔 Tomatoes",
  "OptionC": "🧀 Cheese",
  "OptionD": "🍲 Spinach"
 },
 {
  "Question": "😔 When sad or upset, what xyz wants most?",
  "part1": "😔 When sad or upset, what",
  "part2": "wants most?",
  "Friends": 0,
  "Couple": 1,
  "siblings": 0,
  "OptionA": "☕ Talking over a cup of coffee",
  "OptionB": "🛒 Going shopping",
  "OptionC": "🗣️ Talk to you",
  "OptionD": "🎥 Watching a movie"
 },
 {
  "Question": "😎 What would xyz dare to try?",
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
  "Question": "📱 What app does xyz use most often?",
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
  "Question": "😨 What is xyz's biggest fear?",
  "part1": "😨 What is",
  "part2": "'s biggest fear?",
  "Friends": 1,
  "Couple": 0,
  "siblings": 1,
  "OptionA": "🦗 Cockroach",
  "OptionB": "🐍 Snake",
  "OptionC": "🩸 Blood",
  "OptionD": "🐕 Dog"
 },
 {
  "Question": "😨 What is xyz's biggest fear?",
  "part1": "😨 What is",
  "part2": "'s biggest fear?",
  "Friends": 0,
  "Couple": 1,
  "siblings": 0,
  "OptionA": "💞 You",
  "OptionB": "🦗 Cockroach",
  "OptionC": "🐍 Snake",
  "OptionD": "🐕 Dog"
 },
 {
  "Question": "🎰 Where would xyz spend money from the lottery most likely on?",
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
  "Question": "🤦‍♂️ What kind of addiction xyz might fall into one day?",
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
  "Question": "⏲️ If xyz got a time machine, where he\/she go first?",
  "part1": "⏲️ If",
  "part2": "got a time machine, where he\/she go first?",
  "Friends": 1,
  "Couple": 0,
  "siblings": 1,
  "OptionA": "⏭️ Future",
  "OptionB": "⏮️ Past",
  "OptionC": "🚫 Don't use it",
  "OptionD": "📧 Give it to you"
 },
 {
  "Question": "💪 What magical power would xyz like to possess?",
  "part1": "💪 What magical power would",
  "part2": "like to possess?",
  "Friends": 1,
  "Couple": 0,
  "siblings": 1,
  "OptionA": "🕐 Time Control",
  "OptionB": "🧠 Mind reading",
  "OptionC": "💺 Teleportation",
  "OptionD": "🙅‍♀️ Hypnotize"
 },
 {
  "Question": "🎥 What type of movies does xyz like?",
  "part1": "🎥 What type of movies does",
  "part2": "like?",
  "Friends": 1,
  "Couple": 0,
  "siblings": 0,
  "OptionA": "🧟‍♀️ Horror",
  "OptionB": "👩‍❤️‍💋‍👨 Romance",
  "OptionC": "🤣 Comedy",
  "OptionD": "😲 Thriller"
 },
 {
  "Question": "😎 What matters most in xyz life?",
  "part1": "😎 What matters most in",
  "part2": "life?",
  "Friends": 1,
  "Couple": 0,
  "siblings": 1,
  "OptionA": "💸 Money",
  "OptionB": "👨‍👩‍👧‍👦 Family",
  "OptionC": "🤝 Friendship",
  "OptionD": "🩺 Health"
 },
 {
  "Question": "😎 What matters most in xyz life?",
  "part1": "😎 What matters most in",
  "part2": "life?",
  "Friends": 0,
  "Couple": 1,
  "siblings": 0,
  "OptionA": "💸 Money",
  "OptionB": "👨‍👩‍👧‍👦 Family",
  "OptionC": "🤝 Friendship",
  "OptionD": "💗 You"
 },
 {
  "Question": "🎥 If xyz's life was a movie, which movie would You choose?",
  "part1": "🎥 If",
  "part2": "'s life was a movie, which movie would You choose?",
  "Friends": 1,
  "Couple": 0,
  "siblings": 1,
  "OptionA": "👰‍♀ Dil Wale Dulhaniya Le Jayenge",
  "OptionB": "🧔 Gangs of Wasseypur",
  "OptionC": "👮‍♂️ Shershaah",
  "OptionD": "🧑‍⚕️ Kabir Singh"
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
  "Question": "🧑‍🤝‍🧑 xyz is?",
  "part1": "🧑‍🤝‍🧑",
  "part2": "is?",
  "Friends": 0,
  "Couple": 0,
  "siblings": 1,
  "OptionA": "🧍‍♀️ Single",
  "OptionB": "👫 Taken",
  "OptionC": "💔 Heartbroken",
  "OptionD": "🧍‍♂️🤤 Playboy\/ 🧍‍♀️🤤 Playgirl"
 },
 {
  "Question": "🎃 Is xyz a?",
  "part1": "🎃 Is",
  "part2": "a?",
  "Friends": 1,
  "Couple": 0,
  "siblings": 1,
  "OptionA": "🌝 Morning Person",
  "OptionB": "🌚 NightOwl",
  "OptionC": "🌗 Both",
  "OptionD": "🌗 None"
 },
 {
  "Question": "🧛‍♂️ If xyz meets a genie, what would he\/she wish?",
  "part1": "🧛‍♂️ If",
  "part2": "meets a genie, what would he\/she wish?",
  "Friends": 1,
  "Couple": 0,
  "siblings": 1,
  "OptionA": "💸 Rs100 crore",
  "OptionB": "💑 Beautiful wife\/Handsome Husband",
  "OptionC": "👑 To be the king of the world",
  "OptionD": "👶 Reduce his age upto 20 years"
 },
 {
  "Question": "✈️ Where would xyz like to go with you?",
  "part1": "✈️ Where would",
  "part2": "like to go with you?",
  "Friends": 0,
  "Couple": 1,
  "siblings": 0,
  "OptionA": "🏂 Manali",
  "OptionB": "🏖 Goa",
  "OptionC": "🏔 Leh and Ladakh",
  "OptionD": "⛄ Shimla"
 },
 {
  "Question": "🙃 What does xyz like about himself\/herself?",
  "part1": "🙃 What does",
  "part2": "like about himself\/herself?",
  "Friends": 1,
  "Couple": 0,
  "siblings": 1,
  "OptionA": "👤 Looks",
  "OptionB": "😎 Attitude",
  "OptionC": "🧍 Height",
  "OptionD": "🧔 Beard"
 },
 {
  "Question": "🧍‍♀️ Which part of your body xyz likes more?",
  "part1": "🧍‍♀️ Which part of your body",
  "part2": "likes more?",
  "Friends": 0,
  "Couple": 1,
  "siblings": 0,
  "OptionA": "👤 Face",
  "OptionB": "👙 Chest",
  "OptionC": "🍑 Ass",
  "OptionD": "👀 Eye"
 },
 {
  "Question": "💔 How many Ex xyz had?",
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
  "Question": "💭 The last time when xyz have dreamed about you?",
  "part1": "💭 The last time when",
  "part2": "have dreamed about you?",
  "Friends": 0,
  "Couple": 1,
  "siblings": 0,
  "OptionA": "🕚 Last night",
  "OptionB": "📅 Today",
  "OptionC": "🗓️ Week ago",
  "OptionD": "🗓️ Month ago"
 },
 {
  "Question": "😝 What xyz most want from you?",
  "part1": "😝 What",
  "part2": "most want from you?",
  "Friends": 0,
  "Couple": 1,
  "siblings": 0,
  "OptionA": "👩‍❤️‍💋‍👨 Romance",
  "OptionB": "🤤 Sex",
  "OptionC": "🕐 Time",
  "OptionD": "💸 Money"
 },
 {
  "Question": "🙇‍♀️ When last time xyz say sorry to you?",
  "part1": "🙇‍♀️ When last time",
  "part2": "say sorry to you?",
  "Friends": 0,
  "Couple": 1,
  "siblings": 0,
  "OptionA": "🗓️ In this week",
  "OptionB": "🗓️ In this month",
  "OptionC": "📅 Today",
  "OptionD": "🚫 Never"
 },
 {
  "Question": "💋 Where is xyz favorite spot to be kissed?",
  "part1": "💋 Where is",
  "part2": "favorite spot to be kissed?",
  "Friends": 0,
  "Couple": 1,
  "siblings": 0,
  "OptionA": "👱‍♀️ Forehead",
  "OptionB": "👄 lips",
  "OptionC": "💪 Hand",
  "OptionD": "👙 Boobs"
 },
 {
  "Question": "👩‍❤️‍💋‍👨 When did xyz realize he\/she likes you?",
  "part1": "👩‍❤️‍💋‍👨 When did",
  "part2": "realize he\/she likes you?",
  "Friends": 0,
  "Couple": 1,
  "siblings": 0,
  "OptionA": "6️⃣ Six months ago",
  "OptionB": "1️⃣2️⃣ A year ago",
  "OptionC": "▶️ The first time he\/she saw you",
  "OptionD": "🤔 Not remember"
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
