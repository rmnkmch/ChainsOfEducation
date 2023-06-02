import manim
import KnowledgeBlock


class ChainsOfEducation(manim.Scene):
    def construct(self):
        kb = KnowledgeBlock.KnowledgeBlock("MathМатРyaтика!", '''Матема́тика -
        тоьная наука,ранственньная наука,ьная нау
        ка,ранственные формы''').move_to(3.0 * manim.LEFT).scale(0.3)
        kb2 = KnowledgeBlock.KnowledgeBlock("Русссска!", '''Текст 
        (от лат. textus — ткань; сплетение, сочетание) — 
        зафиксированная на каком-либо материальном носителе 
        человеческая мысль; в общем плане связная и полная 
        последовательность символов.
        Существуют две основные трактовки понятия «текст»: 
        имманентная (расширенная, философски нагруженная) и 
        репрезентативная (более частная).''').move_to(manim.RIGHT)
        kb3 = KnowledgeBlock.KnowledgeBlock("333333тика!", '''3Матема́тика -
        тоьная нdfdgые формы''').move_to(2.0*manim.RIGHT + 2.0*manim.UP).scale(0.3)
        kb4 = KnowledgeBlock.KnowledgeBlock("444444М!", '''4Матема́тика -
        тоьная наукформы''').move_to(2.8*manim.LEFT + 2.0*manim.UP).scale(0.7)
        kb5 = KnowledgeBlock.KnowledgeBlock("M5555555555а!", '''5М889атема́тика -
        тоьнdg нау''').move_to(3.0*manim.RIGHT + 3.0*manim.DOWN).scale(0.5)
        self.add(kb)
        self.add(kb2)
        self.wait()
        self.put_one_kb_into_other(kb, kb2)
        self.wait()
        self.add(kb3)
        self.wait()
        self.put_one_kb_into_other(kb3, kb2)
        self.wait()
        self.add(kb4)
        self.wait()
        self.put_one_kb_into_other(kb4, kb2)
        self.wait()
        self.add(kb5)
        self.wait()
        self.put_one_kb_into_other(kb5, kb2)
        self.wait()

    def put_one_kb_into_other(self, one: KnowledgeBlock, other: KnowledgeBlock):
        other.add(one)
        self.update_subkbs(other)

    def update_subkbs(self, kb: KnowledgeBlock):
        for subkb_info in kb.get_subkb_info_to_update():
            self.play(subkb_info[0].animate.scale(
                subkb_info[1]).move_to(subkb_info[2]))

#cd /d D:\My\LTTDIT\Python\ChainsOfEducation\ChainsOfEducation
#manim -pql ChainsOfEducation.py ChainsOfEducation
