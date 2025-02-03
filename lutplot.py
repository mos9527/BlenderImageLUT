from PIL import Image
from argparse import ArgumentParser
import matplotlib.pyplot as plt


def __main__():
    parser = ArgumentParser(description="Plot RGB curves of a 3D LUT")
    parser.add_argument("input", type=str, help="Input 3D LUT filename")
    args = parser.parse_args()
    img = Image.open(args.input)
    w, h = img.size
    d = w / h
    w = d
    w, h, d = int(w), int(h), int(d)

    # LUT[r,g,b] = LUT_2D[r + b * W, g]
    def plot_curve(r, g, b):
        # fix g,b plot r response
        r_curve = [img.getpixel((i + b * w, g))[0] for i in range(w)]
        # fix r,b plot g response
        g_curve = [img.getpixel((r + b * w, i))[1] for i in range(h)]
        # fix r,g plot b response
        b_curve = [img.getpixel((r + i * w, g))[2] for i in range(d)]
        plt.plot(r_curve, label=f"r g={g} b={b}", color="red")
        plt.plot(g_curve, label=f"g r={r} b={b}", color="green")
        plt.plot(b_curve, label=f"b r={r} g={g}", color="blue")
        plt.legend()

    for b in range(d):
        for g in range(h):
            for r in range(w):
                plot_curve(r, g, b)
            plt.show()


if __name__ == "__main__":
    __main__()
