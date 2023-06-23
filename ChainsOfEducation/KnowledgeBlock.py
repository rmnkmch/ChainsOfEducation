import manim
import Block
import ContainingBlock


DEFAULT_DESCRIPTION_FONT_SIZE: float = 9.9
MIN_DESCRIPTION_FONT_SIZE: float = 10.0

DEFAULT_PADDING: float = Block.DEFAULT_PADDING
DEFAULT_UNDERLINE_TITLE_OFFSET: float = Block.DEFAULT_UNDERLINE_TITLE_OFFSET


class KnowledgeBlock(Block.Block):
    """Class for all blocks of knowledge"""

    def __init__(
        self,
        title: str = "KnowledgeBlockTitle",
        description: str = "KnowledgeBlockDescription",
        height: float = Block.DEFAULT_HEIGHT,
        width: float = Block.DEFAULT_WIDTH,
        **kwargs):
        super().__init__(
            title = title,
            height = height,
            width = width,
            **kwargs)

        self.containing_b = ContainingBlock.ContainingBlock()

        self.description = manim.Text(
            description,
            font_size = DEFAULT_DESCRIPTION_FONT_SIZE)
        self.build_description()
        self.description_hidden = False

        self.add(self.description)

    def update_size(self, scale_factor: float):
        super().update_size(scale_factor)
        self.containing_b.update_size(scale_factor)

    def set_center(self, new_center):
        super().set_center(new_center)
        self.containing_b.set_center(new_center)

    def get_animations_to_play(self):
        return manim.AnimationGroup(super().get_animations_to_play(),
                                    manim.MoveToTarget(self.description),
                                    manim.MoveToTarget(self.containing_b))

    def make_finish_target(self, parent = True):
        super().make_finish_target(parent)
        self.make_description()
        self.make_containing_b()

    def make_description(self):
        text_and_size = self.get_correct_description_text_and_size()
        self.description.generate_target()
        self.description.target = manim.Text(
            text_and_size[0], font_size = self.description.font_size)
        self.description.target.scale(text_and_size[1]).move_to(
            self.get_description_correct_position())
        if not self.is_font_size_clear(self.description.target.font_size - 1.0):
            self.description_hidden = True
            self.save_description_opacity()
            self.target.hide_description()
        else:
            self.description_hidden = False
            self.target.display_description()

    def make_containing_b(self):

        def hide_containing_b():
            nonlocal scale_center, pos_center
            self.containing_b.save_all_opacity()
            self.containing_b.hidden = True
            self.containing_b.target = ContainingBlock.ContainingBlock("0")
            self.containing_b.target.scale(
                scale_center / self.containing_b.target.b_width
                ).move_to(pos_center)
            self.containing_b.target.hide()

        scale_center = self.get_subb_scale(0, True)
        scale_DR = self.get_subb_scale(3)
        pos_center = self.get_subb_pos(0, True)
        pos_DR = self.get_subb_pos(3)
        len_all_subbs = len(self.get_all_subbs())
        self.containing_b.generate_target()
        self.containing_b.update_size(scale_DR / self.containing_b.b_width)
        if not self.containing_b.is_clear():
            if len_all_subbs >= 2:
                self.containing_b.update_size(
                    scale_center / self.containing_b.b_width)
                self.containing_b.set_center(pos_center)
                self.containing_b.hidden = False
                self.containing_b.target = ContainingBlock.ContainingBlock(
                    str(len_all_subbs))
                self.containing_b.target.scale(
                    scale_center / self.containing_b.target.b_width
                    ).move_to(pos_center)
                self.containing_b.target.display()
            else:
                hide_containing_b()
        else:
            if len_all_subbs >= 5:
                self.containing_b.set_center(pos_DR)
                self.containing_b.hidden = False
                self.containing_b.target = ContainingBlock.ContainingBlock(
                    str(len_all_subbs - 3))
                self.containing_b.target.scale(
                    scale_DR / self.containing_b.target.b_width
                    ).move_to(pos_DR)
                self.containing_b.target.display()
            else:
                hide_containing_b()

    def is_font_size_clear(self, font_size: float):
        return font_size > MIN_DESCRIPTION_FONT_SIZE

    def is_acceptable_description_width(self, descr: manim.Text):
        if not self.is_font_size_clear(descr.font_size):
            return True
        if len(self.get_all_subbs()) >= 1:
            return (descr.width <
                    0.5 * self.b_width
                    - 2.0 * DEFAULT_PADDING * self.get_proportion())
        return (descr.width <
                self.b_width - 2.0 * DEFAULT_PADDING * self.get_proportion())

    def is_acceptable_description_height(self, descr: manim.Text):
        if not self.is_font_size_clear(descr.font_size):
            return True
        return (descr.height < self.b_height - self.title.height
                - (2.0 * DEFAULT_PADDING + DEFAULT_UNDERLINE_TITLE_OFFSET)
                * self.get_proportion())

    def build_description(self):
        text_and_size = self.get_correct_description_text_and_size()
        self.description = manim.Text(
            text_and_size[0], font_size = self.description.font_size)
        self.description.scale(text_and_size[1])
        self.description.move_to(self.get_description_correct_position())

    def get_correct_description_text_and_size(self):
        correct_text = self.get_splited_description_text()
        new_description = manim.Text(
            correct_text, font_size = DEFAULT_DESCRIPTION_FONT_SIZE)
        scale_factor: float = (DEFAULT_DESCRIPTION_FONT_SIZE
                               / self.description.font_size)
        while not self.is_acceptable_description_height(new_description):
            new_description.scale(0.9)
            scale_factor *= 0.9
            print(new_description.font_size)
            correct_text = self.get_splited_description_text(
                new_description.font_size)
        while not self.is_acceptable_description_width(new_description):
            new_description.scale(0.9)
            scale_factor *= 0.9
        return (correct_text, scale_factor)

    def get_splited_description_text(
        self, new_font_size: float = DEFAULT_DESCRIPTION_FONT_SIZE):

        def is_there_another_word():
            nonlocal current_word_index, len_all_text
            return current_word_index < len_all_text

        def is_word_insertable(word: str):
            nonlocal current_str, max_line_len
            return len(current_str + " " + word) <= max_line_len

        def update_max_line_len(new_line_len: int):
            nonlocal max_line_len
            if new_line_len > max_line_len:
                max_line_len = new_line_len

        #max_line_len_of_font_size = {[10.0]:  10}
        all_text: list[str] = self.description.original_text.split()
        len_all_text = len(all_text)
        splited_text: str = ""
        current_word_index: int = 0
        current_str: str = ""
        max_line_len: int = 5

        while is_there_another_word():
            current_str = all_text[current_word_index]
            current_word_index += 1
            while (is_there_another_word() and
                   is_word_insertable(all_text[current_word_index])):
                current_str += " " + all_text[current_word_index]
                current_word_index += 1
            while (is_there_another_word() and
                   self.is_acceptable_description_width(
                       manim.Text(
                           current_str + " " + all_text[current_word_index],
                           font_size = new_font_size))):
                current_str += " " + all_text[current_word_index]
                current_word_index += 1
                update_max_line_len(len(current_str))
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

    def is_description_hidden(self):
        return self.description_hidden

    def save_all_opacity(self):
        if super().save_all_opacity():
            self.save_description_opacity()
            return True
        return False

    def save_description_opacity(self):
        if self.is_description_hidden():
            return False
        self.all_old_opacity.append(self.description.get_fill_opacity())
        self.all_old_opacity.append(self.description.get_stroke_opacity())
        return True

    def hide(self):
        if super().hide():
            self.hide_description()
            return True
        return False

    def hide_description(self):
        if self.is_description_hidden():
            return False
        self.description.set_fill(opacity = 0.0)
        self.description.set_stroke(opacity = 0.0)
        return True

    def display(self):
        if super().display():
            self.display_description()
            return True
        return False

    def display_description(self):
        if not self.is_description_hidden():
            return False
        self.description.set_fill(opacity = self.all_old_opacity[6])
        self.description.set_stroke(opacity = self.all_old_opacity[7])
        return True
