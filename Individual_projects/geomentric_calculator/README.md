# Geometric Calculator
***

This project is a geometric calculator built in Python. It allows users to create, store, view, compare, and sort different geometric shapes such as rectangles, squares, circles, and triangles. The program uses custom classes for each shape and stores shape data in a text file for persistence between runs. Users can interact with the program through a menu system to perform various calculations and operations on their shapes.

## How to use
***
1. Open the project in your code editor (such as VS Code).
2. Make sure all project files are in the correct folder structure.
3. Run the main file:
   ```
   python main.py
   ```
4. Use the menu to:
   - Create new shapes
   - View saved shapes
   - Compare shapes
   - Sort shapes
   - View formula guide
5. Follow the prompts in the terminal to input values and navigate the program.

**Libraries required:**
- `math` (built-in, no download needed)

## Details on project features
***
-  **Shape Creation**
  - Create rectangles, squares, circles, and triangles
  - Input validation ensures only positive numbers are accepted
  - Uses custom classes to calculate properties

-  **File Storage System**
  - Shapes are saved to a `.txt` file
  - Data persists between program runs

-  **View Shapes**
  - Displays all saved shapes in a clean format
  - Option to view detailed information about a specific shape

-  **Compare Shapes**
  - Compare two shapes by **area** or **perimeter**
  - Displays which shape is larger and by how much

-  **Sorting System**
  - Sort shapes by **area** or **perimeter**
  - Displays results in descending order

-  **Formula Guide**
  - Built-in reference for all geometric formulas used

-  **Object-Oriented Design**
  - Separate classes for each shape
  - Methods for area, perimeter, and other properties

