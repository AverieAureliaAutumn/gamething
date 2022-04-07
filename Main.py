#Imports ---------------------------------------------------------------------
from Player import Player
from World import World
from Color import Color
import time
import os
import sys
import asyncio
import json

#Global Variables ------------------------------------------------------------
player = Player() #I'm thinking of making it a static class ? since there will only be one player at a time

#General tools --------------------------------------------------------------
#Should make a static Utility Class maybe ?
#---
#here something i just found out
#You can't call a function that havent been defined on top of it
#Unless it's a class i guess ? it's the only language i know who does that
#even Javascript, who is also a runtime program, don't have a problem with it

def clear_terminal():
    #Clear Terminal
    os.system('cls' if os.name == 'nt' else 'clear')

#Menu ------------------------------------------------------------------------
#The Menu don't need to be in a loop
#This is gonna be an example of Asyncrone functions 
#Python with the asyncio library can run functions parralel to each other
#not needing to wait for a function to end for running an another one

#The Async keyword defines functions ready to be await by the main event loop
async def menu(message = ""):
    clear_terminal()
    
    print("")
    print(" Welcome to OGRES & OUBLIETTES!")
    print("")
    print(" Please, select an option below :")
    print("")
    print(" > "+ Color.bold("New") + " Game") #Color now being a Static class
    print(" > "+ Color.bold("Load") + " Game") #I can call its method without instances
    print(" > "+ Color.bold("Quit") + " Game")
    print(message)
    
    #To execute a asyncronu function, you need the keyword await; It will simply tell the main event loop to start
    #as a asyncron function. Here menu() will call menu_input() and directly end it's process. if we did as usual, the main()
    #function would still be active until we exit all the subfunction.
    #and you also always have to be inside a async function to work.
    await menu_input()
    #example : if you do a print("hey !") here, it will show, even as the menu_input() would run

async def load_game(message = ""):
    clear_terminal()
    save_names = []
    
    for x in range(5):
        with open("save/save("+str(x+1)+").json") as savefile:
            data = json.load(savefile)
            save_names.append(data["name"])
    
    print("")
    print(" Please select the slot you wish to load to:")
    print("")
    print(" 1) " + save_names[0])
    print(" 2) " + save_names[1])
    print(" 3) " + save_names[2])
    print(" 4) " + save_names[3])
    print(" 5) " + save_names[4])
    print("")
    print(" Go " + Color.bold("Back"))
    if message != "":
        print(message)
        message = ""
    print("")
    
    #Can be replaced by a is in range, the switch here might be overkill
    slot = input(" > ")
    match slot:
        case "1":
            load_file(1)
            await ready_check()
        case "2":
            load_file(2)
            await ready_check()
        case "3":
            load_file(3)
            await ready_check()
        case "4":
            load_file(4)
            await ready_check()
        case "5":
            load_file(5)
            await ready_check()
        case "Back":
            await menu()
        case _:
            await load_game(" Please try again:")

def load_file(slot):
    with open("save/save("+str(slot)+").json") as savefile:
        data = json.load(savefile)
        player.name = data["name"]
        player.health = data["health"]
        player.inventory = data["inventory"]
        World.story_step = data["story_step"]

async def menu_input():

    menu_input = input(" > ")
    
    match menu_input: #This is pattern matching, it's new to Python, and is the equivalent of a C#
        case "New":   #Switch case, _ represent no match found
            await new_game()
        case "Load":
            await load_game()
        case "Quit":
            sys.exit(" Thank you for playing!") #Clean program exit, with message
        case _:
            await menu(" Please try again:")

async def ready_check(message=""):
    clear_terminal()
    
    print("")
    print(" You are " + player.name)
    print(" Heatlth: "+str(player.health))
    player.look_inventory()
    print("")
    print(" Are you ready ? ("+Color.bold("Yes")+"/"+Color.bold("No")+")")
    print(message)
    
    ready_input = input(" > ")
    match ready_input:
        case "Yes":
            pass
        case "No":
            await menu()
        case _:
            await ready_check(" Please try again:")
    
async def new_game(message=""):
    clear_terminal()
    
    print("")
    print(" Welcome to the world of OGRES & OUBLIETTES, please enter your name :")
    print("")
    print(Color.bold(" Back") + " to menu | "+ Color.bold("Quit") + " game")
    print(message)
    
    name_input = input(" > ")
    match name_input:
        case "":
            await new_game(" Please, try again:")
        case "Empty":
            await new_game(" Please, try again:")
        case "Back":
            await menu()
        case "Quit":
            sys.exit(" Thank you for playing!")
        case _:
            player.name = name_input
            player.starter_pack()
            World.story_step = 0
            World.load()
            await ready_check()

