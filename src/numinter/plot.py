import matplotlib.pyplot as plt
def test():
    from random import randint
    x = []
    y = []
    z = []
    t  = 20
    for i in range(100):
        x.append(randint(1, 100))
        y.append(randint(1, 100))
        z.append(randint(1, 100))
    return x, y, t, z

def plot_data(x, y, t, z=None):
    
    frames = []
    
    if z is None:
        from io import BytesIO
        import imageio.v2 as imageio
        for i in range(1, len(x) + 1):
            fig, ax = plt.subplots()
            ax.plot(x[:i], y[:i], marker='o', linestyle='-')
            ax.set_xlim(min(x), max(x))
            ax.set_ylim(min(y), max(y))
            ax.set_title(f"Step {i}")

            # use BytesIO object
            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            frames.append(imageio.imread(buf))
            buf.close()
            plt.close(fig)
        
        # save the image as a gif
        imageio.mimsave("test.gif", frames, duration=1, loop=0)

    else:
        from io import BytesIO
        import imageio.v2 as imageio
        for i in range(len(x)):
            fig = plt.figure()
            ax = fig.add_subplot(111, projection="3d")
            ax.scatter(x[:i], y[:i], z[:i])
            ax.set_xlim(min(x), max(x))
            ax.set_ylim(min(y), max(y))
            ax.set_zlim(min(z), max(z))
            ax.set_title(f"Step {i}")

            # save
            buf = BytesIO()
            plt.savefig(buf, format="png")
            buf.seek(0)
            frames.append(imageio.imread(buf))
            buf.close()
            plt.close(fig)
        imageio.mimsave("test3d.gif", frames, duration=1, loop=0)

############ TEST the plots
#plot_data(*test())
