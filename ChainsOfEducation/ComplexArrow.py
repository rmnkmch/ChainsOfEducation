import manim
import SimpleCurve
import Tip


class ComplexArrow(manim.VMobject):
    """ComplexArrow"""

    def __init__(self, points, end_tip = None, start_tip = None, **kwargs):
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
        if start_tip is None:
            start_tip = Tip.EllipseTip().set_shift_anchors(-0.5, -0.5)
        self.start_tip = start_tip

        self.make_tips()
        self.add(self.end_tip, self.start_tip)

    @staticmethod
    def vector_len(vector):
        from math import sqrt
        return sqrt(vector[0] * vector[0] + vector[1] * vector[1])

    @staticmethod
    def get_round(
        center = manim.ORIGIN, radius: float = 1.0,
        samples: int = 13, all_samples: int = 24,
        start_angle: float = 0.5 * manim.PI, clockwise = False,
        without_sides = False):
        from math import sin, cos
        points: list = []
        rng = range(0, samples, 1)
        if clockwise: rng = range(0, -samples, -1)
        if without_sides:
            rng = range(1, samples - 1, 1)
            if clockwise: rng = range(-1, -samples + 1, -1)
        for i in rng:
            points.append(
                center
                + manim.RIGHT * radius
                * cos(start_angle + 2.0 * manim.PI * i / all_samples)
                + manim.UP * radius
                * sin(start_angle + 2.0 * manim.PI * i / all_samples))
        return points

    @staticmethod
    def get_line(
        start = manim.ORIGIN, end = manim.RIGHT,
        all_samples: int = 21,
        without_sides = False):
        points: list = []
        rng = range(0, all_samples + 1, 1)
        if without_sides: rng = range(1, all_samples, 1)
        for i in rng:
            points.append(start * (1.0 - i / all_samples) + end * i / all_samples)
        return points

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

    def pop_first_and_last_points(self, first: int, last: int):
        return self.set_points(self.get_all_points()[
            first * self.n_points_per_curve
            : self.get_num_points() - last * self.n_points_per_curve])

    def short(self, length: float, end = True):
        lengths = self.get_curve_functions_with_lengths()
        lts: list = []
        for tup in lengths:
            lts.append(tup)
        i: int = 1
        lng: float = 0.0
        if end:
            while lng < length:
                lng += lts[-i][1]
                i += 1
            if i > 2: self.pop_first_and_last_points(i - 2, 0)
        else:
            i = 0
            while lng < length:
                lng += lts[i][1]
                i += 1
            if i > 1: self.pop_first_and_last_points(0, i - 1)
        return self

    def make_tips(self):
        diff = self.get_end() - self.point_from_proportion(0.999)
        self.end_tip.set_angle(Tip.Tip.get_angle_by_dx_dy(diff[0], diff[1]))
        self.end_tip.move_to(self.get_end() + self.end_tip.get_shift())
        self.end_tip.update_prev_pos()
        diff = self.point_from_proportion(0.001) - self.get_start()
        self.start_tip.set_angle(Tip.Tip.get_angle_by_dx_dy(diff[0], diff[1]))
        self.start_tip.move_to(self.get_start() + self.start_tip.get_shift())
        self.start_tip.update_prev_pos()

    def set_points(self, points):
        super().set_points(points)
        self.make_tips()
        return self

    def start_update_tips(self):
        self.end_tip.set_pos_func(self.get_end)
        self.start_tip.set_pos_func(self.get_start)
        self.end_tip.prepare_to_create()
        self.start_tip.prepare_to_create()
        self.remove(self.end_tip, self.start_tip)

    def stop_update_tips(self):
        self.end_tip.stop_update()
        self.start_tip.stop_update()
        self.add(self.end_tip, self.start_tip)

    def prepare_to_create_1(self):
        diff = self.point_from_proportion(0.001) - self.get_start()
        self.end_tip.set_angle(Tip.Tip.get_angle_by_dx_dy(diff[0], diff[1]))
        self.end_tip.move_to(self.get_start() + self.end_tip.get_shift())
        self.end_tip.update_prev_pos()

    def prepare_to_create_2(self):
        self.start_update_tips()

    def get_creating_anim_1(self):
        return manim.AnimationGroup(
            manim.FadeIn(self.start_tip),
            manim.FadeIn(self.end_tip),
            lag_ratio = 0.5)

    def get_creating_anim_2(self):
        return manim.Create(self)

    def after_create(self):
        self.stop_update_tips()
