import Tkinter
from Tkinter import *

root = Tk()

status =Label(root, text="Working")
status.grid()

def update_status():

    # Get the current message
    current_status = status["text"]

    # If the message is "Working...", start over with "Working"
    if current_status.endswith("..."): current_status = "Working"

    # If not, then just add a "." on the end
    else: current_status += "."

    # Update the message
    status["text"] = current_status

    # After 1 second, update the status
    root.after(1000, update_status)

# Launch the status message after 1 millisecond (when the window is loaded)
root.after(1, update_status)

root.mainloop()