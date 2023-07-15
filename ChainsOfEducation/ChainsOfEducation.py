import manim
import Block
import KnowledgeBlock as KB
import random
import SQLDatabase
import ComplexArrow
import TopicBlock
import Chain


FAST_RUN_TIME: float = 0.1


class ChainsOfEducation(manim.Scene):
    def construct(self):
        self.chapter_1()

    def load_all(self):
        self.sql_db = SQLDatabase.SQLDatabase()
        self.sql_db.create_connection(r"SQLData\KnowledgeBlocks.sqlite")
        self.sql_db.execute_query(self.sql_db.create_table_query())
        ret = self.sql_db.execute_read_query(r"SELECT * FROM KnowledgeBlocks")
        if ret is not None:
            for text in ret:
                print(text)

    def save_all(self):
        self.save_kb(self.kb)
        self.sql_db.close_connection()

    def save_kb(self, kb: KB.KnowledgeBlock):
        if (self.sql_db.execute_read_query(
            f"SELECT * FROM KnowledgeBlocks WHERE title = '{kb.title.text}'")
            is None):
            self.sql_db.execute_query(
                self.sql_db.create_KB_query(kb.title.text, kb.description.text))

    def random_scale_move_fill(self, b: Block.Block, num = 1, anim = True):
        if anim:
            for _ in range(num):
                b.generate_target()
                self.scale_random(b, anim)
                self.move_random(b, anim)
                self.fill_random(b, anim)
                self.update_b(b, False)
        else:
            self.scale_random(b, anim)
            self.move_random(b, anim)
            self.fill_random(b, anim)

    def add_blocks(self, b: Block.Block, num: int = 1):
        for i in range(num):
            kbi = KB.KnowledgeBlock(
                str(i), str(i) * 10 + " th KnowledgeBlock")
            self.random_scale_move_fill(kbi, anim = False)
            self.fill_random(kbi, anim = False)
            self.add_one_into_other(kbi, b)

    def remove_blocks(self, b: Block.Block, num: int = 10):
        for kbi in b.get_all_subbs():
            self.remove_one_outof_other(kbi, b)
            num -= 1
            if num <= 0: break

    def add_one_into_other(self,
                           one: Block.Block,
                           other: Block.Block):
        other.add_subb(one)
        self.update_b(other)

    def remove_one_outof_other(self,
                               one: Block.Block,
                               other: Block.Block):
        other.remove_subb(one)
        for subb in one.get_all_subbs():
            self.remove(subb)
        self.remove(one)
        self.update_b(other)

    def update_b(self, b: Block.Block, gen_tar = True, fast = False,
                 other_animations = None):
        if gen_tar:
            b.generate_target()
        b.make_finish_target()
        if other_animations is None:
            if fast:
                self.play(b.get_animations_to_play().set_run_time(FAST_RUN_TIME))
            else:
                self.play(b.get_animations_to_play())
                self.wait()
        else:
            if fast:
                self.play(manim.AnimationGroup(
                    b.get_animations_to_play(), other_animations,
                    run_time = FAST_RUN_TIME))
            else:
                self.play(manim.AnimationGroup(
                    b.get_animations_to_play(), other_animations))
                self.wait()

    def fill_random(self, b: Block.Block, anim = True):
        my_color = "#" + str((random.random() * 1000000.0).__ceil__())
        while len(my_color) != 7:
            my_color = "#" + str((random.random() * 1000000.0).__ceil__())
        my_opacity = random.random() * 0.8
        if anim:
            b.target.set_fill(my_color, my_opacity)
        else:
            b.set_fill(my_color, my_opacity)

    def move_random(self, b: Block.Block, anim = True):
        my_pos_x = (random.random() - 0.5) * 6.0
        my_pos_y = (random.random() - 0.5) * 3.0
        if anim:
            b.target.move_to(my_pos_x * manim.RIGHT + my_pos_y * manim.UP)
        else:
            b.move_to_outside(my_pos_x * manim.RIGHT + my_pos_y * manim.UP)

    def scale_random(self, b: Block.Block, anim = True):
        my_scl = 1.0 + (random.random() - 0.5) * 0.6
        if anim:
            b.target.scale(my_scl)
        else:
            b.scale_outside(my_scl)

    def wait(self, duration: float = 0.2, **kwargs):
        super().wait(duration, **kwargs)

    def add(self, *mobjects: manim.Mobject):
        super().add(*mobjects)
        for b in mobjects:
            if isinstance(b, KB.KnowledgeBlock):
                self.add(b.containing_b, b.description, b.ellipsis_b)

    def remove(self, *mobjects: manim.Mobject):
        super().remove(*mobjects)
        for b in mobjects:
            if isinstance(b, KB.KnowledgeBlock):
                self.remove(b.containing_b, b.description, b.ellipsis_b)

    def create_kb_no_descr(self, kb: KB.KnowledgeBlock, fast = False):
        kb.save_description_opacity()
        kb.hide_description(False)
        if fast:
            self.play(manim.Create(kb, run_time = FAST_RUN_TIME))
        else:
            self.play(manim.Create(kb, lag_ratio = 0.05, run_time = 5.0))
            self.wait()

    def write_text(self, text, fast = False):
        if fast:
            self.play(manim.Write(text, run_time = FAST_RUN_TIME))
        else:
            self.play(manim.Write(text, run_time = 3.0))
            self.wait()

    def unwrite_text(self, text, fast = False):
        if fast:
            self.play(manim.Unwrite(text, run_time = FAST_RUN_TIME,
                                    reverse = False))
        else:
            self.play(manim.Unwrite(text, run_time = 3.0, reverse = False))
            self.wait()

    def creating_topics_anims(self, topics: manim.VGroup, fast = False):
        if fast:
            animationGroup = manim.AnimationGroup()
            for topic in topics:
                for brief in topic.get_all_briefs_dots():
                    animationGroup = manim.AnimationGroup(
                        animationGroup,
                        manim.Create(brief, run_time = FAST_RUN_TIME))
                animationGroup = (manim.AnimationGroup(
                    animationGroup, manim.Create(topic, run_time = FAST_RUN_TIME)))
            return animationGroup
        else:
            animationGroup = manim.AnimationGroup(rate_func = manim.linear)
            for topic in topics:
                for brief in topic.get_all_briefs_dots():
                    animationGroup = manim.AnimationGroup(
                        animationGroup, manim.Create(brief),
                        lag_ratio = 1.0, rate_func = manim.linear)
                animationGroup = manim.AnimationGroup(
                    manim.Create(topic, lag_ratio = 0.05, run_time = 1.0),
                    animationGroup, lag_ratio = 1.0, rate_func = manim.linear)
            return animationGroup

    r"""
cd /d D:\My\LTTDIT\Python\ChainsOfEducation\ChainsOfEducation
manim -pql --disable_caching ChainsOfEducation.py ChainsOfEducation
manim -pql ChainsOfEducation.py ChainsOfEducation
manim -pqh --disable_caching ChainsOfEducation.py ChainsOfEducation
manim -pqh ChainsOfEducation.py ChainsOfEducation
    """

    def chapter_1(self):
        def get_start_chain(i):
            return manim.UP * y_values[i + 1] + manim.RIGHT * x_values[i + 1]

        def get_end_chain(i):
            return grp[i].get_all_points()[0]

        def get_start_chain_func(n):
            return lambda: get_start_chain(n)

        def get_end_chain_func(n):
            return lambda: get_end_chain(n)

        fast_1 = True
        fast_2 = False
        intro_text = manim.Text("Ну что ж ...")
        self.write_text(intro_text, fast_1)
        self.unwrite_text(intro_text, fast_1)
        x_values = [-7, -3, 1, 5, 7]
        y_values = [0, 0, 0, 0, 0]
        coords = [(x, y, 0.0) for x, y in zip(x_values, y_values)]
        for plots in coords:
            self.add(manim.Dot(plots))
        arrow = ComplexArrow.ComplexArrow(coords)
        anim_1 = ChainsOfEducation.MyMoveAlongPath(
            arrow.end_tip, arrow.copy(), run_time = 3.0)
        anim_2 = manim.Create(arrow, run_time = 3.0)
        anim_3 = manim.AnimationGroup(anim_1, anim_2)
        tb_1 = TopicBlock.TopicBlock("???").move_to(
            2.0 * manim.UP + 5.0 * manim.LEFT).scale(0.4)
        tb_2 = TopicBlock.TopicBlock("???").move_to(
            2.0 * manim.DOWN + 1.0 * manim.LEFT).scale(0.4)
        tb_3 = TopicBlock.TopicBlock("???").move_to(
            2.0 * manim.UP + 3.0 * manim.RIGHT).scale(0.4)
        grp = manim.VGroup(tb_1, tb_2, tb_3)
        anims = manim.AnimationGroup(rate_func = manim.linear)
        for i in range(len(grp)):
            anims = manim.AnimationGroup(
                anims,
                manim.AnimationGroup(
                    manim.Create(Chain.Chain(
                        get_start_chain_func(i),
                        get_end_chain_func(i))),
                    self.creating_topics_anims(manim.VGroup(grp[i]), fast_2),
                    lag_ratio = 1.0, rate_func = manim.linear),
                lag_ratio = 0.4, rate_func = manim.linear)
        played = manim.AnimationGroup(anim_3, anims,
                                      lag_ratio = 0.3, rate_func = manim.linear)
        self.play(played)
        self.play(grp.animate.scale(2.0).shift(manim.DOWN))
        
        #self.play(tb_1.prepare_to_briefs())
        #for _ in range(len(tb_1.get_all_briefs_dots())):
            #self.play(tb_1.show_next_brief())
        kb_1 = KB.KnowledgeBlock("Осознанность!", '''
        Очень сильный и важный инструмент.''')
        kb_1.move_to_outside(manim.LEFT)
        kb_1.scale_outside(1.4)
        #self.create_kb_no_descr(kb_1, fast_1)
        #self.update_b(kb_1, fast = fast_1)
        kb_1.generate_target()
        #kb_1.target.move_to(manim.UP * 7.0)
        #self.update_b(kb_1, False, fast_1)
        text_1 = manim.Text("""Любые суждения или мысли кажутся непонятными
        и автоматически бессмысленными, если у нас нет
        достаточного основания для их понимания.""")
        self.wait(1.0)

    def test_1(self):
        self.wait(1.0)

    class MyMoveAlongPath(manim.Animation):
        def __init__(
            self,
            mobject: manim.Mobject,
            path: manim.VMobject,
            suspend_mobject_updating: bool | None = False,
            **kwargs) -> None:
            self.path = path
            self.previous_pos = self.path.point_from_proportion(0.0)
            self.previous_angle = 0.0
            super().__init__(
                mobject,
                suspend_mobject_updating = suspend_mobject_updating,
                **kwargs)

        def interpolate_mobject(self, alpha: float) -> None:
            pos = self.path.point_from_proportion(self.rate_func(alpha))
            self.mobject.move_to(pos)
            diff_pos = pos - self.previous_pos
            if abs(diff_pos[0]) >= 0.001 and abs(diff_pos[1]) >= 0.001:
                from math import atan
                self.previous_pos = pos
                angle = 0.0
                if diff_pos[0] > 0.0 and diff_pos[1] > 0.0:
                    angle = atan(diff_pos[1] / diff_pos[0])
                elif diff_pos[0] > 0.0 and diff_pos[1] < 0.0:
                    angle = 2.0 * manim.PI - atan(abs(diff_pos[1] / diff_pos[0]))
                elif diff_pos[0] < 0.0 and diff_pos[1] > 0.0:
                    angle = manim.PI - atan(abs(diff_pos[1] / diff_pos[0]))
                else:
                    angle = manim.PI + atan(abs(diff_pos[1] / diff_pos[0]))
                diff_angle = angle - self.previous_angle
                self.previous_angle = angle
                self.mobject.rotate(diff_angle)
