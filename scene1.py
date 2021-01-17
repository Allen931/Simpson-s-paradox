from manimlib.imports import *
import numpy as np
from utils import *


class SCENE1(Scene):
    def construct(self):
        # write title
        title1 = TextMobject(
            "Introduction to",
        )
        title2 = TextMobject(
            "Simpson's Paradox", tex_to_color_map={"Simpson's Paradox": YELLOW}
        )
        title3 = TextMobject(
            "Hanpei, FANG 1W19CF07"
        ).to_edge(DOWN * 2)
        group = VGroup(title1, title2)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(title1))
        self.play(Write(title2))
        self.play(FadeIn(title3))
        self.wait()

        # Move title to the up-left corner
        title2.generate_target()
        title2.target.scale(1 / 2).to_corner(UP + LEFT)
        self.play(MoveToTarget(title2),
                  LaggedStart(*map(FadeOutAndShiftDown, title1)),
                  FadeOut(title3))
        self.wait()

        # new title
        acceptance_rate = TextMobject(
            "Acceptance Rate", tex_to_color_map={"Acceptance Rate": YELLOW}
        )

        acceptance_rate.scale(1.4).to_corner(UP + LEFT)
        self.play(ReplacementTransform(title2, acceptance_rate))
        self.wait()


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

        self.play(horizontal_line_animation, vertical_line_animation, diag_line_animation)
        self.wait()

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
        table_text_animation = [LaggedStart(*[Write(text[0]) for text in table_text])]
        self.play(*table_text_animation)
        self.wait()

        self.play(Indicate(table_text12))
        self.wait()
        self.play(Indicate(table_text13))
        self.wait()
        self.play(Indicate(table_text9), Indicate(table_text11))
        self.wait()
        self.play(Indicate(table_text8), Indicate(table_text10))
        self.wait()

        self.play(Indicate(table_text5))
        self.play(Indicate(table_text6))

        self.play(Indicate(table_text9), Indicate(table_text5))
        self.wait()
        self.play(Indicate(table_text10), Indicate(table_text6))
        self.wait()

        # elements = VGroup(*horizontal_line_group, *vertical_line_group, diag_line, *table_text, acceptance_rate)
        # elements_2 = VGroup(*horizontal_line_group, *vertical_line_group, diag_line, *table_text, acceptance_rate)
        #
        # title = TextMobject(
        #     "Simpson's Paradox"
        # ).set_width(FRAME_WIDTH - 2 * LARGE_BUFF)
        # self.play(ReplacementTransform(elements, title))
        # self.wait()
        # self.play(FadeOutAndShiftDown(title))
        # self.wait()
        # why = TextMobject("WHY?").scale(3)
        # self.play(ShowIncreasingSubsets(why[0], run_time=1.5))
        # self.wait()
        # self.play(ReplacementTransform(why, elements_2))
        # self.wait()

        # modify the table
        for line in horizontal_line_group:
            line.generate_target()
            line.target.scale(0.6)

        for line in vertical_line_group:
            line.generate_target()
            line.target.scale(6 / 4.3)

        horizontal_line1.target.move_to(np.array([-3.5, 2.5, 0]))
        horizontal_line2.target.move_to(np.array([-3.5, 1.0, 0]))
        horizontal_line3.target.move_to(np.array([-3.5, -0.5, 0]))
        horizontal_line4.target.move_to(np.array([-3.5, -2.0, 0]))
        horizontal_line5.target.move_to(np.array([-3.5, -3.5, 0]))

        vertical_line1.target.move_to(np.array([-6.5, -0.5, 0]))
        vertical_line2.target.move_to(np.array([-4.5, -0.5, 0]))
        vertical_line3.target.move_to(np.array([-2.5, -0.5, 0]))
        vertical_line4.target.move_to(np.array([-0.5, -0.5, 0]))

        new_diag_line = Line(start=np.array([-6.5, 2.5, 0]), end=np.array([-4.5, 1.0, 0]))

        new_table_text3 = generate_table_text("Male", [-3.5, 1.75, 0], RED, 2, 0.6)
        new_table_text4 = generate_table_text("Female", [-1.5, 1.75, 0], BLUE, 3, 0.6)
        new_table_text5 = generate_table_text("Business", [-5.5, 0.25, 0], WHITE, 3, 0.60)
        new_table_text6 = generate_table_text("Law", [-5.5, -1.25, 0], WHITE, 2, 0.55)
        new_table_text7 = TextMobject("Total").set_width(2).move_to(np.array([-5.5, -2.75, 0])).scale(0.60)
        new_table_text8 = generate_table_text("15.1\%\\\\(16/106)", [-3.5, 0.25, 0], WHITE, 2, 0.75)
        new_table_text9 = generate_table_text("33.6\%\\\\(51/152)", [-1.5, 0.25, 0], BLUE, 2, 0.75)
        new_table_text10 = generate_table_text("84.1\%\\\\(253/301)", [-3.5, -1.25, 0], WHITE, 2, 0.80)
        new_table_text11 = generate_table_text("91.1\%\\\\(102/112)", [-1.5, -1.25, 0], BLUE, 2, 0.80)
        new_table_text12 = generate_table_text("66.1\%\\\\(269/407)", [-3.5, -2.75, 0], RED, 2, 0.80)
        new_table_text13 = generate_table_text("58.0\%\\\\(153/264)", [-1.5, -2.75, 0], WHITE, 2, 0.80)

        table_text.remove(table_text1)
        table_text.remove(table_text2)
        new_table_text = [new_table_text3, new_table_text4,new_table_text5, new_table_text6,
                          new_table_text7, new_table_text8, new_table_text9, new_table_text10,
                          new_table_text11, new_table_text12, new_table_text13]

        table_text_change_animation = [ReplacementTransform(k, v) for k, v in
                                       dict(zip(table_text, new_table_text)).items()]

        self.play(*[MoveToTarget(line) for line in horizontal_line_group],
                  *[MoveToTarget(line) for line in vertical_line_group],
                  ReplacementTransform(diag_line, new_diag_line), *table_text_change_animation,
                  FadeOut(table_text1), FadeOut(table_text2))

        axes = Axes(
            x_min = 0, x_max = 6,
            y_min = 0, y_max = 6,
            center_point = np.array([0.5, -3, 0]),
            number_line_config = {
                "unit_size": 1,
            },
        )
        self.play(FadeInFromLarge(axes, 0.3))
        self.wait()
        labels = axes.get_axis_labels("Applied", "Accepted")
        self.play(Write(labels))
        self.wait()

        # create vectors (male)
        vector_M1 = create_vector(np.array([1.06, 0.16, 0]), np.array([0.5, -3, 0]), RED)
        draw_vector(self, new_table_text8, vector_M1)
        vector_M2 = create_vector([3.01, 2.53, 0], vector_M1.get_end(), RED)
        draw_vector(self, new_table_text10, vector_M2)
        vector_MT = create_vector([4.07, 2.69, 0], np.array([0.5, -3, 0]), RED)
        draw_vector(self, new_table_text12, vector_MT)

        # create vectors (female)
        vector_F1 = create_vector(np.array([1.52, 0.51, 0]), np.array([0.5, -3, 0]), BLUE)
        draw_vector(self, new_table_text9, vector_F1)
        vector_F2 = create_vector([1.12, 1.02, 0], vector_F1.get_end(), BLUE)
        draw_vector(self, new_table_text11, vector_F2)
        vector_FT = create_vector([2.64, 1.53, 0], np.array([0.5, -3, 0]), BLUE)
        draw_vector(self, new_table_text13, vector_FT)

        vectors = [vector_M1, vector_M2, vector_MT, vector_F1, vector_F2, vector_FT]

        self.play(Indicate(vector_MT), Indicate(new_table_text12))
        self.wait()
        self.play(Indicate(vector_FT), Indicate(new_table_text13))
        self.wait()

        # change the data
        changed_table_text1 = generate_table_text("91.1\%\\\\(306/336)", [-1.5, -1.25, 0], BLUE, 2, 0.80)
        changed_table_text2 = generate_table_text("73.2\%\\\\(357/488)", [-1.5, -2.75, 0], BLUE, 2, 0.80)
        changed_table_text3 = generate_table_text("66.1\%\\\\(269/407)", [-3.5, -2.75, 0], WHITE, 2, 0.80)

        self.play(ReplacementTransform(new_table_text11, changed_table_text1),
                  ReplacementTransform(new_table_text13, changed_table_text2),
                  ReplacementTransform(new_table_text12, changed_table_text3),
                  Transform(vector_F2, create_vector([3.36, 3.06, 0],vector_F1.get_end(), BLUE)),
                  Transform(vector_FT, create_vector([4.88, 3.57, 0], np.array([0.5, -3, 0]), BLUE)))

        self.wait()

        # show the new total acceptance rate (slope)
        self.play(Indicate(vector_FT), ShowCreationThenDestructionAround(changed_table_text2))
        self.wait()
        self.play(Indicate(vector_MT), ShowCreationThenDestructionAround(changed_table_text3))
        self.wait()

        all_elements = [changed_table_text1, changed_table_text2, changed_table_text3, *new_table_text, *vectors,
                        *horizontal_line_group, *vertical_line_group, new_diag_line, axes,
                        labels, acceptance_rate]
        exit_animation = [LaggedStart(*map(FadeOutAndShiftDown, element)) for element in all_elements]
        self.play(*exit_animation)
        self.wait()
