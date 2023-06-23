﻿import manim
import Block
import KnowledgeBlock as KB
import random


class ChainsOfEducation(manim.Scene):
    def construct(self):
        grid = manim.NumberPlane()
        self.kb = KB.KnowledgeBlock("Хи́мия!", '''
        Хи́мия - одна из 
        важнейших и обширных областей естествознания,
        наука, изучающая вещества, также их состав и
        строение, их свойства, зависящие от состава и
        строения, их превращения, ведущие к изменению
        состава.'''
        ).move_to(3.0 * manim.LEFT).scale(0.7)
        kb2 = KB.KnowledgeBlock("Биоло́гия!", '''
        Биоло́гия (греч. βιολογία; от др.-греч.
        βίος «жизнь» + λόγος «учение, наука»[1]) —
        наука о живых существах и их взаимодействии со
        средой обитания. Изучает все аспекты жизни,
        в частности''').move_to(3.0 * manim.RIGHT)
        self.ccountt = 0
        self.debug_group = manim.Group()

        self.add(self.kb, kb2, grid, self.debug_group)

        self.add_one_into_other(kb2, self.kb)
        for _ in range(1):
            self.add_blocks(self.kb, 5)
            self.add_blocks(kb2, 5)
            self.remove_blocks(kb2, 4)
            self.remove_blocks(self.kb)
        self.wait(1.0)

    def debug_def(self):
        self.kb.title.generate_target()
        self.kb.title.target = manim.Text(
            str(self.ccountt),
            font_size = self.kb.title.font_size,
            weight = manim.BOLD)
        self.kb.title.target.move_to(self.kb)
        self.play(manim.MoveToTarget(self.kb.title))
        self.show_debug()

    def show_debug(self):
        self.remove(self.debug_group)
        self.debug_group = manim.Group(
            manim.Text(str(self.kb.title.font_size)),
            manim.Text(str(self.ccountt)))
        self.add(self.debug_group.arrange(
            manim.DOWN).scale(0.3).move_to(3.0 * manim.UR))
        self.ccountt += 1

    def random_scale_move(self, b: Block.Block, num = 1, anim = True):
        if anim:
            for _ in range(num):
                b.generate_target()
                self.scale_random(b.target)
                self.move_random(b.target)
                b.update_size(self.my_scl)
                b.set_center(self.my_pos_x * manim.RIGHT + self.my_pos_y * manim.UP)
                self.play(manim.MoveToTarget(b))
                self.wait()
        else:
            self.scale_random(b)
            self.move_random(b)

    def add_blocks(self, b: Block.Block, num: int = 1):
        for i in range(num):
            kbi = KB.KnowledgeBlock(
                str(i), str(i) * 10 + " th KnowledgeBlock")
            self.random_scale_move(kbi, anim = False)
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
        self.remove(one)
        for subb in one.get_all_subbs():
            self.remove(subb)
        self.update_b(other)

    def update_b(self, b: Block.Block):
        b.make_finish_target()
        self.play(b.get_animations_to_play())
        self.wait()

    def move_random(self, b: Block.Block):
        self.my_pos_x = (random.random() - 0.5) * 6.0
        self.my_pos_y = (random.random() - 0.5) * 3.0
        b.move_to(self.my_pos_x * manim.RIGHT + self.my_pos_y * manim.UP)

    def scale_random(self, b: Block.Block):
        self.my_scl = 1.0 + (random.random() - 0.5) * 0.6
        b.scale(self.my_scl)

    def wait(self, duration: float = 0.25, **kwargs):
        super().wait(duration, **kwargs)

"""
cd /d D:\My\LTTDIT\Python\ChainsOfEducation\ChainsOfEducation
manim -pql --disable_caching ChainsOfEducation.py ChainsOfEducation
manim -pqh --disable_caching ChainsOfEducation.py ChainsOfEducation
"""
