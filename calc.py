from Tkinter import *

class Calculator(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg="#2C2F33")
        self.pack(expand=YES, fill=BOTH)
        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display the calculations
        self.display = Entry(self, width=20, font=("Arial", 20), justify=RIGHT)
        self.display.grid(row=0, column=0, columnspan=4, pady=(20, 10), padx=5, sticky=EW)

        # Bind the Entry widget to the <Return> event
        self.display.bind("<Return>", self.calculate)

        # Buttons for numbers and operators
        button_texts = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        # Create buttons in a loop
        for i, text in enumerate(button_texts):
            button = Button(self, text=text, width=5, height=2, font=("Arial", 16), bg="#99aab5", fg="#000000")
            button.grid(row=i/4+1, column=i%4, pady=5, padx=5, sticky=EW)
            button.bind("<Button-1>", self.button_click)

        # Clear button
        clear_button = Button(self, text="Clear", width=10, height=2, font=("Arial", 16), bg="#99aab5", fg="#000000")
        clear_button.grid(row=5, column=0, columnspan=2, pady=10, padx=5, sticky=EW)
        clear_button.bind("<Button-1>", self.clear_display)

        # Change the background color of the window
        self.master.configure(bg="#2C2F33")

        # Center the window on the screen
        self.master.eval('tk::PlaceWindow %s center' % self.master.winfo_pathname(self.master.winfo_id()))

        # Bind the "=" key to the calculate method
        self.master.bind("<KeyPress-=>", self.calculate)

    def button_click(self, event):
        # Add the clicked button's text to the display
        button = event.widget
        text = button["text"]
        if text == "=":
            self.calculate()
        else:
            self.display.insert(END, text)

    def clear_display(self, event):
        # Clear the display
        self.display.delete(0, END)

    def calculate(self, event=None):
        # Evaluate the expression and display the result
        try:
            result = str(eval(self.display.get()))
            self.display.delete(0, END)
            self.display.insert(END, result)
        except:
            self.display.delete(0, END)
            self.display.insert(END, "Error")

root = Tk()
root.title("Calculator")
root.geometry("320x450")
calculator = Calculator(root)
root.mainloop()
