import manim


MIN_DESCRIPTION_FONT_SIZE: float = 10.5
DEFAULT_DESCRIPTION_FONT_SIZE: float = 32.0
MIN_TITLE_FONT_SIZE: float = 18.5
DEFAULT_TITLE_FONT_SIZE: float = 56.0

DEFAULT_PADDING: float = 0.3


class KnowledgeBlock(manim.RoundedRectangle):
    """Base class for all blocks of knowledge"""

    def __init__(
        self,
        title: str = "KnowledgeBlockTitle",
        description: str = "KnowledgeBlockDescription",
        **kwargs):
        super().__init__(
            height=4.5,
            width=8.0,
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

    def is_acceptable_width(self, text: manim.Text):
        return text.width < self.width - 2.0 * DEFAULT_PADDING

    def is_acceptable_height(self, text: manim.Text):
        return (text.height < self.height - self.title.height
                - 2.0 * DEFAULT_PADDING - 0.3)

    def set_normal_title_size(self):
        while (not self.is_acceptable_width(self.title) and
               self.title.font_size > MIN_TITLE_FONT_SIZE):
            self.title.font_size -= 1.0
        self.title.next_to(self, manim.UP, -self.title.height - DEFAULT_PADDING)

    def build_description(self):
        self.set_normal_description_size()
        self.move_description_in_correct_position()

    def move_description_in_correct_position(self):
        self.description.next_to(self, manim.DOWN,
                                 - 0.5 * (self.height - self.title.height - 0.3)
                                 - 0.5 * self.description.height)

    def set_normal_description_size(self):
        self.split_description_lines()
        while (not self.is_acceptable_height(self.description) and
               self.description.font_size > MIN_DESCRIPTION_FONT_SIZE):
            self.description.font_size -= 1.0
            self.split_description_lines()
        while (not self.is_acceptable_width(self.description) and
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
                   self.is_acceptable_width(
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
