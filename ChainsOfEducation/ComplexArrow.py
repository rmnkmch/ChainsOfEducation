import manim


POINT_ANGLES: list = [0.0, 45.0, 90.0, 135.0, 180.0, 225.0, 270.0, 315.0]


class ComplexArrow(manim.Line):
    """ComplexArrow"""

    def __init__(self, start, end, path_arc = None, **kwargs):
        super().__init__(
            start = start,
            end = end,
            stroke_width = 6,
            buff = 0.0,
            path_arc = path_arc,
            **kwargs)

    def split_by_lines(self, num = 3):
        self.lines = []
        line_part = (self.end - self.start) / num
        print(self.start)
        print(self.end)
        for part in range(num):
            comp_arr = ComplexArrow(
                self.start + line_part * part, self.start + line_part * (part + 1))
            self.lines.append(comp_arr)
            self.add(comp_arr)
