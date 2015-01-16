import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    mat = np.load("fractal.npy")
    plt.imshow(mat)
    plt.show()
