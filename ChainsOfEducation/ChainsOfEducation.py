import manim
import Block
import KnowledgeBlock as KB
import random


class ChainsOfEducation(manim.Scene):
    def construct(self):
        grid = manim.NumberPlane()
        kb = KB.KnowledgeBlock("Хи́мия!", '''
        Хи́мия - одна из 
        важнейших и обширных областей естествознания,
        наука, изучающая вещества, также их состав и
        строение, их свойства, зависящие от состава и
        строения, их превращения, ведущие к изменению
        состава.'''
        ).move_to(4.0 * manim.LEFT).scale(0.5)
        kb2 = KB.KnowledgeBlock("Биоло́гия!", '''
        Биоло́гия (греч. βιολογία; от др.-греч.
        βίος «жизнь» + λόγος «учение, наука»[1]) —
        наука о живых существах и их взаимодействии со
        средой обитания. Изучает все аспекты жизни,
        в частности''').move_to(3.0 * manim.RIGHT)
        self.ccount = 0
        self.info_group = manim.Group()
        self.info_move = manim.Group()
        self.scale_info = manim.Text("?")
        self.add(kb, kb2, grid, self.info_group, self.info_move)
        for i in range(0):
            kb.generate_target()
            self.move_random(kb.target)
            self.scale_random(kb.target)
            self.show_info(kb)
            self.play(manim.MoveToTarget(kb))
            self.show_info(kb)
            kb.update_size(self.my_scl)
            kb.set_center(self.my_pos_x * manim.RIGHT + self.my_pos_y * manim.UP)
            self.show_info(kb)
        kb.add(kb2)
        kb.generate_target()
        kb.correct_subblocks_info()
        kb.target.correct_subblocks()
        kb.description.generate_target()
        kb.description.target = manim.Text("?")
        self.play(manim.MoveToTarget(kb), manim.MoveToTarget(kb.description))
        self.show_info(kb)
        self.show_info(kb.target)
        self.show_info(kb2)
        """for i in range(1):
            kbi = KB.KnowledgeBlock(str(i) * 10, '''
            Биаивсе аспекты жизнив частности''').move_to(i * manim.RIGHT)
            self.add_one_into_other(kbi, kb)
        for i in range(1):
            kbi = KB.KnowledgeBlock(str(i) * 20, '''
            Биаиности''').move_to(i * manim.LEFT)
            self.add_one_into_other(kbi, kb2)"""

    def add_one_into_other(self,
                           one: Block.Block,
                           other: Block.Block):
        other.add(one)
        self.update_b(other)

    def remove_one_outof_other(self,
                               one: Block.Block,
                               other: Block.Block):
        other.remove(one)
        self.remove(one)
        self.update_b(other)

    def update_b(self, b: Block.Block):
        b.make_finish_target()
        self.play(b.get_animations_to_play())
        self.wait()
        #b.build_description()

    def show_info(self, b: Block.Block):
        self.remove(self.info_group)
        self.ccount += 1
        self.b_width_info = manim.Text(str(b.b_width))
        self.width_info = manim.Text(str(b.width))
        self.b_center_info = manim.Text(str(b.get_center()))
        self.not_my_center_info = manim.Text(str(b.get_not_my_center()))
        self.proportion_info = manim.Text(str(b.get_proportion()))
        self.counnt = manim.Text(str(self.ccount))
        self.info_group = manim.Group(self.b_width_info, self.width_info,
                                      self.b_center_info, self.not_my_center_info,
                                     self.proportion_info, self.counnt)
        self.add(self.info_group.arrange(manim.DOWN).move_to(
            4.5 * manim.LEFT + 2.0 * manim.UP).scale(0.4))
        self.wait()

    def move_random(self, b: Block.Block):
        self.my_pos_x = (random.random() - 0.5) * 5.0
        self.my_pos_y = (random.random() - 0.5) * 2.5
        b.move_to(self.my_pos_x * manim.RIGHT + self.my_pos_y * manim.UP)
        self.remove(self.info_move)
        self.pos_x_info = manim.Text(str(self.my_pos_x))
        self.pos_y_info = manim.Text(str(self.my_pos_y))
        self.info_move = manim.Group(self.pos_x_info, self.pos_y_info)
        self.add(self.info_move.arrange(manim.DOWN).move_to(
            4.5 * manim.RIGHT + 2.5 * manim.UP).scale(0.4))

    def scale_random(self, b: Block.Block):
        self.my_scl = 1.0 + (random.random() - 0.5) * 0.5
        b.scale(self.my_scl)
        self.remove(self.scale_info)
        self.scale_info = manim.Text(str(self.my_scl))
        self.add(self.scale_info.move_to(
            4.5 * manim.RIGHT + 2.5 * manim.DOWN).scale(0.4))

        

#cd /d D:\My\LTTDIT\Python\ChainsOfEducation\ChainsOfEducation
#manim  -pql ChainsOfEducation.py ChainsOfEducation
#--disable_caching
