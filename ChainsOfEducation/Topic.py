import manim
import ComplexArrow
import Tip
import TopicBlock


TOPICS: dict = {"Осознанность": ["Что это такое?",
                                 "Несколько\nспециальных методов"],
                }

DEACTIVATED_PROPORTION: float = 0.3


class Topic(manim.VGroup):
    """Topic"""

    def __init__(self, *vmobjects, **kwargs):
        super().__init__(*vmobjects, **kwargs)

        xv = [-6.0, -3.0, 0.0, 3.0, 6.0]
        yv = [3.0, 2.8, 3.0, 2.8, 3.0]
        coords = [(x, y, 0.0) for x, y in zip(xv, yv)]
        self.topic_line = ComplexArrow.ComplexArrow(
            coords,
            Tip.EllipseTip(),
            Tip.EllipseTip().set_shift_anchors(-0.5, -0.5))

        self.selected_tb = None
        self.make_topic_blocks()

    def get_creating_anim_1(self):
        self.topic_line.prepare_to_create_1()
        return self.topic_line.get_creating_anim_1()

    def get_creating_anim_2(self):
        self.topic_line.prepare_to_create_2()
        anims: list = []
        for topic_block in self.topic_blocks:
            topic_block.prepare_to_create()
            anims.append(topic_block.get_creating_anim())
        anims = manim.AnimationGroup(*anims, lag_ratio = 0.1)
        return manim.AnimationGroup(
            self.topic_line.get_creating_anim_2(), anims, lag_ratio = 0.3)

    def get_fade_anim(self, scene):
        for topic_block in self.topic_blocks:
            self.add(topic_block)
            topic_block.prepare_to_destroy()
        for br in self.selected_tb.get_all_briefs_texts():
            self.selected_tb.add(br)
        self.add(self.topic_line)
        scene.camera.frame.generate_target()
        scene.camera.frame.target.move_to(
            self.selected_tb).set(width = self.selected_tb.width * 0.5)
        return manim.AnimationGroup(
            manim.FadeOut(self), manim.MoveToTarget(scene.camera.frame))

    def make_topic_blocks(self):
        self.topic_blocks: list = []
        pos_pp: float = 1.0 / (len(TOPICS) + 1.0)
        curr = 0
        for tb in TOPICS:
            pos = self.topic_line.point_from_proportion(pos_pp * (1 + curr))
            topic_block = TopicBlock.TopicBlock(tb, TOPICS[tb]).move_to(
                pos + 1.8 * manim.DOWN).scale(DEACTIVATED_PROPORTION)
            topic_block.set_ordinary_chain(pos)
            self.topic_blocks.append(topic_block)
            curr += 1

    def after_create(self):
        self.topic_line.after_create()
        for topic_block in self.topic_blocks:
            topic_block.after_create()

    def select_topic_block(self, n):
        self.selected_tb = self.topic_blocks[n]
        self.selected_tb.generate_target()
        self.selected_tb.target.move_to(manim.ORIGIN).scale(
            1.0 / DEACTIVATED_PROPORTION)
        self.selected_tb.target.activate()
        return manim.MoveToTarget(self.selected_tb)

    def show_briefs(self):
        anims = [self.selected_tb.prepare_to_briefs()]
        for _ in range(len(self.selected_tb.get_all_briefs_dots())):
            anims.append(self.selected_tb.show_next_brief())
        return anims
