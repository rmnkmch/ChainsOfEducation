import manim
import Block
import ContainingBlock


DEFAULT_DESCRIPTION_FONT_SIZE: float = 12.0#32.0
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

        self.description = manim.Text(
            description,
            font_size = DEFAULT_DESCRIPTION_FONT_SIZE)
        self.build_description()

        self.containing_b = ContainingBlock.ContainingBlock()

        self.add(self.description, self.containing_b)

    def update_size(self, scale_factor: float):
        super().update_size(scale_factor)
        self.containing_b.update_size(scale_factor)

    def set_center(self, new_center):
        super().set_center(new_center)
        self.containing_b.set_center(new_center)

    def get_animations_to_play(self):
        return manim.AnimationGroup(super().get_animations_to_play(),
                                    #manim.MoveToTarget(self.description),
                                    manim.MoveToTarget(self.containing_b.title))

    def make_finish_target(self):
        super().make_finish_target()
        #self.description.generate_target()
        #text_and_size = self.get_correct_description_text_and_size()
        #self.description.target = manim.Text(
            #text_and_size[0], font_size = self.description.font_size)
        #self.description.target.scale(text_and_size[1])
        #self.description.target.move_to(self.get_description_correct_position())
        self.containing_b.title.generate_target()
        self.containing_b.title.target = manim.Text(
            str(len(self.get_all_subbs())),
            font_size = self.containing_b.title.font_size,
            weight = manim.BOLD)
        self.containing_b.title.target.scale(1.0).move_to(self.containing_b)

    def correct_subblocks_info(self):
        super().correct_subblocks_info()
        self.containing_b.update_size(
            self.get_subb_scale(3) / self.containing_b.b_width)
        self.containing_b.set_center(self.get_subb_pos(0, True))
        if not self.containing_b.is_clear():
            self.containing_b.update_size(
                self.get_subb_scale(0, True) / self.containing_b.b_width)
            self.containing_b.hidden = False
        else:
            if len(self.get_all_subbs()) >= 5:
                self.containing_b.set_center(self.get_subb_pos(3))
                self.containing_b.hidden = False
            else:
                #self.containing_b.save_all_opacity()???
                self.containing_b.hidden = True

    def correct_subblocks(self):
        super().correct_subblocks()
        self.containing_b.scale(
            self.get_subb_scale(3) / self.containing_b.b_width
            ).move_to(self.get_subb_pos(0, True))
        if not self.containing_b.is_clear():
            self.containing_b.scale(
                self.get_subb_scale(0, True) / self.containing_b.b_width)
            self.containing_b.display()
        else:
            if len(self.get_all_subbs()) >= 5:
                self.containing_b.move_to(self.get_subb_pos(3))
                self.containing_b.display()
            else:
                self.containing_b.hide()

    def get_all_subbs(self):
        ret_list = []
        for b in super().get_all_subbs():
            if not isinstance(b, ContainingBlock.ContainingBlock):
                ret_list.append(b)
        return ret_list

    def is_description_clear(self, descr: manim.Text):
        return descr.font_size > MIN_DESCRIPTION_FONT_SIZE

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
            correct_text = self.get_splited_description_text(
                new_description.font_size)
        while not self.is_acceptable_description_width(new_description):
            new_description.scale(0.9)
            scale_factor *= 0.9
        return (correct_text, scale_factor)

    def get_splited_description_text(
        self, new_font_size: float = DEFAULT_DESCRIPTION_FONT_SIZE):
        def is_there_another_word():
            return current_word_index < len_all_text

        all_text: list[str] = self.description.original_text.split()
        len_all_text = len(all_text)
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
        if super().save_all_opacity():
            self.all_old_opacity.append(self.description.get_fill_opacity())
            self.all_old_opacity.append(self.description.get_stroke_opacity())
            return True
        return False

    def hide(self):
        if super().hide():
            self.description.set_fill(opacity = 0.0)
            self.description.set_stroke(opacity = 0.0)
            return True
        return False

    def display(self):
        if super().display():
            self.description.set_fill(opacity = self.all_old_opacity[6])
            self.description.set_stroke(opacity = self.all_old_opacity[7])
            return True
        return False
