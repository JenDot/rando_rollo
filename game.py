"""Rando Rollo: A game to select a winner."""

from pickle import FALSE, TRUE
import random
import os
import time

"""Set global variables"""
staff_names = []
waiter = time.sleep(3.0)

"""Define mechanism to select regional staff for final drawing."""
def random_region(*args):
    regions = ["East Bay", "Peninsula", "San Francisco", "South Bay"]

    for region in regions:
        print(region)
        time.sleep(0.20)
        os.system('clear')
        time.sleep(0.2)
    time.sleep(0.5)
    print("The winning region is ...")
    time.sleep(0.5)
    return print(f"{random.choice(regions)}!")
random_region()

"""Define ultimate drawing to select 2 winners:
Tool will request staff names from input()  and then roll twice with a short pause in between, to select staff people to win the month's drawing."""
def get_staff_names():
    staff_names_full = FALSE
    # Set rule to keep asking for staff names until user says list is full.
    while staff_names_full == FALSE:
        staff_names.append(input("Enter staff person's name:  "))
        print(f"Staff people entered: {staff_names}.")
        staff_full_question = input(
            "Enter another staff person?  (Enter y or n.)")
        # Change 'staff_full_question' to TRUE if the user answers 'n' to 'staff_full_question'.
        if staff_full_question.lower == "n":
            staff_names_full = TRUE
    return random.choice(staff_names)
get_staff_names()