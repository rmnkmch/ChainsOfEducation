import manim
import KnowledgeBlock

class ChainsOfEducation(manim.Scene):
    def construct(self):
        self.add(KnowledgeBlock.KnowledgeBlock())
        self.wait()

#cd /d D:\My\LTTDIT\Python\ChainsOfEducation\ChainsOfEducation
#manim -pql ChainsOfEducation.py ChainsOfEducation
