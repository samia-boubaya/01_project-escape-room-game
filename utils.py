##############################################################################################
#################### HOW TO USE UTILS ########################################################

# def function_name:

##############################################################################################
####################### DATA   ###############################################################
##############################################################################################


################## DATA LISTs  ###############################################################
# LIST : actions available to a player
actions = ['explore', 'examine', 'unlock door', 'navigate', 'restart', 'quit', 'play']

# LIST : spaces
spaces = ['game room', 'bedroom 1', 'bedroom 2', 'living room','outside']

# LIST : items
items = ['couch', 'piano', 'queen bed', 'double bed', 'dresser', "dining table"]

# LIST : doors
doors = ['door A', 'door B', 'door C', 'door D']

# LIST : keys
keys = ['key door A', 'key door B', 'key door C', 'key door D']

################## DICT: GAME_AREAS  #####################################################################

# Each key in this dictionary represents a room; each value is a list of objects, doors and keys
# Dictionary : GAME AREAS
game_areas = {
    "game room" : ['couch', 'piano', 'door A', 'key door A'],
    "bedroom 1": ['queen bed', 'door A', 'door B', 'door C', 'key door B'],
    "bedroom 2": ['double bed', 'door B', 'dresser', 'key door D', 'key door C'],
    "living room": ["dining table", 'door C', 'door D'],
    "outside": ["freedom"]
}

################## DICT: GAME_STATES  #####################################################################

# Dictionary : GAME STATE
game_state = {
    'space path' : [], # player current space to navigate and make a space path
    'item path' : [], # to select an item to examine for key; and make an item path
    'door path': [], # to select a door in currentspace and track unlocked doors already and locked ones
    'inventory': [], # to store found keys
    'time': "display_clock_countdown" , #library time for live timer and countdown
    'health': 100,
}


##############################################################################################
################## FUNCTIONS = ACTIONS  ######################################################
##############################################################################################
#### the order of the main functions :

# 0) player_action
### // can still input another action or repeat same one ####

# 1) explore
# // update_item_path(item) 
# // return list of items in space

# 2) examine
# // return true  if key found
# // return false if key not found and not in inventory
# // return false if key in inventory
# // return 

# 3) unlock_door
# // quiz
# // update_door_path(door)

# 4) navigate
# // 
# // update_space_path(space)


###################################################################################################################
################## MAIN FUNCTION : PLAYER_ACTION(PLAYER_INPUT)  ######################################################
###################################################################################################################
def player_action(player_input: str):
    while True:
        action = player_input.lower()

        # Invalid input → show available actions and ask again
        if action not in actions:
            print("\nInvalid action! Please choose one of the following:")
            print(f'\nPRINT LIST OF ACTIONS: {actions}')
            player_input = input("Enter an action: ")
            continue

        # Quit the game
        if action == 'quit':
            print(f"\nPlayer inputs the action: {action}")
            print("Quitting the game. Goodbye!")
            break

        # Restart the game
        elif action == 'restart':
            print(f"\nPlayer inputs the action: {action}")
            print("Game restarting!")
            player_input = 'play'
            continue  # Restart goes back to play automatically

        # Play the game
        elif action == 'play':
            print(f"\nPlayer inputs the action: {action}")
            print("Starting the game...")
            # You can add your game logic here
            player_input = input("Enter NEXT action: ")
            return player_action('play')

        # Other valid actions
        else:
            print(f"\nPlayer inputs the action: {action}")
            print(f"Performing action: {action}")
            player_input = input("Enter next action: ")
            
###################################################################################################################
################## FUNCTION : EXPLORE  ########################################################################
###################################################################################################################

# define Function : explore(space)
def explore(space: str):
    space_items = []
    print(f"You are exploring {space}. You see these items:")
    for item in items:
        print("-", item,"\n")
        space_items.append(item)
    return space_items

###################################################################################################################
################## FUNCTION : EXAMINE  ########################################################################
###################################################################################################################

