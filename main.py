from pynput import mouse, keyboard
import math

from text_to_speech import speak_text

class MouseClickTracker:
    def __init__(self):
        self.click_count = 0
        self.positions = []
        self.alt_pressed = False

    px_firstPosN = 72 # Initial map view
    px_secondPosN = 294 # First card upgrade
    px_thirdPosN = 207 # Second card upgrade

    # Here we check keystrokes and record the mouse cursor position
    def on_click(self, x, y, button, pressed):
        if self.alt_pressed and pressed:
            if self.click_count < 2:
                self.positions.append((x, y))
                self.click_count += 1

                if self.click_count == 2:
                    distance = self.calculate_distancePx(self.positions[0], self.positions[1])
                    distanceM = self.calculate_meterDistance(distance)
                    print(f"Distance: {distance:.2f} px")
                    print(f"Distance : {distanceM:.2f} m")

                    speak_text(f"{distanceM:.0f}") # Here we transfer the received meters to “text to speach (TTS)"

                    self.click_count = 0
                    self.positions = []
                    self.alt_pressed = False

    def on_key(self, key):
        if key == keyboard.Key.alt_l:
            self.alt_pressed = True
        else:
            self.alt_pressed = False

    # Get the distance in pixels
    def calculate_distancePx(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # One square from the map grid is 300 meters
    square_per_meter = 300

    # We get the distance in meters
    def calculate_meterDistance(self, px):
        px_in_met = self.px_secondPosN / self.square_per_meter 
        dis_in_met = px * px_in_met
        return dis_in_met
    
def track_mouse_clicks():
    listener = mouse.Listener()
    tracker = MouseClickTracker()

    listener.on_click = tracker.on_click
    keyboard_listener = keyboard.Listener(on_press=tracker.on_key)

    listener.start()
    keyboard_listener.start()

    listener.join()
    keyboard_listener.join()

if __name__ == "__main__":
    track_mouse_clicks()