# recurssive_traingle

Recursive Triangle Python Program
Introduction
Welcome to the Recursive Triangle Python program! This program uses the turtle graphics module to draw a beautiful and intricate triangle pattern recursively. A recursive function is used to create smaller triangles, which, when combined, form the larger triangle pattern.

Requirements
This program requires Python 3.x and the turtle graphics module to run.

How to Install Dependencies
If you don't have Python installed, you can download it from the official Python website (https://www.python.org/downloads/). The turtle graphics module comes pre-installed with Python, so no additional installations are necessary.

How to Run the Program
Clone or download the repository to your local machine.
Navigate to the project directory containing the Python script (recursive_triangle.py).
Run the recursive_triangle.py script using the following command:
Copy code
python recursive_triangle.py
A new window will appear displaying the turtle graphics. The program will draw a mesmerizing recursive triangle pattern.
Program Description
The main feature of this program is the recursive function draw_triangle, which is responsible for drawing the triangle pattern. It takes two parameters:

side_length: The size of the largest triangle's sides.
depth: The number of iterations for the recursion, determining the complexity of the pattern.
The function draws three smaller triangles within the larger one and then recursively repeats this process for each of the smaller triangles. As the recursion progresses, smaller triangles are drawn inside each other, creating an intricate pattern.

Customization
You can modify the side_length and depth variables in the main function to change the size and complexity of the triangle pattern.
Adjusting the depth parameter will result in a more intricate or simpler pattern. However, be cautious with extremely large values as it might take longer to render.








