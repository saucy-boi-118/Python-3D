# Python-3D
A simple 3D engine made in pygame with python that has the ability to render Cubes, Pyramids, and Prisms using Classes and major abstraction to make the process simple

# Explanation and Resources
I based off most of my logic and rendering from Tsodings Youtube video that demystifies  3D graphics with a simple equation (Link Below). The video goes in depth about how 3D graphics are rendered on a 2D screen with implementation in JavaScript. I additionally also asked for help on Stack Overflow and I'll link my question and similar questions below.

Tsodings Video: https://www.youtube.com/watch?v=qjWkNZ0SXfo&t=30s
Stack Overflow Questions: https://stackoverflow.com/questions/56285017/pygame-rotating-cubes-around-axis (My question was taken down for being flagged as duplicate)

I am by no means an expert in python or 3D / Graphics Programming so my explanation and implementation may be flawed. To simplfy my implementation, basically all I did was create a point class that takes an (x,y,z) that can convert a normal cartesian coordinate (from -1 to 1) to normal screen coordinates. Additionally, to add rotation it uses a simple rotation matrix that just changes the positions of the points.

# Possible Future Updates
I might make this into useable python library with more features like cylinder, spheres, isohedrons, and custom models. I also might create this project in Golang for speed. 

# Example Output
![image](https://github.com/saucy-boi-118/Python-3D/blob/main/Screenshot%202026-05-29%20121905.png)
