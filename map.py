from items import *

flat = {
    "name": "flat",

    "description":
    """This is your flat""",

    "exits": {"south": "Admins", "east": "Tutor", "west": "Parking"},

    "items": [item_biscuits, item_handbook]
}

taf = {
    "name": "taf",

    "description":
    """This is the taf""",

    "exits":  {"north": "Reception"},

    "items": []
}

room_tutor = {
    "name": "your personal tutor's office",

    "description":
    """You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The reception is to the west.""",

    "exits": {"west": "Reception"},

    "items": []
}

room_parking = {
    "name": "the parking lot",

    "description":
    """You are standing in the Queen's Buildings parking lot.
You can go south to the COMSC reception, or east to the
general office.""",

    "exits": {"east": "Office", "south": "Reception"},

    "items": []
}

room_office = {
    "name": "the general office",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"west": "Parking"},

    "items": [item_pen]
}



rooms = {
    "Reception": room_reception,
    "Admins": room_admins,
    "Tutor": room_tutor,
    "Parking": room_parking,
    "Office": room_office
}
