import tkinter as tk

root = tk.Tk()

frame1 = tk.Frame(root)
frame1.pack()

label1 = tk.Label(frame1, text="This is Frame 1")
label1.pack()

frame2 = tk.Frame(root)
frame2.pack()

label2 = tk.Label(frame2, text="This is Frame 2")
label2.grid(row=0, column=0)

root.mainloop()
