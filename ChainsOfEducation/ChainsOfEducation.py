import manim
import Block
import KnowledgeBlock as KB
import random
import SQLDatabase


class ChainsOfEducation(manim.Scene):
    def construct(self):
        self.load_all()
        grid = manim.NumberPlane()
        self.kb = KB.KnowledgeBlock("Хи́мия!", '''
        Хи́мия - одна из 
        важнейших и обширных областей естествознания,
        наука, изучающая вещества, также их состав и
        строение, их свойства, зависящие от состава и
        строения, их превращения, ведущие к изменению
        состава.''')
        self.kb.move_to_outside(3.0 * manim.LEFT)
        self.kb.scale_outside(0.6)
        kb2 = KB.KnowledgeBlock("Биоло́гия!", '''
        Биоло́гия (греч. βιολογία; от др.-греч.
        βίος «жизнь» + λόγος «учение, наука»[1]) —
        наука о живых существах и их взаимодействии со
        средой обитания. Изучает все аспекты жизни,
        в частности''')
        kb2.move_to_outside(3.0 * manim.RIGHT)

        self.add(self.kb, kb2, grid)
        self.wait()

        for _ in range(0):
            self.add_blocks(self.kb, 1)
            self.random_scale_move_fill(self.kb)
        for _ in range(0):
            self.add_blocks(kb2, 1)
            self.random_scale_move_fill(kb2)
        self.add_one_into_other(kb2, self.kb)
        for _ in range(0):
            self.random_scale_move_fill(self.kb)
        self.wait(1.0)

        self.save_all()

    def load_all(self):
        self.sql_db = SQLDatabase.SQLDatabase()
        self.sql_db.create_connection("SQLData\KnowledgeBlocks.sqlite")
        ret = self.sql_db.execute_read_query(
            "SELECT title, description FROM KnowledgeBlocks")
        if ret is not None:
            for text in ret:
                print(text)

    def save_all(self):
        self.sql_db.execute_query(self.sql_db.create_table_query())
        self.save_kb(self.kb)
        self.sql_db.close_connection()

    def save_kb(self, kb: KB.KnowledgeBlock):
        if self.sql_db.execute_read_query(
            f"SELECT * FROM KnowledgeBlocks WHERE title = {kb.title.text}") is None:
            self.sql_db.execute_query(
                self.sql_db.create_KB_query(kb.title.text, kb.description.text))

    def random_scale_move_fill(self, b: Block.Block, num = 1, anim = True):
        if anim:
            for _ in range(num):
                b.generate_target()
                self.scale_random(b, anim)
                self.move_random(b, anim)
                self.fill_random(b, anim)
                self.update_b(b)
        else:
            self.scale_random(b, anim)
            self.move_random(b, anim)
            self.fill_random(b, anim)

    def add_blocks(self, b: Block.Block, num: int = 1):
        for i in range(num):
            kbi = KB.KnowledgeBlock(
                str(i), str(i) * 10 + " th KnowledgeBlock")
            self.random_scale_move_fill(kbi, anim = False)
            self.fill_random(kbi, anim = False)
            self.add_one_into_other(kbi, b)

    def remove_blocks(self, b: Block.Block, num: int = 10):
        for kbi in b.get_all_subbs():
            self.remove_one_outof_other(kbi, b)
            num -= 1
            if num <= 0: break

    def add_one_into_other(self,
                           one: Block.Block,
                           other: Block.Block):
        other.add_subb(one)
        other.generate_target()
        self.update_b(other)

    def remove_one_outof_other(self,
                               one: Block.Block,
                               other: Block.Block):
        other.remove_subb(one)
        for subb in one.get_all_subbs():
            self.remove(subb)
        self.remove(one)
        other.generate_target()
        self.update_b(other)

    def update_b(self, b: Block.Block):
        b.make_finish_target()
        self.play(b.get_animations_to_play())
        self.wait()

    def fill_random(self, b: Block.Block, anim = True):
        my_color = "#" + str((random.random() * 1000000.0).__ceil__())
        while len(my_color) != 7:
            my_color = "#" + str((random.random() * 1000000.0).__ceil__())
        my_opacity = random.random() * 0.8
        if anim:
            b.target.set_fill(my_color, my_opacity)
        else:
            b.set_fill(my_color, my_opacity)

    def move_random(self, b: Block.Block, anim = True):
        my_pos_x = (random.random() - 0.5) * 6.0
        my_pos_y = (random.random() - 0.5) * 3.0
        if anim:
            b.target.move_to(my_pos_x * manim.RIGHT + my_pos_y * manim.UP)
        else:
            b.move_to_outside(my_pos_x * manim.RIGHT + my_pos_y * manim.UP)

    def scale_random(self, b: Block.Block, anim = True):
        my_scl = 1.0 + (random.random() - 0.5) * 0.6
        if anim:
            b.target.scale(my_scl)
        else:
            b.scale_outside(my_scl)

    def wait(self, duration: float = 0.25, **kwargs):
        super().wait(duration, **kwargs)

    def add(self, *mobjects: manim.Mobject):
        super().add(*mobjects)
        for b in mobjects:
            if isinstance(b, KB.KnowledgeBlock):
                self.add(b.containing_b, b.description, b.ellipsis_b)

    def remove(self, *mobjects: manim.Mobject):
        super().remove(*mobjects)
        for b in mobjects:
            if isinstance(b, KB.KnowledgeBlock):
                self.remove(b.containing_b, b.description, b.ellipsis_b)

"""
cd /d D:\My\LTTDIT\Python\ChainsOfEducation\ChainsOfEducation
manim -pql --disable_caching ChainsOfEducation.py ChainsOfEducation
manim -pql ChainsOfEducation.py ChainsOfEducation
manim -pqh --disable_caching ChainsOfEducation.py ChainsOfEducation
manim -pqh ChainsOfEducation.py ChainsOfEducation
"""
