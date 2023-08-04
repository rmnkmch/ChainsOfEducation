import manim


class Tip(manim.VMobject):
    """Base Tip Class"""

    def __init__(self, **kwargs):
        self.init_length: float = self.height
        self.init_width: float = self.width
        self.shift_x_anchor: float = 0.5
        self.shift_y_anchor: float = 0.5
        self.angle: float = manim.PI * 0.5
        self.prev_angle: float = manim.PI * 0.5
        self.update_prev_pos()
        self.pos_func = None
        self.add_updater(Tip.update_pos)
        self.add_updater(Tip.update_angle)
        #self.add_updater(Tip.update_scale)
        self.add_background_rectangle(opacity = 0.0)

    def get_angle_by_dx_dy(self, dx: float, dy: float):#to static
        from math import atan
        if dx > 0.0:
            if dy > 0.0: return atan(abs(dy / dx))
            elif dy < 0.0: return 2.0 * manim.PI - atan(abs(dy / dx))
            else: return 0.0
        elif dx < 0.0:
            if dy > 0.0: return manim.PI - atan(abs(dy / dx))
            elif dy < 0.0: return manim.PI + atan(abs(dy / dx))
            else: return manim.PI
        else:
            if dy > 0.0: return 0.5 * manim.PI
            elif dy < 0.0: return 1.5 * manim.PI
            else: return 0.0

    def update_angle(self):
        pos_difference = self.get_center() - self.get_shift() - self.prev_pos
        if abs(pos_difference[0]) >= 0.001 and abs(pos_difference[1]) >= 0.001:
            angle = self.get_angle_by_dx_dy(pos_difference[0], pos_difference[1])
            self.update_prev_pos()
            self.set_angle(angle)

    def update_pos(self):
        if self.pos_func is not None:
            self.move_to(self.pos_func() + self.get_shift())

    def update_scale(self):
        self.scale(1.02)
        if self.width > 0.5:
            self.remove_updater(Tip.update_scale)

    def get_shift(self):
        from math import cos, sin
        return (manim.RIGHT * cos(self.angle)
                * self.init_length * self.shift_x_anchor
                + manim.UP * sin(self.angle)
                * self.init_length * self.shift_y_anchor)

    def set_pos_func(self, pos_func):
        self.pos_func = pos_func

    def clear_pos_func(self):
        self.pos_func = None

    def set_angle(self, angle: float):
        self.angle = angle
        angle_difference = self.angle - self.prev_angle
        self.prev_angle = self.angle
        self.rotate(angle_difference)

    def update_prev_pos(self):
        self.prev_pos = self.get_center() - self.get_shift()


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

        self.width = width
        self.stretch_to_fit_height(length)
        self.stretch_to_fit_width(width)
        Tip.__init__(self, **kwargs)


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
        length = 0.5,
        width = 0.5,
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

        self.width = width
        self.stretch_to_fit_height(length)
        self.stretch_to_fit_width(width)
        Tip.__init__(self, **kwargs)


class RhombTip(Tip, manim.Square):
    """RhombTip"""

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
        **kwargs):
        manim.Square.__init__(
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

        self.rotate(manim.PI * 0.25)
        self.width = width
        self.stretch_to_fit_height(length)
        self.stretch_to_fit_width(width)
        Tip.__init__(self, **kwargs)


class EllipseTip(Tip, manim.Ellipse):
    """EllipseTip"""

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

        self.width = width
        self.stretch_to_fit_height(length)
        self.stretch_to_fit_width(width)
        Tip.__init__(self, **kwargs)
