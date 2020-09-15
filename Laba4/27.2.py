from PIL import Image, ImageDraw  # Подключим необходимые библиотеки.

image = Image.open('test.png')  # Открываем изображение.
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
width = image.size[0]  # Определяем ширину.
height = image.size[1]  # Определяем высоту.
pix = image.load()  # Выгружаем значения пикселей.
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
