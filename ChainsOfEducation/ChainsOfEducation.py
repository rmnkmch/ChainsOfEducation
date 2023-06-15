import manim
import Block
import KnowledgeBlock as KB


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
        ).move_to(4.0 * manim.LEFT).scale(0.8)
        kb2 = KB.KnowledgeBlock("Биоло́гия!", '''
        Биоло́гия (греч. βιολογία; от др.-греч.
        βίος «жизнь» + λόγος «учение, наука»[1]) —
        наука о живых существах и их взаимодействии со
        средой обитания. Изучает все аспекты жизни,
        в частности''').move_to(3.0 * manim.RIGHT)
        self.add(kb, kb2, grid)
        self.add_one_into_other(kb2, kb)
        for i in range(3):
            kbi = KB.KnowledgeBlock(str(i) * 10, '''
            Биаивсе аспекты жизнив частности''').move_to(1.0 * manim.RIGHT)
            self.add_one_into_other(kbi, kb)
        for i in range(3):
            kbi = KB.KnowledgeBlock(str(i) * 20, '''
            Биаиности''').move_to(1.0 * manim.LEFT)
            self.add_one_into_other(kbi, kb2)
        kb.make_target_be_hidden()
        self.play(manim.MoveToTarget(kb))
        kb.make_target_be_displayed()
        self.play(manim.MoveToTarget(kb))
        self.wait()

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

    def get_update_description_animation(self, kb: KB.KnowledgeBlock):
        all_info = kb.get_description_info_to_update()
        all_animations = manim.AnimationGroup()
        for description_info in all_info:
            description_info[0].generate_target()
            description_info[0].target = manim.Text(
                description_info[1],
                font_size = KB.DEFAULT_DESCRIPTION_FONT_SIZE)
            description_info[0].target.scale(
                description_info[2] * description_info[0].font_size
                / description_info[0].target.font_size).move_to(
                    description_info[3])
            all_animations = manim.AnimationGroup(
                all_animations, manim.MoveToTarget(description_info[0]))
        return all_animations

    def update_b(self, b):
        b.prepare_target()
        b.make_finish_target()
        self.play(manim.MoveToTarget(b))
        self.wait()

#cd /d D:\My\LTTDIT\Python\ChainsOfEducation\ChainsOfEducation
#manim  -pql ChainsOfEducation.py ChainsOfEducation
#--disable_caching
