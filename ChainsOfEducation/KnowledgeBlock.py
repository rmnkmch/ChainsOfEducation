import manim


DEFAULT_HEIGHT: float = 4.5
DEFAULT_WIDTH: float = 8.0

MIN_DESCRIPTION_FONT_SIZE: float = 10.5
DEFAULT_DESCRIPTION_FONT_SIZE: float = 12.0#32.0
MIN_TITLE_FONT_SIZE: float = 18.5
DEFAULT_TITLE_FONT_SIZE: float = 56.0

DEFAULT_PADDING: float = 0.3
DEFAULT_UNDERLINE_TITLE_OFFSET: float = 0.3


class KnowledgeBlock(manim.RoundedRectangle):
    """Base class for all blocks of knowledge
    kb - KnowledgeBlock"""

    def __init__(
        self,
        title: str = "KnowledgeBlockTitle",
        description: str = "KnowledgeBlockDescription",
        **kwargs):
        super().__init__(
            height=DEFAULT_HEIGHT,
            width=DEFAULT_WIDTH,
            **kwargs)

        self.title = manim.Text(
            title,
            font_size=DEFAULT_TITLE_FONT_SIZE,
            weight=manim.BOLD,
            )
        self.set_normal_title_size()
        self.title_underline = manim.Underline(self.title)

        self.description = manim.Text(
            description,
            font_size=DEFAULT_DESCRIPTION_FONT_SIZE,
            )
        self.build_description()

        self.add(self.title, self.title_underline, self.description)

    def scale(self, scale_factor: float, **kwargs):
        super().scale(scale_factor, **kwargs)
        return self

    def add(self, *mobjects):
        super().add(*mobjects)
        return self

    def get_subkb_info_to_update(self):
        ret_info = []
        current_kb_index = 0
        for kb in self.get_all_subkbs():
            scale = self.get_subkb_scale(current_kb_index)
            pos = self.get_subkb_pos(current_kb_index)
            ret_info.append(tuple([kb, scale, pos]))
            current_kb_index += 1
        return ret_info

    def get_subkb_scale(self, index: int):
        return 1.0
        subkb_scale: float = 0.5
        subkbs = self.get_all_subkbs()
        if (index == 0) and (len(subkbs) == 1):
            subkb_scale = 1.0
        return subkb_scale * 0.5 * self.width / subkbs[index].width

    def get_subkb_pos(self, index: int):
        return self.get_center()
        vertical_space = (self.height - self.title.height
                          - (DEFAULT_UNDERLINE_TITLE_OFFSET
                             + 2.0 * DEFAULT_PADDING)
                          * self.get_kb_proportion())
        subkb_pos = (manim.RIGHT * 0.25 * self.width
                     + manim.DOWN * (0.5 * self.height
                                     - 0.5 * vertical_space
                                     - DEFAULT_PADDING * self.get_kb_proportion())
                     + self.get_center())
        horizontal_dop_part = manim.LEFT * 0.125 * self.width
        vertical_dop_part = 0.25 * manim.UP * vertical_space
        if (index == 0) and not (len(self.get_all_subkbs()) == 1):
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
        return self.width / DEFAULT_WIDTH

    def is_acceptable_title_width(self):
        return self.title.width < self.width - 2.0 * DEFAULT_PADDING

    def is_acceptable_description_width(self, descr: manim.Text):
        if len(self.get_all_subkbs()) >= 1:
            return descr.width < 0.5 * self.width - 2.0 * DEFAULT_PADDING
        return descr.width < self.width - 2.0 * DEFAULT_PADDING

    def is_acceptable_description_height(self, text: manim.Text):
        return (text.height < self.height - self.title.height
                - (2.0 * DEFAULT_PADDING + DEFAULT_UNDERLINE_TITLE_OFFSET)
                * self.get_kb_proportion())

    def set_normal_title_size(self):
        while (not self.is_acceptable_title_width() and
               self.title.font_size > MIN_TITLE_FONT_SIZE):
            self.title.font_size -= 1.0
        self.title.next_to(self, manim.UP, - self.title.height - DEFAULT_PADDING)

    def build_description(self):
        self.set_normal_description_size()
        self.move_description_in_correct_position()

    def move_description_in_correct_position(self):
        self.description.next_to(self, manim.DOWN,
                                 - 0.5 * (self.height - self.title.height
                                          - DEFAULT_UNDERLINE_TITLE_OFFSET)
                                 - 0.5 * self.description.height)
        if len(self.get_all_subkbs()) >= 1:
            self.description.shift(manim.LEFT * 0.5 * self.width)

    def set_normal_description_size(self):
        self.split_description_lines()
        while (not self.is_acceptable_description_height(self.description) and
               self.description.font_size > MIN_DESCRIPTION_FONT_SIZE):
            self.description.font_size -= 1.0
            self.split_description_lines()
        while (not self.is_acceptable_description_width(self.description) and
               self.description.font_size > MIN_DESCRIPTION_FONT_SIZE):
            self.description.font_size -= 1.0

    def split_description_lines(self):

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
                           font_size=self.description.font_size))):
                current_str += " " + all_text[current_word_index]
                current_word_index += 1
            splited_text += current_str
            if is_there_another_word():
                splited_text += "\n"

        self.description = manim.Text(
            splited_text,
            font_size=self.description.font_size)
