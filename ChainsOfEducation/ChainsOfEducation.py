import manim
import KnowledgeBlock


class ChainsOfEducation(manim.Scene):
    def construct(self):
        kb = KnowledgeBlock.KnowledgeBlock("MathМатРyaтика!", '''Матема́тика -
        тоьная наука,ранственньная наука,ьная нау
        ка,ранственные формы''').move_to(3.0 * manim.LEFT).scale(0.3)
        kb2 = KnowledgeBlock.KnowledgeBlock("Руfffffffffffсссска!", '''Текст 
        (от лат. textus — ткань; сплетение, сочетание) — 
        зафиксированная на каком-либо материальном носителе 
        человеческая мысль; в общем плане связная и полная 
        последовательность символов.
        Существуют две основные трактовки понятия «текст»: 
        имманентная (расширенная, философски нагруженная) и 
        репрезентативная (более частная).''').move_to(manim.RIGHT)
        self.add(kb, kb2)
        self.wait()
        kb.generate_target()
        self.add_one_kb_into_other(kb2, kb)
        self.wait()

    def add_one_kb_into_other(self, one: KnowledgeBlock, other: KnowledgeBlock):
        other.add(one)
        self.update_subkbs(other)

    def remove_one_kb_outof_other(self, one: KnowledgeBlock, other: KnowledgeBlock):
        other.remove(one)
        self.remove(one)
        self.update_subkbs(other)

    def update_subkbs(self, kb: KnowledgeBlock):
        all_info = kb.get_subkb_info_to_update()
        all_animations = manim.AnimationGroup()
        for subkb_info in all_info:
            subkb_info[0].generate_target()
            subkb_info[0].target.scale(subkb_info[1]).move_to(subkb_info[2])
            all_animations = manim.AnimationGroup(all_animations,
                                                  manim.MoveToTarget(subkb_info[0]),
                                                  lag_ratio=0.2)
        self.wait()
        self.play(all_animations)

#cd /d D:\My\LTTDIT\Python\ChainsOfEducation\ChainsOfEducation
#manim -pql ChainsOfEducation.py ChainsOfEducation
