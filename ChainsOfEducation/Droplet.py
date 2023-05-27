import manim


class Droplet(manim.Circle):
    """Droplet"""

    def __init__(self, color=manim.WHITE, **kwargs):
        super().__init__(radius=1.0, color=color, **kwargs)

        tail = manim.Circle(radius=0.5, color=color).move_to(3*manim.DOWN)
        leftLine = manim.Line(
            start=manim.LEFT,
            end=3*manim.DOWN+0.5*manim.LEFT)
        rightLine = manim.Line(
            start=manim.RIGHT,
            end=3*manim.DOWN+0.5*manim.RIGHT)
        self.add(tail, leftLine, rightLine)
