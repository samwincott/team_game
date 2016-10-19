from map import *
from player import *
from items import *
from gameparser import *
from memory import *
from friend import *
from minigame import *
import textwrap
from minigame2 import *



def player_level_check_friend(friend):
    if level >= friend["required_level"]:
        return friend["phrase2"]
    else:
        return friend["phrase1"]

def finish_game():
    global game_ongoing 
    game_ongoing = False
    print("Last night:")
    for mem in memory:
        print(mem["description"])
    


def find_key(item_id, level):
    global current_room
    for key in inventory:
        if key["id"] == "container":    
            if level >= 12 and item_id == "container":
                print("You open the kebab container and you find a shiny object covered in sweet chilli sauce and garlic mayonnaise, you have THE KEY")
                inventory.append(item_key)
                for item in inventory:
                    if item['id'] == item_id:
                        inventory.remove(item)
                return
            elif level <= 11 or item_id == "container":
                print("The smell is vile and you quickly put the container away!!")
                return
        if item_id == "bedroom":
            for key in inventory:
                if key["id"] == "key":
                    print("You have opended your Bedroom")
                    current_room = room_bedroom
                    finish_game()
                    return
        else:
            print("You cannot open that!")
            return    
    print("You cannot open that!")


def list_of_items(items):
    items_list =''
    for key in items:
        items_list =  items_list + str(key["name"]) + ', '

    items_list = items_list[:-2]
    return items_list


def print_memory_description(current_memory):
    
    if len(current_memory) != 0:
        print("What I know so far:")
        for mem in current_memory:
            print (mem["description"])
    else:
        print("You can't remember anything yet!")        

def print_room_items(room):
    if str(list_of_items(room["items"])) != '':
        print("There is " + list_of_items(room["items"]) + " here." + "\n")


def print_inventory_items(items):
    if list_of_items(items) != (""):
        print ("You have " + list_of_items(items) + ".\n")
    else:
        print ("You have no items")

def adding_a_memory(timeslot):
    """This will be called when the player can remember something from the night before
    This should be called like adding_a_memory('12pm-1am')"""

    memory.append(timeslot)
    return

def print_memory(current_memory):
    """This will print what you currently know about the night before.
    This should be called with the memory inventory in player.py like print_memory(memory)."""

    if list_of_items(current_memory) != (""):
        for x in current_memory:
            print("You know what happened between " + x["id"] + ".")
    else:
        print("You can't remember anything from last night.")

def what_happened_between(timeslot):
    """This will print what happened at a specific time slot, given the time"""

    if timeslot in memory:
        print(timeslot["description"])
    else:
        print("You can't remember what happened then.")


def print_room(room):
   
    # Display room name
    print("\n" + room["name"].upper() + "\n")
    # Display room description
    print(textwrap.fill((room["description"] + "\n"), 79))
    print_room_items(room)
        

def exit_leads_to(exits, direction):
 
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
  

    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items, room_people):
  
    print('\n')
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    #
    # COMPLETE ME!
    #

    global rick_awake
    global current_room
   
    for name in room_people:
        print("TALK TO " + str(name["name"]).upper() + " to talk to " + name["name"])

    for name in room_items:
        print("TAKE " + str(name["id"]).upper() + " to take " + name["name"])

    for name in inv_items:
        print("DROP " + str(name["id"]).upper() + " to drop your " + name["name"])

    for name in inv_items:
        if name["id"] == "container":
            print("OPEN " + str(name["id"]).upper() + " to open your " + name["name"])
        if name["id"] == "bacon":
            print_cook_bacon()
        if name["id"] == "flyer":
            print_read_flyer()
        if name["id"] == "key":
            print("OPEN BEDROOM to open your Bedroom")
    if current_room["name"] == "Arcade":
        print("PLAY GAME to play on arcade machine")
        print("PLAY GAME2 to play second arcade machine")
    have_item(inventory)
    print("MEMORY to show what you remember from last night")
    print("What do you want to do?")
    print('\n')

def is_valid_exit(exits, chosen_exit):
   
    return chosen_exit in exits

def talk_to(person, room):
    width = 75
    """add this"""
    global level
    people_in_room = current_room["friends"]

    for friend in people_in_room:
        if friend["id"] == person:
            print(player_level_check_friend(friend))

            if friend["memory"] != "" and level >= friend["required_level"]:
                for mem in friend["memory"]:
                    if mem in memory:
                        return
                    else:
                        memory.append(mem)
                        level = level + 1

                        print("Memory added: " + mem["id"])


            return





    print(person + " is not here.")

