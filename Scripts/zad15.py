import threading
import time
from tkinter import messagebox

def job():
    
    messagebox.showinfo('UsefulPython', 'отдохни брат')

while True:
    time.sleep(1)
    job()
        
