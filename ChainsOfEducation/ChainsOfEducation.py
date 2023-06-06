import manim
import KnowledgeBlock as KB


class ChainsOfEducation(manim.Scene):
    def construct(self):
        grid = manim.NumberPlane()
        grid.stroke_opacity = 0.01
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
        self.wait()
        self.add_one_kb_into_other(kb2, kb)
        self.wait()
        for i in range(0):
            self.play(self.get_move_kb_with_scale_to_animation(kb))
            self.wait()
        self.play(self.get_move_kb_with_scale_to_animation(
            kb, 1.5, manim.ORIGIN))
        self.wait()
        manim.FadeOut

    def add_one_kb_into_other(self,
                              one: KB.KnowledgeBlock,
                              other: KB.KnowledgeBlock):
        other.add(one)
        self.update_kb(other)

    def remove_one_kb_outof_other(self,
                                  one: KB.KnowledgeBlock,
                                  other: KB.KnowledgeBlock):
        other.remove(one)
        self.remove(one)
        self.update_kb(other)

    def get_move_kb_with_scale_to_animation(self,
                                            kb: KB.KnowledgeBlock,
                                            scale_factor: float = 1.0,
                                            position = None):
        if position is None:
            position = kb.get_center()
        kb.update_size(scale_factor)
        kb.set_center(position)
        kb.generate_target()
        kb.target.scale(scale_factor).move_to(position)
        return manim.MoveToTarget(kb)

    def get_update_subkbs_animations(self, kb: KB.KnowledgeBlock):
        all_info = kb.get_subkb_info_to_update()
        all_animations = manim.AnimationGroup()
        for subkb_info in all_info:
            all_animations = manim.AnimationGroup(
                all_animations, self.get_move_kb_with_scale_to_animation(
                    subkb_info[0], subkb_info[1], subkb_info[2]))
        return all_animations

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

    def update_kb(self, kb: KB.KnowledgeBlock):
        kb.generate_target()#TODO remove MoveToTarget
        self.play(manim.AnimationGroup(
            manim.MoveToTarget(kb),
            self.get_update_description_animation(kb),
            self.get_update_subkbs_animations(kb),
            lag_ratio = 0.3))

#cd /d D:\My\LTTDIT\Python\ChainsOfEducation\ChainsOfEducation
#manim  -pql ChainsOfEducation.py ChainsOfEducation
#--disable_caching
"""
for i in range(2):
            kbi = KB.KnowledgeBlock(str(i), str(i) * 20).move_to(
                i * manim.LEFT + 3.0 * manim.RIGHT).scale(0.6 + i * 0.1)
            self.add(kbi)
            self.wait()
            self.add_one_kb_into_other(kbi, kb2)
            self.wait()
            self.play(self.get_move_kb_with_scale_to_animation(
                kb, 0.9))
            self.wait()
        self.play(self.get_move_kb_with_scale_to_animation(
            kb, 2.0, manim.ORIGIN))
        self.wait()
        """