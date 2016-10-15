from items import *

room_flat = {
    "name": "flat",

    "description":
    """You awaken in a horrid state, to find that the room around you is littered with rubbish and debris. It feels like a distant dream to you now. You stumble to your feet clutching your head with your hand. Struggling to re-call of what had happened the night before. But nothing comes to fruition. You hear a bestial growl. Upon looking toward, the direction of the noise. Your eyes stop at the table. You notice that your friend Rick is laying there hungover, with a bottle of Budweiser in his hand and drool hanging from his mouth.
    Your stomach rumbles in accordance to the consumption of alcohol. You stare blankly around the room and at the kitchen area.For answers as to what has happened and what to do.""",

    "exits": {"south": "Morty's Place"},

    "items": [item_bacon,]
}

room_Mortys_house = {
    "name": "Mortys",

    "description":
    """Upon reaching Morty’s house, you knock on the door and wait a couple of minutes. You hear Morty, shouting “WAIT! A MIN!?” and a series of thuds following from behind the door. After a couple of seconds of silence, you raise your hand to knock once again and as your hand is abouts to meet the wood of the door. It swings open.
    Morty, who stands before you in all his elegance… with his shirt half over his head and his jeans on one leg.
    He subtly says to you, “ Heeeeey!! Whats up man!? From what I recall you guys were pretty crazy last night. Oh you look like you’ve lost your jacket mate? Well from the portion I remember you had it in The Taf, might want to go check there”""",

    "exits":  {"north": "Your flat", "west":"The Taf"},

    "items": []
}

room_taf = {
    "name": "taf",

    "description":
    """You enter the Taf, with pride in feeling like you totally owned this place last night. Although a breeze of shame seems to have crawled up your spine. Walking now towards the bar you notice a member of staff just stood there, you walk up and ask them “Have you seen my jacket around here?”.
    To which they promptly say,” OH! ITS YOU!? THE LEGEND WHO SMASHED LIKE 15 Jaegar Bombs in 5 mins! You were pretty impressive, can’t believe you were still partying after all that! Oh and your jacket is under the pool table”. """,

    "exits":  {"east": "Morty's place", "south":"PRYZM"},

    "items": [Jacket]
}

room_PRYSM = {
    "name": "The club PRYZM",

    "description":
    """Upon walking up to the club in your jacket looking the most boss you can be, turning to what feels like an adoring crowd as you walk down the road. When…really theres not much of a crowd… it’s just the self-satisfaction of how well you’re doing going to your head… and you probably look like a pretentious dick to some of them. Just saying how it is… Anyway.
    You approach the bouncer; you raise your hand for a fist bump. He fist bumps as you raise it to him. You then say to him, “aaah bouncer you druggo, how you doing?”. To which he replies,” nah yeah, yeah nah. Doing great mate. Just been working all night, you know?”. You then utter to him, “yeah man, I hear ya’. Worlds tough you know?”. He then smacks you in the back with approval, “Mate you know exactly! look you seem busy… so you can get in for free this time yeah?”. In appreciation, you humbly say “Mate you are a legend, I owe you one!”. He turns to t1he cashier, “Sally let this bloke in, his alright”.  She nods with a sigh. 
    You carry on in, as you get to the main room. There is a woman sweeping up glass from the floor, she turns to you, “oh hey! You’re the hot guy from last night” You can see where this is going right? Like do I need to really type out all of her lines? and yours? Good because I’m not…
    After 10 mins of talking, she says. “I have no idea what happened to you last night, all I know is that you went out the back afterwards; with some others to go get a kebab I think”.  
    """,

    "exits": {"west": "Kebab Shop", "north": "The Taf"},

    "items": []
}

room_kebab_shop = {
    "name": "Kebab Shop",

    "description":
    """You walk into the kebab shop… prepared and ready for anything… hell your feeling pretty invincible by this point. Like you could probably wrestle a honey badger with no issue… but mate in fairness that’s pretty messed up… wanting to fight animals like that… you should feel ashamed. Anyway you see the crowd of hungry people waiting for their precious fast food. But by this point you don’t care and have the ingenious idea of distracting them so you get a chance to talk to the guy behind the counter.
    You take in a deep breath… your palms are quite sweaty… knees weak… arms are heavy… still a little bit of vomit on your shirt…. Maybe from mum’s spaghetti?? And finally shout with a might roar. “LOOK IT’S THE NEW MEMBER OF THE BAND GORILLAZ!!! ITS HARAMBE!!! HE IS WALKING DOWN THE STREET OMFG!?”. With a sheer look of confusion from what may as well be called a flock of sheep. Stampede out of the shop to go take a look and try to follow who they assume is the guy. 
    You suavely walk over to the counter, lean over the counter. The shop keeper is looking at you pretty annoyed… well you did just get rid of all his customers… what did you expect to happen? To keep this PG, he started swearing at you with the odd sentence of blaming his wife for choosing such a crazy place to set up shop. But you did manage to concentrate hard enough that he mentioned you and a woman being here last night. By which case you know that it could only be one person… Summer… and you go to step outside, whilst of course he is still rambling behind you. 
    """,

    "exits": {"east": "PRYZM", "south": "Summer's place"},

    "items": []
}

