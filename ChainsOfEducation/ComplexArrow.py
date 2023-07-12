import manim
import SimpleCurve


class ComplexArrow(manim.VMobject):
    """ComplexArrow"""

    def __init__(self, points, **kwargs):
        super().__init__(
            stroke_color = "#FFFFFF",
            stroke_opacity = 1.0,
            stroke_width = 4,
            background_stroke_color = "#000000",
            background_stroke_opacity = 1.0,
            background_stroke_width = 0,
            **kwargs)

        self.set_points_smoothly(points)

        self.num_created_curves: int = 0

        self.end_tip = manim.ArrowTriangleFilledTip().rotate(manim.PI)

    def get_next_curve(self):
        curve = None
        if self.is_created():
            curve = SimpleCurve.SimpleCurve(
                self.get_nth_curve_points(self.num_created_curves))
        else:
            curve = SimpleCurve.SimpleCurve(
                self.get_nth_curve_points(self.num_created_curves))
            self.num_created_curves += 1
        return curve

    def is_created(self):
        return self.num_created_curves >= self.get_num_curves()
