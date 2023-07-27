import manim


class Tip(manim.VMobject):
    """Tip"""

    def __init__(self, **kwargs):
        self.init_length: float = 0.0
        self.init_width: float = 0.0
        self.angle: float = manim.PI * 0.5
        self.prev_angle: float = manim.PI * 0.5
        self.prev_pos = self.get_center()
        self.pos_func = None
        self.add_updater(Tip.update_pos)
        self.add_updater(Tip.update_angle)
        self.add_updater(Tip.update_scale)

    def update_angle(self):
        shift = self.get_shift()
        pos_difference = self.get_center() - shift - self.prev_pos
        if abs(pos_difference[0]) >= 0.001 and abs(pos_difference[1]) >= 0.001:
            from math import atan
            if pos_difference[0] > 0.0 and pos_difference[1] > 0.0:
                self.angle = atan(pos_difference[1] / pos_difference[0])
            elif pos_difference[0] > 0.0 and pos_difference[1] < 0.0:
                self.angle = (2.0 * manim.PI
                         - atan(abs(pos_difference[1] / pos_difference[0])))
            elif pos_difference[0] < 0.0 and pos_difference[1] > 0.0:
                self.angle = (
                    manim.PI - atan(abs(pos_difference[1] / pos_difference[0])))
            elif pos_difference[0] < 0.0 and pos_difference[1] < 0.0:
                self.angle = (
                    manim.PI + atan(abs(pos_difference[1] / pos_difference[0])))
            self.prev_pos = self.get_center() - shift
            self.set_angle(self.angle)

    def update_pos(self):
        if self.pos_func is not None:
            self.move_to(self.pos_func() + self.get_shift())

    def update_scale(self):
        self.scale(1.02)
        if self.width > 0.5:
            self.remove_updater(Tip.update_scale)

    def get_shift(self):
        from math import cos, sin
        return (manim.RIGHT * self.init_length * cos(self.angle) * 0.5
                + manim.UP * self.init_length * sin(self.angle) * 0.5)

    def set_pos_func(self, pos_func):
        self.pos_func = pos_func

    def clear_pos_func(self):
        self.pos_func = None

    def set_angle(self, angle: float):
        self.angle = angle
        angle_difference = self.angle - self.prev_angle
        self.prev_angle = self.angle
        self.rotate(angle_difference)


class TriangleTip(Tip, manim.Triangle):
    """TriangleTip"""

    def __init__(
        self,
        fill_color = "#FFFFFF",
        fill_opacity = 0.0,
        stroke_color = "#FFFFFF",
        stroke_opacity = 1.0,
        stroke_width = 3,
        background_stroke_color = "#000000",
        background_stroke_opacity = 1.0,
        background_stroke_width = 0,
        sheen_factor = 0.0,
        joint_type = None,
        sheen_direction = manim.UL,
        close_new_points = False,
        pre_function_handle_to_anchor_scale_factor = 0.01,
        make_smooth_after_applying_functions = False,
        background_image = None,
        shade_in_3d = False,
        tolerance_for_point_equality = 1e-6,
        n_points_per_cubic_curve = 4,
        length = 0.5,
        width = 0.5,
        start_angle = manim.PI * 0.5,
        **kwargs):
        manim.Triangle.__init__(
            self,
            fill_color = fill_color,
            fill_opacity = fill_opacity,
            stroke_color = stroke_color,
            stroke_opacity = stroke_opacity,
            stroke_width = stroke_width,
            background_stroke_color = background_stroke_color,
            background_stroke_opacity = background_stroke_opacity,
            background_stroke_width = background_stroke_width,
            sheen_factor = sheen_factor,
            joint_type = joint_type,
            sheen_direction = sheen_direction,
            close_new_points = close_new_points,
            pre_function_handle_to_anchor_scale_factor =
            pre_function_handle_to_anchor_scale_factor,
            make_smooth_after_applying_functions =
            make_smooth_after_applying_functions,
            background_image = background_image,
            shade_in_3d = shade_in_3d,
            tolerance_for_point_equality = tolerance_for_point_equality,
            n_points_per_cubic_curve = n_points_per_cubic_curve,
            start_angle = start_angle,
            **kwargs)
        Tip.__init__(self, **kwargs)

        self.width = width
        self.stretch_to_fit_height(length)
        self.stretch_to_fit_width(width)
        self.init_length = self.height
        self.init_width = self.width


