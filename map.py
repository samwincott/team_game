from items import *
from friend import *
room_flat = {

    "id": "flat",

    "name": "Your flat",

    "description":
    """Empty bottles litter the kitchen. plates with half eaten pizzas and kebabs. Tables have empty shot glasses scattered over them as well as half filled pint glasses. Your wallet is next to you, with only some coins left from your depleted funds. In the fridge there is bacon, eggs, milk and chocolate.  """,

    "exits": {"south": "summers", "north": "kebab", "east": "mortys", "west": "taf"},

    "items": [item_bacon, item_kebab_box, item_eggs, item_wallet],

    "friends": [friend_rick],





}

room_mortys = {

    "id": "mortys",

    "name": "Mortys",

    "description":
    """A clean and tidy flat. In his room is his high end gaming computer hooked to a large monitor which dominates the room (There's a reason you're friends with him)""",

    "exits":  {"north": "nbuilding", "west":"flat", "south": "starbucks", "east": "walkabout"},

    "items": [],

    "friends": [friend_morty]
}

room_taf = {

    "id": "taf",

    "name": "The Taf",

    "description": """A relaxed bar atmosphere, a few students (Lizzy and Sarah) are drinking casually as Gunther the bartender wipes the bar. """,

    "exits":  {"east": "flat", "south":"wilko", "north": "talybont"},

    "items": [item_jacket],

    "friends": [friend_bar_staff, friend_lizzy, friend_sarah]
}

room_pryzm = {

    "id": "pryzm",

    "name": "PRYZM",

    "description":
    """A totally different setting in the day, but mamabo number 5 is playing as the place is being cleaned. A few frinds ( Joe and Mike) as well as the club rep Joseph""",

    "exits": {"south": "mcdonalds", "west": "tutor"},

    "items": [],

    "friends": [friend_club_rep_pryzm, friend_joe, friend_mike]
}

room_kebab = {

    "id": "kebab",

    "name": "Kebab Shop",

    "description":
    """A greasy kebab shop, a couple of workers are there (Kirt and Elerado) and there are some flyers on the table""",

    "exits": {"east": "nbuilding", "west": "talybont", "south": "flat"},

    "items": [],

    "friends": [friend_kebab_worker_one, friend_kebab_worker_two]
}

room_summers = {

    "id": "summers",   

    "name": "Summer's Place",

    "description":
    """ An arty room (she's an illustartion student so..). There are paint brushes dottted about the place and pictures getting in the way""",

    "exits": {"north": "flat","west":"wilko", "east": "starbucks"},

    "items": [],

    "friends": [friend_summer]
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

    "exits": {"north":"tutor", "south": "mortys", "east": "mcdonalds", "west": "kebab"},

    "items": [],

    "friends": []

    

}

room_starbucks = {

    "id": "starbucks",

    "name": "Starbucks",

    "description": "A busy starbucks, no one looks like they want to talk, best grab a coffee and get out the way.",

    "exits": {"north":"mortys", "west": "summers", "east": "wetherspoons"},

    "items": [item_coffee],

    "friends": [friend_starbucks_worker]

}

room_wilko = {

    "id": "wilko",

    "name": "Wilko",

    "description": "There isn't much of any interest here.",

    "exits": {"north":"taf", "east": "summers"},

    "items": [],

    "friends": [friend_wilko_worker]

}

room_walkabout = {

    "id": "walkabout",

    "name": "Walkabout",

    "description": "A stange site in the day, the club rep (Bob) stands there and greets you on your way in and is stopping you from looking around",

    "exits": {"west":"mortys", "north": "mcdonalds", "south": "wetherspoons"},

    "items": [],

    "friends": [friend_club_rep_walkabout]

}

room_personal_tutors_office = {

    "id": "tutor",

    "name": "Your personal Tutor's office",

    "description": "There isn't much of any interest here.",

    "exits": {"south":"nbuilding", "east": "pryzm"},

    "items": [],

    "friends": []

}

room_wetherspoons = {

    "id": "wetherspoons",

    "name": "Wetherspoons",

    "description": "Populated by people having lunch and the occasional alcoholic, no body you know is here. However there are some very nice looking glasses there that would be great for the flat...",

    "exits": {"north":"walkabout", "west": "starbucks"},

    "items": [],

    "friends": []

}

room_talybont = {

    "id": "talybont",

    "name": "Talybont",

    "description": "There isn't much of any interest here.",

    "exits": {"south":"taf", "east": "kebab"},

    "items": [],

    "friends": []


}

room_mcdonalds = {

    "id": "mcdonalds",

    "name": "McDonalds",

    "description": "An extreemly busy area, Deborah, the manager, is here and may have been last night",

    "exits": {"north":"pryzm", "west": "nbuilding", "south": "walkabout"},

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
