import pyautogui
from screeninfo import get_monitors
import tkinter as tk

# Dictionary to keep track of dimming windows
dimming_windows = {}

def create_dimming_window(monitor):
    """Create a dimming window for a given monitor."""
    root = tk.Tk()
    root.geometry(f'{monitor.width}x{monitor.height}+{monitor.x}+{monitor.y}')
    root.configure(bg='black')
    root.attributes('-alpha', 1.80)  # 100% transparency
    root.overrideredirect(True)
    root.attributes('-topmost', True)  # Keep window on top
    return root

# Create dimming windows for all monitors and use monitor IDs as keys
monitors = get_monitors()
for monitor in monitors:
    key = (monitor.x, monitor.y, monitor.width, monitor.height)  # Unique key for each monitor
    dimming_windows[key] = create_dimming_window(monitor)
    dimming_windows[key].withdraw()  # Initially hide the dimming window

while True:
    x, y = pyautogui.position()
    active_key = None

    # Determine which monitor the mouse is currently on
    for monitor in monitors:
        if monitor.x <= x <= monitor.x + monitor.width and monitor.y <= y <= monitor.y + monitor.height:
            active_key = (monitor.x, monitor.y, monitor.width, monitor.height)
            break

    # Update the visibility of dimming windows
    for key in dimming_windows:
        if key == active_key:
            dimming_windows[key].withdraw()  # Hide dimming window for active monitor
        else:
            dimming_windows[key].deiconify()  # Show dimming window for inactive monitors

    # Update the Tkinter windows
    for window in dimming_windows.values():
        window.update_idletasks()
        window.update()
