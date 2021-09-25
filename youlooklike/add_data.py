from .models import *

# change all these before run
# n u l l  =  None
# t r u e  =  True
# f a l s e  =  False
# change all img field with image location (location must be in media folder)


YouLookLike_data=[
  {
    "category": "naruto",
    "que1": "An assassination attempt was just made on the chief of your village. What do you do?",
    "image1": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2FYLL_NARUTO_q1.gif?alt=media&token=08b32b34-a674-4698-beb8-af76790c6cce",
    "option1A": "Fight Bravely and take control of the situation",
    "option1B": "Will just let the higher authority do their parts",
    "option1C": "Run away from the battlefield",
    "option1D": "Backup with your team and save civilians",
    "que2": "Which justsu you love the most?",
    "image2": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2FYLL_NARUTO_q2.gif?alt=media&token=479455aa-93a0-48c7-a345-3babd3c1be75",
    "option2A": "Ninjutsu",
    "option2B": "Taijutsu",
    "option2C": "Kekkei Genkai",
    "option2D": "Dōjutsu",
    "que3": "What is the most important thing?",
    "image3": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2FYLL_NARUTO_q10.gif?alt=media&token=ff6d3339-866c-4537-9eed-d56de42ca377",
    "option3A": "Friends",
    "option3B": "Power",
    "option3C": "Winning War",
    "option3D": "Intelligence",
    "que4": "Who did you want to train under?",
    "image4": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2FYLL_NARUTO_q13-min.jpg?alt=media&token=b0b04457-2ebf-4a9d-9229-ab826fe0b05c",
    "option4A": "Jiraiya",
    "option4B": "Orochimaru",
    "option4C": "Kakashi",
    "option4D": "Minato"
  },
  {
    "category": "transformer",
    "que1": "How others describe you?",
    "image1": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20transformer%20are%20you%3F%2FYLL_TRANS_q2-min.png?alt=media&token=7b58d0bc-cb7f-4624-8191-c460ba2d7b13",
    "option1A": "Stubborn",
    "option1B": "Caring",
    "option1C": "Sarcastic",
    "option1D": "Brave",
    "que2": "What is one of your weaknesses?",
    "image2": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20transformer%20are%20you%3F%2FYLL_TRANS_q4.gif?alt=media&token=31be1ee1-ccba-4e04-a1ea-4e3eb79a4122",
    "option2A": "Acting without consulting others",
    "option2B": "Trusting people",
    "option2C": "Being too forgiving",
    "option2D": "Coward",
    "que3": "What is a great strength of yours?",
    "image3": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20transformer%20are%20you%3F%2FYLL_TRANS_q7-min.jpg?alt=media&token=5fc7ac14-3fb8-4d56-9fe5-70e5d793c466",
    "option3A": "Determination",
    "option3B": "Handiness",
    "option3C": "Sense of humor",
    "option3D": "Strength",
    "que4": "Which do you like much?",
    "image4": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20transformer%20are%20you%3F%2FYLL_TRANS_q10.gif?alt=media&token=55e53379-c508-43fd-856c-281668742567",
    "option4A": "Megan fox",
    "option4B": "Autobot",
    "option4C": "Decepticons",
    "option4D": "Bumblebee"
  }
]

