 Triangle Generator

## Description

This program generates a **Sierpinski Triangle fractal pattern** using recursion and Python’s built-in `turtle` graphics module.

The user can:
- Choose a color for the pattern
- Select a recursion depth (1–5)
- Generate a fractal triangle pattern
- Exit the program using a simple menu

This project demonstrates recursive problem solving and graphical programming in Python.

---

## How It Works

The program uses recursion to draw a Sierpinski Triangle.

### Recursive Structure

**Base Case**
- When `depth == 0`, the program draws a single equilateral triangle.

**Recursive Case**
- When `depth > 0`, the function:
  1. Draws the bottom-left triangle
  2. Draws the bottom-right triangle
  3. Draws the top triangle  

Each recursive call draws triangles that are half the size of the previous one.

To ensure accurate positioning, the program:
- Saves the turtle’s starting position and heading
- Restores them after each recursive call

This prevents distortion and keeps the fractal aligned correctly.

---

## Requirements

- Python 3.x
- The `turtle` module (included with standard Python installations)
- A local environment that supports graphical windows  

This program will NOT run in cloud-based environments like GitHub Codespaces because `turtle` requires a GUI display.

---

##  How To Run

1. Make sure Python is installed on your computer.
2. Save the file as:

fractal_pattern_generator.py


3. Open a terminal or command prompt.
4. Run:

python fractal_pattern_generator.py


5. Follow the on-screen menu prompts.

---

## User Instructions

When the program starts:

1. Select **1** to generate a pattern.
2. Enter a valid color name (example: `blue`, `red`, `green`, `purple`).
3. Enter a recursion depth between **1 and 5**.
4. The fractal will be drawn in a turtle graphics window.

Select **2** from the menu to exit the program.

---

## Features

- Recursive fractal generation
- User-selected color
- Depth validation (1–5)
- Turtle position and heading reset for accurate recursion
- Menu-driven interface

---

## Limitations

- Depth is limited to 1–5 to prevent long drawing times.
- Must be run locally (requires graphical display support).
- Triangles are drawn as outlines (not filled).
