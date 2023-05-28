import manim


class KnowledgeBlock(manim.RoundedRectangle):
    """Base class for all blocks of knowledge"""

    def __init__(self, **kwargs):
        super().__init__(
            height=5.0,
            width=10.0,
            **kwargs)

        self.title = manim.Text(
            "Knowledge Block Title",
            weight=manim.BOLD,
            )
        self.set_normal_title_size()
        self.description = manim.Text(
            "Knowledge Block Description\n1 2 3 4 5 6 7 8 9",
            font_size=24,
            )
        #self.set_normal_description_size()
        self.split_description_lines()

        self.add(self.title, self.description)

    def set_normal_title_size(self):
        while ((self.title.width > self.width - 0.5) and
               (self.title.font_size >= 20)):
            self.title.font_size -= 1
        self.title.next_to(self, manim.UP, -self.title.height - 0.25)

    def set_normal_description_size(self):
        while ((self.description.width > self.width - 0.5) and
               (self.description.font_size >= 14)):
            self.description.font_size -= 1
        self.description.next_to(self, manim.DOWN, -self.description.height - 0.25)

    def split_description_lines(self):
        print(self.description.text)#already splited?
        all_text = self.description.text.split()
        print(all_text)
        ret_text = ""
        for str in all_text:
            ret_text = str + "\n"
        self.description = manim.Text(ret_text, font_size=24)
        self.description.next_to(self, manim.DOWN, -self.description.height - 0.25)
