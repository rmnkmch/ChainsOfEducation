import manim


class Tip(manim.VMobject):
    """Tip"""

    def __init__(self, **kwargs):
        super().__init__(
            stroke_color = "#FFFFFF",
            stroke_opacity = 1.0,
            stroke_width = 3,
            background_stroke_color = "#000000",
            background_stroke_opacity = 1.0,
            background_stroke_width = 0,
            **kwargs)

        self.angle: float = 0.0
        self.prev_angle: float = manim.PI * 0.5
        self.prev_pos = self.get_center()
        self.pos_func = None
        self.add_updater(Tip.update_pos)
        self.add_updater(Tip.update_angle)
        #self.add_updater(Tip.update_scale)

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
            angle_difference = self.angle - self.prev_angle
            self.prev_pos = self.get_center() - shift
            self.prev_angle = self.angle
            self.rotate(angle_difference)

    def update_pos(self):
        if self.pos_func is not None:
            self.move_to(self.pos_func() + self.get_shift())

    def update_scale(self):
        self.scale(1.02)
        if self.width > 0.5:
            self.remove_updater(Tip.update_scale)

    def get_shift(self):
        u_min = 1.0
        r_min = 1.0
        #if manim.PI < self.angle <= 2.0 * manim.PI: u_min = 1.0
        #if 0.5 * manim.PI < self.angle < 1.5 * manim.PI: r_min = 1.0
        return (manim.RIGHT * self.width * 0.5 * r_min
                + manim.UP * self.width * 0.5 * u_min)

    def set_pos_func(self, pos_func):
        self.pos_func = pos_func

    def clear_pos_func(self):
        self.pos_func = None


class TriangleTip(Tip, manim.Triangle):
    """TriangleTip"""

    def __init__(
        self,
        fill_opacity = 0.0,
        stroke_width = 3,
        length = 1.0,
        width = 0.2,
        start_angle = 0.0,
        **kwargs):
        manim.Triangle.__init__(
            self,
            fill_opacity = fill_opacity,
            stroke_width = stroke_width,
            start_angle = start_angle,
            **kwargs)
        Tip.__init__(self, **kwargs)

        self.width = width
        self.stretch_to_fit_width(length)
        self.stretch_to_fit_height(width)

class RectangleTip(Tip, manim.Rectangle):
    """RectangleTip"""

    def __init__(
        self,
        fill_opacity = 0.0,
        stroke_width = 3,
        length = 0.2,
        width = 1.2,
        **kwargs):
        manim.Rectangle.__init__(self, **kwargs)
        Tip.__init__(self, **kwargs)

        self.width = width
        self.stretch_to_fit_width(length)
        self.stretch_to_fit_height(width)