YouLookLike_result=[
  {
    "category": "naruto",
    "code": 1111,
    "name": "Naruto Uzumaki",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fnaruto.gif?alt=media&token=2abc78f1-cd97-4f55-92c8-02f253982141",
    "text": "You are no doubt a unique ninja within the realms of the Naruto universe.You had gone through many hardships and ordeals.Your vilage and friends are everything for you. With you 'Never Give Up' attitude you can achieve anything."
  },
  {
    "category": "naruto",
    "code": 1112,
    "name": "Kabuto Yakushi",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fkabuto-yakushi.gif?alt=media&token=c1fa23e8-ea3f-41c1-ae02-b8688569cb9b",
    "text": "You are shy ,quite ,polite and an intelligent boy.You are always confident on your words and actions..You can use your opponent's weaknesses and phobias against them."
  },
  {
    "category": "naruto",
    "code": 1113,
    "name": "Sasuke Uchiha",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fsasuke.gif?alt=media&token=0f6f51b5-5b36-4b41-869a-c1be12f13ab3",
    "text": "You share good bonds with others and have a charming personality liked by girls.You never settle for less.You are focused on your goals and go to any extent to achieve them."
  },
  {
    "category": "naruto",
    "code": 1114,
    "name": "Kakashi Hatake",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fkakashi.gif?alt=media&token=d6120e3c-17d4-4220-bfb6-63b1869b2e4a",
    "text": "You are independent and self-confident, at times even appearing arrogant and condescending. Despite that, You are very perceptive and intuitive, quickly realising the situation for what it was.But as an adult, you typically has a relaxed and almost bored attitude."
  },
  {
    "category": "naruto",
    "code": 1121,
    "name": "Nagato",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fpain-nagato.gif?alt=media&token=ca7a5ed9-a2f2-4ddf-86df-9ec71bb45a0f",
    "text": "You have a sensitive character, but your sensitive character is actually your strength.You are the Pain."
  },
  {
    "category": "naruto",
    "code": 1122,
    "name": "Sasuke Uchiha",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fsasuke.gif?alt=media&token=0f6f51b5-5b36-4b41-869a-c1be12f13ab3",
    "text": "You share good bonds with others.You never settle for less.You are focused on your goals and go to any extent to achieve them."
  },
  {
    "category": "naruto",
    "code": 1123,
    "name": "Naruto Uzumaki",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fnaruto.gif?alt=media&token=2abc78f1-cd97-4f55-92c8-02f253982141",
    "text": "You are no doubt a unique ninja within the realms of the Naruto universe.You had gone through many hardships and ordeals.Your vilage and friends are everything for you. With you 'Never Give Up' attitude you can achieve anything."
  },
  {
    "category": "naruto",
    "code": 1124,
    "name": "Obito Uzumaki",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fobito.gif?alt=media&token=6e3a3cbb-457b-468c-8054-2990168882c9",
    "text": "You are more calm ,focused and deterministic than others.You believe in hard work rather than talent. You can go to any extent to achieve your dreams.You have a greater thoughts of conquering the world."
  },
  {
    "category": "naruto",
    "code": 1132,
    "name": "Nagato",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fnaruto.gif?alt=media&token=2abc78f1-cd97-4f55-92c8-02f253982141",
    "text": "You have a sensitive character, but your sensitive character is actually your strength.You are the Pain."
  },
  {
    "category": "naruto",
    "code": 1133,
    "name": "Itachi Uchiha",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fitachi.gif?alt=media&token=9e06c80a-4509-4f25-9662-2224984a6801",
    "text": "You are a generally calm, soft-spoken person who tends to keep his thoughts and emotions to himself.You are more powerful, more capable than anyone else.You lived at a distance, observing individuals and ideas without getting directly involved so that you could fully understand them."
  },
  {
    "category": "naruto",
    "code": 1134,
    "name": "Obito Uzumaki",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fobito.gif?alt=media&token=6e3a3cbb-457b-468c-8054-2990168882c9",
    "text": "You are more calm ,focused and deterministic than others.You believe in hard work rather than talent. You can go to any extent to achieve your dreams.You have a greater thoughts of conquering the world."
  },
  {
    "category": "naruto",
    "code": 1141,
    "name": "Hashirama Senju",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fhashirama.gif?alt=media&token=0755e106-3727-4068-bee1-1a9900a1e4c9",
    "text": "You are also known as a good-deeder. You are a kind and caring person with a deep sense of loyalty, great charisma, and skill in negotiation."
  },
  {
    "category": "naruto",
    "code": 2213,
    "name": "Rock Lee",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Frock-lee.gif?alt=media&token=32968c75-426e-4836-83c3-600e62529711",
    "text": "You are energetic, optimistic, and hot-blooded, and shows the epitome of a \"nice guy\"."
  },
  {
    "category": "naruto",
    "code": 2214,
    "name": "Mighty Guy",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fmight-guy.gif?alt=media&token=e7117003-bcd9-4568-84f6-98616ae5eb60",
    "text": "Your pose captures your optimism and confidence.You are full of energy and have greater will power than others."
  },
  {
    "category": "naruto",
    "code": 2114,
    "name": "Shikamaru Nara",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fshikamaru.gif?alt=media&token=570af104-7eb9-4ad6-8fe7-50d6bf069d98",
    "text": "You are lazy by nature, but have a rare intellect that consistently allows you to prevail in tough situations."
  },
  {
    "category": "naruto",
    "code": 1243,
    "name": "Shikamaru Nara",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fshikamaru.gif?alt=media&token=570af104-7eb9-4ad6-8fe7-50d6bf069d98",
    "text": "You are lazy by nature, but have a rare intellect that consistently allows you to prevail in tough situations."
  },
  {
    "category": "naruto",
    "code": 1144,
    "name": "Shikamaru Nara",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fshikamaru.gif?alt=media&token=570af104-7eb9-4ad6-8fe7-50d6bf069d98",
    "text": "You are lazy by nature, but have a rare intellect that consistently allows you to prevail in tough situations."
  },
  {
    "category": "naruto",
    "code": 4142,
    "name": "Ino Yamanaka",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fino.gif?alt=media&token=51a8d986-30c8-4964-9f2a-61acff8224f1",
    "text": "You have confident and bold nature. You are very nature friendly and loyal to your allies. You are also compassionate and kind person at heart."
  },
  {
    "category": "naruto",
    "code": 4143,
    "name": "Ino Yamanaka",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fino.gif?alt=media&token=51a8d986-30c8-4964-9f2a-61acff8224f1",
    "text": "You have confident and bold nature. You are very nature friendly and loyal to your allies. You are also compassionate and kind person at heart."
  },
  {
    "category": "naruto",
    "code": 4144,
    "name": "Choji Akimichi",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fchoji.gif?alt=media&token=f4d531bc-e1cf-497b-8a45-b4f20991a542",
    "text": "Only few people have a heart as kind and caring as you.You are always there for everyone in their hard times."
  },
  {
    "category": "naruto",
    "code": 4144,
    "name": "Choji Akimichi",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fchoji.gif?alt=media&token=f4d531bc-e1cf-497b-8a45-b4f20991a542",
    "text": "Only few people have a heart as kind and caring as you.You are always there for everyone in their hard times."
  },
  {
    "category": "naruto",
    "code": 2111,
    "name": "Itachi Uchiha",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fitachi.gif?alt=media&token=9e06c80a-4509-4f25-9662-2224984a6801",
    "text": "You are a generally calm, soft-spoken person who tends to keep his thoughts and emotions to himself.You are more powerful, more capable than anyone else.You lived at a distance, observing individuals and ideas without getting directly involved so that you could fully understand them."
  },
  {
    "category": "naruto",
    "code": 2121,
    "name": "Itachi Uchiha",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fitachi.gif?alt=media&token=9e06c80a-4509-4f25-9662-2224984a6801",
    "text": "You are a generally calm, soft-spoken person who tends to keep his thoughts and emotions to himself.You are more powerful, more capable than anyone else.You lived at a distance, observing individuals and ideas without getting directly involved so that you could fully understand them."
  },
  {
    "category": "naruto",
    "code": 2131,
    "name": "Itachi Uchiha",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fitachi.gif?alt=media&token=9e06c80a-4509-4f25-9662-2224984a6801",
    "text": "You are a generally calm, soft-spoken person who tends to keep his thoughts and emotions to himself.You are more powerful, more capable than anyone else.You lived at a distance, observing individuals and ideas without getting directly involved so that you could fully understand them."
  },
  {
    "category": "naruto",
    "code": 2142,
    "name": "Itachi Uchiha",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fitachi.gif?alt=media&token=9e06c80a-4509-4f25-9662-2224984a6801",
    "text": "You are a generally calm, soft-spoken person who tends to keep his thoughts and emotions to himself.You are more powerful, more capable than anyone else.You lived at a distance, observing individuals and ideas without getting directly involved so that you could fully understand them."
  },
  {
    "category": "naruto",
    "code": 2112,
    "name": "Itachi Uchiha",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fitachi.gif?alt=media&token=9e06c80a-4509-4f25-9662-2224984a6801",
    "text": "You are a generally calm, soft-spoken person who tends to keep his thoughts and emotions to himself.You are more powerful, more capable than anyone else.You lived at a distance, observing individuals and ideas without getting directly involved so that you could fully understand them."
  },
  {
    "category": "naruto",
    "code": 2114,
    "name": "Itachi Uchiha",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fitachi.gif?alt=media&token=9e06c80a-4509-4f25-9662-2224984a6801",
    "text": "You are a generally calm, soft-spoken person who tends to keep his thoughts and emotions to himself.You are more powerful, more capable than anyone else.You lived at a distance, observing individuals and ideas without getting directly involved so that you could fully understand them."
  },
  {
    "category": "naruto",
    "code": 2113,
    "name": "Itachi Uchiha",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fitachi.gif?alt=media&token=9e06c80a-4509-4f25-9662-2224984a6801",
    "text": "You are a generally calm, soft-spoken person who tends to keep his thoughts and emotions to himself.You are more powerful, more capable than anyone else.You lived at a distance, observing individuals and ideas without getting directly involved so that you could fully understand them."
  },
  {
    "category": "naruto",
    "code": 2122,
    "name": "Itachi Uchiha",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fitachi.gif?alt=media&token=9e06c80a-4509-4f25-9662-2224984a6801",
    "text": "You are a generally calm, soft-spoken person who tends to keep his thoughts and emotions to himself.You are more powerful, more capable than anyone else.You lived at a distance, observing individuals and ideas without getting directly involved so that you could fully understand them."
  },
  {
    "category": "naruto",
    "code": 2123,
    "name": "Itachi Uchiha",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fitachi.gif?alt=media&token=9e06c80a-4509-4f25-9662-2224984a6801",
    "text": "You are a generally calm, soft-spoken person who tends to keep his thoughts and emotions to himself.You are more powerful, more capable than anyone else.You lived at a distance, observing individuals and ideas without getting directly involved so that you could fully understand them."
  },
  {
    "category": "naruto",
    "code": 2124,
    "name": "Itachi Uchiha",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fitachi.gif?alt=media&token=9e06c80a-4509-4f25-9662-2224984a6801",
    "text": "You are a generally calm, soft-spoken person who tends to keep his thoughts and emotions to himself.You are more powerful, more capable than anyone else.You lived at a distance, observing individuals and ideas without getting directly involved so that you could fully understand them."
  },
  {
    "category": "naruto",
    "code": 2124,
    "name": "Itachi Uchiha",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fitachi.gif?alt=media&token=9e06c80a-4509-4f25-9662-2224984a6801",
    "text": "You are a generally calm, soft-spoken person who tends to keep his thoughts and emotions to himself.You are more powerful, more capable than anyone else.You lived at a distance, observing individuals and ideas without getting directly involved so that you could fully understand them."
  },
  {
    "category": "naruto",
    "code": 1231,
    "name": "Madara Uchiha",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fmadara-uchiha.gif?alt=media&token=10d8afcd-fbc8-4b63-b980-0ea1dabbfeaf",
    "text": "You never settle for less and always gave a good competition to your opponents.You can go to any extent for your wills."
  },
  {
    "category": "naruto",
    "code": 3234,
    "name": "Minato Namikaze",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2Fresult%2Fminato-namikaze.gif?alt=media&token=26065551-66b6-4d0c-a067-df9f11558287",
    "text": "You are a respectful and friendly person with sharp intellect and strong personality."
  },
  {
    "category": "transformer",
    "code": 1112,
    "name": "bumblebee",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20transformer%20are%20you%3F%2Fresults%2Fbumblebee.gif?alt=media&token=1035d6ff-bf1b-4f40-a922-8b75be54a5c4",
    "text": "Despite his rather violent and brutal nature on the battlefield, Bumblebee is actually a gentle and sweet Autobot."
  },
  {
    "category": "transformer",
    "code": 1311,
    "name": "Prowl",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20transformer%20are%20you%3F%2Fresults%2Fprowl.jpg?alt=media&token=f97df6de-ffc5-4db8-8541-6435db946b90",
    "text": "You are quiet, competent, loyal, and possessed of almost endless patience. Your dedication to logic and reason make him an excellent strategist, but not much of a socialite."
  },
  {
    "category": "transformer",
    "code": 1324,
    "name": "Bulkhead",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20transformer%20are%20you%3F%2Fresults%2Fbulkhead.png?alt=media&token=18016685-42c0-4a69-8f05-0ea4a6ba2025",
    "text": "You are one of the most sturdy members of Team Prime. You are afraid of hurting things smaller and more fragile than you."
  },
  {
    "category": "transformer",
    "code": 1223,
    "name": "Megatron",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20transformer%20are%20you%3F%2Fresults%2Fmegatron.gif?alt=media&token=14bce5c7-9017-4057-86b8-12d26ad0ebb9",
    "text": "You find all others inferior and disgusting to his mechanical form. You cares for nothing but yourself and your quest for power."
  },
  {
    "category": "transformer",
    "code": 1123,
    "name": "Starscream",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20transformer%20are%20you%3F%2Fresults%2Fstarscream.jpg?alt=media&token=5bd582bb-d305-44a3-a60e-7d1a683714d5",
    "text": "You possesses impressive strength, but your speed and high intellect is one of your most defining traits.You are one of the smartest and most cunning characters."
  },
  {
    "category": "transformer",
    "code": 2234,
    "name": "Optimus Prime",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20transformer%20are%20you%3F%2Fresults%2Foptimusprime.gif?alt=media&token=3df08c51-6485-4182-9a5f-024751e726ee",
    "text": "You are kind, caring, selfless, serious, highly intelligent, calculating and wise. You have a strong sense of justice, honor and good morals. On the battlefield, you are a great fighter, leader and tactician."
  }
]

