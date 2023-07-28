from operator import index
import manim as M
import Block
import KnowledgeBlock as KB
import random
import SQLDatabase
import ComplexArrow
import TopicBlock
import Chain


FAST_RUN_TIME: float = 0.1


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
            self.play(M.Unwrite(text, run_time = FAST_RUN_TIME,
                                    reverse = False))
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
        x_values = [-7, -4, 0, 4, 7]
        y_values = [3.2, 2.8, 3.2, 2.8, 3.2]
        coords = [(x, y, 0.0) for x, y in zip(x_values, y_values)]
        arrow = ComplexArrow.ComplexArrow(coords)
        anim_1 = ChainsOfEducation.MyMoveAlongPath(
            arrow.end_tip, arrow.copy(), run_time = 1.0)
        anim_2 = M.Create(arrow, run_time = 1.0)
        anim_3 = M.AnimationGroup(anim_1, anim_2)
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
        played = M.AnimationGroup(anim_3, anims, lag_ratio = 0.3)
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
        x_values_2 = [0, 0]
        y_values_2 = [0.8, -1.0]
        coords_2 = [(x, y, 0.0) for x, y in zip(x_values_2, y_values_2)]
        arrow_2 = ComplexArrow.ComplexArrow(coords_2)
        arrow_2.end_tip.rotate(- 0.5 * M.PI)
        anim_10 = ChainsOfEducation.MyMoveAlongPath(
            arrow_2.end_tip, arrow_2.copy())
        anim_11 = M.Create(arrow_2)
        text_1 = M.Text(
        "Осознавая свои принятые решения,\nжелаемое будет достигаться быстрее.",
        font_size = 30).move_to(2.0 * M.DOWN)
        anim_12 = M.AddTextLetterByLetter(text_1, time_per_char = 0.01)
        anim_13 = M.AnimationGroup(anim_11, anim_10)
        anim_14 = M.AnimationGroup(anim_13, anim_12, lag_ratio = 0.5)
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
        self.play(M.AddTextLetterByLetter(text_2, time_per_char = 0.01))
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
        anim_1 = ChainsOfEducation.MyMoveAlongPath(
            arrow_2.end_tip, arrow_2.copy())
        anim_2 = M.Create(arrow_2)
        anim_3 = M.AnimationGroup(anim_1, anim_2)
        self.play(anim_3)
        self.wait(1.0)

        r"""
manim -pqk --disable_caching ChainsOfEducation.py ChainsOfEducation
"""

    def test_1(self):
        txt = """竹 | бамбук. | たけ. | チク.
田 | рисовое поле. рисовые плантации. | た. | デン.
雨 | дождь. | あめ. あま. さめ. | ウ.
花 | цветок. | はな. | カ. ケ.
草 | трава. сорняки. пастбище. | くさ. ぐさ. | ソウ.
石 | камень. | いし. | セキ. シャク. コク.
貝 | моллюск. | かい. | バイ.
生 | жизнь. рождение. | いきる. いかす. いける. うまれる. うまれ. うむ. おう. はえる. はやす. き. なま. なる. なす. むす. う. | セイ. ショウ.
人 | человек. | ひと. り. と. | ジン. ニン.
女 | женщина. самка. | おんな. め. | ジョ. ニョ. ニョウ.
男 | мужчина. самец. | おとこ. お. | ダン. ナン.
子 | ребёнок. дитя. | こ. ね. | シ. ス. ツ.
犬 | собака. | いぬ. | ケン.
虫 | насекомое. букашка. | むし. | チュウ. キ.
白 | белый. | しろ. しら. しろい. | ハク. ビャク.
青 | синий. зелёный. голубой. | あお. あおい. | セイ. ショウ.
赤 | красный. | あか. あかい. あからむ. あからめる. | セキ. シャク."""
        txt2 = """

挨拶より円札. あいさつよりえんさつ. лучше деньги, чем сладкие слова."""
        txt3 = """生
5 strokes
Radical: life 生
Parts: 生
life, genuine, birth
Kun: い.きる、 い.かす、 い.ける、 う.まれる、 うま.れる、 う.まれ、 うまれ、 う.む、 お.う、 は.える、 は.やす、 き、 なま、 なま-、 な.る、 な.す、 む.す、 -う
On: セイ、 ショウ
目
5 strokes
Radical: eye 目
Parts: 目
eye, class, look, insight, experience, care, favor
Kun: め、 -め、 ま-
On: モク、 ボク
耳
6 strokes
Radical: ear 耳
Parts: 耳
ear
Kun: みみ
On: ジ
口
3 strokes
Radical: mouth, opening 口
Parts: 口 囗
mouth
Kun: くち
On: コウ、 ク
手
4 strokes
Radical: hand 手 (扌龵)
Parts: 手
hand
Kun: て、 て-、 -て、 た-
On: シュ、 ズ
足
7 strokes
Radical: foot 足 (⻊)
Parts: 口 止 足
leg, foot, be sufficient, counter for pairs of footwear
Kun: あし、 た.りる、 た.る、 た.す
On: ソク
見
7 strokes
Radical: see 見
Parts: 儿 目 見
see, hopes, chances, idea, opinion, look at, visible
Kun: み.る、 み.える、 み.せる
On: ケン
音
9 strokes
Radical: sound 音
Parts: 日 立 音
sound, noise
Kun: おと、 ね
On: オン、 イン、 -ノン
気
6 strokes
Radical: steam, breath 气
Parts: 丶 ノ 气 乞
Variants: 氣 炁
spirit, mind, air, atmosphere, mood
Kun: き
On: キ、 ケ
力
2 strokes
Radical: power, force 力
Parts: 力
power, strength, strong, strain, bear up, exert
Kun: ちから
On: リョク、 リキ、 リイ
円
4 strokes
Radical: open country 冂
Parts: 一 ｜ 亠 冂
Variants: 圓
circle, yen, round
Kun: まる.い、 まる、 まど、 まど.か、 まろ.やか
On: エン"""

        self.resplit_to_JP_read(txt3)

        """
        M.always_redraw()
        x_values = [-2.3, 2.3, 2.3, -2.3, -2.3]
        y_values = [2.3, 2.3, -2.3, -2.3, 2.3]
        coords = [(x, y, 0.0) for x, y in zip(x_values, y_values)]
        arrow = ComplexArrow.ComplexArrow(coords)
        self.add(arrow.end_tip)
        arrr_curr = arrow.get_next_curves(50)
        arrow.end_tip.set_pos_func(lambda: arrr_curr.get_last_point())
        anim_5 = M.AnimationGroup(M.Create(
            arrr_curr, run_time = 10.0,
            rate_func = lambda t: M.smooth(t, inflection = 8)))
        self.play(anim_5)
        self.wait(1.0)"""
        '''arrr_curr = arrow_2.get_next_curves(10)
        arrow.end_tip.set_pos_func(lambda: arrr_curr.get_last_point())
        self.wait(1.0)
        anim_6 = M.AnimationGroup(M.Create(arrr_curr, run_time = 3.0))
        self.play(anim_6)
        self.wait(1.0)'''

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

    def resplit_JP(self, text: str):
        lines = text.split("\n")
        for line in lines:
            ln = " "
            parts = line.split("|")
            parts = [parts[0], parts[2], parts[3], parts[1]]
            for part in parts:
                part_striped = part.rstrip(". ")
                part_striped = part_striped.lstrip()
                words = part_striped.split(". ")
                for word in words:
                    ln += word
                    if words.index(word) < len(words) - 1:
                        ln += ", "
                if parts.index(part) < len(parts) - 1:
                    if parts.index(part) == 0 or parts.index(part) == 2:
                        ln += " - "
                    else:
                        ln += "; "
            print(ln)

    def resplit_JP2(self, text: str):
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

    def resplit_to_post_kanji(self, text: str): #native kanji kun, on
        lines = text.split("\n")
        ln = ""
        trlt = ""
        for line in lines:
            if len(line) == 1: ln = " " + line + " - "
            elif not line[0].isupper(): trlt = line
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

    def resplit_to_JP_read(self, text: str): #native kanji kun, on
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

        r"""
manim ChainsOfEducation.py ChainsOfEducation
"""
