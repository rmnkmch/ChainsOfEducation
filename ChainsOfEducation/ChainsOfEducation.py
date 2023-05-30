import manim
import KnowledgeBlock

class ChainsOfEducation(manim.Scene):
    def construct(self):
        kb = KnowledgeBlock.KnowledgeBlock("MathМатРyaтика!", '''Матема́тика -
        тоьная наука,ранственньная наука,ьная наука,ранственные формы''')
        self.add(kb)
        self.play(kb.animate().scale(0.1))
        self.wait()

#cd /d D:\My\LTTDIT\Python\ChainsOfEducation\ChainsOfEducation
#manim -pql ChainsOfEducation.py ChainsOfEducation
