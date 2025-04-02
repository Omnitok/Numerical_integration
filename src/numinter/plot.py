# Plot the data (in terminal)
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint
import PIL
import numpy as np

###### generate test data
x = []
y = []
z = []
h = 20
for i in range(100):
    x.append(randint(1, 100))
    y.append(randint(1, 100))
    z.append(randint(1, 100))
print(z)
###############

#fig, ax = plt.subplots()
#scat = ax.scatter([], []) 

#def animate(i):
#    scat.set_offsets(np.c_[x[:i+1], y[:i+1]])
#    return(scat,)


def plot_data(x, y, h, z=None):
#    fig, ax = plt.subplots()
    frames = []
    if z is None:
#        for i in range(h):
 #           plt.scatter(x[i], y[i])
  #          plt.title("Plot for the stuff")
        
#        fig, ax = plt.subplots()

#        def animate(i):
#            scat.set_offsets((x[i], 0))
#            return(scat,)

#        ani = animation.FuncAnimation(
#                fig,
#                animate,
#                repeat=True,
#                frames= 60,
#                interval = 100 
#                )
#        writer = animation.PillowWriter(fps=15,
#                                        metadata=dict(artist="János"),
#                                        bitrate=1800)
#        ani.save("test.gif", writer=writer)

        from io import BytesIO
        import imageio.v2 as imageio
        for i in range(1, len(x) + 1):
            fig, ax = plt.subplots()
            ax.plot(x[:i], y[:i], marker='o', linestyle='-')
            ax.set_xlim(min(x), max(x))
            ax.set_ylim(min(y), max(y))
            ax.set_title(f"Step {i}")

            # Save the figure to a BytesIO object
            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            frames.append(imageio.imread(buf))
            buf.close()
            plt.close(fig)
#            plt.show()

        import imageio.v2 as imageio
        imageio.mimsave("test.gif", frames, duration=1, loop=0)

    else:
        for i in range(1, len(x) + 1):
            
            ax.scatter(x, y, z)

        plt.show()

plot_data(x, y, h, z)

