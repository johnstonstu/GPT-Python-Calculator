from Tkinter import *

class Calculator(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display the calculations
        self.display = Entry(self, width=30, justify=RIGHT)
        self.display.grid(row=0, column=0, columnspan=4, pady=5)

        # Buttons for numbers and operators
        button_texts = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        # Create buttons in a loop
        for i, text in enumerate(button_texts):
            button = Button(self, text=text, width=5)
            button.grid(row=i/4+1, column=i%4)
            button.bind("<Button-1>", self.button_click)

        # Clear button
        clear_button = Button(self, text="Clear", width=5)
        clear_button.grid(row=5, column=0, columnspan=2, pady=5)
        clear_button.bind("<Button-1>", self.clear_display)

    def button_click(self, event):
        # Add the clicked button's text to the display
        button = event.widget
        text = button["text"]
        self.display.insert(END, text)

    def clear_display(self, event):
        # Clear the display
        self.display.delete(0, END)

root = Tk()
root.title("Calculator")
calculator = Calculator(root)
root.mainloop()
