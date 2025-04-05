# 👋🎮 Hand Gesture-Controlled Block Breaker Game

Control a browser-based Block Breaker game using hand gestures via your webcam! This Python project combines computer vision with gaming for a fun and interactive experience.

## ✨ Features
- ←→ **Swipe Detection**: Control paddle movement with hand gestures.
- ✊ **Fist Recognition**: Close your hand to launch the ball.
- 🖥 **Real-Time Feedback**: On-screen directions and terminal logging for easy interaction.
- 🕹 **Cross-Game Compatibility**: Works with most games controlled by arrow keys.
- ⏱ **Cooldown System**: Prevents accidental rapid inputs and enhances user experience.

## 🛠 Technologies Used
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.8%2B-orange)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-0.9%2B-yellow)

## 🚀 Installation
1. Clone the repository:
```bash
git clone https://github.com/aitiwari/cv2game.git
cd cv2game
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```
*(or)*  
Manual install:
```bash
pip install opencv-python mediapipe pyautogui
```

## 🎮 Usage
1. Launch your favorite Block Breaker game in the browser:
```bash
# Recommended: https://www.crazygames.com/game/block-breaker
```

2. Run the control system:
```bash
python block_breaker_control.py
```

3. **Gestures**:
   - 👉👈 Horizontal swipes → Move paddle
   - ✊ Closed fist → Launch ball
   - 🖐 Open hand → Stop paddle
   - Press 'Q' to exit the game control system.

## ⚙️ Configuration
You can adjust the following settings in `block_breaker_control.py`:
```python
SWIPE_THRESHOLD = 40    # Sensitivity (pixels)
PADDLE_MOVE_DELAY = 0.1 # Movement responsiveness
COOLDOWN_TIME = 0.3     # Input cooldown (seconds)
```

## 🕹 Compatible Games
| Game            | Controls               | Demo URL                      |
|-----------------|------------------------|-------------------------------|
| Block Breaker   | ← → + SPACE            | [Play](https://crazygames.com) |
| Chrome Dino     | SPACE + ↓              | chrome://dino                 |
| Google Snake    | ← ↑ → ↓                | [Play](https://google.com)    |
| Subway Surfers  | ← → ↑ ↓                | (BlueStacks required)         |

## 🚨 Troubleshooting
| **Issue**                   | **Solution**                                              |
|-----------------------------|-----------------------------------------------------------|
| Webcam not detected         | Check camera permissions.<br>Try `cv2.VideoCapture(1)`   |
| Laggy controls              | Reduce `SWIPE_THRESHOLD`.<br>Close background apps.      |
| False positives             | Increase `COOLDOWN_TIME`.<br>Improve lighting conditions. |
| Ball not launching          | Make a clearer fist gesture.<br>Ensure browser is focused. |
