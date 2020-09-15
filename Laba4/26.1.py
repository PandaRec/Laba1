from PIL import Image, ImageDraw


def gradient(color):
    new_image = Image.new("RGB", (512, 200), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    n = 0
    if color.lower().__eq__('r'):
        for i in range(0, 512, 2):
            draw.line((i, 0, i, 200), fill=(n, 0, 0), width=1)
            draw.line((i + 1, 0, i + 1, 200), fill=(n, 0, 0), width=1)
            n += 1
        n = 0

    elif color.lower().__eq__('g'):
        for i in range(0, 512, 2):
            draw.line((i, 0, i, 200), fill=(0, n, 0), width=1)
            draw.line((i + 1, 0, i + 1, 200), fill=(0, n, 0), width=1)
            n += 1
        n = 0
    else:
        for i in range(0, 512, 2):
            draw.line((i, 0, i, 200), fill=(0, 0, n), width=1)
            draw.line((i + 1, 0, i + 1, 200), fill=(0, 0, n), width=1)
            n += 1
        n = 0

    new_image.save("res.png", "PNG")


gradient('g')