YouLookLikeRandom_data=[
  {
    "que": "Choose one visual prowess",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2FYLL_NARUTO_q3.gif?alt=media&token=a1ef632f-9304-49be-9f7f-7718a924d120",
    "category": "naruto",
    "optionA": "Mangekyo Sharingan",
    "optionB": "Rinnengan",
    "optionC": "Byakugan",
    "optionD": "Rinne-Sharingan"
  },
  {
    "que": "Choose any one which you will never let happen?",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2FYLL_NARUTO_q4.gif?alt=media&token=a77a5f0b-960e-4026-b0f5-9737b2dd593b",
    "category": "naruto",
    "optionA": "Loose your parents",
    "optionB": "Loose your friends",
    "optionC": "Loose your dreams",
    "optionD": "Loss on Battlefield"
  },
  {
    "que": "If there was one word people use to describe you , what would it be?",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2FYLL_NARUTO_q5.gif?alt=media&token=f2969019-3a17-4218-b18c-d41bfbfffc2d",
    "category": "naruto",
    "optionA": "Smart",
    "optionB": "Enthusiastic",
    "optionC": "Hardworking",
    "optionD": "Helpful"
  },
  {
    "que": "What would be your fighting style?",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2FYLL_NARUTO_q6.gif?alt=media&token=d569c695-7ffc-4d06-b011-725ac1cc2d48",
    "category": "naruto",
    "optionA": "Unpredictable and Bold",
    "optionB": "Calm and Smooth",
    "optionC": "Planned and skillful",
    "optionD": "Outrageous"
  },
  {
    "que": "What does your pet hate?",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2FYLL_NARUTO_q7.gif?alt=media&token=299e840e-2233-4ac5-a6f7-d16a9bc3eea3",
    "category": "naruto",
    "optionA": "Losing",
    "optionB": "Being teased",
    "optionC": "Imprisoned",
    "optionD": "Your annoying attitude"
  },
  {
    "que": "What is your worst characteristic?",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2FYLL_NARUTO_q8.gif?alt=media&token=76717716-dcc2-43cb-85f1-369a391332c3",
    "category": "naruto",
    "optionA": "I can be forgetful",
    "optionB": "I can be secretly angry",
    "optionC": "I am shy in telling my feelings",
    "optionD": "I am a little dumb"
  },
  {
    "que": "What hairstyle most appeals to you?",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2FYLL_NARUTO_q9.gif?alt=media&token=a5603f3a-b0c9-4362-a002-61ca146dea06",
    "category": "naruto",
    "optionA": "Short and Scruffy",
    "optionB": "Blue and Pigtail",
    "optionC": "Blone and Moppy",
    "optionD": "Silver and Ponytailed"
  },
  {
    "que": "What kind of student were/are you?",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2FYLL_NARUTO_q11.gif?alt=media&token=d31b4f8c-b107-49d8-9f71-5bbfeaf03f38",
    "category": "naruto",
    "optionA": "The shy one",
    "optionB": "The intelligent one",
    "optionC": "The bold one",
    "optionD": "A Loser with big dreams"
  },
  {
    "que": "Favorite Jutsu",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2FYLL_NARUTO_q12.gif?alt=media&token=a3bff145-84ae-472e-a786-3237bc6eec3d",
    "category": "naruto",
    "optionA": "Shadow Clone",
    "optionB": "Mind Transfer",
    "optionC": "Rasengan",
    "optionD": "Chidori"
  },
  {
    "que": "Whom you think Boruto will marry to?",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2FYLL_NARUTO_q14-min.jpg?alt=media&token=d49a8c97-f511-4238-b9e5-2c0a89bf370f",
    "category": "naruto",
    "optionA": "Class Rep",
    "optionB": "Sarada",
    "optionC": "Mitsuki",
    "optionD": "Other"
  },
  {
    "que": "Who's your crush?",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2FYLL_NARUTO_q15-min.jpg?alt=media&token=705b03d0-6f47-4c4b-b9c9-ceff6f42a8b9",
    "category": "naruto",
    "optionA": "Hanabi",
    "optionB": "Tsunade",
    "optionC": "Sakura",
    "optionD": "Hinata"
  },
  {
    "que": "Whom power do you want",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20naruto%20character%20you%20look%20like%3F%2FYLL_NARUTO_q16.gif?alt=media&token=cef8358e-acfa-4797-80ce-babb65be7d4b",
    "category": "naruto",
    "optionA": "Hashirama",
    "optionB": "Madara",
    "optionC": "Minato",
    "optionD": "Pain"
  },
  {
    "que": "What's your favorite color?",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20transformer%20are%20you%3F%2FYLL_TRANS_q1.gif?alt=media&token=0be02fad-a58f-4b7f-aacb-7bb18e0b2ff0",
    "category": "transformer",
    "optionA": "Gray",
    "optionB": "Yellow",
    "optionC": "Blue",
    "optionD": "Black"
  },
  {
    "que": "How easy is it for you to make friends?",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20transformer%20are%20you%3F%2FYLL_TRANS_q3-min.jpg?alt=media&token=defbffe4-bcda-44e8-9586-5a2e36f3c1db",
    "category": "transformer",
    "optionA": "Difficult",
    "optionB": "Easy, but not much",
    "optionC": "I have trust issues",
    "optionD": "Very difficult"
  },
  {
    "que": "What would you do if a friend was in danger?",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20transformer%20are%20you%3F%2FYLL_TRANS_q5.gif?alt=media&token=e39ca12b-51a1-4ccb-86cd-f5a7219df8de",
    "category": "transformer",
    "optionA": "Fight my way to saving them immediately",
    "optionB": "Friends? They can die for all I care",
    "optionC": "Risk my life to help them",
    "optionD": "Devise a quick plan to help"
  },
  {
    "que": "What do you like to do in your free time?",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20transformer%20are%20you%3F%2FYLL_TRANS_q6.gif?alt=media&token=bca30e42-5d16-4c64-bbc6-4e976cfbad09",
    "category": "transformer",
    "optionA": "Work out",
    "optionB": "Reading Books",
    "optionC": "Chill with friends",
    "optionD": "Play sports and game"
  },
  {
    "que": "If you could travel anywhere, where would you go?",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20transformer%20are%20you%3F%2FYLL_TRANS_q8.gif?alt=media&token=e402399a-38f5-4cef-8e12-696f9aaf9c88",
    "category": "transformer",
    "optionA": "Anywhere far away from everyone else",
    "optionB": "Washington D.C.",
    "optionC": "Tokyo",
    "optionD": "India"
  },
  {
    "que": "How big is your circle of friends?",
    "image": "https://firebasestorage.googleapis.com/v0/b/truebuddyz-b0d8a.appspot.com/o/You%20look%20like%2FWhich%20transformer%20are%20you%3F%2FYLL_TRANS_q9-min.jpg?alt=media&token=47df8136-7f1b-46ae-acd7-8d2de6a0bdc9",
    "category": "transformer",
    "optionA": "I have no friends",
    "optionB": "I have ton of friends",
    "optionC": "I have few friends but the best ones.",
    "optionD": "I have a couple of very close friends"
  }
]


