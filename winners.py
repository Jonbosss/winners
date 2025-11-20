from tkinter import *
from random import randint

root = Tk()
root.title('Winner Randomizer')
root.geometry('400x400')


def pick():
    # 20 entries with 2 duplicates
    entries = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5',
               'Item 6', 'Item 7', 'Item 8', 'Item 9', 'Item 10',
               'Item 10', 'Item 11', 'Item 12', 'Item 13', 'Item 14',
               'Item 15', 'Item 16', 'Item 17', 'Item 18', 'Item 18']

    # convert to a set to eliminate duplicates
    entries_set = set(entries)
    # convert back to a list - 18 unique Items
    entries_list = list(entries_set)

    # create our list size variable
    our_number = len(entries_list) - 1
    # create a random number between 0 and 18
    rando = randint(0, our_number)

    winner_label = Label(
        root, text=(entries_list[rando]), font=('Helvetica', 18))
    winner_label.pack(pady=50)


top_label = Label(root, text='Win-O-Rama', font=('Helvetica', 24))
top_label.pack(pady=20)

win_button = Button(root, text='PICK OUR WINNER!!!',
                    font=('Helvetica', 24), command=pick)
win_button.pack(pady=20)

root.mainloop()
