import random
import itertools
import numpy as np

ikachan = (
    '0000000011100000000',
    '0000000133310000000',
    '0000001333331000000',
    '0000013333333100000',
    '0000133333333310000',
    '0001333333333331000',
    '0013333333333333100',
    '0133333333333333310',
    '0133312221222133310',
    '1333122112112213331',
    '1333122211122213331',
    '1333122112112213331',
    '0113112221222113110',
    '0001311111111131000',
    '0001333333334331000',
    '0000133333333310000',
    '0001433333334341000',
    '0001433343343341000',
    '0000141441441410000',
    '0000110110110110000',
)
ikachan = np.array([[int(_) for _ in line] for line in ikachan], np.uint8)

base_colors = (
    (4, 62, 80), (240, 240, 240),
)

body_colors = (
    ((85, 239, 196), (0, 184, 148)),
    ((129, 236, 236), (0, 206, 201)),
    ((116, 185, 255), (9, 132, 227)),
    ((162, 155, 254), (108, 92, 231)),
    ((255, 234, 167), (253, 203, 110)),
    ((250, 177, 160), (225, 112, 85),),
    ((255, 118, 117), (214, 48, 49)),
    ((253, 121, 168), (232, 67, 147))
)


def draw_ikachan(im, offset, color):
    colors = (None, ) + base_colors + body_colors[color]

    for i, j in np.ndindex(ikachan.shape):
        if ikachan[i, j] == 0:
            continue
        y0 = i * 4 + offset[1] + 10
        y1 = y0 + 4
        x0 = j * 4 + offset[0] + 12
        x1 = x0 + 4
        im[y0:y1, x0:x1] = colors[ikachan[i, j]]


def make_banner():
    rows = range(0, 500, 100)
    cols = range(0, 1500, 100)
    offsets = itertools.product(cols, rows)

    color_indices = tuple(range(len(body_colors))) * 10
    color_indices = random.sample(color_indices, k=75)

    im = np.full((500, 1500, 3), 255, np.uint8)

    for args in zip(offsets, color_indices):
        draw_ikachan(im, *args)

    return im


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    plt.imshow(make_banner())
    plt.show()
