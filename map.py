from items import *
from friend import *
room_flat = {
    "name": "Your flat",

    "description":
    """You awaken in a horrid state, to find that the room around you is littered with rubbish and debris. It feels like a distant dream to you now. You stumble to your feet clutching your head with your hand. Struggling to re-call of what had happened the night before. But nothing comes to fruition. You hear a bestial growl. Upon looking toward, the direction of the noise. Your eyes stop at the table. You notice that your friend Rick is laying there hungover, with a bottle of Budweiser in his hand and drool hanging from his mouth.
    Your stomach rumbles in accordance to the consumption of alcohol. You stare blankly around the room and at the kitchen area.For answers as to what has happened and what to do.""",

    "exits": {"south": "Mortys"},

    "items": [item_bacon],

    "friends": [friend_rick_asleep]
}

room_mortys = {
    "name": "Mortys",

    "description":
    """Upon reaching Morty’s house, you knock on the door and wait a couple of minutes. You hear Morty, shouting “WAIT! A MIN!?” and a series of thuds following from behind the door. After a couple of seconds of silence, you raise your hand to knock once again and as your hand is abouts to meet the wood of the door. It swings open.
    Morty, who stands before you in all his elegance… with his shirt half over his head and his jeans on one leg.""",

    "description_alt":
    """Upon reaching Morty’s house, you knock on the door and wait a couple of minutes. You hear nothing except for the voice in your head saying one thing… “Where is he?” … upon waiting for a sign nothing is happening and your starting to look strange standing outside your friend’s house for a while now whilst still half hung over. """,

    "exits":  {"north": "flat", "west":"The_Taf"},

    "items": [],

    "friends": [friend_morty]
}

room_taf = {
    "name": "The Taf",

    "description":
    """You enter the Taf, with pride in feeling like you totally owned this place last night. Although a breeze of shame seems to have crawled up your spine. Walking now towards the bar you notice a member of staff just stood there, you walk up and ask them “Have you seen my jacket around here?”.
    """,

    "description_alt":
    """You look around in sheer confusion as to why no one is here, you approach the bar and you see no one is around. Your conscious tells you “Now is your chance to drink as much as you want!” but then stomach feels irritable on account of last night’s session. So you walk away from the bar and inspect the rest of the place. However you have no luck in seeing anything important. """,

    "exits":  {"east": "Mortys", "south":"PRYZM"},

    "items": [item_jacket],

    "friends": [friend_bar_staff]
}

room_pryzm = {
    "name": "PRYZM",

    "description":
    """Upon walking up to the club in your jacket looking the most boss you can be, turning to what feels like an adoring crowd as you walk down the road. When…really theres not much of a crowd… it’s just the self-satisfaction of how well you’re doing going to your head… and you probably look like a pretentious dick to some of them. Just saying how it is… Anyway.
    You approach the bouncer; you raise your hand for a fist bump. He fist bumps as you raise it to him. You then say to him, “aaah bouncer you druggo, how you doing?”. To which he replies,” nah yeah, yeah nah. Doing great mate. Just been working all night, you know?”. You then utter to him, “yeah man, I hear ya’. Worlds tough you know?”. He then smacks you in the back with approval, “Mate you know exactly! look you seem busy… so you can get in for free this time yeah?”. In appreciation, you humbly say “Mate you are a legend, I owe you one!”. He turns to t1he cashier, “Sally let this bloke in, his alright”.  She nods with a sigh.
    You carry on in, as you get to the main room. There is a woman sweeping up glass from the floor.""",

    "description_alt":
    """Upon walking up to the club, looking the bouncer straight in the face, with the best line you could think of for you getting into the club for free. The bouncer says to you, “mate, I don’t know what your problem is, but due to the code. Can’t let you any further into the club”. Now stood at the entrance of the club, you can only but feel two things…. Regret and cold. """,

    "exits": {"north": "The_Taf", "west": "Kebab_Shop"},

    "items": [],

    "friends": [friend_club_rep]
}

