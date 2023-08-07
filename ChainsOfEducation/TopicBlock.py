import manim
import Chain


class TopicBlock(manim.RoundedRectangle):
    """TopicBlock"""

    def __init__(
        self,
        title: str = "TopicBlock",
        briefs: list = [],
        height: float = 4.0,
        width: float = 8.0,
        corner_radius: float = 1.8,
        fill_color = "#777777",
        fill_opacity = 0.2,
        stroke_color = "#FFFFFF",
        stroke_opacity = 1.0,
        stroke_width = 4,
        background_stroke_color = "#000000",
        background_stroke_opacity = 1.0,
        background_stroke_width = 0,
        **kwargs):
        super().__init__(
            height = height,
            width = width,
            corner_radius = corner_radius,
            fill_color = fill_color,
            fill_opacity = fill_opacity,
            stroke_color = stroke_color,
            stroke_opacity = stroke_opacity,
            stroke_width = stroke_width,
            background_stroke_color = background_stroke_color,
            background_stroke_opacity = background_stroke_opacity,
            background_stroke_width = background_stroke_width,
            **kwargs)

        self.title = manim.Text(title, font_size = 56.0, weight = manim.BOLD)
        self.title_underline = manim.Underline(self.title)
        self.add(self.title, self.title_underline)

        self.chain_line = None

        self.briefs = []
        self.brief_shown = 0
        for brief in briefs:
            offset = (len(briefs) - 1) * 0.25
            if len(briefs) <= 1: offset = 0.0
            d = manim.Dot().move_to(
                manim.DOWN + manim.RIGHT
                * (0.5 * briefs.index(brief) - offset))
            self.briefs.append(d)
            self.add(d)
            dtext = manim.Text(brief, font_size = 32.0)
            self.briefs.append(dtext)

        self.deactivate()

    def get_title_pos(self):
        return (self.get_center() + manim.UP
                * (self.height * 0.5 - self.title.height * 0.5 - 0.3))

    def get_underline_pos(self):
        return (self.get_center() + manim.UP
                * (self.height * 0.5 - self.title.height - 0.4))

    def get_all_briefs(self):
        return self.briefs

    def get_all_briefs_dots(self):
        return self.get_all_briefs()[::2]

    def get_all_briefs_texts(self):
        return self.get_all_briefs()[1::2]

    def get_briefs_pos(self):
        ret = []
        vert = (self.get_center() + 3.0 * manim.LEFT
                + manim.UP * (0.5 * self.height - self.title.height - 0.5))
        hor = manim.DOWN * ((self.height - self.title.height - 0.5)
               / (len(self.get_all_briefs_dots()) + 1))
        for brief in self.get_all_briefs_dots():
            ret.append(vert + hor + hor * self.get_all_briefs_dots().index(brief))
        return ret

    def prepare_to_briefs(self):
        self.generate_target()
        self.target.title.move_to(self.get_title_pos())
        self.target.title_underline.move_to(self.get_underline_pos())
        ret = manim.AnimationGroup(manim.MoveToTarget(self))
        for brief in self.get_all_briefs_dots():
            brief.generate_target()
            brief.target.move_to(
                self.get_briefs_pos()[self.get_all_briefs_dots().index(brief)])
            ret = manim.AnimationGroup(ret, manim.MoveToTarget(brief))
        return ret

    def show_next_brief(self):
        br = self.get_all_briefs_texts()[self.brief_shown]
        br.next_to(self.get_all_briefs_dots()[self.brief_shown])
        if self.brief_shown + 1 < len(self.get_all_briefs_texts()):
            self.brief_shown += 1
        return manim.FadeIn(br)

    def get_chain_end(self):
        return self.point_from_proportion(0.2)

    def set_ordinary_chain(self, start):
        self.chain_line = Chain.Chain(start, self.get_chain_end())

    def make_chain_redrawable(self):
        self.chain_line.add_updater(
            lambda m: self.chain_line.become(
                Chain.Chain(
                    self.chain_line.get_start(), self.get_chain_end())))

    def deactivate(self):
        self.set_fill(opacity = 0.1)
        self.set_stroke(opacity = 0.75)
        self.title.set_fill(opacity = 0.2)
        self.title.set_stroke(opacity = 0.5)
        self.title_underline.set_fill(opacity = 0.2)
        self.title_underline.set_stroke(opacity = 0.5)

    def activate(self):
        self.set_fill(opacity = 0.2)
        self.set_stroke(opacity = 1.0)
        self.title.set_fill(opacity = 1.0)
        self.title.set_stroke(opacity = 1.0)
        self.title_underline.set_fill(opacity = 1.0)
        self.title_underline.set_stroke(opacity = 1.0)
        for dot in self.get_all_briefs_dots():
            dot.set_fill(opacity = 1.0)

    def prepare_to_create(self):
        self.chain_line.prepare_to_create()
        for br in self.get_all_briefs_texts():
            self.remove(br)

    def get_creating_anim(self):
        return manim.AnimationGroup(
            self.chain_line.get_creating_anim(),
            manim.Create(self, lag_ratio = 0.1),
            lag_ratio = 0.5)

    def after_create(self):
        self.chain_line.after_create()
        self.make_chain_redrawable()

    def prepare_to_destroy(self):
        self.chain_line.clear_updaters()
        self.add(self.chain_line)
        for br in self.get_all_briefs_texts():
            self.add(br)
