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

        self.b_height: float = height
        self.b_width: float = width
        self.b_center = super().get_center()

        self.title = manim.Text(
            title,
            font_size = DEFAULT_TITLE_FONT_SIZE,
            weight = manim.BOLD)
        self.set_normal_title()
        self.title_underline = manim.Underline(self.title)

        self.add(self.title, self.title_underline)

    def add(self, *mobjects):
        return super().add(*mobjects)

    def remove(self, *mobjects):
        return super().remove(*mobjects)

    def scale(self, scale_factor: float, **kwargs):
        super().scale(scale_factor, **kwargs)
        self.update_size(scale_factor)
        print(self.b_width)
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
            subb.set_center(subb.get_subb_pos(current_subb_index))
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

    def prepare_target(self):
        self.make_target_with_correct_subblocks()

    def make_finish_target(self):
        self.make_target_with_correct_subblocks()

    def make_target_with_correct_subblocks(self):
        current_subb_index: int = 0
        for subb in self.get_all_subbs():
            new_scale = self.get_subb_scale(current_subb_index)
            pos = self.get_subb_pos(current_subb_index)
            subb.scale(new_scale).move_to(pos)
            current_subb_index += 1

    """def get_subb_info_to_update(self):
        ret_info = []
        current_subb_index: int = 0
        for subb in self.get_all_subbs():
            scale = self.get_subb_scale(current_subb_index)
            pos = self.get_subb_pos(current_subb_index)
            if ((abs(scale - 1.0) >= 0.001) or
                (abs(pos[0] - subb.get_center()[0]) >= 0.001) or
                (abs(pos[1] - subb.get_center()[1]) >= 0.001)):
                ret_info.append(tuple([subb, scale, pos]))
            current_subb_index += 1
        return ret_info"""

    def get_subb_scale(self, index: int):
        subb_scale: float = 0.5
        subbs = self.get_all_subbs()
        if (index == 0) and (len(subbs) == 1):
            subb_scale = 1.0
        return subb_scale * 0.5 * self.b_width / subbs[index].b_width

    def get_subb_pos(self, index: int):
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
        if (index == 0) and (len(self.get_all_subbs()) == 1):
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
        ret_list = []
        for b in self.submobjects:
            if isinstance(b, Block):
                ret_list.append(b)
        return ret_list

    def get_proportion(self):
        return self.b_width / DEFAULT_WIDTH

    def is_acceptable_title_width(self):
        return (self.title.width <
                self.b_width - 2.0 * DEFAULT_PADDING * self.get_proportion())

    def set_normal_title(self):
        while not self.is_acceptable_title_width():
            self.title.font_size -= 2.0
        self.title.next_to(self, manim.UP, - self.title.height - DEFAULT_PADDING)

    def set_fill(self, color: str | None = None,
                 opacity: float | None = None, family: bool = False):
        return super().set_fill(color, opacity, family)

    def set_stroke(self, color = None, width = None,
                   opacity = None, background = False, family = False):
        return super().set_stroke(color, width, opacity, background, family)

    def save_all_opacity(self):
        self.all_old_opacity = [
            self.get_fill_opacity(),
            self.get_stroke_opacity(),
            self.title.get_fill_opacity(),
            self.title.get_stroke_opacity(),
            self.title_underline.get_fill_opacity(),
            self.title_underline.get_stroke_opacity()]
        for subb in self.get_all_subbs():
            subb.save_all_opacity()

    def hide(self):
        self.set_fill(opacity = 0.0)
        self.set_stroke(opacity = 0.0)
        self.title.set_fill(opacity = 0.0)
        self.title.set_stroke(opacity = 0.0)
        self.title_underline.set_fill(opacity = 0.0)
        self.title_underline.set_stroke(opacity = 0.0)
        for subb in self.get_all_subbs():
            subb.hide()

    def display(self):
        self.set_fill(opacity = self.all_old_opacity[0])
        self.set_stroke(opacity = self.all_old_opacity[1])
        self.title.set_fill(opacity = self.all_old_opacity[2])
        self.title.set_stroke(opacity = self.all_old_opacity[3])
        self.title_underline.set_fill(opacity = self.all_old_opacity[4])
        self.title_underline.set_stroke(opacity = self.all_old_opacity[5])
        #self.set_stroke(opacity=opacity, background=True)???
        for subb in self.get_all_subbs():
            subb.display()

    def make_target_be_hidden(self):
        self.generate_target()
        self.save_all_opacity()
        self.target.hide()

    def make_target_be_displayed(self):
        self.generate_target()
        self.target.display()
