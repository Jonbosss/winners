from tkinter import *

root = Tk()
root.title('Winner Randomizer')
root.geometry('400x400')

entries = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5',
           'Item 6', 'Item 7', 'Item 8', 'Item 9', 'Item 10']


def pick():
    return


topLabel = Label(root, text='Win-O-Rama', font=('Helvetica', 24))
topLabel.pack(pady=20)

winButton = Button(root, text='PICK OUR WINNER!!!',
                   font=('Helvetica', 24), command=pick)
winButton.pack(pady=20)


root.mainloop()
