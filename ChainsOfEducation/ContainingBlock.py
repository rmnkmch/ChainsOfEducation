import Block


class ContainingBlock(Block.Block):
    """Class for fourth and next subblocks of KnowledgeBlock"""

    def __init__(self, title: str = "0", **kwargs):
        super().__init__(title, **kwargs)
        self.save_all_opacity()
        self.hide()

    def set_normal_title(self):
        super().set_normal_title()
        self.title.scale(5.0).move_to(self)
