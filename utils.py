from manimlib.imports import *
import numpy as np


def generate_table_text(text, position, color, width, scale):
    return TextMobject(
        text, tex_to_color_map={text: color}
    ).set_width(width).move_to(np.array(position)).scale(scale)


def create_vector(direction, shift_to, color):
    return Vector(direction=direction).set_color(color).shift(shift_to)


def draw_vector(scene, data, vector):
    scene.play(GrowArrow(vector), ShowCreationThenDestructionAround(data))


def return_coords_from_csv(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            x, y, z = row
            coord = [float(x), float(y), z]
            coords.append(coord)
    csvFile.close()
    return coords
