import manim
import enum


class Directions(enum.Enum):
    UP = "UP",
    DOWN = "DOWN",
    RIGHT = "RIGHT",
    LEFT = "LEFT",
    IN = "IN",
    OUT = "OUT",
    UL = "UL",
    UR = "UR",
    DL = "DL",
    DR = "DR",


class TextBlock(manim.Text):
    """TextBlock"""

    def __init__(
        self,
        text: str,
        fill_opacity: float  = 0.5,
        stroke_width: float = 0.0,
        color: str = "#FFFFFF",
        font_size: float = 30.0,
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

    def pp2direction(self):
        pass

    def direction2pp(self, direction: Directions):
        match direction:
            case Directions.UP:
                return 0.5 * self.init_width / self.perimeter()
            case Directions.DOWN:
                return ((1.5 * self.init_width + self.init_height)
                        / self.perimeter())
            case Directions.RIGHT:
                return ((2.0 * self.init_width + 1.5 * self.init_height)
                        / self.perimeter())
            case Directions.LEFT:
                return (self.init_width + 0.5 * self.init_height) / self.perimeter()
            case Directions.UL:
                return self.init_width / self.perimeter()
            case Directions.UR:
                return 0.0
            case Directions.DL:
                return 0.5
            case Directions.DR:
                return (2.0 * self.init_width + self.init_height) / self.perimeter()
            case _:
                return 0.0

    def get_arrow_point(self, pp = 0.0):
        return self.background_rectangle.point_from_proportion(pp)

    def get_arrright(self):
        return self.get_arrow_point(self.direction2pp(Directions.RIGHT))

    def get_arrup(self):
        return self.get_arrow_point(self.direction2pp(Directions.UP))

    def get_arrleft(self):
        return self.get_arrow_point(self.direction2pp(Directions.LEFT))

    def get_arrdown(self):
        return self.get_arrow_point(self.direction2pp(Directions.DOWN))

    def get_arrur(self):
        return self.get_arrow_point(self.direction2pp(Directions.UR))

    def get_arrul(self):
        return self.get_arrow_point(self.direction2pp(Directions.UL))

    def get_arrdl(self):
        return self.get_arrow_point(self.direction2pp(Directions.DL))

    def get_arrdr(self):
        return self.get_arrow_point(self.direction2pp(Directions.DR))

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

    def get_smooth_arrow_side(
        self, direction, buff = 1.0, outer_buff_num = 1, inner_buff_num = 20):
        from math import floor
        opposite = direction + 0.5
        if opposite > 1.0: opposite -= 1.0
        points: list = []
        dops = (self.vector_len(
            self.get_arrow_point(direction) - self.get_center()) / buff)
        dops = min(floor(dops), inner_buff_num)
        for i in range(outer_buff_num, -dops, -1):
            points.append(self.get_buff_arrow_point(
                self.get_arrow_point(direction), buff * i))
        points.append(self.get_center())
        for i in range(-dops + 1, outer_buff_num + 1, 1):
            points.append(self.get_buff_arrow_point(
                self.get_arrow_point(opposite), buff * i))
        return points

    def get_smooth_arrright(self, buff = 1.0):
        return self.get_smooth_arrow_side(
            self.direction2pp(Directions.RIGHT), buff)

    def get_smooth_arrup(self, buff = 1.0):
        return self.get_smooth_arrow_side(
            self.direction2pp(Directions.UP), buff)

    def get_smooth_arrleft(self, buff = 1.0):
        return self.get_smooth_arrow_side(
            self.direction2pp(Directions.LEFT), buff)

    def get_smooth_arrdown(self, buff = 1.0):
        return self.get_smooth_arrow_side(
            self.direction2pp(Directions.DOWN), buff)

    def get_smooth_arrur(self, buff = 1.0):
        return self.get_smooth_arrow_side(
            self.direction2pp(Directions.UR), buff)

    def get_smooth_arrul(self, buff = 1.0):
        return self.get_smooth_arrow_side(
            self.direction2pp(Directions.UL), buff)

    def get_smooth_arrdl(self, buff = 1.0):
        return self.get_smooth_arrow_side(
            self.direction2pp(Directions.DL), buff)

    def get_smooth_arrdr(self, buff = 1.0):
        return self.get_smooth_arrow_side(
            self.direction2pp(Directions.DR), buff)
