import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def generate_graph(A1, A2, f1, f2, shift, debug = False):
    
    X = np.linspace(0, 2*np.pi, 300)
    W = A1 * np.sin(X*f1 + 0) 
    Y = A2 * np.sin(X*f2 + shift)

    #print(X)
    #print(W)
    #print(Y)

    fig, ax = plt.subplots()
    ax.plot(W, Y, color = 'green')

    plt.show()
    fig.savefig("./curve")
    
