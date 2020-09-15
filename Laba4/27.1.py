from PIL import Image


def make_preview(size, n_colors):
    image = Image.open('nastol.com.ua-225408.jpg')
    image = image.resize(size)
    image.show()
    image = image.quantize(n_colors)
    image.save('res3.bmp')


make_preview((400, 200), 64)