def add_YouLookLike():
    try:
        print("try YouLookLike que")
        if len(YouLookLike.objects.all()):
            print("YouLookLike already have que")
            return 0

        for data in YouLookLike_data:
            print("YouLookLike que added")
            YouLookLike.objects.create(
                category = data["category"],
                que1 = data["que1"],
                option1A = data["option1A"],
                option1B = data["option1B"],
                option1C = data["option1C"],
                option1D = data["option1D"],
                image1 = data["image1"],

                que2 = data["que2"],
                option2A = data["option2A"],
                option2B = data["option2B"],
                option2C = data["option2C"],
                option2D = data["option2D"],
                image2 = data["image2"],

                que3 = data["que3"],
                option3A = data["option3A"],
                option3B = data["option3B"],
                option3C = data["option3C"],
                option3D = data["option3D"],
                image3 = data["image3"],

                que4 = data["que4"],
                option4A = data["option4A"],
                option4B = data["option4B"],
                option4C = data["option4C"],
                option4D = data["option4D"],
                image4 = data["image4"],
            )
        print("try YouLookLike que complete")
    except:
        print("except in YouLookLike que")
        pass


def add_YouLookLikeRandom():
    try:
        print("try YouLookLikeRandom que")
        if len(YouLookLikeRandom.objects.all()):
            print("YouLookLikeRandom already have que")
            return 0

        for data in YouLookLikeRandom_data:
            print("YouLookLikeRandom que added")
            YouLookLikeRandom.objects.create(
                category = data["category"],
                que = data["que"],
                optionA = data["optionA"],
                optionB = data["optionB"],
                optionC = data["optionC"],
                optionD = data["optionD"],
                image = data["image"],
            )
        print("try YouLookLikeRandom que complete")
    except:
        print("except in YouLookLikeRandom que")
        pass


def add_YouLookLikeScore():
    try:
        print("try YouLookLikeScore que")
        if len(YouLookLikeScore.objects.all()):
            print("YouLookLikeScore already have que")
            return 0

        for data in YouLookLike_result:
            print("YouLookLikeScore que added")
            YouLookLikeScore.objects.create(
                image = data["image"],
                name = data["name"],
                category = data["category"],
                code = data["code"],
                text = data["text"],
                )
        print("try YouLookLikeScore que complete")
    except:
        print("except in YouLookLikeScore que")
        pass


def add_data():
    print("YouLookLike")
    add_YouLookLike()
    add_YouLookLikeScore()
    add_YouLookLikeRandom()
