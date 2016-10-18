def mini (guesstaken, youlose, number, Name):
    import random

    guesstaken = 1
    youlose = 4

    Name = input("Please enter your name ")
    print("")
    number = random.randint(1,10)
    print("Hello! " + Name + " The number that I'm currently thinking of is between 1 and 10")


    while guesstaken < 4:
        print('Take a guess.') 
        guess = input()
        guess = int(guess)



    
        if guess < number:
            print("You are guessing too low")

        if guess > number:
            print("You are too guessing too high")

        if guess == number:
            break

        guesstaken = guesstaken + 1
    



    if guesstaken == youlose:
    
        print(" _____ ____  _      _____   ____  _     _____ ____  _    ")
        print("/  __//  _ \/ \__/|/  __/  /  _ \/ \ |\/  __//  __\/ \   ")
        print("| |  _| / \|| |\/|||  \    | / \|| | //|  \  |  \/|| |   ")
        print("| |_//| |-||| |  |||  /_   | \_/|| \// |  /_ |    /\_/   ")
        print("\____\\_/ \|\_/  \|\____\  \____/\__/  \____\\_/\_\(_)   ")   
        number = str(number)
        print("")
        print("Sorry " + Name + " the number i was thinking of was " + number)
         
 

    if guesstaken != youlose and guess == number:
        print(
            """
        ___  _ ____  _       _      _  _      _   
        \  \///  _ \/ \ /\  / \  /|/ \/ \  /|/ \  
         \  / | / \|| | ||  | |  ||| || |\ ||| |  
         / /  | \_/|| \_/|  | |/\||| || | \||\_/  
        /_/   \____/\____/  \_/  \|\_/\_/  \|(_)
           """)
        guesstaken = str(guesstaken)
        print("You " + Name + " have guessed correct within: " + guesstaken + " guesses!") 
     

    return Minigame
    
