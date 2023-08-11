import manim
import Block


class EllipsisBlock(manim.RoundedRectangle):
    """Block for hidden information"""

    def __init__(self, **kwargs):
        super().__init__(
            height = 0.2 * Block.DEFAULT_WIDTH,
            width = 0.4 * Block.DEFAULT_WIDTH,
            fill_color = "#A09A8D",
            fill_opacity = 0.1,
            stroke_color = "#FFFFFF",
            stroke_opacity = 1.0,
            stroke_width = 4,
            background_stroke_color = "#000000",
            background_stroke_opacity = 1.0,
            background_stroke_width = 0,
            **kwargs)

        radius_dot = 0.04 * Block.DEFAULT_WIDTH
        pos_dot = manim.LEFT * (0.5 * (self.width * 0.5 - radius_dot) + radius_dot)
        color_dot = "#FFFFFF"

        self.dot_1 = manim.Circle(
            radius_dot, color_dot, fill_opacity = 0.1).move_to(pos_dot)
        self.dot_2 = manim.Circle(
            radius_dot, color_dot, fill_opacity = 0.1)
        self.dot_3 = manim.Circle(
            radius_dot, color_dot, fill_opacity = 0.1).move_to(- pos_dot)

        self.add(self.dot_1, self.dot_2, self.dot_3)

        self.hidden = False
        self.all_old_opacity = []
        self.save_all_opacity()
        self.hide()

    def is_hidden(self):
        return self.hidden

    def save_all_opacity(self):
        if self.is_hidden():
            return False
        already_saved = self.all_old_opacity.copy()
        self.all_old_opacity = [
            self.get_fill_opacity(),
            self.get_stroke_opacity(),
            self.get_stroke_opacity(True)]
        for op in range(len(self.all_old_opacity), len(already_saved)):
            self.all_old_opacity.append(already_saved[op])
        return True

    def hide(self):
        if self.is_hidden():
            return False
        self.hidden = True
        self.set_fill(opacity = 0.0)
        self.set_stroke(opacity = 0.0)
        self.set_stroke(opacity = 0.0, background = True)
        return True

    def display(self):
        if not self.is_hidden():
            return False
        self.hidden = False
        self.set_fill(opacity = self.all_old_opacity[0])
        self.set_stroke(opacity = self.all_old_opacity[1])
        self.set_stroke(opacity = self.all_old_opacity[2], background = True)
        return True