room_summers_place = {
    "name": "Summer's House",

    "description":
    """You walk up to Summer’s place… feeling pretty good still, the sun is shining, the bees are buzzing. There is a helicopter flying over your head… maybe a military one? Who knows. All you know is that today’s going pretty swell for an adventure. You get to her door and see a note; it reads “Hung Over… don’t piss me off”. Having a quick think about how she has acted in the past in this situation, you wittedly go rummaging through your pockets and pull out a can of RedBull and pull a flower from her garden. 
    You then stand braced in front of her door, with both items acting like a sword and shield; ready to take on the dragon that’s in hey lair. You then take a brave step forward and with a valiant lunge you press the doorbell ringing it multiple times. Congratulations… you have now gained a new item… it’s called man hood. After hearing what could potentially be the start of the apocalypse to you, the noise stops and the door slightly creeks open. You see an eye appear which is surrounded by hair, it peers down to the items in your hands. The door swiftly opens and Summer takes the Redbull from your hand. 
    She then downs the RedBull like she needs it to live. And then throws the empty can into the next room. Hastily then turns back to face you. “So what’s up then?” she says casually. To which you reply, “can you remember what happened last night and if I did anything stupid specifically that stood out?”. She sarcastically replies, “But your stupid all the time” with a cheeky look on her face. You glare at her annoyed. She then sighs and rolls her eyes at you, “For some strange reason you threw most people’s keys into a kebab box and starting hiding it around the house, saying the kebab knight will protect our keys! Which… by the way was not fun when you put it in the bin… which is where I last left it”. 
    After a few minutes passing of casual pleasantries… trying to keep things pg here people… don’t judge me… she closes the door and you must take the final path on your epic adventure! ON WARDS BRAVE ADVENTURER!… just mind arrows and getting hit in the knee… its not fun trust… 
    """,

    "exits": {"north": "Kebab Shop","west":"Your Flat"},

    "items": []
}

room_end_game = {
    "name": "Summer's House",

    "description":
    """You run through your door with a massive smile on your face and feeling rather accomplished. Bravo you clever little sausage. Rick turns his head from the TV in confusement; then shrugs his shoulders and says, “mate just remembered that your keys are in the kebab box in the bin”. And he then turns back to the TV.  You then drop your noble pose and face-palm, then slowly walk over to the now less than sanitary kitchen. You then walk over to the bin and Jab your finger at its lid. As you do so, you can smell the horrid remains linger from its container. It sends your nostrils into disarray; which causes you to leap backwards. You grab a peg from among the random objects in the kitchen and put it on your nose. You then, quickly turn your side to the bin and shove your hand straight into it without looking to see if you can feel the kebab box.
    After a couple of seconds of searching, you feel what appears to be the box at the bottom you pull it out with full force and even let out a little grunt. Kind of imagine a warrior that’s just ripped out the heart of his foe with his hand… only it’s you… and well… its rubbish in your hand. Rick turns and looks at your accomplishment and slowly claps and subtly says, “Mate, you need to calm down… like have a pint or something” then he just goes back to watching TV. You open the box and grab the key which is covered in kebab sauce and other contents of the bin. You hurry to the sink like your life depends on it and wash off the waste. You then walk over to your bedroom door and unlock it. As your key turns in the lock, Rick is screaming “GOOOOAAAL!” As Manchester United scored against Liverpool. To which you afterwards then step through the door and close it behind you and notice a video camera sat on the bed still recording. You take the camera into the next room where Rick is sat. 
    And you tell him, “mate want to see what actually happened last night?”. He grabs the remote for the TV and turns it off and shouts, “Lets do this!”.""",

    "exits": {"north": "your bedroom","east":"Summer's Place"},

    "items": [item_kebab_box]
}


rooms = {
    "Flat": room_flat,
    "Morty's Place": room_Mortys_House,
    "The Taf": room_taf,
    "PRYZM": room_PRYZM,
    "Kebab Shop": room_kebab_shop
    "Summer's Place": room_summers_place
    "Your Flat": room_end_game
    
}
