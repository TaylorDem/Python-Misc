# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 20:31:03 2024

@author: demar
"""

import matplotlib.pyplot as plt
import numpy as np
"""
plt.plot([1,2,3,4], "kx")   # black X's
plt.plot([1,2,3,4], "r--")  # red dashed line
plt.plot([1,2,3,4], "c:")   # cyan dotted line
plt.plot([1,2,3,4], "b-")   # blue straight line, this is default. 
plt.axis([0,6,0,6])         # sets the axis view. xmin, xmax, ymin, ymax
#plt.axis("off")            #this turns off the axes.
"""
t = np.arange(0, 5, .2)     #create array quick
#lines collects the 3 different lines created.
lines = plt.plot(t, t, t, t**2, 'rs', t, t**3, 'g^')        #plot 3 lines, (t,t), (t,t^2) as red squares, (t,t^3) as green triangles

#add text to the graphs.
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Example Exponential Growth", fontweight = "bold")    #set properties
txt = plt.text(1,65,"Hello!!")
#after the fact you can modify outside of initialization the things like font with setp().
plt.setp(txt, color="r", fontweight="bold")

#create a legend
plt.legend(lines, [r'Y', r'Y$^2$', r'Y$^3$'])
#        ^ = superscript,    r'$insert math expression here$'