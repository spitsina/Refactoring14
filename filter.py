from PIL import Image
import numpy as np


def get_mosaice_image(image, mosaice_size=10, gradation=4):
    threshold = 255 // gradation
    processed_image = np.array(image)
    image_length = len(processed_image)
    image_height = len(processed_image[1])
    i = 0
    while i < image_length - 1:
        j = 0
        while j < image_height - 1:
            sector = processed_image[i: i + mosaice_size, j: j + mosaice_size]
            color_sum = np.sum(sector)
            average_color = int(color_sum // (mosaice_size ** 2))
            set_color(int(average_color // threshold) * threshold / 3, processed_image, i, j, mosaice_size)
            j += mosaice_size
        i += mosaice_size

    return Image.fromarray(np.uint8(processed_image))


def set_color(new_color, source_color, i, j, size):
    for sector_i in range(i, i + size):
        for sector_j in range(j, j + size):
            for color_id in range(3):
                source_color[sector_i][sector_j][color_id] = new_color


if __name__ == "__main__":
    img = Image.open(f"{input('Input image name:')}.jpg")
    res = get_mosaice_image(img, gradation= 6)
    img_res = input("Input name result:")
    res.save(f"{ img_res }.jpg")
