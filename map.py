from items import *
from friend import *
room_flat = {

    "id": "flat",

    "name": "Your flat",

    "description":
    """Empty bottles litter the kitchen. plates with half eaten pizzas and kebabs. Tables have empty shot glasses scattered over them as well as half filled pint glasses. Your wallet is next to you, with only some coins left from your depleted funds. In the fridge there is bacon, eggs, milk and chocolate.  """,

    "exits": {"south": "mortys"},

    "items": [item_bacon],

    "friends": [friend_rick_asleep]
}

room_mortys = {

    "id": "mortys",

    "name": "Mortys",

    "description":
    """A clean and tidy flat. In his room is his high end gaming computer hooked to a large monitor which dominates the room (There's a reason you're friends with him)""",

    "exits":  {"north": "flat", "west":"taf"},

    "items": [],

    "friends": [friend_morty_without_coat]
}

room_taf = {

    "id": "taf",

    "name": "The Taf",

    "description": """A relaxed bar atmosphere, a few students (Lizzy and Sarah) are drinking casually as Gunther the bartender wipes the bar. """,

    "exits":  {"east": "mortys", "south":"pryzm"},

    "items": [item_jacket],

    "friends": [friend_bar_staff, friend_lizzy, friend_sarah]
}

room_pryzm = {

    "id": "pryzm",

    "name": "PRYZM",

    "description":
    """A totally different setting in the day, but mamabo number 5 is playing as the place is being cleaned. A few frinds ( Joe and Mike) as well as the club rep Joseph""",

    "exits": {"north": "taf", "west": "kebab"},

    "items": [],

    "friends": [friend_club_rep, friend_joe, friend_mike]
}

room_kebab = {

    "id": "kebab",

    "name": "Kebab Shop",

    "description":
    """A greesy kebab shop, a couple of workers are there (Kirt and Elerado) and there are some flyers on the table""",

    "exits": {"east": "pryzm", "south": "summers"},

    "items": [],

    "friends": [friend_kebab_worker_one, friend_kebab_worker_two]
}

room_summers = {

    "id": "summers",   

    "name": "Summer's Place",

    "description":
    """ An arty room (she's an illustartion student so..). There are paint brushes dottted about the place and pictures getting in the way""",

    "exits": {"north": "kebab","west":"end"},

    "items": [],

    "friends": [friend_summer_without_coffee]
}

room_end = {

    "id": "end",

    "name": "End",

    "description":
    """ Your room, in the same bomsite you left it in before drinking last night. Clothes on the floor, work on the bed and your laptop on the desk""",
    "exits": {"east":"summers", "north": "end"},

    "items": [item_kebab_box],

    "friends": []
}

room_north_building = {

    "id": "nbuilding",

    "name": "The North Building",

    "description": "There isn't much of any interest here.",

    "exits": {"east":"flat"},

    "items": [],

    "friends": []

    

}

room_starbucks = {

    "id": "matalan",

    "name": "Matalan",

    "description": "A busy starbucks, no one looks like they want to talk, best grab a coffee and get out the way.",

    "exits": {"east":"flat"},

    "items": [],

    "friends": [friend_starbucks_worker]

}

room_wilko = {

    "id": "wilko",

    "name": "Wilko",

    "description": "There isn't much of any interest here.",

    "exits": {"east":"flat"},

    "items": [],

    "friends": []

}

room_walkabout = {

    "id": "walkabout",

    "name": "Walkabout",

    "description": "A stange site in the day, the club rep (Bob) stands there and greets you on your way in and is stopping you from looking around",

    "exits": {"east":"flat"},

    "items": [],

    "friends": [friend_club_rep]

}

room_personal_tutors_office = {

    "id": "tutor",

    "name": "Your personal Tutor's office",

    "description": "There isn't much of any interest here.",

    "exits": {"east":"flat"},

    "items": [],

    "friends": []

}

room_wetherspoons = {

    "id": "wetherspoons",

    "name": "Wetherspoons",

    "description": "Populated by people having lunch and the occasional alcoholic, no body you know is here. However there are some very nice looking glasses there that would be great for the flat...",

    "exits": {"east":"flat"},

    "items": [],

    "friends": []

}

room_talybont = {

    "id": "talybont",

    "name": "Talybont",

    "description": "There isn't much of any interest here.",

    "exits": {"east":"flat"},

    "items": [],

    "friends": []

}

room_mcdonalds = {

    "id": "mcdonalds",

    "name": "McDonalds",

    "description": "An extreemly busy area, Deborah, the manager, is here and may have been last night",

    "exits": {"east":"flat"},

    "items": [],

    "friends": [friend_mcdonalds_worker]
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
    "starbucks": room_starbucks,
    "wilko": room_wilko,
    "walkabout": room_walkabout,
    "tutor": room_personal_tutors_office,
    "wetherspoons": room_wetherspoons,
    "talybont": room_talybont,
    "mcdonalds": room_mcdonalds

}
