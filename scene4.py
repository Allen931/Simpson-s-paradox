from manimlib.imports import *
import numpy as np
from utils import *

class SCENE4(Scene):
    def construct(self):
        acceptance_rate = TextMobject(
            "Acceptance Rate", tex_to_color_map={"Acceptance Rate": YELLOW}
        )

        acceptance_rate.scale(1.4).to_corner(UP + LEFT)


        # draw table
        horizontal_line1 = Line(start=np.array([-5, 1.8, 0]), end=np.array([5, 1.8, 0]))
        horizontal_line2 = Line(start=np.array([-5, 0.5, 0]), end=np.array([5, 0.5, 0]))
        horizontal_line3 = Line(start=np.array([-5, -0.5, 0]), end=np.array([5, -0.5, 0]))
        horizontal_line4 = Line(start=np.array([-5, -1.5, 0]), end=np.array([5, -1.5, 0]))
        horizontal_line5 = Line(start=np.array([-5, -2.5, 0]), end=np.array([5, -2.5, 0]))

        vertical_line1 = Line(start=np.array([-5, 1.8, 0]), end=np.array([-5, -2.5, 0]))
        vertical_line2 = Line(start=np.array([-1.5, 1.8, 0]), end=np.array([-1.5, -2.5, 0]))
        vertical_line3 = Line(start=np.array([1.75, 1.8, 0]), end=np.array([1.75, -2.5, 0]))
        vertical_line4 = Line(start=np.array([5, 1.8, 0]), end=np.array([5, -2.5, 0]))

        diag_line = Line(start=np.array([-5, 1.8, 0]), end=np.array([-1.5, 0.5, 0]))

        horizontal_line_group = VGroup(horizontal_line1, horizontal_line2,
                                       horizontal_line3, horizontal_line4, horizontal_line5)
        vertical_line_group = VGroup(vertical_line1, vertical_line2, vertical_line3, vertical_line4)
        horizontal_line_animation = LaggedStart(
            *[Write(line) for line in horizontal_line_group]
        )

        vertical_line_animation = LaggedStart(
            *[Write(line) for line in vertical_line_group]
        )

        diag_line_animation = Write(diag_line)

        # write contents in the table
        table_text1 = TextMobject("Gender").set_width(3).move_to(np.array([-2.5, 1.4, 0])).scale(0.55)
        table_text2 = TextMobject("School").set_width(3).move_to(np.array([-3.8, 0.8, 0])).scale(0.55)
        table_text3 = generate_table_text("Male", [0.125, 1.15, 0], RED, 2, 0.65)
        table_text4 = generate_table_text("Female", [3.375, 1.15, 0], BLUE, 3, 0.65)
        table_text5 = generate_table_text("Business", [-3.25, 0, 0], WHITE, 3, 0.70)
        table_text6 = generate_table_text("Law", [-3.25, -1, 0], WHITE, 2, 0.50)
        table_text7 = generate_table_text("Total", [-3.25, -2, 0], WHITE, 3, 0.45)
        table_text8 = generate_table_text("15.1\% (16/106)", [0.125, 0, 0], WHITE, 4, 0.70)
        table_text9 = generate_table_text("33.6\% (51/152)", [3.375, 0, 0], BLUE, 4, 0.70)
        table_text10 = generate_table_text("84.1\% (253/301)", [0.125, -1, 0], WHITE, 4, 0.75)
        table_text11 = generate_table_text("91.1\% (102/112)", [3.375, -1, 0], BLUE, 4, 0.75)
        table_text12 = generate_table_text("66.1\% (269/407)", [0.125, -2, 0], RED, 4, 0.75)
        table_text13 = generate_table_text("58.0\% (153/264)", [3.375, -2, 0], WHITE, 4, 0.75)

        table_text = [table_text1, table_text2, table_text3, table_text4, table_text5, table_text6, table_text7,
                      table_text8, table_text9, table_text10, table_text11, table_text12, table_text13]
        elements = VGroup(*horizontal_line_group, *vertical_line_group, diag_line, *table_text, acceptance_rate)

        title = TextMobject(
            "Simpson's Paradox"
        ).set_width(FRAME_WIDTH - 2 * LARGE_BUFF)
        self.play(ReplacementTransform(elements, title))
        self.wait()
        self.play(FadeOutAndShiftDown(title))
        self.wait()
        why = TextMobject("WHY?").scale(3)
        self.play(ShowIncreasingSubsets(why[0], run_time=1.5))
        self.wait()