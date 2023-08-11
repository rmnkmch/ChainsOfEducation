import manim as M
import Block
import KnowledgeBlock as KB
import random
import SQLDatabase
import ComplexArrow
import Topic
import Tip
import TextBlock


FAST_RUN_TIME: float = 0.1


class ChainsOfEducation(M.MovingCameraScene):
    def construct(self):
        self.chapter_1_1()

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

    def dots_by_text(self, text):
        ret_x: list = []
        ret_y: list = []
        for line in text.split('\n'):
            if len(line) <= 1: continue
            s = line.split()
            if s[0][0] != '−': ret_x.append(float(s[0]))
            else: ret_x.append(-float(s[0][1:]))
            if s[1][0] != '−': ret_y.append(float(s[1]))
            else: ret_y.append(-float(s[1][1:]))
        return (ret_x, ret_y)

    r"""
cd /d D:\My\LTTDIT\Python\ChainsOfEducation\ChainsOfEducation
manim -pql ChainsOfEducation.py ChainsOfEducation
manim -pqh --disable_caching -s ChainsOfEducation.py ChainsOfEducation
manim -pqh --format=gif --disable_caching ChainsOfEducation.py ChainsOfEducation
manim -pqh ChainsOfEducation.py ChainsOfEducation
    """

    def chapter_1_0(self):
        #self.add(M.NumberPlane())
        intro_text = M.Text("Ну что ж ...")
        #self.play(M.Write(intro_text, run_time = 1.0))
        #self.wait()
        #self.play(M.Unwrite(intro_text, run_time = 1.0, reverse = False))
        #self.wait()
        natp = '''−0.05 0.04
0.36 0.136
0.78 0.12
1.084 −0.09
1.42 −0.32
1.9 −0.46
2.36 −0.47
2.76 −0.224
3.076 0.094
3.46 0.406
1
3.985 0.44
4.36 0.226
4.4 −0.184
4.155 −0.423
3.62 −0.38
3.23 −0.19
2.81 0.15
2.45 0.33
2.01 0.43
1.586 0.31
1.386 −0.03
1.62 −0.447
1.93 −0.7
2.17 −0.97
2.17 −1.294
1.974 −1.587
1.617 −1.76
1.16 −1.725
0.74 −1.647
0.286 −1.704
−0.07 −1.86
−0.51 −1.97
−0.93 −1.873
−1.383 −1.673
−1.81 −1.52
−2.22 −1.406
−2.734 −1.407
−3.2 −1.55
−3.61 −1.726
−3.94 −1.95
−4.27 −2.223
−4.464 −2.536
−4.794 −2.797
−5.25 −2.994
−5.74 −3.106
−6.23 −3.14
−6.73 −3.13
−7.35 −3.175
−8 −3.275
−8.745 −3.236
−9.37 −3.05
−10.2 −2.92
−10.88 −2.93
−12.32 −3.14
−13.38 −3.4
−14.51 −3.5
−15.98 −3.37
−17.25 −3.13
−19.17 −3.18
−17.57 −2.41
−15.32 −2.43
−13.36 −2.45
−11.4 −2.26
−9.825 −2.146
−9.24 −2.08
−8.63 −1.89
−8.13 −1.67
−7.74 −1.413
−8 −1.16
−8.57 −1.09
−9.13 −1.02
−9.725 −0.963
−10.35 −0.51
−10 −0.33
−9.19 −0.275
−8.43 −0.304
−7.76 0
−7.24 0.41
−6.87 1.05
−6.7 1.84
−6.53 2.71
−6.24 3.38
−5.74 3.955
−5.1 4.215
−4.22 4.26
−3.18 4.3
−2.3 4.88
−1.43 5.45
−0.85 6.5
−0.07 7.46
0.72 8.09
1.74 8
2.36 7.29
3.08 6.75
3.98 6.55
5.22 6.73
6.67 6.73
7.96 6.75
9.14 6.86
10.34 7.17
11.82 7.9
13.41 7.76
14.63 6.03
15.55 2.48
16.7 −1.52
17.93 −3.76
19.02 −4.69
20.43 −5
22 −4.6
23.68 −3.77
25.23 −2.6
27.18 −2.05
29.35 −1.66
32.92 −1.5
37.2 −0.85
51.53 0.41'''
        natp_2 = '''−25.05 6.3
−16.56 4.52
−14.38 3.9
−9.33 1.59
−8.18 0.93
−8.72 0.11
−10.31 −0.01
−11.3 −0.4
−9.76 −1.19
−8.43 −1.37
−9.24 −1.8
−10.58 −1.79
−12.17 −1.73
−14.23 −2.06
−16.14 −1.83
−19.42 −2.32
−20.27 −3.78
−17.8 −3.52
−15.66 −3.75
−14.11 −3.85
−12.7 −3.61
−11.37 −3.28
−10.05 −3.3
−8.97 −3.64
−8.33 −4.27
−7.95 −6.64
−8.25 −11.47
−14.35 −14.24
−23.5 −14.25
−30.2 −10.92
−32.7 −2.8
−32.58 3.6
−27.84 5.93
−26.12 6.04'''
        natp_3 ='''−0.01 0.09
1.12 −0.35
2.54 −0.74
4.115 −0.22
4.81 0.764
3.68 1.176
2.62 1.205
1.53 0.48
3.18 −0.766
3.88 −1.39
4.09 −1.81
4.27 −2.23
3.62 −2.745
2.55 −2.55
1.05 −2.24
−0.48 −2.4
−2.07 −2.25
−3.47 −2.48
−4.66 −3.54
−5.93 −3.8
−6.89 −3.78
−7.81 −3.64
−8.78 −4.06
−9.82 −3.99
−10.87 −3.94
−11.69 −4.04
3
−12.6 −4.15
−13.71 −4.56
−15.19 −4.57
−16.55 −4.58
−16.13 −3.13
−8.02 −2.3
−7.74 −0.42
−6.49 4.55
−2.6 5.86
6.66 7.54
14.78 9.18
20.13 −4.21
23.3 −2.3
29.6 −0.68
34.64 −0.36'''

        x_values = []
        y_values = []
        x_values_2 = []
        y_values_2 = []
        x_values_3 = []
        y_values_3 = []
        x_values, y_values = self.dots_by_text(natp)
        x_values_2, y_values_2 = self.dots_by_text(natp_2)
        x_values_3, y_values_3 = self.dots_by_text(natp_3)
        coords = [(x, y, 0.0) for x, y in zip(x_values, y_values)]
        coords_2 = [(x, y, 0.0) for x, y in zip(x_values_2, y_values_2)]
        coords_3 = [(x, y, 0.0) for x, y in zip(x_values_3, y_values_3)]
        arrow = ComplexArrow.ComplexArrow(
            coords, Tip.TriangleTip(length = 0.3, width = 0.3, fill_opacity = 1.0),
            Tip.EllipseTip(
                length = 0.3, width = 0.3, fill_opacity = 1.0
                ).set_shift_anchors(-0.5, -0.5))
        arrow_2 = ComplexArrow.ComplexArrow(coords_2, fill_color = "#987791", fill_opacity = 0.5)
        arrow_3 = ComplexArrow.ComplexArrow(coords_3)
        self.add(arrow_2)
        arrow.prepare_to_create_1()
        anim_3 = M.MoveAlongPath(self.camera.frame.set(width = 40.0, height = 25.0),
                                 arrow_3, run_time = 10.0, rate_func = M.linear)
        self.play(arrow.get_creating_anim_1().set_run_time(1.0))
        arrow.prepare_to_create_2()
        anims = M.AnimationGroup(arrow.get_creating_anim_2().set_run_time(15.0), anim_3)
        self.play(anims)
        arrow.after_create()
        self.wait(1.0)

    def chapter_1_1(self):
        t = Topic.Topic()
        self.wait(1.0)

    def chapter_1_2(self):
        kb_1 = KB.KnowledgeBlock("Осознанность!",
        '''Очень сильный и важный инструмент.''')
        self.create_kb_no_descr(kb_1)
        self.update_b(kb_1)
        kb_1.generate_target()
        kb_1.target.move_to(M.UP * 2.2).scale(0.5)
        self.update_b(kb_1, False)
        x_values_2 = [0.0, 0.0, 0.0]
        y_values_2 = [0.8, -0.1, -1.0]
        coords_2 = [(x, y, 0.0) for x, y in zip(x_values_2, y_values_2)]
        arrow_2 = ComplexArrow.ComplexArrow(coords_2)
        arrow_2.prepare_to_create_1()
        self.play(arrow_2.get_creating_anim_1())
        arrow_2.prepare_to_create_2()
        anim_11 = arrow_2.get_creating_anim_2()
        text_1 = TextBlock.TextBlock(
            "Осознавая свои принятые решения,\nжелаемое будет достигаться быстрее.",
        font_size = 30).move_to(2.0 * M.DOWN)
        anim_12 = M.FadeIn(text_1)
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

    def chapter_1_3(self):
        self.add(M.NumberPlane())
        text_2 = M.Text("""Любые суждения или мысли кажутся непонятными
и автоматически бессмысленными,
если у нас нет достаточного основания
для их понимания.""", font_size = 30).move_to(2.0 * M.UP)
        self.play(M.AddTextLetterByLetter(text_2, time_per_char = 0.001))
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
        self.wait(5.0)

    def test_1(self):
        self.add(M.NumberPlane())
        tb = TextBlock.TextBlock(
            """нашими друзьями\nи знакомыми,""").move_to(0.2 * M.UR).rotate(0.05)
        tb2 = TextBlock.TextBlock("""нашими друзьями
        и знакомыми,
        ми друзьями
        ми друзьями
        ми друзьями""")
        self.add(tb, tb2)
        x_values_1 = [0.0, 2.7, 2.7, 2.7, 0.0, -2.7, -2.7, -2.7, 0.0]
        y_values_1 = [2.7, 2.7, 0.0, -2.7, -2.7, -2.7, 0.0, 2.7, 2.7]
        coords = [(x, y, 0.0) for x, y in zip(x_values_1, y_values_1)]
        def get_arr():
            b = tb.get_arrow_to_tb(
                tb2, TextBlock.Directions.LEFT, TextBlock.Directions.RIGHT,
                1.0, 1.0, 1, 1, 1, 1)[0]
            vg = b
            vg = M.VGroup()
            a = []
            for dot in b.get_anchors():
                a.append(M.Dot(dot, radius = 0.04,
                               color = "#1312F5", fill_opacity = 0.5))
            vg = M.VGroup(b, *a)
            return vg
        arrow = M.always_redraw(get_arr)
        self.add(arrow)
        self.play(M.MoveAlongPath(tb2, ComplexArrow.ComplexArrow(coords),
                                  run_time = 1.0, rate_func = M.linear))
        #self.add(M.ThreeDScene())
        self.wait(1.0)

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

