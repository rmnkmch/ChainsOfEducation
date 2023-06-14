import manim
import Block
import ContainingBlock


DEFAULT_HEIGHT: float = Block.DEFAULT_HEIGHT
DEFAULT_WIDTH: float = Block.DEFAULT_WIDTH

DEFAULT_DESCRIPTION_FONT_SIZE: float = 12.0#32.0
DEFAULT_TITLE_FONT_SIZE: float = Block.DEFAULT_TITLE_FONT_SIZE

DEFAULT_PADDING: float = Block.DEFAULT_PADDING
DEFAULT_UNDERLINE_TITLE_OFFSET: float = Block.DEFAULT_UNDERLINE_TITLE_OFFSET


class KnowledgeBlock(Block.Block):
    """Class for all blocks of knowledge"""

    def __init__(
        self,
        title: str = "KnowledgeBlockTitle",
        description: str = "KnowledgeBlockDescription",
        height: float = DEFAULT_HEIGHT,
        width: float = DEFAULT_WIDTH,
        **kwargs):
        super().__init__(
            title = title,
            height = height,
            width = width,
            **kwargs)

        self.description = manim.Text(
            description,
            font_size = DEFAULT_DESCRIPTION_FONT_SIZE)
        self.build_description()

        #self.containing_b = ContainingBlock.ContainingBlock("0")

        self.add(self.description)#, self.containing_b)

    def is_acceptable_description_width(self, descr: manim.Text):
        if len(self.get_all_subbs()) >= 1:
            return (descr.width <
                    0.5 * self.b_width
                    - 2.0 * DEFAULT_PADDING * self.get_proportion())
        return (descr.width <
                self.b_width - 2.0 * DEFAULT_PADDING * self.get_proportion())

    def is_acceptable_description_height(self, descr: manim.Text):
        return (descr.height < self.b_height - self.title.height
                - (2.0 * DEFAULT_PADDING + DEFAULT_UNDERLINE_TITLE_OFFSET)
                * self.get_proportion())

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
        vertical_space = (self.b_height - self.title.height
                          - (DEFAULT_UNDERLINE_TITLE_OFFSET
                             + 2.0 * DEFAULT_PADDING)
                          * self.get_proportion())
        description_pos = (manim.DOWN * (0.5 * self.b_height
                                         - 0.5 * vertical_space
                                         - DEFAULT_PADDING
                                         * self.get_proportion())
                           + self.get_center())
        if len(self.get_all_subbs()) >= 1:
            description_pos += manim.LEFT * 0.25 * self.b_width
        return description_pos

    def save_all_opacity(self):
        super().save_all_opacity()
        self.all_old_opacity.append(self.description.get_fill_opacity())
        self.all_old_opacity.append(self.description.get_stroke_opacity())

    def hide(self):
        super().hide()
        self.description.set_fill(opacity = 0.0)
        self.description.set_stroke(opacity = 0.0)

    def display(self):
        super().display()
        self.description.set_fill(opacity = self.all_old_opacity[6])
        self.description.set_stroke(opacity = self.all_old_opacity[7])
