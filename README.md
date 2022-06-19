- This program is designed to solve a differential equation like this: $m*y'' + p * y' + k * y = 0$


- Program uses Runge-Kutta method of the fourth order
- First of all, we need to convert the equation to the following system:
    - $y'=z$
    - $y'' = z'=\ - p / m * z - k / m * y = f(y,z)$
- Then we apply the method to each of the equations
- Finally, we create a plot using matplotlib.