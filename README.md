- This program is designed to solve a differential equation like this: $m*y'' + p * y' + k * y = 0$


- Program uses Runge-Kutta method of the fourth order
- First of all, we need to convert the equation to the following system:
    - $y'=z$
    - $y'' = z'=\ - p / m * z - k / m * y = f(y,z)$
- Then we apply the method to each of the equations
- Finally, we create a plot using matplotlib.

Here is plot for $m = 1, p = 0.2$ and $k = 2$

![image](https://user-images.githubusercontent.com/58353454/174498517-bd9a6c80-7085-4b91-b4b9-9e67b0a8675f.png)

