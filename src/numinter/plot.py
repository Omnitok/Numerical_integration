import matplotlib.pyplot as plt

def test():
    from random import randint
###### generate test data
    x = []
    y = []
    z = []
    t  = 20
    for i in range(100):
        x.append(randint(1, 100))
        y.append(randint(1, 100))
        z.append(randint(1, 100))
    return x, y, z, t
    
def plot_data(input_data):
    """
    Defines the plot for 2d and 3d data
    """
    if len(input_data) == 3: # 2D matrix, x, y, and t 
        x, y, t = (input_data[i]["solution"] for i in ("x", "y", "t"))
        plt.scatter(x, y, t)
        plt.show()
        plt.savefig("test2d.png")

    else: # 3D matrix, x, y, z and t
        fig = plt.figure()
        ax = fig.add_subplot(projection="3d")
        x, y, z, t = (input_data[i]["solution"] for i in ("x", "y", "z", "t"))
        ax.scatter(x, y, z, c=t)
        plt.show()
        plt.savefig("test3d.png")

def plot_csv_data(data):
    """
    Create a 2d or 3d plot from previous calculations
    """
    if len(data) == 3: # 2D matrix, x, y, and t 
        x, y, t = (data[i]["solution"] for i in ("x", "y", "t"))
        plt.scatter(x, y, t)
        plt.show()
        plt.savefig("test2d.png")

    else: # 3D matrix, x, y, z and t
        fig = plt.figure()
        ax = fig.add_subplot(projection="3d")
        x, y, z, t = (data[i]["solution"] for i in ("x", "y", "z", "t"))
        ax.scatter(x, y, z, c=t)
        plt.show()
        plt.savefig("test3d.png")
############ #TEST the plots
#plot_data(test())
