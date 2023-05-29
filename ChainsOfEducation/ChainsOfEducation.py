import manim
import KnowledgeBlock

class ChainsOfEducation(manim.Scene):
    def construct(self):
        kb = KnowledgeBlock.KnowledgeBlock("MathМатРyaтика!", '''Матема́тика -
        тоьная наука,ранственньная наука,ьная наука,ранственные формы''')
        self.add(kb)
        self.play(kb.animate.scale(0.5))
        self.wait()
        self.play(kb.animate.scale(3.2).move_to(manim.UR))
        self.wait()

#cd /d D:\My\LTTDIT\Python\ChainsOfEducation\ChainsOfEducation
#manim -pqh ChainsOfEducation.py ChainsOfEducation
