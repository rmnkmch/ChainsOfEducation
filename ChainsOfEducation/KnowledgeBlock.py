import manim
import Block
import ContainingBlock
import EllipsisBlock


DEFAULT_DESCRIPTION_FONT_SIZE: float = 11.0#30.0
MIN_DESCRIPTION_FONT_SIZE: float = 10.0
DEFAULT_PADDING: float = Block.DEFAULT_PADDING


class KnowledgeBlock(Block.Block):
    """Class for all blocks of knowledge"""

    def __init__(
        self,
        title: str = "KnowledgeBlockTitle",
        description: str = "KnowledgeBlockDescription",
        **kwargs):
        super().__init__(
            title = title,
            fill_color = "#F08A5D",
            **kwargs)

        self.containing_b = ContainingBlock.ContainingBlock()
        self.ellipsis_b = EllipsisBlock.EllipsisBlock()

        self.description = manim.Text(
            description,
            font_size = DEFAULT_DESCRIPTION_FONT_SIZE)
        self.build_description()
        self.description_hidden = False
        self.save_description_opacity()
        self.description_should_be_hidden = False

    def scale_outside(self, scale_factor: float, **kwargs):
        super().scale_outside(scale_factor, **kwargs)
        self.containing_b.scale_outside(scale_factor, **kwargs)
        self.containing_b.move_to_outside(self.get_containing_b_positions()[0])
        text_and_size = self.get_description_text_and_size()
        self.description = manim.Text(
            text_and_size[0], font_size = DEFAULT_DESCRIPTION_FONT_SIZE)
        self.description.scale(
            text_and_size[1]).move_to(self.get_description_position())
        self.ellipsis_b.scale(
            scale_factor, **kwargs).move_to(
                self.get_description_position())

    def move_to_outside(self, point_or_mobject, **kwargs):
        super().move_to_outside(point_or_mobject, **kwargs)
        self.containing_b.move_to_outside(self.get_containing_b_positions()[0])
        self.description.move_to(self.get_description_position())
        self.ellipsis_b.move_to(self.get_description_position())

    def get_animations_to_play(self):
        return manim.AnimationGroup(super().get_animations_to_play(),
                                    manim.MoveToTarget(self.containing_b),
                                    manim.MoveToTarget(self.description),
                                    manim.MoveToTarget(self.ellipsis_b))

    def generate_target(self):
        super().generate_target()
        self.containing_b.generate_target()
        self.description.generate_target()
        self.ellipsis_b.generate_target()

    def make_finish_target(self):
        super().make_finish_target()
        self.make_containing_b()
        self.make_description()

    def make_containing_b(self):
        def hide_containing_b():
            nonlocal scale_cont_b, pos_cont_b
            self.containing_b.save_all_opacity()
            self.containing_b.hidden = True
            self.containing_b.target = ContainingBlock.ContainingBlock("0")
            self.containing_b.target.scale(
                scale_cont_b[0] / self.containing_b.target.width
                ).move_to(pos_cont_b[0])
            self.containing_b.target.hide()

        scale_cont_b = self.get_containing_b_scales(True)
        pos_cont_b = self.get_containing_b_positions(True)
        len_all_subbs = len(self.get_all_subbs())
        self.containing_b.target.scale(
            scale_cont_b[1] / self.containing_b.target.width)
        if self.target.is_hidden():
            hide_containing_b()
            return
        if not self.containing_b.target.is_clear():
            if len_all_subbs >= 2:
                self.containing_b.hidden = False
                self.containing_b.target = ContainingBlock.ContainingBlock(
                    str(len_all_subbs))
                self.containing_b.target.scale(
                    scale_cont_b[0] / self.containing_b.target.width
                    ).move_to(pos_cont_b[0])
                self.containing_b.target.display()
            else:
                hide_containing_b()
        else:
            if len_all_subbs >= 5:
                self.containing_b.hidden = False
                self.containing_b.target = ContainingBlock.ContainingBlock(
                    str(len_all_subbs - 3))
                self.containing_b.target.scale(
                    scale_cont_b[1] / self.containing_b.target.width
                    ).move_to(pos_cont_b[1])
                self.containing_b.target.display()
            else:
                hide_containing_b()

    def make_description(self):
        text_and_size = self.get_description_text_and_size(True)
        self.description.target = manim.Text(
            text_and_size[0], font_size = DEFAULT_DESCRIPTION_FONT_SIZE)
        self.description.target.scale(text_and_size[1]).move_to(
            self.get_description_position(True))
        self.display_description()
        self.ellipsis_b.target.scale(
            self.get_ellipsis_b_scale(True) / self.ellipsis_b.target.width
            ).move_to(self.get_description_position(True))
        if not self.ellipsis_b.is_hidden():
            self.ellipsis_b.save_all_opacity()
            self.ellipsis_b.hidden = True
            self.ellipsis_b.target.hide()
        if self.description_should_be_hidden or self.target.is_hidden():
            self.description_should_be_hidden = False
            self.save_description_opacity()
            self.hide_description()
            if not self.target.is_hidden() and self.ellipsis_b.is_hidden():
                self.ellipsis_b.hidden = False
                self.ellipsis_b.target.display()

    def get_containing_b_scales(self, from_target = False):
        used_b = self
        if from_target:
            used_b = self.target
        containing_scale = Block.DEFAULT_SUBB_PROPORTION * used_b.width
        return [containing_scale, 0.5 * containing_scale]

    def get_containing_b_positions(self, from_target = False):
        used_b = self
        if from_target:
            used_b = self.target
        containing_pos = (manim.RIGHT * 0.25 * used_b.width
                          + used_b.get_middle_space()
                          + used_b.get_center())
        containing_pos2 = (containing_pos - used_b.get_horizontal_sub_part()
                           - used_b.get_vertical_sub_part())
        return [containing_pos, containing_pos2]

    def is_font_size_clear(self, font_size: float):
        return font_size > MIN_DESCRIPTION_FONT_SIZE

    def is_acceptable_description_width(self, descr: manim.Text):
        if len(self.get_all_subbs()) >= 1:
            return (descr.width < 0.5 * self.width
                    - 2.0 * DEFAULT_PADDING * self.get_proportion())
        return (descr.width <
                self.width - 2.0 * DEFAULT_PADDING * self.get_proportion())

    def is_acceptable_description_height(self, descr: manim.Text):
        return (descr.height < self.height - self.title.height
                - (2.0 * DEFAULT_PADDING + Block.DEFAULT_UNDERLINE_TITLE_OFFSET)
                * self.get_proportion())

    def build_description(self):
        text_and_size = self.get_description_text_and_size()
        self.description = manim.Text(
            text_and_size[0], font_size = DEFAULT_DESCRIPTION_FONT_SIZE)
        self.description.scale(text_and_size[1])
        self.description.move_to(self.get_description_position())

    def get_description_text_and_size(self, from_target = False):
        used_b = self
        if from_target:
            used_b = self.target
        scale_const: float = 0.8
        correct_text = used_b.get_splited_description_text()
        new_description = manim.Text(
            correct_text, font_size = DEFAULT_DESCRIPTION_FONT_SIZE)
        scale_factor: float = 1.0
        while not used_b.is_acceptable_description_height(new_description):
            if not used_b.is_font_size_clear(new_description.font_size):
                self.description_should_be_hidden = True
                correct_text = used_b.get_splited_description_text(
                    MIN_DESCRIPTION_FONT_SIZE / DEFAULT_DESCRIPTION_FONT_SIZE)
                return (correct_text,
                        MIN_DESCRIPTION_FONT_SIZE / DEFAULT_DESCRIPTION_FONT_SIZE)
            new_description.scale(scale_const)
            scale_factor *= scale_const
            correct_text = used_b.get_splited_description_text(scale_factor)
        while not used_b.is_acceptable_description_width(new_description):
            if not used_b.is_font_size_clear(new_description.font_size):
                self.description_should_be_hidden = True
                return (correct_text, (MIN_DESCRIPTION_FONT_SIZE
                                       / DEFAULT_DESCRIPTION_FONT_SIZE))
            new_description.scale(scale_const)
            scale_factor *= scale_const
        return (correct_text, scale_factor)

    def get_splited_description_text(self, scale_ratio: float = 1.0):
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
                           font_size = DEFAULT_DESCRIPTION_FONT_SIZE
                           ).scale(scale_ratio))):
                current_str += " " + all_text[current_word_index]
                current_word_index += 1
                update_max_line_len(len(current_str))
            splited_text += current_str
            if is_there_another_word():
                splited_text += "\n"
        return splited_text

    def get_description_position(self, from_target = False):
        used_b = self
        if from_target:
            used_b = self.target
        description_position = used_b.get_middle_space() + used_b.get_center()
        if len(self.get_all_subbs()) >= 1:
            description_position += manim.LEFT * 0.25 * used_b.width
        return description_position

    def get_ellipsis_b_scale(self, from_target = False):
        used_b = self
        if from_target:
            used_b = self.target
        return 0.4 * used_b.width

    def is_description_hidden(self):
        return self.description_hidden

    def save_description_opacity(self):
        if self.is_description_hidden():
            return False
        self.all_old_opacity.append(self.description.get_fill_opacity())
        self.all_old_opacity.append(self.description.get_stroke_opacity())
        return True

    def hide_description(self):
        if self.is_description_hidden():
            return False
        self.description_hidden = True
        self.description.target.set_fill(opacity = 0.0)
        self.description.target.set_stroke(opacity = 0.0)
        return True

    def display_description(self):
        if not self.is_description_hidden():
            return False
        self.description_hidden = False
        self.description.target.set_fill(opacity = self.all_old_opacity[7])
        self.description.target.set_stroke(opacity = self.all_old_opacity[8])
        return True
