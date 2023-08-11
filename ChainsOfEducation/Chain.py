import manim
import ComplexArrow
import Tip


class Chain(ComplexArrow.ComplexArrow):
    """Chain"""

    def __init__(self, start, end):
        super().__init__(
            [start, end],
            Tip.EllipseTip(
                fill_opacity = 1.0, length = 0.2, width = 0.2
                ).set_shift_anchors(0.0, 0.0),
            Tip.EllipseTip(
                fill_opacity = 1.0, length = 0.2, width = 0.2
                ).set_shift_anchors(0.0, 0.0))

    def prepare_to_create(self):
        self.remove(self.end_tip, self.start_tip)

    def get_creating_anim(self):
        return manim.AnimationGroup(
            manim.FadeIn(self.start_tip),
            manim.Write(self),
            manim.Create(self.end_tip),
            lag_ratio = 0.75)
