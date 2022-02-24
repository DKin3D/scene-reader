import Scrolltext as Scr

# Scr.st = 'typing' speed (Scr is module, st is variable)
# Scr.txt = text to scroll (Scr is module, txt is function)

# These next lines are for adding the quit function at any input interval. Maybe there's an easier way of doing this.
# If there isn't this will be easier if it's literally added every f#$%ing time from the start.
# Change variable_changeme to whatever the input is to be called OFC
#     variable_changeme = input("")
#     if variable_changeme.lower() == 'q':
#         quit()
#     else:
#     slide_2()

Scr.st = .001


# This needs to be updated for each slide function.
def scene_select():
    Scr.txt("Select a slide from 1 to 3: ")
    select_option = input("")
    if select_option == '1':
        slide_1()
    elif select_option == '2':
        slide_2()
    elif select_option == '3':
        slide_3()
    elif select_option == 'q':
        quit()


def slide_1():
    Scr.txt("Does this work? This should be the first slide...")
    Scr.txt("Press any key to continue:")
    choice = input("")
    if choice.lower() == 'q':
        quit()
    else:
        slide_2()


def slide_2():
    Scr.txt("This should be the second slide...")
    Scr.txt("Press any key to continue: ")
    choice = input("")
    if choice.lower() == 'q':
        quit()
    else:
        slide_3()


def slide_3():
    Scr.txt("This should be the third slide...")
    Scr.txt("Press any key to continue: ")
    choice = input("")
    if choice.lower() == 'q':
        quit()
    else:
        start_text()


def start_text():
    Scr.txt("Start from beginning with any key, press 's' to select slide, or press 'q' to quit at any prompt: ")
    choice_1 = input("")
    if choice_1.lower() == 's':
        scene_select()
    elif choice_1.lower() == 'q':
        quit()
    else:
        slide_1()


start_text()
