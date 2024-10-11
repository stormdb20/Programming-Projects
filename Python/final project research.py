#Larry Baucum INT-1111

#Defining a function to create my gui with buttons
def main():
    
#Import tkinter library module
    import tkinter
#Import the dialog box 
    import tkinter.messagebox
#class and init method to build the gui
    class MyGUI:
        def __init__(self):
#Creating the main window
            self.main_window= tkinter.Tk()
#Creating my show details button with the do_something finction callback
            self.show_details= tkinter.Button(self.main_window,
                                             text='Show Details',
                                             command=self.do_something)
#Creating my exit button with the command to terminate the program
            self.exit= tkinter.Button(self.main_window,
                                     text='Exit Program',
                                     command=self.main_window.destroy)
#Calling the show details button
            self.show_details.pack()
#Calling my exit program button
            self.exit.pack()                                 
#The tkinter infinite loop to keep the window up
            tkinter.mainloop()
#executes the do_something command to show the text in the messagebox
        def do_something(self):
            tkinter.messagebox.showinfo('Larry Baucum',
                                        'INT-1111\nLD01\nIntro To Programming Logic and Design')
#Creating the instance for MyGUI
    my_gui=MyGUI()
#Calling the function
main()        