def remove_all_memories(friend):
    for mem in friend["memory"]:
        friend_memory.remove(mem)

def execute_go(direction):
    global current_room
    global level
    exits = current_room["exits"]
    if is_valid_exit(exits, direction):
        next_room = move(exits, direction)

    if is_valid_exit(exits, direction):
        if level < 4:
            print("I'd better not leave the flat until Rick's awake, I don't have my keys.")
        elif level < next_room["required_level"]:
            print(next_room["lockout_phrase"])    
        else:
            current_room = move(exits, direction)
            print("You went " + str(direction).upper() + " to " + next_room["name"])
    else:
        print("You cannot go there.")

def print_cook_bacon():
    """this function will print an additional action the user can take depending on
    if they have bacon in their inventory"""

    print("COOK BACON to cook the bacon")




def execute_take(item_id):
    for item in current_room["items"]:
        if item["id"] == item_id:
            current_room["items"].remove(item)
            inventory.append(item)
            print("You have taken " + item["name"])
            return


    print("You cannot take that.")


def execute_drop(item_id):
    for item in inventory:
        if item["id"] == item_id:
            current_room["items"].append(item)
            inventory.remove(item)
            print("You have dropped " + item["id"])
        return

    print("You cannot drop that.")



def execute_cook(item_id):
    global level
    for item in inventory:
      if item["id"] == item_id:
          print("you have cooked the bacon, the smell wakes up Rick from his deep sleep!!")
          inventory.remove(item)
          level = level + 1
          

          return

    print("you cannot cook that")


def have_item(item_id):
    global level
    for item in inventory:
        if item["name"] == "jacket" and current_room["id"] == "mortys":
            inventory.remove(item)
            inventory.append(item_flyer)
            level = level + 1
            return
        elif item["name"] == "coffee" and current_room["id"] == "summers":
            level = level + 1
            inventory.remove(item)
            return

def print_read_flyer():
    print("READ FLYER to read flyer")

def read_flyer(item_id, inventory):

    global level

    for key in inventory:
        if item_id == "flyer" and key["id"] == "flyer":
            print(key["description"])
            level = level + 1
            return

    print("you cannot read that.")

def play_on_phone(command):
    if command == "game":
        mini()
    elif command == "game2":
        mini_game_2()
    else:
        print("You can't play " + command)
    
def execute_command(command):

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
    elif command[0] == "cook":
        if len(command) > 1:
            execute_cook(command[1])
        else:
            print("you cannot cook that")
    elif command[0] == "talk":
        if len(command) > 1:
            talk_to(command[1], current_room)
        else:
            print("that won't help")
    elif command[0] == "read":
        if len(command) > 1:
            read_flyer(command[1], inventory)
        else:
            print("that won't help")
    elif command[0] == "open":
        if len(command) > 1:
            find_key(command[1], level)
        else:
            print("that won't help")
    elif command[0] == "play":
        if len(command) > 1:
            play_on_phone(command[1])
        else:
            print("that won't help") 
    elif command[0] == "memory":
        print_memory_description(memory)
    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items, room_people):

    # Display menu
    print_menu(exits, room_items, inv_items, room_people)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    return rooms[exits[direction]]


# This is the entry point of our program
def main():
    global rick_awake
    global game_ongoing
    rick_awake = False
    width = 75
    game_ongoing = True

    print('\n' * 50)
    print('+-' + '-' * width + '-+')
    print('\n')
    print(textwrap.fill("You wake up in your kitchen, next to your flat mate Rick, who is fast asleep, with no recolection of what last night entailed. You've cleraly had an adventurous, alcohol driven night. You try to go into your rooom, but you can't seem to find your key. You must piece what happened last night to find your key...", 79))
    print('\n')
    
    
    # Main game loop
    while  game_ongoing == True:

        
        print('+-' + '-' * width + '-+')
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)
        print_memory(memory)

        print('\n')
        print('+-' + '-' * width + '-+')
        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory, current_room["friends"])
        print('\n' * 100)
        print('+-' + '-' * width + '-+')
        # Execute the player's command

        execute_command(command)
        





# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
