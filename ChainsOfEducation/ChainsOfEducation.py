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
        for i in range(1):
            kbi = KB.KnowledgeBlock(str(i) * 10, '''
            Биаивсе аспекты жизнив частности''').move_to(i * manim.RIGHT)
            self.add_one_into_other(kbi, kb)
        for i in range(1):
            kbi = KB.KnowledgeBlock(str(i) * 20, '''
            Биаиности''').move_to(i * manim.LEFT)
            self.add_one_into_other(kbi, kb2)

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

#cd /d D:\My\LTTDIT\Python\ChainsOfEducation\ChainsOfEducation
#manim  -pql ChainsOfEducation.py ChainsOfEducation
#--disable_caching
