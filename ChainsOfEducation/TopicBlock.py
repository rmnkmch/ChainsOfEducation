import manim


class TopicBlock(manim.RoundedRectangle):
    """TopicBlock"""

    def __init__(
        self,
        title: str = "TopicBlock",
        height: float = 4.0,
        width: float = 8.0,
        corner_radius: float = 1.8,
        fill_color = "#777777",
        fill_opacity = 0.1,
        stroke_color = "#FFFFFF",
        stroke_opacity = 1.0,
        stroke_width = 4,
        background_stroke_color = "#000000",
        background_stroke_opacity = 1.0,
        background_stroke_width = 0,
        **kwargs):
        super().__init__(
            height = height,
            width = width,
            corner_radius = corner_radius,
            fill_color = fill_color,
            fill_opacity = fill_opacity,
            stroke_color = stroke_color,
            stroke_opacity = stroke_opacity,
            stroke_width = stroke_width,
            background_stroke_color = background_stroke_color,
            background_stroke_opacity = background_stroke_opacity,
            background_stroke_width = background_stroke_width,
            **kwargs)

        self.title = manim.Text(title, font_size = 56.0, weight = manim.BOLD)
        self.title_underline = manim.Underline(self.title)

        self.briefs = []

        self.add(self.title, self.title_underline)
