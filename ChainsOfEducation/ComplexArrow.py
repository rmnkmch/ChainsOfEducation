import manim
import SimpleCurve
import Tip


class ComplexArrow(manim.VMobject):
    """ComplexArrow"""

    def __init__(self, points, end_tip = None, **kwargs):
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

        if end_tip is None: end_tip = Tip.TriangleTip()
        self.end_tip = end_tip
        diff = self.point_from_proportion(0.001) - points[0]
        self.end_tip.set_angle(self.end_tip.get_angle_by_dx_dy(diff[0], diff[1]))
        self.end_tip.move_to(points[0] + self.end_tip.get_shift())
        self.end_tip.update_prev_pos()
        self.end_tip.set_pos_func(self.get_end)

    def get_next_curves(self, n: int):
        if self.is_created():
            curve = self.get_n_curves(self.get_num_curves() - 1, 1)
            self.curves.append(curve)
            self.end_tip.set_pos_func(curve.get_end)
            return curve
        else:
            if self.num_created_curves + n > self.get_num_curves():
                n = self.get_num_curves() - self.num_created_curves
            curve = self.get_n_curves(self.num_created_curves, n)
            self.curves.append(curve)
            self.num_created_curves += n
            self.end_tip.set_pos_func(curve.get_end)
            return curve

    def get_n_curves(self, start: int, n: int):
        points: list = self.get_nth_curve_points(start).tolist()
        for i in range(start + 1, start + n):
            points += self.get_nth_curve_points(i).tolist()
        return SimpleCurve.SimpleCurve(points)

    def is_created(self):
        return self.num_created_curves >= self.get_num_curves()

    def pop_first_and_last_points(self, first, last):
        return self.get_all_points()[
            first * self.n_points_per_curve
            : self.get_num_points() - last * self.n_points_per_curve]
