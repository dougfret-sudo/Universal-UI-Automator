import pyautogui
import random
import time
import math

# 1. THE PLUG-PULL FAILSAFE
# Moving your mouse to any corner of the screen will kill the script immediately.
pyautogui.FAILSAFE = True

def human_move(target_x, target_y):
    """Moves the mouse to a target using a curved, variable-speed path."""
    start_x, start_y = pyautogui.position()
    
    # Create a 'Control Point' for the curve (The Human 'Sway')
    control_x = (start_x + target_x) / 2 + random.randint(-100, 100)
    control_y = (start_y + target_y) / 2 + random.randint(-100, 100)
    
    steps = random.randint(20, 45) # How many 'micro-moves' in the curve
    
    for i in range(steps + 1):
        t = i / steps
        # Bezier Curve Formula: Smooth, non-linear motion
        x = (1-t)**2 * start_x + 2*(1-t)*t * control_x + t**2 * target_x
        y = (1-t)**2 * start_y + 2*(1-t)*t * control_y + t**2 * target_y
        
        # Add 'Hand Jitter' (Tiny 1-2 pixel offsets)
        jitter_x = x + random.uniform(-1, 1)
        jitter_y = y + random.uniform(-1, 1)
        
        pyautogui.moveTo(jitter_x, jitter_y)
        
        # Variable Latency: Humans don't move at a constant speed
        time.sleep(random.uniform(0.001, 0.005))

def human_click(x, y):
    """Clicks with a slight delay and a 'fuzzy' target area."""
    # Never click the exact same pixel twice (The 'Fuzzy' Target)
    fuzzy_x = x + random.randint(-3, 3)
    fuzzy_y = y + random.randint(-3, 3)
    
    human_move(fuzzy_x, fuzzy_y)
    time.sleep(random.uniform(0.1, 0.3)) # Human 'Reaction' time
    pyautogui.click()
    print(f"Verified Human-Like Click at: {fuzzy_x}, {fuzzy_y}")

# --- SANDBOX TEST ---
print("--- STEALTH ENGINE ACTIVE: MOVE MOUSE TO CORNER TO KILL ---")
time.sleep(2) # Give yourself time to switch windows
# Test: Move to a random spot on your screen
human_click(800, 400)
