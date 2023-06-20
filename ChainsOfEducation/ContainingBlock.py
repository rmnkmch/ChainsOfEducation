import manim
import Block


class ContainingBlock(Block.Block):
    """Class for fourth and next subblocks of KnowledgeBlock"""

    def __init__(self, title: str = "0", **kwargs):
        super().__init__(title, **kwargs)
        self.save_all_opacity()
        self.hide()

    def make_finish_target(self):
        return

    def correct_subblocks_info(self):
        return

    def correct_subblocks(self):
        return

    def get_subb_scale(self, index: int):
        return

    def get_subb_pos(self, index: int):
        return

    def get_all_subbs(self):
        return []

    def set_normal_title(self):
        super().set_normal_title()
        self.title.scale(5.0).move_to(self)
