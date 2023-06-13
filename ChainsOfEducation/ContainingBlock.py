import manim
import Block


class ContainingBlock(Block.Block):
    """Class for fourth and next subblocks of KnowledgeBlock"""

    def __init__(self, **kwargs):
        super().__init__("0", **kwargs)

        self.set_normal_title()
        self.title_underline = manim.Underline(self.title)

    def add(self, *mobjects):
        return

    def remove(self, *mobjects):
        return

    def get_subb_info_to_update(self):
        return

    def get_subb_scale(self, index: int):
        return

    def get_subb_pos(self, index: int):
        return

    def get_all_subbs(self):
        return

    def set_normal_title(self):
        super().set_normal_title()
        self.title.move_to(self)
