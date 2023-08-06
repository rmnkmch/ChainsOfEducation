import manim
import ComplexArrow
import Tip


class Chain(ComplexArrow.ComplexArrow):
    """Chain"""

    def __init__(self, start, end):
        super().__init__(
            [start, end],
            Tip.EllipseTip().set_shift_anchors(0.0, 0.0),
            Tip.EllipseTip().set_shift_anchors(0.0, 0.0))
