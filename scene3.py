from manimlib.imports import *
import numpy as np
from utils import *

class SCENE3(Scene):
    def construct(self):
        title1 = TextMobject(
            "Simpson's Paradox"
        ).set_width((FRAME_WIDTH - 2 * LARGE_BUFF) / 1.5)

        title2 = TextMobject(
            "Inspired by 3Blue1Brown"
        ).set_width(5)

        title3 = TextMobject(
            "Made with manim"
        ).set_width(3)

        title4 = TextMobject(
            "Music by Vincent Rubinetti"
        ).set_width(5)

        self.play(FadeIn(title1))
        title1.generate_target()
        title1.target.to_edge(UP * 3)
        self.play(MoveToTarget(title1))

        title2.to_edge(DOWN * 7)
        title3.next_to(title2, DOWN)
        title4.to_edge(DOWN * 3)
        self.play(FadeIn(VGroup(title2, title3, title4)))
        self.wait()