class ChangingCameraWidthAndRestore(M.MovingCameraScene):
        def construct(self):
            text = M.Text("Hello World").set_color(M.BLUE)
            self.add(text)
            self.camera.frame.save_state()
            self.play(self.camera.frame.animate.set(width=text.width * 1.2))
            self.wait(0.3)
            self.play(M.Restore(self.camera.frame))

class MovingCameraOnGraph(M.MovingCameraScene):
        def construct(self):
            self.camera.frame.save_state()
            ax = M.Axes(x_range=[-1, 10], y_range=[-1, 10])
            graph = ax.plot(lambda x: M.np.sin(x), color=M.WHITE, x_range=[0, 3 * M.PI])
            dot_1 = M.Dot(ax.i2gp(graph.t_min, graph))
            dot_2 = M.Dot(ax.i2gp(graph.t_max, graph))
            self.add(ax, graph, dot_1, dot_2)
            self.play(self.camera.frame.animate.scale(0.5).move_to(dot_1))
            self.play(self.camera.frame.animate.move_to(dot_2))
            self.play(M.Restore(self.camera.frame))
            self.wait()

class ChangingZoomScale(M.ZoomedScene):
        def __init__(self, **kwargs):
            M.ZoomedScene.__init__(
                self,
                zoom_factor=0.3,
                zoomed_display_height=1,
                zoomed_display_width=3,
                image_frame_stroke_width=20,
                zoomed_camera_config={
                    "default_frame_stroke_width": 3,
                },
                **kwargs
            )

        def construct(self):
            dot = M.Dot().set_color(M.GREEN)
            sq = M.Circle(fill_opacity=1, radius=0.2).next_to(dot, M.RIGHT)
            self.add(dot, sq)
            self.wait(1)
            self.activate_zooming(animate=False)
            self.wait(1)
            self.play(dot.animate.shift(M.LEFT * 0.3))
            self.play(self.zoomed_camera.frame.animate.scale(4))
            self.play(self.zoomed_camera.frame.animate.shift(0.5 * M.DOWN))
