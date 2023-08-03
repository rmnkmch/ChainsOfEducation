import manim as M
import Block
import KnowledgeBlock as KB
import random
import SQLDatabase
import ComplexArrow
import TopicBlock
import Chain
import Tip
import TextBlock


FAST_RUN_TIME: float = 0.1
c_1 = "1⃣"
c_2 = "2⃣"
c_3 = "3⃣"
c_4 = "4⃣"
c_5 = "5⃣"
c_6 = "6⃣"
c_7 = "7⃣"
c_8 = "8⃣"
c_9 = "9⃣"
c_0 = "0⃣"
c_off = "🏢"
c_cap = "🏛"
c_lang = "👅"
c_mon = "💰"


class ChainsOfEducation(M.Scene):
    def construct(self):
        self.test_1()

    def load_all(self):
        self.sql_db = SQLDatabase.SQLDatabase()
        self.sql_db.create_connection(r"SQLData\KnowledgeBlocks.sqlite")
        self.sql_db.execute_query(self.sql_db.create_table_query())
        ret = self.sql_db.execute_read_query(r"SELECT * FROM KnowledgeBlocks")
        if ret is not None:
            for text in ret:
                print(text)

    def save_all(self):
        self.save_kb(self.kb)
        self.sql_db.close_connection()

    def save_kb(self, kb: KB.KnowledgeBlock):
        if (self.sql_db.execute_read_query(
            f"SELECT * FROM KnowledgeBlocks WHERE title = '{kb.title.text}'")
            is None):
            self.sql_db.execute_query(
                self.sql_db.create_KB_query(kb.title.text, kb.description.text))

    def random_scale_move_fill(self, b: Block.Block, num = 1, anim = True):
        if anim:
            for _ in range(num):
                b.generate_target()
                self.scale_random(b, anim)
                self.move_random(b, anim)
                self.fill_random(b, anim)
                self.update_b(b, False)
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
        self.update_b(other)

    def remove_one_outof_other(self,
                               one: Block.Block,
                               other: Block.Block):
        other.remove_subb(one)
        for subb in one.get_all_subbs():
            self.remove(subb)
        self.remove(one)
        self.update_b(other)

    def update_b(self, b: Block.Block, gen_tar = True, fast = False,
                 other_animations = None):
        if gen_tar:
            b.generate_target()
        b.make_finish_target()
        if other_animations is None:
            if fast:
                self.play(b.get_animations_to_play().set_run_time(FAST_RUN_TIME))
            else:
                self.play(b.get_animations_to_play())
                self.wait()
        else:
            if fast:
                self.play(M.AnimationGroup(
                    b.get_animations_to_play(), other_animations,
                    run_time = FAST_RUN_TIME))
            else:
                self.play(M.AnimationGroup(
                    b.get_animations_to_play(), other_animations))
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
            b.target.move_to(self.pos_by(my_pos_x, my_pos_y))
        else:
            b.move_to_outside(self.pos_by(my_pos_x, my_pos_y))

    def scale_random(self, b: Block.Block, anim = True):
        my_scl = 1.0 + (random.random() - 0.5) * 0.6
        if anim:
            b.target.scale(my_scl)
        else:
            b.scale_outside(my_scl)

    def wait(self, duration: float = 0.2, **kwargs):
        super().wait(duration, **kwargs)

    def add(self, *mobjects: M.Mobject):
        super().add(*mobjects)
        for b in mobjects:
            if isinstance(b, KB.KnowledgeBlock):
                self.add(b.containing_b, b.description, b.ellipsis_b)

    def remove(self, *mobjects: M.Mobject):
        super().remove(*mobjects)
        for b in mobjects:
            if isinstance(b, KB.KnowledgeBlock):
                self.remove(b.containing_b, b.description, b.ellipsis_b)

    def create_kb_no_descr(self, kb: KB.KnowledgeBlock, fast = False):
        kb.save_description_opacity()
        kb.hide_description(False)
        if fast:
            self.play(M.Create(kb, run_time = FAST_RUN_TIME))
        else:
            self.play(M.Create(kb, lag_ratio = 0.1, run_time = 3.0))
            self.wait()

    def write_text(self, text, fast = False):
        if fast:
            self.play(M.Write(text, run_time = FAST_RUN_TIME))
        else:
            self.play(M.Write(text, run_time = 3.0))
            self.wait()

    def unwrite_text(self, text, fast = False):
        if fast:
            self.play(
                M.Unwrite(text, run_time = FAST_RUN_TIME, reverse = False))
        else:
            self.play(M.Unwrite(text, run_time = 3.0, reverse = False))
            self.wait()

    def creating_topic_anim(self, topic: TopicBlock.TopicBlock, fast = False):
        if fast:
            return M.Create(topic, run_time = FAST_RUN_TIME)
        else:
            return M.Create(topic, lag_ratio = 0.1)

    def creating_chain_anim(self, chain: Chain.Chain, fast = False):
        if fast:
            return M.AnimationGroup(
                M.FadeIn(chain.start_dot),
                M.Write(chain),
                M.Create(chain.end_dot),
                run_time = FAST_RUN_TIME)
        else:
            return M.AnimationGroup(
                M.FadeIn(chain.start_dot),
                M.Write(chain),
                M.Create(chain.end_dot),
                lag_ratio = 0.75)

    def creating_chain_and_topic_anim(self, chain, topic, fast = False):
        if fast:
            return M.AnimationGroup(
                self.creating_chain_anim(chain, fast),
                self.creating_topic_anim(topic, fast),
                run_time = FAST_RUN_TIME)
        else:
            return M.AnimationGroup(
                self.creating_chain_anim(chain, fast),
                self.creating_topic_anim(topic, fast),
                lag_ratio = 0.5)

    def pos_by(self, x: float, y: float):
        return M.RIGHT * x + M.UP * y

    def shift_by_text(self, text: str):
        caps = "бё"#ДЁЙЦЩQJ
        caps_2 = "йАБВГЕЖЗИКЛМНОПРСТУФХЧШЪЫЬЭЮЯABCDEFGHIKLMNOPRSTUVWXYZ"
        lows = "дцщ"
        lows_2 = "ру"
        caps = [i for i in caps]
        caps_2 = [i for i in caps_2]
        lows = [i for i in lows]
        lows_2 = [i for i in lows_2]
        for char in text:
            if char in caps: return 0.084
            elif char in caps_2: return 0.065
            elif char in lows: return - 0.041
            elif char in lows_2: return - 0.056
        return 0.0

    r"""
cd /d D:\My\LTTDIT\Python\ChainsOfEducation\ChainsOfEducation
manim -pql --disable_caching ChainsOfEducation.py ChainsOfEducation
manim -pql ChainsOfEducation.py ChainsOfEducation
manim -pqh --disable_caching ChainsOfEducation.py ChainsOfEducation
manim -pqh ChainsOfEducation.py ChainsOfEducation
    """

    def chapter_1_0(self):
        self.nnn = 0
        def get_start_chain_func():
            n = self.nnn
            self.nnn += 1
            return lambda: self.pos_by(x_values[n + 1], y_values[n + 1])

        fast_1 = True
        fast_2 = False
        intro_text = M.Text("Ну что ж ...")
        self.write_text(intro_text, fast_1)
        self.unwrite_text(intro_text, fast_1)
        x_values = [-6, -4, 0, 4, 6]
        y_values = [3.0, 2.8, 3.0, 2.8, 3.0]
        coords = [(x, y, 0.0) for x, y in zip(x_values, y_values)]
        arrow = ComplexArrow.ComplexArrow(coords, Tip.EllipseTip())
        self.add(arrow.end_tip)
        anim_1 = M.Create(arrow, run_time = 3.0)
        tb_1 = TopicBlock.TopicBlock(
            "Осознание",
            ["Что такое осознанность?",
             "Несколько\nуниверсальных методов"]).move_to(
                 self.pos_by(- 4.0, 1.9)).scale(0.3)
        tb_1.set_chain(get_start_chain_func())
        tb_2 = TopicBlock.TopicBlock("???").move_to(
            self.pos_by(0.0, 1.9)).scale(0.3)
        tb_2.set_chain(get_start_chain_func())
        tb_3 = TopicBlock.TopicBlock("???").move_to(
            self.pos_by(4.0, 1.9)).scale(0.3)
        tb_3.set_chain(get_start_chain_func())
        grp = [tb_1, tb_2, tb_3]
        anims = []
        for topic_block in grp:
            anims.append(self.creating_chain_and_topic_anim(
                topic_block.chain, topic_block, fast_1))
            topic_block.chain.stop_follow()
        anims = M.AnimationGroup(*anims, lag_ratio = 0.1)
        played = M.AnimationGroup(anim_1, anims, lag_ratio = 0.3)
        self.play(played)
        for topic_block in grp:
            topic_block.chain.start_follow()
        tb_1.generate_target()
        tb_1.target.move_to(1.5 * M.DOWN + 3.0 * M.LEFT).scale(1.0 / 0.3)
        tb_1.target.activate()
        self.play(M.MoveToTarget(tb_1))
        self.play(tb_1.prepare_to_briefs())
        for _ in range(len(tb_1.get_all_briefs_dots())):
            self.play(tb_1.show_next_brief())

        kb_1 = KB.KnowledgeBlock("Осознанность!",
        '''Очень сильный и важный инструмент.''')
        self.create_kb_no_descr(kb_1, fast_1)
        self.update_b(kb_1, fast = fast_1)
        kb_1.generate_target()
        kb_1.target.move_to(M.UP * 2.2).scale(0.5)
        self.update_b(kb_1, False, fast_1)
        x_values_2 = [0.01, -0.01, 0.01]
        y_values_2 = [0.8, -0.1, -1.0]
        coords_2 = [(x, y, 0.0) for x, y in zip(x_values_2, y_values_2)]
        arrow_2 = ComplexArrow.ComplexArrow(coords_2)
        self.add(arrow_2.end_tip)
        anim_11 = M.Create(arrow_2)
        text_1 = M.Text(
        "Осознавая свои принятые решения,\nжелаемое будет достигаться быстрее.",
        font_size = 30).move_to(2.0 * M.DOWN)
        anim_12 = M.AddTextLetterByLetter(text_1, time_per_char = 0.01)
        anim_14 = M.AnimationGroup(anim_11, anim_12, lag_ratio = 0.5)
        self.play(anim_14)
        vgrp_1 = M.VGroup(arrow_2, arrow_2.end_tip, text_1)
        vgrp_1.generate_target()
        vgrp_1.target.shift(14.0 * M.LEFT)
        kb_1.generate_target()
        kb_1.target.shift(14.0 * M.LEFT)
        kb_1.make_finish_target()
        self.play(M.MoveToTarget(vgrp_1), kb_1.get_animations_to_play())
        self.wait(1.0)

    def chapter_1_1(self):
        self.add(M.NumberPlane())
        text_2 = M.Text("""Любые суждения или мысли кажутся непонятными
и автоматически бессмысленными,
если у нас нет достаточного основания
для их понимания.""", font_size = 30).move_to(2.0 * M.UP)
        #self.play(M.AddTextLetterByLetter(text_2, time_per_char = 0.001))
        texts_2 = ["Любые суждения или мысли",
                   "Всё когда-либо",
                   "сказанное нами,",
                   "нашими друзьями и знакомыми,",
                   "и даже незнакомыми,",
                   "прочитанное в интернете,",
                   "книгах,",
                   "газетах,",
                   "услышанное по радио,",
                   "придуманное во сне или наяву,",
                   "увиденное на улице или по телевизору и т.д"]
        mtexts = [[texts_2[0], self.pos_by(-3.0, 1.0)],
                  [texts_2[1], self.pos_by(-2.0, 1.0)],
                  [texts_2[2], self.pos_by(1.0, 1.0)],
                  [texts_2[3], self.pos_by(-2.0, 0.0)],
                  [texts_2[4], self.pos_by(3.0, 0.0)],
                  [texts_2[5], self.pos_by(-2.0, -1.0)],
                  [texts_2[6], self.pos_by(0.0, -1.0)],
                  [texts_2[7], self.pos_by(1.0, -1.0)],
                  [texts_2[8], self.pos_by(3.0, -1.0)],
                  [texts_2[9], self.pos_by(-1.0, -2.0)],
                  [texts_2[10], self.pos_by(-1.0, -3.0)]]
        self.play(M.FadeIn(M.Text(mtexts[0][0]).move_to(mtexts[0][1])))
        x_values_2 = [- 3, -6, -5]
        y_values_2 = [2, 2, 1]
        coords = [(x, y, 0.0) for x, y in zip(x_values_2, y_values_2)]
        arrow_2 = ComplexArrow.ComplexArrow(coords)
        self.add(arrow_2.end_tip)
        self.wait()
        anim_1 = M.Create(arrow_2)
        self.play(anim_1)

       
        x_values = [-2.3, 2.3, 2.3, -2.3, -2.3]
        y_values = [2.3, 2.3, -2.3, -2.3, 2.3]
        coords = [(x, y, 0.0) for x, y in zip(x_values, y_values)]
        arrow = ComplexArrow.ComplexArrow(coords)
        self.add(arrow.end_tip)
        arrr_curr = arrow.get_next_curves(50)
        def fnc():
            return M.Text(str(1)).move_to(arrr_curr.get_last_point())
        tx = M.always_redraw(fnc)
        self.add(tx)
        arrow.end_tip.set_pos_func(lambda: arrr_curr.get_last_point())
        anim_5 = M.AnimationGroup(M.Create(
            arrr_curr, run_time = 5.0))
        self.play(anim_5)
        self.wait(5.0)

        r"""
manim -pql --disable_caching ChainsOfEducation.py ChainsOfEducation
    """

    def test_1(self):
        self.add(M.NumberPlane())
        tb = TextBlock.TextBlock(
            """нашими друзьями\nи знакомыми,""")
        tb.rotate(0.01)
        tb2 = TextBlock.TextBlock("""нашими друзьями и знакомыми,
        ми друзьями
        ми друзьями
        ми друзьями""").move_to(2.0 * M.DL)
        tb2.rotate(-0.01)
        self.add(tb, tb2)
        x_values_1 = [-5.8, -6.0, -5.8]
        y_values_1 = [1.1, 0.0, -1.1]
        coords = [(x, y, 0.0) for x, y in zip(x_values_1, y_values_1)]
        arrow = tb2.get_arrow_to_tb(
            tb, TextBlock.Directions.UP, TextBlock.Directions.DOWN,
            0.99, 0.99, 0, 0, 1, 1)
        for tupl in arrow.get_curve_functions_with_lengths():
            pass
            #print(tupl)
        for pos in arrow.get_anchors():
            self.add(M.Dot(pos, color = "#56F288"))
        self.add(arrow.end_tip)
        anim_1 = M.Create(arrow, run_time = 5.0)
        self.play(anim_1)
        self.wait(1.0)

    def Jpn_Geo(self):
        """
        #menu
        #Geography
        #Japanese
        #English
        #Quote"""
        native_examples = """花火. はなび. фейрверк.
"""
        native_kun_on = """
        """
        geo = """Нигерия; Федеративная Республика Нигерия
государство в Западной Африке.
Nigeria; Federal Republic of Nigeria
Абуджа; Abuja
английский; English
NGN, найра; Nigerian naira"""

        self.resplit_to_JP_read_kanji(native_kun_on)
        self.resplit_to_RU_read_kanji(native_kun_on)
        self.resplit_to_post_kanji(native_kun_on)
        self.resplit_to_post_examples(native_examples)
        self.resplit_to_post_geo(geo)
        self.resplit_to_z_name_geo(geo)

    class MyMoveAlongPath(M.Animation):
        def __init__(
            self,
            mobject: M.Mobject,
            path: M.VMobject,
            suspend_mobject_updating: bool | None = False,
            **kwargs) -> None:
            self.path = path
            self.previous_pos = self.path.point_from_proportion(0.0)
            self.previous_angle = 0.0
            super().__init__(
                mobject,
                suspend_mobject_updating = suspend_mobject_updating,
                **kwargs)

        def interpolate_mobject(self, alpha: float) -> None:
            pos = self.path.point_from_proportion(self.rate_func(alpha))
            self.mobject.move_to(pos)
            diff_pos = pos - self.previous_pos
            if abs(diff_pos[0]) >= 0.001 and abs(diff_pos[1]) >= 0.001:
                from math import atan
                self.previous_pos = pos
                angle = 0.0
                if diff_pos[0] > 0.0 and diff_pos[1] > 0.0:
                    angle = atan(diff_pos[1] / diff_pos[0])
                elif diff_pos[0] > 0.0 and diff_pos[1] < 0.0:
                    angle = 2.0 * M.PI - atan(abs(diff_pos[1] / diff_pos[0]))
                elif diff_pos[0] < 0.0 and diff_pos[1] > 0.0:
                    angle = M.PI - atan(abs(diff_pos[1] / diff_pos[0]))
                else:
                    angle = M.PI + atan(abs(diff_pos[1] / diff_pos[0]))
                diff_angle = angle - self.previous_angle
                self.previous_angle = angle
                self.mobject.rotate(diff_angle)

    def resplit_to_post_geo(self, text: str):
        lines = text.split("\n")
        num_line = 0
        ln = ""
        rus = ""
        for line in lines:
            if num_line == 0:
                num_line = 1
                print("#Geography")
                rus = line.split("; ")
                ln = rus[0] + " - "
            elif num_line == 1:
                num_line = 2
                ln += line
                print(ln)
            elif num_line == 2:
                num_line = 3
                eng = line.split("; ")
                ln = c_off + " - "
                for word_num in range(len(eng)):
                    ln += rus[word_num] + " (" + eng[word_num] + ")"
                    if word_num < len(eng) - 1: ln += " / "
                print(ln)
            elif num_line == 3:
                num_line = 4
                wr = line.split("; ")
                print(c_cap + " - " + wr[0] + " (" + wr[1] + ")")
            elif num_line == 4:
                num_line = 5
                part = line.split("; ")
                ln = c_lang + " - " + part[0] + " (" + part[1] + ")"
                print(ln)
            elif num_line == 5:
                num_line = 0
                part = line.split("; ")
                lower = part[0][:5] + part[0][5].lower() + part[0][6:]
                ln = c_mon + " - " + lower + " (" + part[1] + ")"
                print(ln)

    def resplit_to_z_name_geo(self, text: str):
        lines = text.split("\n")
        num_line = 0
        num = 63
        for line in lines:
            if num_line == 2:
                num_line = 3
                eng = line.split("; ")
                print("#" + str(num) + " z_" + eng[0])
                num += 1
            elif num_line == 5: num_line = 0
            else: num_line += 1

    def resplit_to_post_examples(self, text: str):
        lines = text.split("\n")
        for line in lines:
            ln = ""
            parts = line.split(". ", 2)
            for part in parts:
                part_striped = part.rstrip(". ")
                part_striped = part_striped.lstrip()
                words = part_striped.split(". ")
                for word in words:
                    ln += word
                    if words.index(word) < len(words) - 1:
                        ln += ", "
                if parts.index(part) < len(parts) - 1:
                    if parts.index(part) == 0:
                        ln += " ("
                    elif parts.index(part) == 1:
                        ln += ") - "
            print(ln)

    def resplit_to_post_kanji(self, text: str):
        lines = text.split("\n")
        ln = ""
        trlt = ""
        for line in lines:
            if len(line) == 1: ln = " " + line + " - "
            elif len(line) > 1 and not line[0].isupper(): trlt = line
            elif line.startswith("Kun: "):
                kuns = line.removeprefix("Kun: ")
                kuns = kuns.split("、 ")
                for kun in kuns:
                    ln += kun
                    if kuns.index(kun) < len(kuns) - 1:
                        ln += ", "
            elif line.startswith("On: "):
                ons = line.removeprefix("On: ")
                ons = ons.split("、 ")
                ln += "; "
                for on in ons:
                    ln += on
                    if ons.index(on) < len(ons) - 1:
                        ln += ", "
                ln += " - " + trlt
                print(ln)

    def resplit_to_JP_read_kanji(self, text: str):
        lines = text.split("\n")
        ln = ""
        for line in lines:
            if len(line) == 1: ln = line + ",-. / "
            elif line.startswith("Kun: "):
                kuns = line.removeprefix("Kun: ")
                kuns = kuns.split("、 ")
                for kun in kuns:
                    ln += kun + ",-. "
            elif line.startswith("On: "):
                ons = line.removeprefix("On: ")
                ons = ons.split("、 ")
                ln += " / "
                for on in ons:
                    ln += on + ",-. "
                print(ln)

    def resplit_to_RU_read_kanji(self, text: str):
        lines = text.split("\n")
        ln = ""
        for line in lines:
            if len(line) > 1 and not line[0].isupper() and not line[0].isnumeric():
                words = line.split(", ")
                for word in words:
                    ln += word + ",-. "
                print(ln)
                ln = ""

        r"""
manim ChainsOfEducation.py ChainsOfEducation
"""
