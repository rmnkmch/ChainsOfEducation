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
        # self.chapter_1_0()
        # self.chapter_1_00()
        # self.chapter_1_000()
        # self.chapter_1_1()
        # self.chapter_1_2()
        # self.chapter_1_3()
        # from TitleBlock import TitleBlock
        # TitleBlock.Jpn_Geo(self)
        # from SSCTV import SSCTV
        # SSCTV.make_tv(self)
        from SIPK import SIPK
        SIPK.make_sipk(self)
        # from welldungeon import Welldungeon
        # Welldungeon.do(self)

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

    def wait(self, duration: float = 0.02, **kwargs):
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
cd ChainsOfEducation
manim ChainsOfEducation.py ChainsOfEducation
manim -pqh ChainsOfEducation.py ChainsOfEducation
manim -pqh ChainsOfEducation.py ChainsOfEducation --format=png
manim -pqh ChainsOfEducation.py ChainsOfEducation --format=png -r 800,800
manim -pqh --disable_caching -s ChainsOfEducation.py ChainsOfEducation
manim -pqh --format=gif --disable_caching ChainsOfEducation.py ChainsOfEducation
    """

    def chapter_1_000(self):
        self.wait(1.0)
        logo = M.SVGMobject(
            r"D:\My\LTTDIT\Python\ChainsOfEducation\ChainsOfEducation\media\SVGs\logo_1",
            stroke_color = "#FFFFFF").scale(2.5)
        self.play(M.Write(logo, run_time = 5.0))
        self.play(M.Unwrite(logo, run_time = 5.0, reverse = False))
        self.wait(1.0)

    def chapter_1_00(self):
        self.wait()
        intro_text = M.Text("Ну что ж ...")
        self.play(M.Write(intro_text, run_time = 3.0))
        self.wait()
        self.play(M.Unwrite(intro_text, run_time = 3.0, reverse = False))
        self.wait()

    def chapter_1_0(self):
        natp = '''0.0 0.0
0.344 0.153
0.77 0.11
1.084 −0.09
1.453 −0.33
1.916 −0.46
2.38 −0.46
2.76 −0.224
3.092 0.12
3.48 0.415
1
3.965 0.444
4.356 0.217
4.416 −0.163
4.073 −0.43
3.624 −0.397
3.234 −0.19
2.806 0.15
2.45 0.347
2.01 0.44
1.594 0.323
1.404 −0.07
1.632 −0.447
1.926 −0.7
2.16 −0.987
2.12 −1.354
1.954 −1.626
1.605 −1.77
1.164 −1.72
0.74 −1.647
0.286 −1.71
−0.074 −1.864
−0.47 −1.97
−0.91 −2.01
−1.363 −2.026
−1.757 −2.055
−2.196 −2.06
−2.62 −2.084
−3.03 −2.16
−3.406 −2.287
−3.776 −2.39
−4.13 −2.51
−4.47 −2.63
−4.806 −2.823
−5.262 −3.03
−5.71 −3.23
−6.303 −3.417
−6.855 −3.546
−7.56 −3.596
−8.25 −3.42
−8.745 −3.236
−9.37 −3.05
−10.2 −2.92
−10.88 −2.93
−12.3 −3.13
−13.38 −3.4
−14.63 −3.51
−15.94 −3.39
−17.16 −3.25
−18.34 −3.26
−19.41 −3.44
−19.02 −2.69
−17.53 −2.45
−15.76 −2.48
−14.21 −2.43
−12.68 −2.35
−11.4 −2.26
−10.08 −2.22
−9.15 −2.17
−8.47 −2.01
−8.04 −1.76
−7.73 −1.42
−8 −1.07
−8.54 −1.04
−9.21 −0.98
−9.9 −0.82
−10.59 −0.52
−9.87 −0.31
−9.18 −0.23
−8.49 −0.17
−7.78 0.13
−7.41 0.5
−7.04 1.09
−6.67 1.8
−6.52 2.56
−6.23 3.36
−5.8 3.89
−5.1 4.215
−4.22 4.26
−3.11 4.43
−2.3 4.88
−1.62 5.76
−1.1 6.85
−0.62 7.89
0.24 8.88
1.36 8.52
2.2 7.7
3 7
3.98 6.55
5.34 6.3
6.78 6.42
7.96 6.75
9.58 7.32
10.73 8.34
12.03 9.35
14.02 9.7
14.63 6.03
15.55 2.48
16.7 −1.52
17.5 −3.35
18.78 −4.55
20.43 −5
22 −4.6
23.68 −3.77
25.17 −2.76
27.18 −2.05
29.8 −1.45
33.17 −1.03
37.2 −0.85
45.4 −0.77
51.1 −1.06
55.05 −1.56'''
        natp_2 = '''−28.27 9.16
−22.34 8.8
−15.17 6.8
−10.8 4.94
−8.53 2.6
−8.46 0.67
−10.35 0.21
−11.38 −0.48
−9.81 −1.23
−8.43 −1.45
−9.24 −1.8
−10.58 −1.79
−12.17 −1.73
−13.78 −2.04
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
−7.98 −4.48
−6.33 −8.76
−8.3 −13.95
−12.83 −15.46
−21.15 −15.55
−29.62 −13.1
−34.18 −7.5
−34.82 −0.65
−33.34 5.15
−29.7 9.07'''
        natp_3 ='''0.0 0.0
0.246 −0.05
0.47 −0.15
1.01 −0.324
1.59 −0.403
2.59 −0.643
3.21 −0.84
3.83 −1.48
3.9 −2.48
2.92 −2.8
1.14 −2.94
−1.49 −3.1
−5.3 −3.41
−9.38 −3.63
−13.5 −4.08
−15.12 −4.04
−15.44 −2.65
−11.72 −2.06
−6.95 −0.06
−5.5 3.16
−1.15 7.62
1.17 8.03
8.35 7.38
14.54 10.47
19.38 −3.51
22.5 −3.38
3
31.85 −0.24
38.13 −0.01
39.7 0.09
40.73 0.16
41.38 0.16'''
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
            coords,
            Tip.TriangleTip(length = 0.3, width = 0.3, fill_opacity = 1.0),
            Tip.EllipseTip(
                length = 0.3, width = 0.3, fill_opacity = 1.0
                ).set_shift_anchors(-0.5, -0.5))
        arrow_2 = ComplexArrow.ComplexArrow(
            coords_2, fill_color = "#987791", fill_opacity = 0.5)
        arrow_3 = ComplexArrow.ComplexArrow(coords_3)
        text_1 = M.Text("человеческие достижения", font_size = 52.0
                        ).move_to(M.DOWN * 4.8 + 14.8 * M.LEFT)
        text_2 = M.Text("сложнейшие\nалгоритмы", font_size = 52.0
                        ).move_to(M.UP * 10.1 + 1.0 * M.RIGHT)
        text_3 = M.Text("новые\nсущности", font_size = 52.0
                        ).move_to(M.UP * 10.9 + 15.6 * M.RIGHT)
        text_4 = M.Text("несуществующие\nзакономерности", font_size = 52.0
                        ).move_to(M.DOWN * 5.9 + 20.9 * M.RIGHT)
        self.add(arrow_2, text_1, text_2, text_3, text_4)
        arrow.prepare_to_create_1()
        #self.camera.frame.set(width = 20.0, height = 12.0)
        anim: list = []
        while not arrow_3.is_created():
            anim.append(M.MoveAlongPath(
                self.camera.frame,
                arrow_3.get_next_curves(1), run_time = 1.0,
                rate_func = M.linear))
        anim_5 = M.Succession(*anim)
        self.play(arrow.get_creating_anim_1().set_run_time(3.0))
        arrow.prepare_to_create_2()
        anims = M.AnimationGroup(
            arrow.get_creating_anim_2().set_run_time(
                28.0).set_rate_func(lambda t: M.smooth(t, 4.0)), anim_5)
        self.play(anims)
        arrow.after_create()
        self.play(M.FadeOut(arrow))
        self.wait(1.0)

    def chapter_1_1(self):
        t = Topic.Topic()
        self.play(t.get_creating_anim_1())
        self.play(t.get_creating_anim_2())
        t.after_create()
        self.play(t.select_topic_block(0))
        self.wait()
        for a in t.show_briefs():
            self.play(a)
            self.wait(0.5)
        self.wait(1.9)
        self.play(t.get_fade_anim(self))
        self.wait(1.0)

    def chapter_1_2(self):
        kb_1 = KB.KnowledgeBlock("Понятия",
        '''Любые объекты, вещи, процессы или явления''')
        self.create_kb_no_descr(kb_1)
        self.update_b(kb_1)
        kb_1.generate_target()
        kb_1.target.move_to(M.UP * 2.2).scale(0.5)
        self.update_b(kb_1, False)
        kb_2 = KB.KnowledgeBlock("Cущность",
        '''Любые объекты, вещи, процессы или явления''')
        self.create_kb_no_descr(kb_2)
        self.update_b(kb_2)
        kb_2.generate_target()
        kb_2.target.move_to(M.UP * 2.2).scale(0.5)
        self.update_b(kb_2, False)
        self.wait(1.0)

    def chapter_1_3(self):
        self.wait(1.0)

    def test_1(self):
        #self.add(M.NumberPlane())
        sv = M.SVGMobject(
            r"D:\My\LTTDIT\Python\ChainsOfEducation\ChainsOfEducation\media\SVGs\tree_1",
            stroke_color = "#FFFFFF").scale(2.5)
        self.play(M.Write(sv, run_time = 5.0))
        
        '''tb = TextBlock.TextBlock(
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
        #self.add(M.ThreeDScene())'''
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
