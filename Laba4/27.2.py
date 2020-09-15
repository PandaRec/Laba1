from PIL import Image, ImageDraw

image = Image.open('test.png')
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()
depth = int(input('depth:'))


def image_filter(pixels, i=0, j=0):
    """Сепия с пользовательской глубиной"""
    for i in range(width):
        for j in range(height):
            a = pixels[i, j][0]
            b = pixels[i, j][1]
            c = pixels[i, j][2]
            S = (a + b + c) // 3
            a = S + depth * 2
            b = S + depth
            c = S
            if (a > 255):
                a = 255
            if (b > 255):
                b = 255
            if (c > 255):
                c = 255
            draw.point((i, j), (a, b, c))
    image.save("ans.jpg", "JPEG")


image_filter(pix)
