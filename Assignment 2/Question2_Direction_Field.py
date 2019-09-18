# This is for Direction field of the 2nd question

import matplotlib.pyplot as plt
import numpy as np

[p,q]=np.meshgrid(np.linspace(0.3,0.6,8),np.linspace(1,1.8,8));

q1=(-0.7)*q+(1.6)*p*q;
p1=p*((1.3)*(1-p))-(0.5)*p*q;

plt.quiver(p,q,p1,q1);
plt.show();


