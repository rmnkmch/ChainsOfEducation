import manim
import ComplexArrow
import Tip


class Topic(manim.VGroup):
    """Topic"""

    def __init__(self, *vmobjects, **kwargs):
        super().__init__(*vmobjects, **kwargs)

        xv = [-6.0, -4.0, 0.0, 4.0, 6.0]
        yv = [3.0, 2.8, 3.0, 2.8, 3.0]
        coords = [(x, y, 0.0) for x, y in zip(xv, yv)]
        self.topic_line = ComplexArrow.ComplexArrow(
            coords, Tip.EllipseTip(), Tip.EllipseTip())

    def get_creating_anim_1(self):
        self.topic_line.prepare_to_create_1()
        return self.topic_line.get_creating_anim_1()

    
    def get_creating_anim_2(self):
        self.topic_line.prepare_to_create_2()
        return self.topic_line.get_creating_anim_2()

    '''self.nnn = 0
        def get_start_chain_func():
            n = self.nnn
            self.nnn += 1
            return self.pos_by(x_values[n + 1], y_values[n + 1])
        
        
       
        tb_1 = TopicBlock.TopicBlock(
            "Осознание",
            ["Что такое осознанность?",
             "Несколько\nуниверсальных методов"]).move_to(
                 self.pos_by(- 4.0, 1.9)).scale(0.3)
        tb_1.set_ordinary_chain(get_start_chain_func())
        tb_2 = TopicBlock.TopicBlock("???").move_to(
            self.pos_by(0.0, 1.9)).scale(0.3)
        tb_2.set_ordinary_chain(get_start_chain_func())
        tb_3 = TopicBlock.TopicBlock("???").move_to(
            self.pos_by(4.0, 1.9)).scale(0.3)
        tb_3.set_ordinary_chain(get_start_chain_func())
        grp = [tb_1, tb_2, tb_3]
        anims = []
        for topic_block in grp:
            topic_block.prepare_to_create()
            anims.append(topic_block.get_creating_anim())
        anims = M.AnimationGroup(*anims, lag_ratio = 0.1)
        played = M.AnimationGroup(anim_1, anims, lag_ratio = 0.3)
        self.play(played)
        arrow.after_create()
        for topic_block in grp:
            topic_block.after_create()
        tb_1.generate_target()
        tb_1.target.move_to(1.5 * M.DOWN + 3.0 * M.LEFT).scale(1.0 / 0.3)
        tb_1.target.activate()
        self.play(M.MoveToTarget(tb_1))
        self.play(tb_1.prepare_to_briefs())
        for _ in range(len(tb_1.get_all_briefs_dots())):
            self.play(tb_1.show_next_brief())
        self.wait()
        vgrp_1 = M.VGroup()
        chosed = tb_1.get_center()
        for mob in grp:
            vgrp_1 = M.VGroup(vgrp_1, mob)
            mob.prepare_to_destroy()
        vgrp_1 = M.VGroup(vgrp_1, arrow)
        vgrp_1.generate_target()
        self.camera.frame.generate_target()
        self.camera.frame.target.move_to(chosed).set(width = tb_1.width * 0.5)
        anim_3 = M.MoveToTarget(self.camera.frame)
        self.play(M.FadeOut(vgrp_1, run_time = 1.0), anim_3)'''