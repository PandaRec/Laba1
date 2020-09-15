from PIL import Image, ImageDraw


def board(num, size):
    new_image = Image.new("RGB", (size * num, size * num), (255, 255, 255))
    draw = ImageDraw.Draw(new_image)
    x1 = 0
    y1 = 0
    x2 = 50
    y2 = 50
    black_fill = draw.fill = (0, 0, 0)
    white_fill = draw.fill = (255, 255, 255)

    for j in range(num):
        for i in range(num):
            draw.rectangle((x1, y1, x2, y2), fill=black_fill)
            x1 += size
            x2 += size
            draw.rectangle((x1, y1, x2, y2), fill=white_fill)
            x1 += size
            x2 += size
        y1 += 50
        y2 += 50
        x1 = 0
        x2 = 50
        black_fill, white_fill = white_fill, black_fill

    new_image.save("res2.png", "PNG")


board(10, 50)
