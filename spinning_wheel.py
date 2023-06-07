from tkinter import *
from PIL import Image, ImageTk
import time
import json
import math
import random
import colorsys
import sys

def load_states(json_file):
    with open(json_file, "r") as f:
        states = json.load(f)

    n_states = len(states)
    for i, state in enumerate(states):
        if "color" not in state:
            rgb = [int(c * 255) for c in colorsys.hls_to_rgb(i / n_states, 0.5, 1.0)]
            state["color"] = "#{:02x}{:02x}{:02x}".format(*rgb)

    return states

def spin_wheel(states, visited=None):
    if visited is None:
        return random.choice(states)

    if len(visited) == len(states):
        visited.clear()

    while True:
        state = random.choice(states)
        if state not in visited:
            visited.append(state)
            break
    return state

def spin_wheel_animation(states, target_state, canvas, label):
    n_states = len(states)
    target_idx = states.index(target_state)

    for i in range(target_idx + n_states*10):  # Spin 10 rounds before stopping
        draw_wheel(canvas, states, i % n_states)
        canvas.update()
        time.sleep(0.01)

    label.config(text=target_state["text"], bg=target_state["color"])

def draw_wheel(canvas, states, rotation):
    n_states = len(states)
    canvas.delete("all")

    center_x, center_y = canvas.winfo_width() / 2, canvas.winfo_height() / 2
    radius = min(center_x, center_y) * 0.8

    for i, state in enumerate(states):
        angle1 = 2 * math.pi * ((i + rotation) / n_states)
        angle2 = 2 * math.pi * (((i + 1) + rotation) / n_states)

        x1, y1 = center_x + radius * math.cos(angle1), center_y - radius * math.sin(angle1)
        x2, y2 = center_x + radius * math.cos(angle2), center_y - radius * math.sin(angle2)

        canvas.create_polygon(center_x, center_y, x1, y1, x2, y2, fill=state["color"])

        text_angle = (angle1 + angle2) / 2
        text_x = center_x + 0.5 * radius * math.cos(text_angle)
        text_y = center_y - 0.5 * radius * math.sin(text_angle)
        canvas.create_text(text_x, text_y, text=state["text"], font=("Helvetica", int(min(center_x, center_y)/10)))

    # Draw stationary dial
    dial_x = center_x + radius * math.cos(-math.pi / 2)
    dial_y = center_y - radius * math.sin(-math.pi / 2)
    canvas.create_line(center_x, center_y, dial_x, dial_y, width=3, arrow="last")

def spin_button_click(states, visited, canvas, label):
    target_state = spin_wheel(states, visited)
    spin_wheel_animation(states, target_state, canvas, label)

def random_spin_button_click(states, canvas, label):
    target_state = spin_wheel(states)
    spin_wheel_animation(states, target_state, canvas, label)

def main(json_file):
    states = load_states(json_file)
    visited = []

    root = Tk()
    root.title("Spinning Wheel")
    root.geometry("1200x1200")

    canvas = Canvas(root, width=900, height=900, bg="white")
    canvas.pack(fill=BOTH, expand=YES)

    draw_wheel(canvas, states, 0)

    spin_button = Button(root, text="Spin (unvisited)!", command=lambda: spin_button_click(states, visited, canvas, label))
    spin_button.pack()

    random_spin_button = Button(root, text="Spin (random)!", command=lambda: random_spin_button_click(states, canvas, label))
    random_spin_button.pack()

    label = Label(root, text="", font=("Helvetica", 40), wraplength=200)
    label.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python spinning_wheel.py <json_file>")
        sys.exit(1)

    main(sys.argv[1])