def examine(space: str):
    print(f'Here is a list of items in {space}:', explore(space))
    select_item = input("Select an item to examine: ").strip().lower()  # select an item to examine
    trigger_event("examine")
    print(f'Examining the {select_item} carefully...')
    
    #### ITEMS in SPACE ############################################
    # We don't loop through 'space' because it's a string, not a list.
    # Instead, we check based on the selected item.
    
    #### GAME ROOM ITEMS ################
    if select_item == 'couch':
        key = 'no key found'
        result = check(select_item, key)

    elif select_item == 'piano':
        key = 'key door A'
        result = check(select_item, key)

    #### BEDROOM 1 ITEM ################
    elif select_item == 'queen bed':
        key = 'key door B'
        result = check(select_item, key)
    
    #### BEDROOM 2 ITEMS ################
    elif select_item == 'double bed':
        key = 'key door C'
        result = check(select_item, key)

    elif select_item == 'dresser':
        key = 'key door D'
        result = check(select_item, key)

    #### LIVING ROOM ITEMS ########
    elif select_item == 'dinning table':
        key = ''
        result = check(select_item, key)

    # Re-INPUT
    else:
        print("Value ERROR! Invalid item.")
        return examine(space)  # allows the user to try again safely

    return result


# call function : examine('game room')
# define Function : examine
def examine(space:str):
    print(f'Here is a list of items in {space}:', explore(space))
    select_item = input("Select an item to examine:") #select an item to examine
    print((f'You are examining :{select_item}'))
    
    print(f'Examining the {select_item} carefully...')
    #### ITEMS in SPACE ############################################
    for select_item in space:
        #### GAME ROOM ITEMS ################
        # ITEM = PIANO
        if select_item == 'couch':
            key= 'no key found'
            check(select_item, key)

        # ITEM = COUCH
        elif select_item == 'piano':
            key= 'key door A'
            check(select_item, key)

        #### BEDROOM 1 ITEM ################
        # ITEM = QUEEN BED
        elif select_item == 'queen bed':
            key= 'key door B'
            check(select_item, key)
        
        #### BEDROOM 2 ITEMS ################
        # ITEM = DOUBLE BED
        elif select_item == 'double bed':
            key= 'key door C'
            check(select_item, key)

        # ITEM = DRESSER
        elif select_item == 'dresser':
            key= 'key door D'
            check(select_item, key)

        #### LIVING ROOM ITEMS ########
        # ITEM = DINNING TABLE
        elif select_item == 'dinning table':
            key= ''
            check(select_item, key)

        # Re-INPUT
        else:
            print("Value ERROR !", examine(space))

        result=check(select_item, key)
        return result

###################################################################################################################
################## FUNCTION : CHECK  ########################################################################
###################################################################################################################

#check for key in selected item in current space
# use this function inside examine()
def check(select_item, key):
    #if found key and not in inventory then update inventory
    if ( key!='' and key not in game_state['inventory'] ): 
        print(f'You found {key} in {select_item}')
        update_inventory(key)
        result = True
    #elif no key found
    elif key=='no key found':
        print(f'No key found in {select_item}')
        result=False
    #else key in inventory
    else: 
        print(f'You already have the key in your inventory {game_state["inventory"]}')  
        result=False
    return result
#####################################################################################################
################## PLAYER_INPUT = UNLOCK DOOR  ######################################################
#####################################################################################################
    #player_input = 'unlock door'
    # action = player_input  
    # action = 'unlock door'

inventory = game_state['inventory']
action = 'unlock door'
space = 'game room'
door = 'door A'
# define Function : unlock_door(action, door, inventory, space)
action = 'unlock door'
def unlock_door(inventory:list, action, space, door):
    while action=='unlock door' and action!='quit' and action!='restart': # While action is not 'quit' and 'restart'
        # we check every key and door cuz we have to compare two string 'door A' in 'key door A'
        for key in game_state['inventory']:
            if  door in game_state['inventory'][key]:
                print("You have the key in your inventory to unlock it ... POP QUIZ! Answer correctly to unlock it! ")
                quiz(door)
                if quiz(door)==True:
                    update_door_path(door)

            
        # unlocked door

    while door in doors:    
        print(f'You chose to unlock {door} in {space}')
        if door in space:
            door = input("Enter the door you want to try unlock : ").lower() # Player inputs space of choice
            print(f'Player chose to try unlock: {door}')
    for i in game_state[inventory]:
        if key  in inventory[i]:
            print(f"This key is already in your inventory !")
            return True
        quiz(door)
        update_door_path(door)
        
    return result # if true unlocked if false still locked

