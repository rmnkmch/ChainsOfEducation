import math
import manim


class TextBlock(manim.Text):
    """TextBlock"""

    def __init__(
        self,
        text: str,
        fill_opacity: float  = 0.5,
        stroke_width: float = 0.0,
        color: str = "#FFFFFF",
        font_size: float = 48.0,
        line_spacing: float = - 1.0,
        font: str = "",
        slant: str = "NORMAL",
        weight: str = "NORMAL",
        t2c: dict[str, str] = None,
        t2f: dict[str, str] = None,
        t2g: dict[str, tuple] = None,
        t2s: dict[str, str] = None,
        t2w: dict[str, str] = None,
        gradient: tuple = None,
        tab_width: int = 4,
        warn_missing_font: bool = True,
        height: float = None,
        width: float = None,
        should_center: bool = True,
        disable_ligatures: bool = False,
        **kwargs) -> None:
        super().__init__(
            text, fill_opacity, stroke_width, color,
            font_size, line_spacing, font, slant, weight,
            t2c, t2f, t2g, t2s, t2w, gradient, tab_width,
            warn_missing_font, height, width,
            should_center, disable_ligatures, **kwargs)

        self.add_background_rectangle(color, 0.05)
        self.init_width = self.background_rectangle.width
        self.init_height = self.background_rectangle.height

    def perimeter(self):
        return 2.0 * (self.init_width + self.init_height)

    def vector_len(self, vector):
        from math import sqrt
        return sqrt(vector[0] * vector[0] + vector[1] * vector[1])

    def get_arrow_point(self, direction = 0.0):
        return self.background_rectangle.point_from_proportion(direction)

    def get_arrright(self):
        return self.get_arrow_point(
            (2.0 * self.init_width + 1.5 * self.init_height) / self.perimeter())

    def get_arrup(self):
        return self.get_arrow_point(0.5 * self.init_width / self.perimeter())

    def get_arrleft(self):
        return self.get_arrow_point(
            (self.init_width + 0.5 * self.init_height) / self.perimeter())

    def get_arrdown(self):
        return self.get_arrow_point(
            (1.5 * self.init_width + self.init_height) / self.perimeter())

    def get_arrur(self):
        return self.get_arrow_point(0.0)

    def get_arrul(self):
        return self.get_arrow_point(self.init_width / self.perimeter())

    def get_arrdl(self):
        return self.get_arrow_point(0.5)

    def get_arrdr(self):
        return self.get_arrow_point(
            (2.0 * self.init_width + self.init_height) / self.perimeter())

    def get_buff_arrow_point(self, direction, buff = 0.5):
        vect = direction - self.get_center()
        return vect / self.vector_len(vect) * buff + direction

    def get_buff_arrright(self, buff = 0.5):
        return self.get_buff_arrow_point(self.get_arrright(), buff)

    def get_buff_arrup(self, buff = 0.5):
        return self.get_buff_arrow_point(self.get_arrup(), buff)

    def get_buff_arrleft(self, buff = 0.5):
        return self.get_buff_arrow_point(self.get_arrleft(), buff)

    def get_buff_arrdown(self, buff = 0.5):
        return self.get_buff_arrow_point(self.get_arrdown(), buff)
