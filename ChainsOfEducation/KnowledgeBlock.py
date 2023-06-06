import manim


DEFAULT_HEIGHT: float = 4.5
DEFAULT_WIDTH: float = 8.0

DEFAULT_DESCRIPTION_FONT_SIZE: float = 12.0#32.0
DEFAULT_TITLE_FONT_SIZE: float = 56.0

DEFAULT_PADDING: float = 0.3
DEFAULT_UNDERLINE_TITLE_OFFSET: float = 0.3


class KnowledgeBlock(manim.RoundedRectangle):
    """Base class for all blocks of knowledge"""

    def __init__(
        self,
        title: str = "KnowledgeBlockTitle",
        description: str = "KnowledgeBlockDescription",
        height: float = DEFAULT_HEIGHT,
        width: float = DEFAULT_WIDTH,
        **kwargs):
        super().__init__(
            height = height,
            width = width,
            **kwargs)

        self.kb_height: float = DEFAULT_HEIGHT
        self.kb_width: float = DEFAULT_WIDTH
        self.center = super().get_center()

        self.title = manim.Text(
            title,
            font_size = DEFAULT_TITLE_FONT_SIZE,
            weight = manim.BOLD)
        self.set_normal_title()
        self.title_underline = manim.Underline(self.title)

        self.description = manim.Text(
            description,
            font_size = DEFAULT_DESCRIPTION_FONT_SIZE)
        self.build_description()

        self.add(self.title, self.title_underline, self.description)

    def add(self, *mobjects):
        super().add(*mobjects)
        return self

    def remove(self, *mobjects):
        super().remove(*mobjects)
        return self

    def scale(self, scale_factor: float, **kwargs):
        super().scale(scale_factor, **kwargs)
        self.update_size(scale_factor)
        return self

    def update_size(self, scale_factor: float):
        self.kb_height *= scale_factor
        self.kb_width *= scale_factor
        for subkb in self.get_all_subkbs():
            subkb.update_size(scale_factor)

    def set_center(self, new_center):
        self.center = new_center
        current_kb_index = 0
        for subkb in self.get_all_subkbs():
            subkb.set_center(subkb.get_subkb_pos(current_kb_index))
            current_kb_index += 1

    def get_center(self):
        return self.center

    def move_to(self, point_or_mobject, aligned_edge = manim.ORIGIN, **kwargs):
        super().move_to(point_or_mobject, aligned_edge, **kwargs)
        if (isinstance(point_or_mobject, KnowledgeBlock) and
            aligned_edge == manim.ORIGIN):
            self.set_center(point_or_mobject.get_center())
        elif isinstance(point_or_mobject, manim.Mobject):
            self.set_center(point_or_mobject.get_critical_point(aligned_edge))
        else:
            self.set_center(point_or_mobject)
        return self

    def get_subkb_info_to_update(self):
        ret_info = []
        current_subkb_index = 0
        for subkb in self.get_all_subkbs():
            scale = self.get_subkb_scale(current_subkb_index)
            pos = self.get_subkb_pos(current_subkb_index)
            if ((abs(scale - 1.0) >= 0.001) or
                (abs(pos[0] - subkb.get_center()[0]) >= 0.001) or
                (abs(pos[1] - subkb.get_center()[1]) >= 0.001)):
                ret_info.append(tuple([subkb, scale, pos]))
            current_subkb_index += 1
        return ret_info

    def get_subkb_scale(self, index: int):
        subkb_scale: float = 0.5
        subkbs = self.get_all_subkbs()
        if (index == 0) and (len(subkbs) == 1):
            subkb_scale = 1.0
        return subkb_scale * 0.5 * self.kb_width / subkbs[index].kb_width

    def get_subkb_pos(self, index: int):
        vertical_space = (self.kb_height - self.title.height
                          - (DEFAULT_UNDERLINE_TITLE_OFFSET
                             + 2.0 * DEFAULT_PADDING)
                          * self.get_kb_proportion())
        subkb_pos = (manim.RIGHT * 0.25 * self.kb_width
                     + manim.DOWN * (0.5 * self.kb_height
                                     - 0.5 * vertical_space
                                     - DEFAULT_PADDING * self.get_kb_proportion())
                     + self.get_center())
        horizontal_dop_part = manim.LEFT * 0.125 * self.kb_width
        vertical_dop_part = 0.25 * manim.UP * vertical_space
        if (index == 0) and (len(self.get_all_subkbs()) == 1):
            return subkb_pos
        if index == 0:
            subkb_pos += horizontal_dop_part + vertical_dop_part
        elif index == 1:
            subkb_pos += - horizontal_dop_part + vertical_dop_part
        elif index == 2:
            subkb_pos += horizontal_dop_part - vertical_dop_part
        else:
            subkb_pos += - horizontal_dop_part - vertical_dop_part
        return subkb_pos

    def get_all_subkbs(self):
        return [kb for kb in self.submobjects if isinstance(kb, KnowledgeBlock)]

    def get_kb_proportion(self):
        return self.kb_width / DEFAULT_WIDTH

    def is_acceptable_title_width(self):
        return (self.title.width <
                self.kb_width - 2.0 * DEFAULT_PADDING * self.get_kb_proportion())

    def is_acceptable_description_width(self, descr: manim.Text):
        if len(self.get_all_subkbs()) >= 1:
            return (descr.width <
                    0.5 * self.kb_width
                    - 2.0 * DEFAULT_PADDING * self.get_kb_proportion())
        return (descr.width <
                self.kb_width - 2.0 * DEFAULT_PADDING * self.get_kb_proportion())

    def is_acceptable_description_height(self, descr: manim.Text):
        return (descr.height < self.kb_height - self.title.height
                - (2.0 * DEFAULT_PADDING + DEFAULT_UNDERLINE_TITLE_OFFSET)
                * self.get_kb_proportion())

    def set_normal_title(self):
        while not self.is_acceptable_title_width():
            self.title.font_size -= 1.0
        self.title.next_to(self, manim.UP, - self.title.height - DEFAULT_PADDING)

    def build_description(self):
        text_and_size = self.get_correct_description_size_and_text()
        self.description = manim.Text(
            text_and_size[0], font_size = DEFAULT_DESCRIPTION_FONT_SIZE)
        self.description.scale(text_and_size[1])
        self.description.move_to(self.get_description_correct_position())

    def get_description_info_to_update(self):
        ret_info = []
        text_and_size = self.get_correct_description_size_and_text()
        pos = self.get_description_correct_position()
        if ((abs(text_and_size[1] - 1.0) >= 0.001) or
            (abs(pos[0] - self.description.get_center()[0]) >= 0.001) or
            (abs(pos[1] - self.description.get_center()[1]) >= 0.001)):
            ret_info.append(tuple([self.description, text_and_size[0],
                                   text_and_size[1], pos]))
        return ret_info

    def get_correct_description_size_and_text(self):
        correct_text = self.get_splited_description_text()
        new_description = manim.Text(
            correct_text, font_size = DEFAULT_DESCRIPTION_FONT_SIZE)
        scale_factor: float = (DEFAULT_DESCRIPTION_FONT_SIZE
                               / self.description.font_size)
        while not self.is_acceptable_description_height(new_description):
            new_description.scale(0.9)
            scale_factor *= 0.9
            correct_text = self.get_splited_description_text(
                new_description.font_size)
            new_description = manim.Text(
                correct_text, font_size = new_description.font_size)
        while not self.is_acceptable_description_width(new_description):
            new_description.scale(0.9)
            scale_factor *= 0.9
        return (correct_text, scale_factor)

    def get_splited_description_text(
        self, new_font_size: float = DEFAULT_DESCRIPTION_FONT_SIZE):
        def is_there_another_word():
            return current_word_index < len(all_text)

        all_text: list[str] = self.description.original_text.split()
        splited_text: str = ""
        current_word_index: int = 0
        while is_there_another_word():
            current_str: str = all_text[current_word_index]
            current_word_index += 1
            while (is_there_another_word() and
                   self.is_acceptable_description_width(
                       manim.Text(
                           current_str + " " + all_text[current_word_index],
                           font_size = new_font_size))):
                current_str += " " + all_text[current_word_index]
                current_word_index += 1
            splited_text += current_str
            if is_there_another_word():
                splited_text += "\n"

        return splited_text

    def get_description_correct_position(self):
        vertical_space = (self.kb_height - self.title.height
                          - (DEFAULT_UNDERLINE_TITLE_OFFSET
                             + 2.0 * DEFAULT_PADDING)
                          * self.get_kb_proportion())
        description_pos = (manim.DOWN * (0.5 * self.kb_height
                                         - 0.5 * vertical_space
                                         - DEFAULT_PADDING
                                         * self.get_kb_proportion())
                           + self.get_center())
        if len(self.get_all_subkbs()) >= 1:
            description_pos += manim.LEFT * 0.25 * self.kb_width
        return description_pos


class ContainingBlock(KnowledgeBlock):
    """Class for fourth and next subblocks of KnowledgeBlock"""

    def __init__(self, title: str = "0", **kwargs):
        super().__init__(title = title, **kwargs)
