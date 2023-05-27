import manim
import Droplet


class ChainsOfEducation(manim.Scene):
    def construct(self):
        self.add(Droplet.Droplet())
        self.wait()

#cd /d D:\My\LTTDIT\Python\ChainsOfEducation\ChainsOfEducation
#manim -pql ChainsOfEducation.py ChainsOfEducation
