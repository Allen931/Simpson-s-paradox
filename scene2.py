from manimlib.imports import *
import numpy as np
from utils import *


class SCENE2(Scene):
    def construct(self):
        title = TextMobject(
            "Simpson's Paradox"
        ).set_width(FRAME_WIDTH - 2 * LARGE_BUFF)
        self.play(ShowIncreasingSubsets(title[0], run_time=1.5))
        self.wait()
        self.play(FadeOutAndShiftDown(title))
        self.wait()
        why = TextMobject("WHY?").scale(3)
        self.play(ShowIncreasingSubsets(why[0], run_time=1.5))
        self.wait()
        self.play(Uncreate(why))
        self.wait()
        axes = Axes(
            center_point=LEFT * 6 + DOWN * 3,
            x_min=-2, x_max=15,
            y_min=-2, y_max=10
        )
        self.play(ShowCreation(axes, run_time=3, lag_ratio=0.1))
        self.wait()
        labels = axes.get_axis_labels("GPA", "Rejected\\\\Rate")
        self.play(Write(labels))
        self.wait()

        coords = return_coords_from_csv("simpson-paradox-data")
        dots = {Dot(np.array([coord[0] / 40 - 6, coord[1] / 60 - 3, 0])): coord[2] for coord in coords}
        self.play(*[LaggedStart(*[GrowFromCenter(dot) for dot in dots.keys()], lag_ratio=0.007)])
        self.wait()
        line_W = Line(start=np.array([-5.3, -1.1, 0]), end=np.array([7, 2, 0])).set_color(BLUE)
        self.play(GrowArrow(line_W))
        self.wait()
        self.play(Indicate(line_W))
        self.wait()
        self.play(FadeOut(line_W))
        self.wait()

        red_dots = [dot[0] for dot in dots.items() if dot[1] == 'a']
        green_dots = [dot[0] for dot in dots.items() if dot[1] == 'b']
        yellow_dots = [dot[0] for dot in dots.items() if dot[1] == 'c']
        purple_dots = [dot[0] for dot in dots.items() if dot[1] == 'd']
        self.play(*[LaggedStart(*[Transform(dot, dot.copy().set_color(RED), run_time=0.3) for dot in red_dots], lag_ratio=0.01)])
        self.play(*[LaggedStart(*[Transform(dot, dot.copy().set_color(GREEN), run_time=0.3) for dot in green_dots], lag_ratio=0.01)])
        self.play(
            *[LaggedStart(*[Transform(dot, dot.copy().set_color(YELLOW), run_time=0.3) for dot in yellow_dots], lag_ratio=0.01)])
        self.play(
            *[LaggedStart(*[Transform(dot, dot.copy().set_color(PURPLE), run_time=0.3) for dot in purple_dots], lag_ratio=0.01)])
        self.wait()

        line_R = Line(start=np.array([-5.5, -0.4, 0]), end=np.array([1, -1.7, 0])).set_color(RED)
        line_G = Line(start=np.array([-4.5, 1.2, 0]), end=np.array([3, -1.55, 0])).set_color(GREEN)
        line_Y = Line(start=np.array([-3, 2.4, 0]), end=np.array([3.5, -0.6, 0])).set_color(YELLOW)
        line_P = Line(start=np.array([-0.5, 2.45, 0]), end=np.array([6.5, 1.6, 0])).set_color(PURPLE)

        self.play(GrowArrow(line_R))
        self.play(GrowArrow(line_G))
        self.play(GrowArrow(line_Y))
        self.play(GrowArrow(line_P))
        self.wait()

        self.play(Indicate(line_R), Indicate(line_G), Indicate(line_Y), Indicate(line_P))
        self.wait()

        self.play(Indicate(line_R), *[Indicate(dot) for dot in red_dots])
        self.play(Indicate(line_G), *[Indicate(dot) for dot in green_dots])
        self.play(Indicate(line_Y), *[Indicate(dot) for dot in yellow_dots])
        self.play(Indicate(line_P), *[Indicate(dot) for dot in purple_dots])


        self.play(GrowArrow(line_W))
        self.wait()
        self.play(Indicate(line_W))
        self.wait()

        labels_2 = axes.get_axis_labels("Dose", "Response")
        self.play(Transform(labels, labels_2))
        self.wait()
        self.play(Indicate(line_R), Indicate(line_G), Indicate(line_Y), Indicate(line_P))
        self.wait()
        self.play(Indicate(line_W))
        self.wait()

        all_lines = [line_R, line_G, line_Y, line_P, line_W]
        self.play(LaggedStart(*[Uncreate(dot) for dot in dots], lag_ratio=0.0035),
                  *[Uncreate(line) for line in all_lines], Uncreate(axes), FadeOut(labels))
        self.wait()
