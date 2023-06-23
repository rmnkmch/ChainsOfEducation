import manim


DEFAULT_HEIGHT: float = 4.5
DEFAULT_WIDTH: float = 8.0

DEFAULT_TITLE_FONT_SIZE: float = 56.0

DEFAULT_PADDING: float = 0.3
DEFAULT_UNDERLINE_TITLE_OFFSET: float = 0.3


class Block(manim.RoundedRectangle):
    """Base class for all blocks"""

    def __init__(
        self,
        title: str = "Block",
        height: float = DEFAULT_HEIGHT,
        width: float = DEFAULT_WIDTH,
        **kwargs):
        super().__init__(
            height = height,
            width = width,
            **kwargs)

        self.subbs = []
        self.b_height: float = height
        self.b_width: float = width
        self.b_center = super().get_center()

        self.title = manim.Text(
            title,
            font_size = DEFAULT_TITLE_FONT_SIZE,
            weight = manim.BOLD)
        self.set_normal_title()
        self.title_underline = manim.Underline(self.title)

        self.hidden = False

        self.add(self.title, self.title_underline)

    def add_subb(self, subb):
        if subb not in self.get_all_subbs():
            self.subbs.append(subb)

    def remove_subb(self, subb):
        if subb in self.get_all_subbs():
            self.subbs.remove(subb)

    def scale(self, scale_factor: float, **kwargs):
        super().scale(scale_factor, **kwargs)
        self.update_size(scale_factor)
        return self

    def update_size(self, scale_factor: float):
        self.b_height *= scale_factor
        self.b_width *= scale_factor
        for subb in self.get_all_subbs():
            subb.update_size(scale_factor)

    def set_center(self, new_center):
        self.b_center = new_center
        current_subb_index: int = 0
        for subb in self.get_all_subbs():
            subb.set_center(self.get_subb_pos(current_subb_index))
            current_subb_index += 1

    def get_center(self):
        return self.b_center

    def move_to(self, point_or_mobject, aligned_edge = manim.ORIGIN, **kwargs):
        super().move_to(point_or_mobject, aligned_edge, **kwargs)
        if (isinstance(point_or_mobject, Block) and aligned_edge == manim.ORIGIN):
            self.set_center(point_or_mobject.get_center())
        elif isinstance(point_or_mobject, manim.Mobject):
            self.set_center(point_or_mobject.get_critical_point(aligned_edge))
        else:
            self.set_center(point_or_mobject)
        return self

    def get_animations_to_play(self):
        animations_to_play = manim.AnimationGroup(manim.MoveToTarget(self))
        for subb in self.get_all_subbs():
            animations_to_play = manim.AnimationGroup(
                animations_to_play, subb.get_animations_to_play())
        return animations_to_play

    def make_finish_target(self, parent = True):
        if parent:
            self.generate_targets()
        self.make_subblocks()
        for subb in self.get_all_subbs():
            subb.make_finish_target(False)

    def generate_targets(self):
        self.generate_target()
        for subb in self.get_all_subbs():
            subb.generate_targets()

    def make_subblocks(self):
        current_subb_index: int = 0
        loc_subbs = self.get_all_subbs()
        len_subbs = len(loc_subbs)
        for subb in loc_subbs:
            sub_scale = self.get_subb_scale(current_subb_index) / subb.b_width
            sub_pos = self.get_subb_pos(current_subb_index)
            subb.update_size(sub_scale)
            subb.set_center(sub_pos)
            subb.target.scale(sub_scale).move_to(sub_pos)
            if ((current_subb_index >= 4) or
                ((current_subb_index >= 3) and len_subbs >= 5) or
                (not subb.is_clear() and len_subbs >= 2)):
                subb.save_all_opacity()
                subb.hidden = True
                subb.target.hide()
            else:
                subb.hidden = False
                subb.target.display()
            current_subb_index += 1

    def get_subb_scale(self, index: int, containing = False):
        subb_scale: float = 0.5
        if ((index == 0) and (len(self.get_all_subbs()) <= 1)) or containing:
            subb_scale = 1.0
        return subb_scale * 0.5 * self.b_width

    def get_subb_pos(self, index: int, containing = False):
        vertical_space = (self.b_height - self.title.height
                          - (DEFAULT_UNDERLINE_TITLE_OFFSET
                             + 2.0 * DEFAULT_PADDING)
                          * self.get_proportion())
        subb_pos = (manim.RIGHT * 0.25 * self.b_width
                    + manim.DOWN * (0.5 * self.b_height
                                    - 0.5 * vertical_space
                                    - DEFAULT_PADDING * self.get_proportion())
                    + self.get_center())
        horizontal_dop_part = manim.LEFT * 0.125 * self.b_width
        vertical_dop_part = 0.25 * manim.UP * vertical_space
        if ((index == 0) and (len(self.get_all_subbs()) <= 1)) or containing:
            return subb_pos
        if index == 0:
            subb_pos += horizontal_dop_part + vertical_dop_part
        elif index == 1:
            subb_pos += - horizontal_dop_part + vertical_dop_part
        elif index == 2:
            subb_pos += horizontal_dop_part - vertical_dop_part
        else:
            subb_pos += - horizontal_dop_part - vertical_dop_part
        return subb_pos

    def get_all_subbs(self):
        return self.subbs

    def get_proportion(self):
        return self.b_width / DEFAULT_WIDTH

    def is_clear(self):
        return self.b_width > 1.0

    def is_acceptable_title_width(self):
        return (self.title.width <
                self.b_width - 2.0 * DEFAULT_PADDING * self.get_proportion())

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
        self.all_old_opacity = [
            self.get_fill_opacity(),
            self.get_stroke_opacity(),
            self.title.get_fill_opacity(),
            self.title.get_stroke_opacity(),
            self.title_underline.get_fill_opacity(),
            self.title_underline.get_stroke_opacity()]
        for subb in self.get_all_subbs():
            subb.save_all_opacity()
        return True

    def hide(self):
        if self.is_hidden():
            return False
        self.hidden = True
        self.set_fill(opacity = 0.0)
        self.set_stroke(opacity = 0.0)
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
        self.title.set_fill(opacity = self.all_old_opacity[2])
        self.title.set_stroke(opacity = self.all_old_opacity[3])
        self.title_underline.set_fill(opacity = self.all_old_opacity[4])
        self.title_underline.set_stroke(opacity = self.all_old_opacity[5])
        #self.set_stroke(opacity=opacity, background=True)???
        for subb in self.get_all_subbs():
            subb.display()
        return True
