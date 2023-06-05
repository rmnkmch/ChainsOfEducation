import manim
import KnowledgeBlock


class ChainsOfEducation(manim.Scene):
    def construct(self):
        kb = KnowledgeBlock.KnowledgeBlock("MathМатРyaтика!", '''Матема́тика -
        тоьная наука,ранственньная наука,ьная нау
        ка,ранственные формы''').move_to(3.0 * manim.LEFT).scale(0.3)
        kb2 = KnowledgeBlock.KnowledgeBlock("Руfffffffffffсссска!", '''Текст 
        (от лат. textus — ткань; сплетение, сочетание) — 
        зафски нагруженная) и 
        репрезентативная (более частная).''').move_to(manim.RIGHT)
        self.add(kb, kb2)
        self.wait()
        self.add_one_kb_into_other(kb2, kb)
        self.wait()
        for i in range(2):
            kbi = KnowledgeBlock.KnowledgeBlock("!!!", '''ика -
            тоьная наука,ран наука,ранственные формы''').move_to(
                2.0 * manim.RIGHT).scale(0.7)
            self.add(kbi)
            self.wait()
            self.add_one_kb_into_other(kbi, kb)
            self.wait()
        self.play(self.get_move_kb_with_scale_to_animation(
            kb, 2.0, manim.ORIGIN).set_run_time(2.0))
        self.wait()

    def add_one_kb_into_other(self, one: KnowledgeBlock, other: KnowledgeBlock):
        other.add(one)
        self.update_kb(other)

    def remove_one_kb_outof_other(self, one: KnowledgeBlock, other: KnowledgeBlock):
        other.remove(one)
        self.remove(one)
        self.update_kb(other)

    def get_move_kb_with_scale_to_animation(self, kb: KnowledgeBlock,
                                            scale_factor: float = 1.0,
                                            position = None):
        if position is None:
            position = kb.get_center()
        kb.set_center(position)
        kb.generate_target()
        kb.target.scale(scale_factor).move_to(position)
        return manim.MoveToTarget(kb)

    def get_update_subkbs_animations(self, kb: KnowledgeBlock):
        all_info = kb.get_subkb_info_to_update()
        all_animations = manim.AnimationGroup()
        for subkb_info in all_info:
            all_animations = manim.AnimationGroup(
                all_animations, self.get_move_kb_with_scale_to_animation(
                    subkb_info[0], subkb_info[1], subkb_info[2]))
        return all_animations

    def get_update_description_animation(self, kb: KnowledgeBlock):
        all_info = kb.get_description_info_to_update()
        all_animations = manim.AnimationGroup()
        for description_info in all_info:
            description_info[0].generate_target()
            description_info[0].target = manim.Text(
                description_info[1],
                font_size = KnowledgeBlock.DEFAULT_DESCRIPTION_FONT_SIZE)
            description_info[0].target.scale(
                description_info[2] * description_info[0].width
                / description_info[0].target.width).move_to(
                    description_info[3])
            all_animations = manim.AnimationGroup(
                all_animations, manim.MoveToTarget(description_info[0]))
        return all_animations

    def update_kb(self, kb: KnowledgeBlock):
        kb.generate_target()#TODO remove MoveToTarget
        self.play(manim.AnimationGroup(
            manim.MoveToTarget(kb),
            self.get_update_description_animation(kb),
            self.get_update_subkbs_animations(kb),
            lag_ratio=0.3))

#cd /d D:\My\LTTDIT\Python\ChainsOfEducation\ChainsOfEducation
#manim  -pql ChainsOfEducation.py ChainsOfEducation
#--disable_caching
