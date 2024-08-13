# CognitoCurtain

**CognitoCurtain** is a Python application that dynamically dims inactive monitors based on the position of the mouse. This tool helps in focusing attention on the active monitor while dimming others to minimize distractions.

## Features

- **Mouse-Driven Dimming**: Automatically dims monitors that are not under the mouse cursor.
- **Full-Screen Dimming**: Covers the entire screen of inactive monitors with a semi-transparent black overlay.
- **Customizable**: Easy to modify the dimming effect or add additional features.

## Requirements

- Python 3.x
- `pyautogui` - For getting the current mouse position.
- `screeninfo` - For retrieving monitor information.
- `tkinter` - For creating and managing the dimming windows.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/PSEUDO-SAPPHO/CognitoCurtain.git
    ```
2. Navigate to the project directory:
    ```sh
    cd CognitoCurtain
    ```
3. Install the required packages:
    ```sh
    pip install pyautogui screeninfo
    ```

## Usage

1. Ensure that your Python environment is set up correctly.
2. Run the `cognito_curtain.py` script:
    ```sh
    python cognito_curtain.py
    ```

3. The application will start running and monitor the mouse position. It will automatically dim inactive monitors.

## Code Overview

The `cognito_curtain.py` script performs the following tasks:

- **Create Dimming Windows**: For each monitor, a transparent Tkinter window is created to act as the dimming overlay.
- **Track Mouse Position**: Continuously checks the mouse cursor position using `pyautogui`.
- **Update Window Visibility**: Shows or hides the dimming windows based on which monitor the mouse is currently on.

## Example

If you have three monitors and your mouse is on the middle monitor, the left and right monitors will be dimmed.

## Troubleshooting

- **Flickering**: If you experience flickering on the dimmed monitors, try adjusting the transparency level or monitor refresh rates.
- **Application Not Responding**: Ensure that your Python environment is correctly set up and all required packages are installed.