##################################################################################################################
############################## FUNCTION : QUIZ ###########################################################################################
##################################################################################################################

inventory = game_state['inventory']
key = 'key door A'
door = 'door A'

def quiz(inventory:list, door:str, key:str):
    # Quiz function to unlock doors
    for key in inventory:
        if door in inventory:
            print("You have the key to this door in your inventory ~ you can proceed to unlock!")
            #######################################################################################
            if door == 'door A': # quiz('door A')
                print("Question: What is the primary function of Door A, as suggested by its location in the floor plan?")
                print("A) To access the outdoors.")
                print("B) To provide entry or exit to a specific room.")
                print("C) To serve as a decorative element.")

                answer = input("Enter your choice (A, B, or C): ").upper()
                if answer == "B":
                    print("Correct! Door A is most likely for entering or exiting a room.")
                    quiz_answer=True
                else:
                    print("Incorrect. Try another time!")
                    quiz_answer=False
                    return player_action('play')
                    
            #######################################################################################
            elif door == 'door B': # quiz('door B')
                print("Question: Considering the layout, which room is Door B most likely connected to?")
                print("A) The Game Room")
                print("B) Bedroom 1")
                print("C) The Outdoors")

                answer = input("Enter your choice (A, B, or C): ").upper()
                if answer == "B":
                    print("Correct! Based on the plan, Door B likely leads to Bedroom 1.")
                    quiz_answer=True
                else:
                    print("Incorrect. Try another time!")
                    quiz_answer=False
                    return player_action('play')
            #######################################################################################
            elif door == 'door C': # quiz('door C')
                print("Question: If you wake up on the couch, and the key to Door C is found nearby, what is the most logical room Door C leads to, considering the floor plan?")
                print("A) The Game Room")
                print("B) Bedroom 2")
                print("C) The Outdoors")
                
                answer = input("Enter your choice (A, B, or C): ").upper()
                if answer == "C":
                    print("Correct! It makes sense that Door C might lead outside.")
                    quiz_answer=True
                else:
                    print("Incorrect. Consider the layout again!")
                    quiz_answer=False
                    return player_action('play')
            #######################################################################################
            elif door == 'door D': # quiz('door D')
                print("Question: Considering the floor plan, and the fact you woke up on the couch, where is Door D most likely located?")
                print("A) In the Game Room")
                print("B) In Bedroom 1")
                print("C) Not visible on the plan")

                answer = input("Enter your choice (A, B, or C): ").upper()
                if answer == "C":
                    print("Correct! Since Door D isn't shown, it's not visible on the plan.")
                    quiz_answer=True
                else:
                    print("Incorrect. Maybe Door D is a secret door?")
                    quiz_answer=False
                    return player_action('play')
            #######################################################################################
    return quiz_answer

######################################################################################################











##################################################################################################################
############################## FUNCTIONs : UPDATE PATHS ###########################################################################################
##################################################################################################################

# update space path [game room, bedroom 1, bedroom 2...]
def update_space_path(current_space:str):
    game_state['space path'].append(current_space)
    return game_state['space path']

# update item path [couch, piano, queen bed...]
def update_item_path(item:str):
    game_state['item path'].append(item)
    return game_state['item path']

# update door path [door A, door B, door C, ...]
def update_door_path(door:str):
    game_state['door path'].append(door)
    return game_state['door path']

# update inventory [key door A, key door B, key door C...]
def update_inventory(key:str):
    game_state['inventory'].append(key)
    return game_state['inventory']

# display_clock_countdown


##################################################################################################################
################# FUNCTIONs : UPDATE GAME STATE ###############################################################################################
##################################################################################################################

