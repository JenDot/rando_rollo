"""Rando Rollo: A game to select a winner."""

from pickle import FALSE, TRUE
import random, os, time, waiter

"""Set global variables"""
PEOPLE = []


"""Define mechanism to select regional staff for final drawing."""
def random_region(*args):
    regions = ["East Bay", "Peninsula", "San Francisco", "South Bay"]

    for region in regions:
        waiter.waiter(region)
    time.sleep(0.5)
    print("The winning region is ...")
    time.sleep(0.5)
    return print(f"{random.choice(regions)}!")

"""Define ultimate drawing to select 2 winners:
Tool will request staff names from input()  and then roll twice with a short pause in between, to select staff people to win the month's drawing."""
def get_people():
    people_full = FALSE
    print("Now let's enter staff names.")
    time.sleep(2.0)
    # Set rule to keep asking for staff names until user says list is full.
    while people_full == FALSE:
        PEOPLE.append(input("Enter staff person's name:  "))
        print(f"Staff people entered: {PEOPLE}.")
        people_full_question = input(
            "Enter another staff person?  (Enter y or n.)  ")
        # Change 'people_full_question' to TRUE if the user answers 'n' to 'people_full_question'.
        if people_full_question == "n":
            # people_full = TRUE
            break
    return PEOPLE

def drawing(*args):
    print("Who will be the winner!?")
    for person in PEOPLE:
        waiter.waiter(person)
    time.sleep(0.5)
    print("The winner is ...")
    time.sleep(0.5)
    winner = random.choice(PEOPLE)
    PEOPLE.pop(PEOPLE.index(winner))      # Remove the winner from the list because (s)he can only win once per month.
    return print(f"{winner}!")

"""Put all of the parts together!"""
def raffle():
    random_region()
    time.sleep(5.0)
    get_people()
    time.sleep(5.0)
    drawing(PEOPLE)
    time.sleep(5.0)
    drawing(PEOPLE)     # drawing() needs to be executed twice because there will be 2 winners.

raffle()