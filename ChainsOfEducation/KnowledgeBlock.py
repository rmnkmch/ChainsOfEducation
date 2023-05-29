import manim


MIN_DESCRIPTION_FONT_SIZE: float = 10.0
DEFAULT_DESCRIPTION_FONT_SIZE: float = 30.0
MIN_TITLE_FONT_SIZE: float = 16.0
DEFAULT_TITLE_FONT_SIZE: float = 48.0


class KnowledgeBlock(manim.RoundedRectangle):
    """Base class for all blocks of knowledge"""

    def __init__(self, **kwargs):
        super().__init__(
            height=5.0,
            width=10.0,
            **kwargs)

        self.title = manim.Text(
            "KnowledgeBlockTitle",
            font_size=DEFAULT_TITLE_FONT_SIZE,
            weight=manim.BOLD,
            )
        self.set_normal_title_size()
        self.description = manim.Text(
            '''Матема́тика (др.-греч. μᾰθημᾰτικά[1] < μάθημα «изучение; наука») —
            точная формальная наука[2], первоначально исследовавшая
            количественные отношения и пространственные
            формы[3]. В более современном понимании, это наука об отношениях
            между объектами, о которых ничего не известно,
            кроме описывающих их некоторых свойств, — именно тех, которые
            в качестве аксиом положены в основание той или иной
            математической теории[4].
            Математика исторически сложилась на основе операций подсчёта,
            измерения и описания формы объектов[5]. Математические
            объекты создаются путём идеализации свойств реальных или
            других математических объектов и записи этих свойств на
            формальном языке.
            Математика не относится к естественным наукам, но широко
            используется в них как для точной формулировки их содержания,
            так и для получения новых результатов. Она является
            фундаментальной наукой, предоставляющей (общие) языковые
            средства другим наукам; тем самым она выявляет их
            структурную взаимосвязь и способствует нахождению самых
            общих законов природы[6].''',
            font_size=DEFAULT_DESCRIPTION_FONT_SIZE,
            )
        self.set_normal_description_size()
        self.split_description_lines()

        self.add(self.title, self.description)

    def is_unacceptable_width(self, text: manim.Text):
        return self.width - 0.5 <= text.width

    def set_normal_title_size(self):
        while (self.is_unacceptable_width(self.title) and
               self.title.font_size > MIN_TITLE_FONT_SIZE):
            self.title.font_size -= 1
        self.title.next_to(self, manim.UP, -self.title.height - 0.25)

    def set_normal_description_size(self):
        while (self.is_unacceptable_width(self.description) and
               self.description.font_size > MIN_DESCRIPTION_FONT_SIZE):
            self.description.font_size -= 1
        self.description.next_to(self, manim.DOWN, -self.description.height - 0.25)

    def split_description_lines(self):

        def is_there_another_word():
            return current_word_index < len(all_text)

        all_text = self.description.original_text.split()
        splited_text = ""
        current_word_index = 0
        while is_there_another_word():
            current_str = all_text[current_word_index]
            current_word_index += 1
            while (is_there_another_word() and
                   manim.Text(
                       current_str + " " + all_text[current_word_index],
                       font_size=self.description.font_size,
                       ).width < self.width - 0.5):
                current_str += " " + all_text[current_word_index]
                current_word_index += 1
            splited_text += current_str
            if is_there_another_word():
                splited_text += "\n"

        self.description = manim.Text(
            splited_text,
            font_size=self.description.font_size)
        self.description.next_to(self, manim.DOWN, -self.description.height - 0.25)
