import manim
import SimpleCurve
import Tip


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

        self.curves: list = []
        self.num_created_curves: int = 0

        self.end_tip = Tip.EllipseTip().move_to(points[0])

    def get_next_curves(self, n: int):
        if self.is_created():
            curve = self.get_n_curves(self.get_num_curves() - 1, 1)
            self.curves.append(curve)
            return curve
        else:
            if self.num_created_curves + n > self.get_num_curves():
                n = self.get_num_curves() - self.num_created_curves
            curve = self.get_n_curves(self.num_created_curves, n)
            self.curves.append(curve)
            self.num_created_curves += n
            return curve

    def get_n_curves(self, start: int, n: int):
        points: list = self.get_nth_curve_points(start).tolist()
        for i in range(start + 1, start + n):
            points += self.get_nth_curve_points(i).tolist()
        return SimpleCurve.SimpleCurve(points)

    def is_created(self):
        return self.num_created_curves >= self.get_num_curves()