def update_game_state(space, item, key, door):
    update_space_path(space) #update space
    update_item_path(item) #update item
    update_inventory(key) #update key

    #display_clock_countdown() #run clock countdown

################## PLAYER_INPUT = NAVIGATE  ######################################################

print('Player is navigating to a new space!')

def navigate(space, door, inventory):
    print(f'Navigating through the {door}')
    if door in game_state['door path'] and space in spaces:

        # space is new_space
        while (action == 'unlock door' and action != 'quit' and action != 'restart'): # While loop
            if ('door A' in space) and ('door B' not in space) and ('door C' not in space) and ('door D' not in space):
                update_space_path('game room')

            elif ('door A' in space) and ('door B' in space) and ('door C' in space) and ('door D' not in space):
                update_space_path('bedroom 1')
        
            elif ('door A' not in space) and ('door B' in space) and ('door C' not in space) and ('door D' not in space):
                update_space_path('bedroom 2')
        
            elif ('door A' not in space) and ('door B' not in space) and ('door C' in space) and ('door D' in space):
                update_space_path('living room')
        
            elif ('door A' not in space) and ('door B' not in space) and ('door C' not in space) and ('door D' in space):
                update_space_path('outside')
                print("FREEDOM | YOU WIN !")
                print(game_state)
                break
            else:
                print("UNKNOWN SPACE in the system?")
            
            print(f'You are now in {space}')
        update_space_path(space)





    
##################################################################################################################
################# PLAYER_INPUT = RESTART  ###############################################################################################
##################################################################################################################
def restart(answer: bool):
    reset_game()
################## FUNCTION : RESET_GAME  ###########################################################################
def reset_game():
    answer = input("Do you want to restart the game? Enter: YES or NO")
    while answer !='YES' and answer!='NO':
        answer = input("To restart Enter only : YES or NO")
    
    if answer.low() == 'yes':
        print("Restarting the game...")
        game_state["space path"].clear()
        game_state["item path"].clear()
        game_state["inventory"].clear()
        game_state["door path"].clear()
    elif answer.low() == 'no':
        print("Continue to play...")
        player_action('play')
    else:
        print("Value Error: Enter YES or NO")

    return game_state


##################################################################################################################
################# PLAYER_INPUT = QUIT  ###############################################################################################
##################################################################################################################



################## PLAYER_INPUT = QUIT ######################################################

def quit():
    print("Quitting the game...")
    return game_state



##########################################################################################################
################## EXTRA FEATURES CAN BE ADDED HERE ######################################################
##########################################################################################################

# define a function that starts the clock, countdown, and display
''' def display_clock_countdown(t): '''

# Starts the live clock and countdown display for t minutes.
# Example: Start 5-minute countdown
''' display_clock_countdown(5) '''

# define Function to display live clock and countdown timer
import time
import sys
from datetime import datetime, timedelta

def display_clock_countdown(minutes):
    try:
        while True:  # Repeat indefinitely (change True to play=true)
            end_time = datetime.now() + timedelta(minutes=minutes)

            while True:
                # Current time
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")

                # Remaining time
                remaining_time = end_time - now
                if remaining_time.total_seconds() <= 0:
                    print(f"\rClock: {current_time} | Countdown: 00:00:00 ⌛", end="")
                    break

                hours, remainder = divmod(int(remaining_time.total_seconds()), 3600)
                mins, secs = divmod(remainder, 60)
                countdown_str = f"{hours:02}:{mins:02}:{secs:02}"

                # Print live clock and countdown on one line
                print(f"\r🕰️ Clock: {current_time} | ⏳ Countdown: {countdown_str}", end="")
                sys.stdout.flush()

                time.sleep(1)

            # Big "Time's Up" banner
            print("\n" + "*"*50)
            print("*****            TIME'S UP!            *****")
            print("*****      Restarting countdown...     *****")
            print("*"*50 + "\n")
            time.sleep(1)  # Optional pause before restarting

    except KeyboardInterrupt:
        print("\nCountdown stopped manually.")