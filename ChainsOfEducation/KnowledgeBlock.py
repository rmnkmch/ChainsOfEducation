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

    def scale(self, scale_factor: float, **kwargs):
        super().scale(scale_factor, **kwargs)
        self.containing_b.scale(scale_factor, **kwargs)
        text_and_size = self.get_correct_description_text_and_size()
        self.description = manim.Text(
            text_and_size[0], font_size = self.description.font_size)
        self.description.scale(
            text_and_size[1]).move_to(self.get_description_correct_position())
        return self

    def move_to(self, point_or_mobject, aligned_edge = manim.ORIGIN, **kwargs):
        super().move_to(point_or_mobject, aligned_edge, **kwargs)
        self.containing_b.move_to(self.get_subb_pos(0))
        self.description.move_to(self.get_description_correct_position())
        return self

    def get_animations_to_play(self):
        return manim.AnimationGroup(super().get_animations_to_play(),
                                    manim.MoveToTarget(self.description),
                                    manim.MoveToTarget(self.containing_b))

    def make_finish_target(self):
        super().make_finish_target()
        self.make_description()
        self.make_containing_b()

    def make_description(self):
        text_and_size = self.get_correct_description_text_and_size()
        self.description.generate_target()
        self.description.target = manim.Text(
            text_and_size[0], font_size = self.description.font_size)
        self.description.target.scale(text_and_size[1]).move_to(
            self.get_description_correct_position())
        if (not self.is_font_size_clear(self.description.target.font_size - 1.0) or
            self.target.hidden):
            self.description_hidden = True
            self.save_description_opacity()
            self.target.hide_description()
        else:
            self.description_hidden = False
            if len(self.all_old_opacity) >= 8:
                self.target.display_description()

    def make_containing_b(self):

        def hide_containing_b():
            nonlocal scale_center, pos_center
            self.containing_b.save_all_opacity()
            self.containing_b.hidden = True
            self.containing_b.target = ContainingBlock.ContainingBlock("0")
            self.containing_b.target.scale(
                scale_center / self.containing_b.target.width
                ).move_to(pos_center)
            self.containing_b.target.hide()

        scale_center = self.get_subb_scale(0, True, True)
        scale_DR = self.get_subb_scale(3, from_target = True)
        pos_center = self.get_subb_pos(0, True, True)
        pos_DR = self.get_subb_pos(3, from_target = True)
        len_all_subbs = len(self.get_all_subbs())
        self.containing_b.generate_target()
        self.containing_b.target.scale(scale_DR / self.containing_b.target.width)
        if not self.containing_b.target.is_clear():
            if len_all_subbs >= 2:
                self.containing_b.hidden = False
                self.containing_b.target = ContainingBlock.ContainingBlock(
                    str(len_all_subbs))
                self.containing_b.target.scale(
                    scale_center / self.containing_b.target.width
                    ).move_to(pos_center)
                self.containing_b.target.display()
            else:
                hide_containing_b()
        else:
            if len_all_subbs >= 5:
                self.containing_b.hidden = False
                self.containing_b.target = ContainingBlock.ContainingBlock(
                    str(len_all_subbs - 3))
                self.containing_b.target.scale(
                    scale_DR / self.containing_b.target.width
                    ).move_to(pos_DR)
                self.containing_b.target.display()
            else:
                hide_containing_b()

    def is_font_size_clear(self, font_size: float):
        return font_size > MIN_DESCRIPTION_FONT_SIZE

    def is_acceptable_description_width(
        self, descr: manim.Text, check_font = False):
        if (check_font and not self.is_font_size_clear(descr.font_size)):
            return True
        if len(self.get_all_subbs()) >= 1:
            return (descr.width <
                    0.5 * self.width
                    - 2.0 * DEFAULT_PADDING * self.get_proportion())
        return (descr.width <
                self.width - 2.0 * DEFAULT_PADDING * self.get_proportion())

    def is_acceptable_description_height(self, descr: manim.Text):
        if not self.is_font_size_clear(descr.font_size):
            return True
        return (descr.height < self.height - self.title.height
                - (2.0 * DEFAULT_PADDING + DEFAULT_UNDERLINE_TITLE_OFFSET)
                * self.get_proportion())

    def build_description(self):
        text_and_size = self.get_correct_description_text_and_size()
        self.description = manim.Text(
            text_and_size[0], font_size = self.description.font_size)
        self.description.scale(text_and_size[1])
        self.description.move_to(self.get_description_correct_position())

    def get_correct_description_text_and_size(self, from_target = False):
        used_b = self
        if from_target:
            used_b = self.target
        correct_text = used_b.get_splited_description_text()
        new_description = manim.Text(
            correct_text, font_size = DEFAULT_DESCRIPTION_FONT_SIZE)
        scale_factor: float = (DEFAULT_DESCRIPTION_FONT_SIZE
                               / used_b.description.font_size)
        while not self.is_acceptable_description_height(new_description):
            new_description.scale(0.9)
            scale_factor *= 0.9
            correct_text = used_b.get_splited_description_text(
                new_description.font_size)
        while not self.is_acceptable_description_width(new_description, True):
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

    def get_description_correct_position(self, from_target = False):
        used_b = self
        if from_target:
            used_b = self.target
        vertical_space = (used_b.height - used_b.title.height
                          - (DEFAULT_UNDERLINE_TITLE_OFFSET
                             + 2.0 * DEFAULT_PADDING)
                          * used_b.get_proportion())
        description_pos = (manim.DOWN * (0.5 * used_b.height
                                         - 0.5 * vertical_space
                                         - DEFAULT_PADDING
                                         * used_b.get_proportion())
                           + used_b.get_center())
        if len(self.get_all_subbs()) >= 1:
            description_pos += manim.LEFT * 0.25 * used_b.width
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
            if len(self.all_old_opacity) >= 8:
                self.display_description()
            return True
        return False

    def display_description(self):
        if not self.is_description_hidden():
            return False
        self.description.set_fill(opacity = self.all_old_opacity[6])
        self.description.set_stroke(opacity = self.all_old_opacity[7])
        return True
