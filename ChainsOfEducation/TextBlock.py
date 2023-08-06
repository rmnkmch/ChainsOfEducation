import manim
import ComplexArrow
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
        fill_opacity: float  = 1.0,
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

        self.add_background_rectangle(color, 0.3)
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

    def opposite_direction(self, direction: Directions):
        match direction:
            case Directions.UP: return Directions.DOWN
            case Directions.DOWN: return Directions.UP
            case Directions.RIGHT: return Directions.LEFT
            case Directions.LEFT: return Directions.RIGHT
            case Directions.UL: return Directions.DR
            case Directions.UR: return Directions.DL
            case Directions.DL: return Directions.UR
            case Directions.DR: return Directions.UL
            case _: return  Directions.UP

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
        self, direction, buff = 1.0, outer_buff_num = 1, inner_buff_num = 1):
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

    def get_v_x(self, vector):
        return vector[0]

    def get_v_y(self, vector):
        return vector[1]

    def get_arrow_to_tb(
        self,
        tb_to,
        from_direction: Directions = Directions.UP,
        to_direction: Directions = Directions.UP,
        from_buff: float = 1.0,
        to_buff: float = 1.0,
        from_outer_buff_num: int = 1,
        to_outer_buff_num: int = 1,
        from_inner_buff_num: int = 1,
        to_inner_buff_num: int = 1,
        through_points: list = []):
        if (len(through_points) == 0 and
            (from_direction == Directions.UP and to_direction == Directions.DOWN) or
            (from_direction == Directions.DOWN and to_direction == Directions.UP) or
            (from_direction == Directions.RIGHT and to_direction == Directions.LEFT) or
            (from_direction == Directions.LEFT and to_direction == Directions.RIGHT)):
            radius = (self.get_center() - tb_to.get_center()) * 0.5
            sa = self.get_start_angle(radius, from_direction, to_direction)
            cw = self.get_clockwise(radius, from_direction, to_direction)
            centr = (self.get_mid_point(tb_to, to_direction)
                     + self.get_far_side(tb_to, to_direction))
            radius = self.get_radius(radius, from_direction, to_direction)
            through_points = ComplexArrow.ComplexArrow.get_round(
                centr, radius, 13, 24, sa, cw, True)
        if len(through_points) >= 2:
            from math import floor
            vl = self.vector_len([
                through_points[0][0] - through_points[1][0],
                through_points[0][1] - through_points[1][1]])
            vl = max(vl, 0.01)
            func = self.get_v_x
            if to_direction in [Directions.UP, Directions.DOWN]:
                func = self.get_v_y
            from_len = abs(func(
                self.get_arrow_point(
                    self.direction2pp(self.opposite_direction(to_direction)))
                - self.get_arrow_point(self.direction2pp(to_direction))) * 0.49)
            to_len = abs(func(
                tb_to.get_arrow_point(
                    tb_to.direction2pp(tb_to.opposite_direction(to_direction)))
                - tb_to.get_arrow_point(tb_to.direction2pp(to_direction))) * 0.49)
            vl = min(vl, from_len, to_len)
            from_buff = vl
            to_buff = vl
            fs = self.get_far_side(tb_to, to_direction)
            from_outer_buff_num = floor(abs(func(
                fs - self.get_arrow_point(
                    self.direction2pp(to_direction))) / vl))
            to_outer_buff_num = floor(abs(func(
                fs - tb_to.get_arrow_point(
                    tb_to.direction2pp(to_direction))) / vl))
            from_inner_buff_num = floor(from_len / vl)
            to_inner_buff_num = floor(to_len / vl)
        points: list = self.get_smooth_arrow_side(
            self.direction2pp(from_direction),
            from_buff, from_outer_buff_num, from_inner_buff_num)
        for point in through_points:
            points.append(point)
        for point in tb_to.get_smooth_arrow_side(
            tb_to.direction2pp(to_direction),
            to_buff, to_outer_buff_num, to_inner_buff_num):
            points.append(point)
        ret_CA = ComplexArrow.ComplexArrow(points)
        ret_CA.set_points(ret_CA.pop_first_and_last_points(
            from_inner_buff_num * 2 + from_outer_buff_num,
            to_inner_buff_num * 2 + to_outer_buff_num))
        return (ret_CA, ComplexArrow.ComplexArrow(points))

    def get_start_angle(self, radius, from_direction, to_direction):
        pi = manim.PI
        match from_direction:
            case Directions.UP:
                if to_direction == Directions.DOWN:
                    if radius[0] < 0.0: return pi
                    else: return 0.0
            case Directions.DOWN:
                if to_direction == Directions.UP:
                    if radius[0] < 0.0: return pi
                    else: return 0.0
            case Directions.RIGHT:
                if to_direction == Directions.LEFT:
                    if radius[1] < 0.0: return 1.5 * pi
                    else: return 0.5 * pi
            case Directions.LEFT:
                if to_direction == Directions.RIGHT:
                    if radius[1] < 0.0: return 1.5 * pi
                    else: return 0.5 * pi
        return 0.0

    def get_clockwise(self, radius, from_direction, to_direction):
        match from_direction:
            case Directions.UP:
                if to_direction == Directions.DOWN:
                    if radius[0] > 0.0: return True
                    else: return False
            case Directions.DOWN:
                if to_direction == Directions.UP:
                    if radius[0] < 0.0: return True
                    else: return False
            case Directions.RIGHT:
                if to_direction == Directions.LEFT:
                    if radius[1] < 0.0: return True
                    else: return False
            case Directions.LEFT:
                if to_direction == Directions.RIGHT:
                    if radius[1] > 0.0: return True
                    else: return False
        return False

    def get_far_side(self, tb_to, direction):
        slf = self.get_arrow_point(self.direction2pp(direction))
        tbt = tb_to.get_arrow_point(tb_to.direction2pp(direction))
        match direction:
            case Directions.UP:
                if slf[1] > tbt[1]: return slf[1] * manim.UP
                else: return tbt[1] * manim.UP
            case Directions.DOWN:
                if slf[1] < tbt[1]: return slf[1] * manim.UP
                else: return tbt[1] * manim.UP
            case Directions.RIGHT:
                if slf[0] > tbt[0]: return slf[0] * manim.RIGHT
                else: return tbt[0] * manim.RIGHT
            case Directions.LEFT:
                if slf[0] < tbt[0]: return slf[0] * manim.RIGHT
                else: return tbt[0] * manim.RIGHT
        return manim.ORIGIN

    def get_mid_point(self, tb_to, direction):
        slf = self.get_arrow_point(self.direction2pp(direction))
        tbt = tb_to.get_arrow_point(tb_to.direction2pp(direction))
        match direction:
            case Directions.UP | Directions.DOWN:
                return (slf + tbt)[0] * 0.5 * manim.RIGHT
            case Directions.RIGHT | Directions.LEFT:
                return (slf + tbt)[1] * 0.5 * manim.UP
        return manim.ORIGIN

    def get_radius(self, radius, from_direction, to_direction):
        if from_direction == Directions.UP and to_direction == Directions.DOWN:
            return abs(radius[0])
        elif from_direction == Directions.DOWN and to_direction == Directions.UP:
            return abs(radius[0])
        elif from_direction == Directions.RIGHT and to_direction == Directions.LEFT:
            return abs(radius[1])
        elif from_direction == Directions.LEFT and to_direction == Directions.RIGHT:
            return abs(radius[1])
        return abs(radius[0])
