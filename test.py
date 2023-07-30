from tkinter import *

root = Tk()
root.title('Entry Widget with Caption')

# Create a label as the caption
caption_label = Label(root, text='Enter your name:')
caption_label.pack()

# Create an Entry widget
entry_widget = Entry(root)
entry_widget.pack()

root.mainloop()
