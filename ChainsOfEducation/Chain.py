import manim
import ComplexArrow
import Tip


class Chain(ComplexArrow.ComplexArrow):
    """Chain"""

    def __init__(self, start, end):
        super().__init__(
            [start, end],
            Tip.EllipseTip(
                fill_opacity = 0.6, length = 0.3, width = 0.3
                ).set_shift_anchors(0.0, 0.0),
            Tip.EllipseTip(
                fill_opacity = 0.6, length = 0.3, width = 0.3
                ).set_shift_anchors(0.0, 0.0))

    def get_creating_anim(self):
        return manim.AnimationGroup(
            manim.Write(self), lag_ratio = 0.75)
