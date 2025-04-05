import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

# Control parameters
SWIPE_THRESHOLD = 40
PADDLE_MOVE_DELAY = 0.1
COOLDOWN_TIME = 0.3

# Game controls
GAME_CONTROLS = {'left': 'left', 'right': 'right'}

cap = cv2.VideoCapture(0)
last_move_time = time.time()
prev_x = 0
current_direction = None

def detect_swipe(current_x, prev_x):
    dx = current_x - prev_x
    if abs(dx) > SWIPE_THRESHOLD:
        return 'right' if dx > 0 else 'left'
    return None

def draw_game_overlay(img):
    cv2.putText(img, "Block Breaker Controls:", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.putText(img, "Swipe LEFT <- -> RIGHT", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
    cv2.putText(img, "Fist to Launch", (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
    cv2.putText(img, "Press 'Q' to exit", (10, 450),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    if current_direction:
        arrow_x = 300 if current_direction == 'right' else 100
        cv2.arrowedLine(img, (arrow_x, 200), (arrow_x + (50 if current_direction == 'right' else -50), 200), 
                       (0, 255, 255), 5)

while True:
    success, img = cap.read()
    if not success:
        continue

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    results = hands.process(img_rgb)
    hand_closed = False
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_finger = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            
            # Detect closed fist
            if index_finger.y > middle_finger.y:
                hand_closed = True
                pyautogui.press('space')
                print("[TERMINAL] Command: Ball launched! (SPACE)")  # New print
            
            current_x = int(index_finger.x * SCREEN_WIDTH)
            
            # Detect and print swipe direction
            if prev_x != 0:
                direction = detect_swipe(current_x, prev_x)
                
                if direction and (time.time() - last_move_time) > PADDLE_MOVE_DELAY:
                    pyautogui.keyDown(GAME_CONTROLS[direction])
                    current_direction = direction
                    last_move_time = time.time()
                    # Print to terminal with timestamp
                    print(f"[TERMINAL] Command: Swiped {direction.upper()}! ({time.strftime('%H:%M:%S')})")  # New print
                
                elif current_direction and (time.time() - last_move_time) > COOLDOWN_TIME:
                    pyautogui.keyUp(GAME_CONTROLS[current_direction])
                    current_direction = None
            
            prev_x = current_x
            
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    if not results.multi_hand_landmarks and current_direction:
        pyautogui.keyUp(GAME_CONTROLS[current_direction])
        current_direction = None
    
    draw_game_overlay(img)
    cv2.imshow("Hand-Controlled Block Breaker", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()