+++
date = "2016-12-20T12:00:00"
draft = true
image = ""
tags = ["howto"]
title = "Contributing"
math = true
summary = """
Some remarks about the homepage layout and how to contribute.
"""
+++

This is a test page/playground with some examples on how to use the blog.

## Rendering Latex

Inline math like $21 \cdot 2 = 42$ is introduced with ``$ ... $``, while double signs ``$$ ... $$`` create
a new paragraph containing the equation:

$$
f(x) = \int\_{x' \in \Omega} u(x') k(x-x') \text{d}x'
$$

Since it is really annoying that using single ``_`` signs in formulas are usually mistaken by markdown editors,
make sure to use ``\_`` in latex formulas instead.

## Inserting code snippets

Rendering code is of course also possible:

``` python
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from numpy import ma
%matplotlib inline

ϵ = 0.1
b0 = 2.
b1 = 1.5

dudt = lambda U,W,I : U - U**3 / 3 - W + I
dwdt = lambda U,W : ϵ * (b0 + b1 * U - W)

def compute_trajectory(u0, w0, I, steps, dt):
    uu = [u0]
    ww = [w0]
    
    for t in range(steps):
        uu.append(uu[-1] + dudt(uu[-1], ww[-1], I) * dt)
        ww.append(ww[-1] + dwdt(uu[-1], ww[-1]) * dt)
        
    return np.array(uu), np.array(ww)

def trajectory_plot(I = 2):
    w_u0 = lambda u : (u - u**3 / 3 + I)
    u_u0 = lambda u : b0 + b1 * u

    U, W = np.meshgrid(np.arange(-3, 3, .5), np.arange(-3, 5, .5))
    dU = dudt(U,W,I)
    dW = dwdt(U,W)

    # Quiver Plot
    plt.figure()
    Q = plt.quiver(U,W,dU, dW, width=0.003, scale=100)
    qk = plt.quiverkey(Q, 0, 0, 3, r'$\dot x$', labelpos='N',
                       fontproperties={'weight': 'bold'})
    l, r, b, t = plt.axis()
    dx, dy = r - l, t - b
    plt.axis([-3,3,-3,5])

    # Zero Lines
    uu = np.linspace(-3,3,100)
    plt.plot(uu, w_u0(uu))
    plt.plot(uu, u_u0(uu))

    # Trajectory
    uu, ww = compute_trajectory(-2,-2,I,10000,0.01)
    plt.plot(uu, ww)

    plt.xlabel(r"$u$")
    plt.ylabel(r"$w$")
```
