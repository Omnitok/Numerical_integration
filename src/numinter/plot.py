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
    
def plot_data(*input_data)
    """
    Defines the plot for 2d and 3d data
    """
    if len(input_data) == 3: # 2D matrix, x, y, and t 
        plt.scatter(x, y, t)

    else: # 3D matrix, x, y, z and t
        plt.scatter(x, y, z, t)

############ TEST the plots
plot_data(test())