room_kebab = {
    "name": "Kebab Shop",

    "description":
    """You walk into the kebab shop… prepared and ready for anything… hell your feeling pretty invincible by this point. Like you could probably wrestle a honey badger with no issue… but mate in fairness that’s pretty messed up… wanting to fight animals like that… you should feel ashamed. Anyway you see the crowd of hungry people waiting for their precious fast food. But by this point you don’t care and have the ingenious idea of distracting them so you get a chance to talk to the guy behind the counter.
    You take in a deep breath… your palms are quite sweaty… knees weak… arms are heavy… still a little bit of vomit on your shirt…. Maybe from mum’s spaghetti?? And finally shout with a might roar. “LOOK IT’S THE NEW MEMBER OF THE BAND GORILLAZ!!! ITS HARAMBE!!! HE IS WALKING DOWN THE STREET OMFG!?”. With a sheer look of confusion from what may as well be called a flock of sheep. Stampede out of the shop to go take a look and try to follow who they assume is the guy.
    You suavely walk over to the counter, lean over the counter. The shop keeper is looking at you pretty annoyed… well you did just get rid of all his customers… what did you expect to happen? To keep this PG, he started swearing at you with the odd sentence of blaming his wife for choosing such a crazy place to set up shop.""",

    "description alt":
    """You walk into the kebab shop and smell the intoxicating aroma of meats and chips, you try to follow the scent and try to talk to the guy behind the counter, however your attempts are useless as the place is packed with people also craving the delicacy known only as… Kebabs.  You stand alone in the crowd… now hungry and only left with the real option of leaving. Well unless you like feeling like a sardine in a can… in which case why not go to London Underground tubes, huh? """,

    "exits": {"east": "PRYZM", "south": "Summers"},

    "items": [],

    "friends": [friend_kebab_worker]
}

room_summers = {
    "name": "Summer's Place",

    "description":
    """You walk up to Summer’s place… feeling pretty good still, the sun is shining, the bees are buzzing. There is a helicopter flying over your head… maybe a military one? Who knows. All you know is that today’s going pretty swell for an adventure. You get to her door and see a note; it reads “Hung Over… don’t piss me off”. Having a quick think about how she has acted in the past in this situation, you wittedly go rummaging through your pockets and pull out a can of RedBull and pull a flower from her garden.
    You then stand braced in front of her door, with both items acting like a sword and shield; ready to take on the dragon that’s in hey lair. You then take a brave step forward and with a valiant lunge you press the doorbell ringing it multiple times. Congratulations… you have now gained a new item… it’s called man hood. After hearing what could potentially be the start of the apocalypse to you, the noise stops and the door slightly creeks open. You see an eye appear which is surrounded by hair, it peers down to the items in your hands. The door swiftly opens and Summer takes the Redbull from your hand.
    She then downs the RedBull like she needs it to live. And then throws the empty can into the next room. Hastily then turns back to face you. “So what’s up then?” she says casually. To which you reply, “can you remember what happened last night and if I did anything stupid specifically that stood out?”. She sarcastically replies, “But your stupid all the time” with a cheeky look on her face. You glare at her annoyed. After a few minutes passing of casual pleasantries… trying to keep things pg here people… don’t judge me… she closes the door and you must take the final path on your epic adventure! ON WARDS BRAVE ADVENTURER!… just mind arrows and getting hit in the knee… its not fun trust…
    """,

    "description alt":
    """You walk to Summer’s place after such a long distance and seeing many sights and hearing many sounds, you feel like your day could really have gone better to begin with. But hey things could have been worse right? So you approach the door to Summer’s place, about to knock on the door. When you notice a note reading, “Hung over… don’t piss me off”. Your memory kicks in of previous times to when she has been angry… like the time you pissed on her door step because you hated her next door neighbour and tried blaming it on them… when in reality doing that when you were drunk… probably not the most of helpful things in your quest.
    So now you stand outside another person’s house…. Looking strange as you contemplate over whether it’s a good idea to disturb her. You are really out to make friends today aren’t you?
    """,

    "exits": {"north": "Kebab_Shop","west":"End"},

    "items": [],

    "friends": [friend_summer]
}

