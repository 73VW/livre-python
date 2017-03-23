import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, np.pi * 2, 0.1)
y = np.cos(x)
plt.plot(x, y, "ro")  # ro pour rond... ou round... qu'importe!

plt.show()