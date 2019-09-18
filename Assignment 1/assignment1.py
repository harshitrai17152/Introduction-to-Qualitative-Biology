# Harshit Rai
# 2017152

import numpy as np
import matplotlib.pyplot as plt



# Given function
def func_gen(a, Nt):     
    return a*Nt*(1-Nt)




# For first part
def part_a(a, start, gra=None):  
    gra.set_title(f"$a={a:.1f}, x_0={start:.1f}, Part A$")
    x=0
    graph = np.linspace(0,1,200)
    t = func_gen(a,graph)
    gra.plot(graph, t, 'k', lw=1)
    gra.plot([0,1], [0,1],'k', lw=1) 

    x_p_1=0
    x=start
    for k in range(200):
        x_p_1 = func_gen(a,x)
        gra.plot([x,x], [x, x_p_1], 'k', lw=1)
        gra.plot([x, x_p_1], [x_p_1, x_p_1], 'k', lw=1)
        x = x_p_1




# For third part
def part_c(start, gra=None):
    gra.set_title(f"$x_0={start:.1f},Part C$")
    x=start
    a = np.linspace(1.4,4,260)
    for i in range(160):
        x_p_1 = func_gen(a,x)
        if (i>=100):
            gra.plot(a, x, 'k', lw=1)     
        x=x_p_1   





# For second part
def b_part(a, start, gra=None):    
    gra.set_title(f"$a={a:.1f}, x_0={start:.1f}, Part B$")
    x=0
    arre2 = [];
    arre = np.linspace(0,1, 100)
    val=0
    x=start
    for k in range(100):
        x_p_1 = func_gen(a,x)
        arre2.append(x_p_1)
        x = x_p_1
    gra.plot(arre, arre2, 'k', lw=1)




# Plotting Graphs
fig_1, (gra1) = plt.subplots(1, 1, figsize=(6, 6))
fig_2, (gra2) = plt.subplots(1, 1, figsize=(6, 6))
fig_3, (gra3) = plt.subplots(1, 1, figsize=(6, 6))
fig_a, (grgra) = plt.subplots(1, 1, figsize=(6, 6))

fig_4, (gra4) = plt.subplots(1, 1, figsize=(6, 6))
fig_4, (gra5) = plt.subplots(1, 1, figsize=(6, 6))
fig_4, (gra6) = plt.subplots(1, 1, figsize=(6, 6))
fig_b, (gray) = plt.subplots(1, 1, figsize=(6, 6))

fig_5, (gra7) = plt.subplots(1, 1, figsize=(6, 6))

gra1.set_ylim(0,1)
gra1.set_xlim(0,1)
grgra.set_ylim(0,1)
grgra.set_xlim(0,1)
gray.set_xlim(0,1)
gray.set_ylim(0,1)
gra2.set_ylim(0,1)
gra2.set_xlim(0,1)
gra3.set_ylim(0,1)
gra3.set_xlim(0,1)
gra4.set_ylim(0,1)
gra4.set_xlim(0,1)
gra5.set_ylim(0,1)
gra5.set_xlim(0,1)
gra6.set_ylim(0,1)

part_a(0.1, .1, gra=gra1)
part_a(1.356, .1, gra=gra2)
part_a(2.9, .1, gra=gra3)
part_a(4.1, .1, gra=grgra)

b_part(0.1, .1, gra=gra4)
b_part(1.356, .1, gra=gra5)
b_part(2.9, .1, gra=gra6)
b_part(4.1, .1, gra=gray)

part_c(.1, gra=gra7)

plt.show()