class RectangleTip(Tip, manim.Rectangle):
    """RectangleTip"""

    def __init__(
        self,
        fill_color = "#FFFFFF",
        fill_opacity = 0.0,
        stroke_color = "#FFFFFF",
        stroke_opacity = 1.0,
        stroke_width = 3,
        background_stroke_color = "#000000",
        background_stroke_opacity = 1.0,
        background_stroke_width = 0,
        sheen_factor = 0.0,
        joint_type = None,
        sheen_direction = manim.UL,
        close_new_points = False,
        pre_function_handle_to_anchor_scale_factor = 0.01,
        make_smooth_after_applying_functions = False,
        background_image = None,
        shade_in_3d = False,
        tolerance_for_point_equality = 1e-6,
        n_points_per_cubic_curve = 4,
        length = 2.6,
        width = 0.2,
        **kwargs):
        manim.Rectangle.__init__(
            self,
            fill_color = fill_color,
            fill_opacity = fill_opacity,
            stroke_color = stroke_color,
            stroke_opacity = stroke_opacity,
            stroke_width = stroke_width,
            background_stroke_color = background_stroke_color,
            background_stroke_opacity = background_stroke_opacity,
            background_stroke_width = background_stroke_width,
            sheen_factor = sheen_factor,
            joint_type = joint_type,
            sheen_direction = sheen_direction,
            close_new_points = close_new_points,
            pre_function_handle_to_anchor_scale_factor =
            pre_function_handle_to_anchor_scale_factor,
            make_smooth_after_applying_functions =
            make_smooth_after_applying_functions,
            background_image = background_image,
            shade_in_3d = shade_in_3d,
            tolerance_for_point_equality = tolerance_for_point_equality,
            n_points_per_cubic_curve = n_points_per_cubic_curve,
            **kwargs)
        Tip.__init__(self, **kwargs)

        self.width = width
        self.stretch_to_fit_height(length)
        self.stretch_to_fit_width(width)
        self.init_length = self.height
        self.init_width = self.width


class EllipseTip(Tip, manim.Ellipse):
    """EllipseTip"""

    def __init__(
        self,
        fill_color = "#00EF12",
        fill_opacity = 0.2,
        stroke_color = "#981624",
        stroke_opacity = 1.0,
        stroke_width = 1,
        background_stroke_color = "#000000",
        background_stroke_opacity = 1.0,
        background_stroke_width = 0,
        sheen_factor = 0.0,
        joint_type = None,
        sheen_direction = manim.UL,
        close_new_points = False,
        pre_function_handle_to_anchor_scale_factor = 0.01,
        make_smooth_after_applying_functions = False,
        background_image = None,
        shade_in_3d = False,
        tolerance_for_point_equality = 1e-6,
        n_points_per_cubic_curve = 4,
        length = 1.5,
        width = 0.5,
        **kwargs):
        manim.Ellipse.__init__(
            self,
            fill_color = fill_color,
            fill_opacity = fill_opacity,
            stroke_color = stroke_color,
            stroke_opacity = stroke_opacity,
            stroke_width = stroke_width,
            background_stroke_color = background_stroke_color,
            background_stroke_opacity = background_stroke_opacity,
            background_stroke_width = background_stroke_width,
            sheen_factor = sheen_factor,
            joint_type = joint_type,
            sheen_direction = sheen_direction,
            close_new_points = close_new_points,
            pre_function_handle_to_anchor_scale_factor =
            pre_function_handle_to_anchor_scale_factor,
            make_smooth_after_applying_functions =
            make_smooth_after_applying_functions,
            background_image = background_image,
            shade_in_3d = shade_in_3d,
            tolerance_for_point_equality = tolerance_for_point_equality,
            n_points_per_cubic_curve = n_points_per_cubic_curve,
            **kwargs)
        Tip.__init__(self, **kwargs)

        self.width = width
        self.stretch_to_fit_height(length)
        self.stretch_to_fit_width(width)
        self.init_length = self.height
        self.init_width = self.width
