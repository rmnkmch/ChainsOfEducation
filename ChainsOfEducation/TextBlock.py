import manim


class TextBlock(manim.Text):
    """TextBlock"""

    def __init__(
        self,
        text: str,
        fill_opacity: float = 1.0,
        stroke_width: float = 0.0,
        color: str | None = None,
        font_size: float = ...,
        line_spacing: float = - 1.0,
        font: str = "",
        slant: str = ...,
        weight: str = ...,
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

    def get_arrow_point(self):
        return self.get_center()
