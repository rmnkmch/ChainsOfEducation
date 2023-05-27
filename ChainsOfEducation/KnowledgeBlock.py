import manim


class KnowledgeBlock(manim.RoundedRectangle):
    """Base class for all blocks of knowledge"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        title = manim.Text()
        self.add(title)
