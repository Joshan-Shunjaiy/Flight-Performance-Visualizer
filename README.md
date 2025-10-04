# Flight-Performance-Visualizer
Python tool to model aircraft performance with Lift, Drag, Thrust, and Rate of Climb plots.
This project models aircraft flight performance using fundamental aerodynamic equations in Python.  
It generates performance curves such as Lift vs Speed, Drag breakdown, Thrust Required vs Available, and Rate of Climb vs Speed.

## Features
- Implements the ISA atmosphere model for density variation with altitude.  
- Uses the drag polar equation (CD = CD0 + k·CL²) with aspect ratio and Oswald efficiency factor.  
- Calculates and plots:
  - Lift vs Speed (with weight comparison)  
  - Parasite, Induced, and Total Drag vs Speed  
  - Thrust Required vs Thrust Available  
  - Rate of Climb vs Speed  
- Parameterized inputs: weight, wing area, drag coefficients, aspect ratio, thrust available.  
- Built with Python, Numpy, Matplotlib for numerical computation and visualization.  
