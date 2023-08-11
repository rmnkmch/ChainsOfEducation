import manim


DEFAULT_WIDTH: float = 8.0
DEFAULT_SUBB_PROPORTION: float = 0.45
DEFAULT_PADDING: float = 0.3
DEFAULT_UNDERLINE_TITLE_OFFSET: float = 0.3


class Block(manim.RoundedRectangle):
    """Base class for all blocks"""

    def __init__(
        self,
        title: str = "Block",
        height: float = 4.5,
        width: float = DEFAULT_WIDTH,
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
            fill_color = fill_color,
            fill_opacity = fill_opacity,
            stroke_color = stroke_color,
            stroke_opacity = stroke_opacity,
            stroke_width = stroke_width,
            background_stroke_color = background_stroke_color,
            background_stroke_opacity = background_stroke_opacity,
            background_stroke_width = background_stroke_width,
            **kwargs)

        self.subbs: list = []

        self.title = manim.Text(
            title, font_size = 56.0, weight = manim.BOLD)
        self.set_normal_title()
        self.title_underline = manim.Underline(self.title)

        self.hidden = False
        self.all_old_opacity = []
        self.save_all_opacity()

        self.add(self.title, self.title_underline)

    def add_subb(self, subb):
        if subb not in self.get_all_subbs():
            self.subbs.append(subb)

    def remove_subb(self, subb):
        if subb in self.get_all_subbs():
            self.subbs.remove(subb)

    def scale_outside(self, scale_factor: float, **kwargs):
        self.scale(scale_factor, **kwargs)
        subbs = self.get_all_subbs()
        for subb in subbs:
            subb.scale_outside(scale_factor, **kwargs)
            subb.move_to_outside(self.get_subb_positions()[subbs.index(subb)])

    def move_to_outside(self, point_or_mobject, **kwargs):
        self.move_to(point_or_mobject, **kwargs)
        subbs = self.get_all_subbs()
        for subb in subbs:
            subb.move_to_outside(self.get_subb_positions()[subbs.index(subb)])

    def get_animations_to_play(self):
        animations_to_play = manim.AnimationGroup(manim.MoveToTarget(self))
        for subb in self.get_all_subbs():
            animations_to_play = manim.AnimationGroup(
                animations_to_play, subb.get_animations_to_play())
        return animations_to_play

    def generate_target(self):
        super().generate_target()
        for subb in self.get_all_subbs():
            subb.generate_target()

    def make_finish_target(self):
        self.make_subblocks()
        for subb in self.get_all_subbs():
            subb.make_finish_target()

    def make_subblocks(self):
        subbs = self.get_all_subbs()
        len_subbs = len(subbs)
        scales = self.get_subb_scales(True)
        positions = self.get_subb_positions(True)
        for subb in subbs:
            current_subb_index = subbs.index(subb)
            subb.target.scale(scales[current_subb_index] / subb.target.width
                              ).move_to(positions[current_subb_index])
            if ((current_subb_index >= 4) or
                ((current_subb_index >= 3) and len_subbs >= 5) or
                (not subb.target.is_clear() and len_subbs >= 2) or
                self.target.is_hidden()):
                subb.save_all_opacity()
                subb.hidden = True
                subb.target.hide()
            else:
                subb.hidden = False
                subb.target.display()

    def get_subb_scales(self, from_target = False):
        used_b = self
        if from_target:
            used_b = self.target
        subb_scale = DEFAULT_SUBB_PROPORTION * used_b.width
        all_scales = []
        for _ in self.get_all_subbs():
            if len(all_scales) == 0:
                all_scales = [subb_scale]
            elif len(all_scales) == 1:
                all_scales = [0.5 * subb_scale, 0.5 * subb_scale]
            else:
                all_scales.append(0.5 * subb_scale)
        return all_scales

    def get_subb_positions(self, from_target = False):
        used_b = self
        if from_target:
            used_b = self.target
        subb_pos = (manim.RIGHT * 0.25 * used_b.width
                    + used_b.get_middle_space()
                    + used_b.get_center())
        hor_dop_part = used_b.get_horizontal_sub_part()
        vert_dop_part = used_b.get_vertical_sub_part()
        all_positions = []
        for _ in self.get_all_subbs():
            if len(all_positions) == 0:
                all_positions = [subb_pos]
            elif len(all_positions) == 1:
                all_positions = [subb_pos + hor_dop_part + vert_dop_part,
                                 subb_pos - hor_dop_part + vert_dop_part]
            elif len(all_positions) == 2:
                all_positions.append(subb_pos + hor_dop_part - vert_dop_part)
            else:
                all_positions.append(subb_pos - hor_dop_part - vert_dop_part)
        return all_positions

    def get_middle_space(self):
        return (manim.DOWN * (0.5 * self.height - 0.5 * self.get_vertical_space()
                              - DEFAULT_PADDING * self.get_proportion()))

    def get_vertical_space(self):
        return (self.height - self.title.height - self.get_proportion()
                * (DEFAULT_UNDERLINE_TITLE_OFFSET + 2.0 * DEFAULT_PADDING))

    def get_vertical_sub_part(self):
        return manim.UP * 0.25 * self.get_vertical_space()

    def get_horizontal_sub_part(self):
        return manim.LEFT * 0.125 * self.width

    def get_all_subbs(self):
        return self.subbs

    def get_proportion(self):
        return self.width / DEFAULT_WIDTH

    def is_clear(self):
        return self.width > 1.0

    def is_acceptable_title_width(self):
        return (self.title.width <
                self.width - 2.0 * DEFAULT_PADDING * self.get_proportion())

    def set_normal_title(self):
        while not self.is_acceptable_title_width():
            self.title.font_size -= 2.0
        self.title.next_to(self, manim.UP, - self.title.height
                           - DEFAULT_PADDING * self.get_proportion())

    def set_fill(self, color: str | None = None,
                 opacity: float | None = None, family: bool = False):
        return super().set_fill(color, opacity, family)

    def set_stroke(self, color = None, width = None,
                   opacity = None, background = False, family = False):
        return super().set_stroke(color, width, opacity, background, family)

    def is_hidden(self):
        return self.hidden

    def save_all_opacity(self):
        if self.is_hidden():
            return False
        already_saved = self.all_old_opacity.copy()
        self.all_old_opacity = [
            self.get_fill_opacity(),
            self.get_stroke_opacity(),
            self.get_stroke_opacity(True),
            self.title.get_fill_opacity(),
            self.title.get_stroke_opacity(),
            self.title_underline.get_fill_opacity(),
            self.title_underline.get_stroke_opacity()]
        for op in range(len(self.all_old_opacity), len(already_saved)):
            self.all_old_opacity.append(already_saved[op])
        for subb in self.get_all_subbs():
            subb.save_all_opacity()
        return True

    def hide(self):
        if self.is_hidden():
            return False
        self.hidden = True
        self.set_fill(opacity = 0.0)
        self.set_stroke(opacity = 0.0)
        self.set_stroke(opacity = 0.0, background = True)
        self.title.set_fill(opacity = 0.0)
        self.title.set_stroke(opacity = 0.0)
        self.title_underline.set_fill(opacity = 0.0)
        self.title_underline.set_stroke(opacity = 0.0)
        for subb in self.get_all_subbs():
            subb.hide()
        return True

    def display(self):
        if not self.is_hidden():
            return False
        self.hidden = False
        self.set_fill(opacity = self.all_old_opacity[0])
        self.set_stroke(opacity = self.all_old_opacity[1])
        self.set_stroke(opacity = self.all_old_opacity[2], background = True)
        self.title.set_fill(opacity = self.all_old_opacity[3])
        self.title.set_stroke(opacity = self.all_old_opacity[4])
        self.title_underline.set_fill(opacity = self.all_old_opacity[5])
        self.title_underline.set_stroke(opacity = self.all_old_opacity[6])
        for subb in self.get_all_subbs():
            subb.display()
        return True
