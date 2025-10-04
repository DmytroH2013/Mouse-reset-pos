import pyautogui
import keyboard
import tkinter as tk
import threading
import os

def teleport_mouse_to_center():
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2
    pyautogui.moveTo(center_x, center_y)

# Function to show the UI
def show_window():
    root.deiconify()  # Show the window

# Function to hide the UI
def hide_window():
    root.withdraw()  # Hide the window

# Function to quit the app
def quit_app():
    root.destroy()

# Start a background listener to keep hotkeys active
def run_keyboard_listener():
    keyboard.wait()  # Keeps hotkeys alive

# Register hotkeys
keyboard.add_hotkey('home', teleport_mouse_to_center)
keyboard.add_hotkey('end+home', show_window)  # Press End + Home to show UI

listener_thread = threading.Thread(target=run_keyboard_listener, daemon=True)
listener_thread.start()

# Build the UI
root = tk.Tk()
root.title("Mouse Teleporter")
root.geometry("300x140")

# Set the icon for the tkinter window
# Make sure your icon file is in the same folder as this script
icon_path = os.path.join(os.path.dirname(__file__), "mouse_icon.ico")
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)

label = tk.Label(root, text="Press HOME to center the mouse.", font=("Arial", 12))
label.pack(pady=10)

background_button = tk.Button(root, text="Run in Background", command=hide_window)
background_button.pack(pady=5)

quit_button = tk.Button(root, text="Quit", command=quit_app)
quit_button.pack(pady=5)

# Start minimized
root.withdraw()

root.mainloop()