#Python Async works with a "Event loop", any async function need a starting point, and it's here
#Thread will be terminated when all asyncrone function inside of it will stop running
asyncio.run(menu())

#Game loop ------------------------------------------------------------------
def main_loop():
    message = ""
    while True:
        clear_terminal()
        
        print("")
        World.read_story()
        print("")
        World.currentLocation.look_around()
        print("")
        player.look_inventory()
        print("")
        print(" Travel | Talk | Attack | Save | Quit")
        if message != "":
            print(message)
            message = ""
        print("")
        main_input()

def main_input():
    category_input = input(" > ")
    match category_input:
        case "Travel":
            travel_input()
        case "Talk":
            talk_input()
        case "Attack":
            pass
        case "Save":
            save_game()
        case "Quit":
            sys.exit(" Thank you for playing!")
        case _:
            message = " Please try again:"

def talk_input(message=""):
    clear_terminal()
    
    if World.currentLocation.has_npc() == False:
        talk_interface(False, message)
    elif World.currentLocation.npc.health <= 0:
        talk_interface(False, message)
    else:
        talk_interface(True, message)
    
    match input(" > "):
        case "Back":
            pass
        case _:
            talk_input(" Please try again")

def talk_interface(check, message=""):
    if check != True:
        print("")
        print(" There is no one to talk to")
        print("")
        if message != "":
            print("")
            print(message)
            message = ""
        print(" Go Back")
        print("")
    else:
        print("")
        print(" You talk with " + World.currentLocation.npc.description())
        print("")
        print(" " + World.currentLocation.npc.dialogue)
        if message != "":
            print("")
            print(message)
            message = ""
        print("")
        print(" Go Back")
        print("")

def travel_input(message=""):
    clear_terminal()
    print("")
    print(" Where do you want to go ?")
    if message != "":
        print(message)
        message = ""
    print("")
    for location in World.currentLocation.connections:
        print(" > " + location.name)
    
    destination_input = input(" > ")
    print(destination_input)
    if destination_input == "Back":
        pass
    else:
        if World.travel(destination_input):
            pass
        else:
            travel_input(" Please try again:")
    
def save_game(message = ""):
    clear_terminal()
    save_names = []
        
    for x in range(5):
        with open("save/save("+str(x+1)+").json") as savefile:
            data = json.load(savefile)
            save_names.append(data["name"])
    
    print("")
    print(" Please select the slot you wish to save to:")
    print("")
    print(" 1) " + save_names[0])
    print(" 2) " + save_names[1])
    print(" 3) " + save_names[2])
    print(" 4) " + save_names[3])
    print(" 5) " + save_names[4])
    print("")
    print(" Go " + Color.bold("Back"))
    if message != "":
        print(message)
        message = ""
    print("")
    
    #Can be replaced by a is in range, the switch here might be overkill
    slot = input(" > ")
    match slot:
        case "1":
            save_file(1)
        case "2":
            save_file(2)
        case "3":
            save_file(3)
        case "4":
            save_file(4)
        case "5":
            save_file(5)
        case "Back":
            pass
        case _:
            save_game(" Please try again:")

def save_file(slot):
    save_data = {
        "name": player.name,
        "health": player.health,
        "inventory": player.inventory,
        "story_step": World.story_step
    }
    
    json_string = json.dumps(save_data)
    
    with open("save/save("+str(slot)+").json","w") as outfile:
        outfile.write(json_string)

# def attack_input(message = ""):
    # if World.currentLocation.has_npc() == False:
        # attack_interface(False, message)
    # elif World.currentLocation.npc.health <= 0:
        # attack_interface(False, message)
    # else:
        # attack_interface(True, message)
        
        # match input(" > "):
            # case "Attack":
                # pass
            # case "Drink":
                # pass
            # case "Back":
                # pass
            # case _:
                # attack_input(" Please try again:")

# def attack_interface(check, message=""):
    # if check:
        # npc = Wolrd.currentLocation.npc
        # print("")
        # print(" You enter combat with " + npc.description())
        # print("")
        # print(" " + npc.description()+ " " + str(npc.health) + "HP")
        # print(" "+ player.name + )
        # print(" Attack | Drink | Back")
        # if message != "":
            # print("")
            # print(message)
            # message = ""
        # print("")
        
    # else:
        # print("")
        # print(" There is no one here")
        # if message != "":
            # print("")
            # print(message)
            # message = ""
        # print("Go Back")
        # print("")
    

#Start the game
main_loop()