room_end = {
    "name": "End",

    "description":
    """You run through your door with a massive smile on your face and feeling rather accomplished. Bravo you clever little sausage. Rick turns his head from the TV in confusement; then shrugs his shoulders and says, “mate just remembered that your keys are in the kebab box in the bin”. And he then turns back to the TV.  You then drop your noble pose and face-palm, then slowly walk over to the now less than sanitary kitchen. You then walk over to the bin and Jab your finger at its lid. As you do so, you can smell the horrid remains linger from its container. It sends your nostrils into disarray; which causes you to leap backwards. You grab a peg from among the random objects in the kitchen and put it on your nose. You then, quickly turn your side to the bin and shove your hand straight into it without looking to see if you can feel the kebab box.
    After a couple of seconds of searching, you feel what appears to be the box at the bottom you pull it out with full force and even let out a little grunt. Kind of imagine a warrior that’s just ripped out the heart of his foe with his hand… only it’s you… and well… its rubbish in your hand. Rick turns and looks at your accomplishment and slowly claps and subtly says, “Mate, you need to calm down… like have a pint or something” then he just goes back to watching TV. You open the box and grab the key which is covered in kebab sauce and other contents of the bin. You hurry to the sink like your life depends on it and wash off the waste. You then walk over to your bedroom door and unlock it. As your key turns in the lock, Rick is screaming “GOOOOAAAL!” As Manchester United scored against Liverpool. To which you afterwards then step through the door and close it behind you and notice a video camera sat on the bed still recording. You take the camera into the next room where Rick is sat.
    And you tell him, “mate want to see what actually happened last night?”. He grabs the remote for the TV and turns it off and shouts, “Lets do this!”.""",

    "exits": {"east":"Summers", "north": "End"},

    "items": [item_kebab_box],

    "friends": []
}

room_north_building = {
    "name": "The North Building",

    "description": "There isn't much of any interest here.",

    "exits": {"east":"flat"},

    "items": [],

    "friends": []

    

}

room_matalan = {
    "name": "Matalan",

    "description": "There isn't much of any interest here.",

    "exits": {"east":"flat"},

    "items": [],

    "friends": []

}

room_wilko = {
    "name": "Wilko",

    "description": "There isn't much of any interest here.",

    "exits": {"east":"flat"},

    "items": [],

    "friends": []

}

room_walkabout = {
    "name": "Walkabout",

    "description": "There isn't much of any interest here.",

    "exits": {"east":"flat"},

    "items": [],

    "friends": []

}

room_personal_tutors_office = {
    "name": "Your personal Tutor's office",

    "description": "There isn't much of any interest here.",

    "exits": {"east":"flat"},

    "items": [],

    "friends": []

}

room_wetherspoons = {
    "name": "Wetherspoons",

    "description": "There isn't much of any interest here.",

    "exits": {"east":"flat"},

    "items": [],

    "friends": []

}

room_talybont = {
    "name": "Talybont",

    "description": "There isn't much of any interest here.",

    "exits": {"east":"flat"},

    "items": [],

    "friends": []

}

rooms = {
    "flat": room_flat,
    "mortys": room_mortys,
    "taf": room_taf,
    "pryzm": room_pryzm,
    "kebab": room_kebab,
    "summers": room_summers,
    "end": room_end,
    "nbuilding": room_north_building,
    "matalan": room_matalan,
    "wilko": room_wilko,
    "walkabout": room_walkabout,
    "tutor": room_personal_tutors_office,
    "wetherspoons": room_wetherspoons,
    "talybont": room_talybont,

}
