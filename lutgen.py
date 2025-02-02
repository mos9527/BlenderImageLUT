from PIL import Image
from argparse import ArgumentParser


def generate_neutral_lut(D: int):
    # Create a new RGB image with size (D^2, D)
    lut = Image.new("RGB", (D * D, D))

    # Fill the image with RGB values
    for b in range(D):
        for g in range(D):
            for r in range(D):
                x = r + b * D
                y = g
                lut.putpixel(
                    (x, y), (r * 255 // (D - 1), g * 255 // (D - 1), b * 255 // (D - 1))
                )

    return lut


if __name__ == "__main__":
    parser = ArgumentParser(description="Generate a neutral 2D LUT")
    parser.add_argument(
        "-d", "--dimension", type=int, default=16, help="Dimension (default=16)"
    )
    parser.add_argument(
        "-o", "--output", type=str, default="neutral.png", help="Output filename"
    )
    args = parser.parse_args()

    lut = generate_neutral_lut(args.dimension)
    lut.save(args.output)
    print(f"Saved. D={args.dimension}, filename={args.output}")
