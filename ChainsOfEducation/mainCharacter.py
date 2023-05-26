import manim


class MainCharacter(manim.RoundedRectangle):
    """Character which explain everything"""

    def __init__(self, **kwargs):
        super().__init__(
            corner_radius=1.2,
            height=5.0,
            width=5.0,
            fill_color=manim.color.MAROON_E,
            fill_opacity=1.0,
            **kwargs)

        leftEye = manim.RoundedRectangle(
            corner_radius=0.6,
            height=1.5,
            width=1.5,
            fill_color=manim.color.GRAY_A,
            fill_opacity=1.0,
            ).move_to(manim.UL)
        rightEye = manim.RoundedRectangle(
            corner_radius=0.6,
            height=1.5,
            width=1.5,
            fill_color=manim.color.GRAY_A,
            fill_opacity=1.0,
            ).move_to(manim.UR)
        mouth = manim.RoundedRectangle(
            corner_radius=0.5,
            height=1.0,
            width=2.5,
            fill_color=manim.color.BLACK,
            fill_opacity=1.0,
            ).move_to(manim.DOWN)
        leftPupil = manim.RoundedRectangle(
            corner_radius=0.4,
            height=1.0,
            width=1.0,
            fill_color=manim.color.BLACK,
            fill_opacity=1.0,
            ).move_to(manim.UL)
        rightPupil = manim.RoundedRectangle(
            corner_radius=0.4,
            height=1.0,
            width=1.0,
            fill_color=manim.color.BLACK,
            fill_opacity=1.0,
            ).move_to(manim.UR)
        self.add(leftEye, rightEye, mouth, leftPupil, rightPupil)

    def blink(self):
        pass

    def watch_at(self):
        pass
