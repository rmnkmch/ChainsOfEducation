import manim


class Droplet(manim.Circle):
    """Droplet"""

    def __init__(self, color=manim.WHITE, **kwargs):
        super().__init__(
            radius=1.0,
            color=color,
            fill_color=color,
            fill_opacity=1.0,
            **kwargs)

        self.tail = manim.Circle(
            radius=0.5,
            color=color,
            fill_color=color,
            fill_opacity=1.0,
            ).move_to(3*manim.DOWN)
        self.leftTriangle = manim.Polygon(
            [-1.0, 0.0, 0.0],
            [0.5, -3.0, 0.0],
            [-0.5, -3.0, 0.0],
            color=color,
            fill_color=color,
            fill_opacity=1.0,
            **kwargs)
        self.rightTriangle = manim.Polygon(
            [-1.0, 0.0, 0.0],
            [1.0, 0.0, 0.0],
            [0.5, -3.0, 0.0],
            color=color,
            fill_color=color,
            fill_opacity=1.0,
            **kwargs)

        self.add(self.tail, self.leftTriangle, self.rightTriangle)
