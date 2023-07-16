import manim


class Chain(manim.Line):
    """Chain"""

    def __init__(self, start_func, end_func):
        super().__init__(start_func(), end_func())

        self.get_start_func = start_func
        self.get_end_func = end_func
        self.start_dot = manim.Dot(start_func())
        self.end_dot = manim.Dot(end_func())

        self.start_follow()

    def start_follow(self):
        self.add_updater(Chain.update_chain)

    def stop_follow(self):
        self.remove_updater(Chain.update_chain)

    def update_chain(self):
        self.put_start_and_end_on(self.get_start_func(), self.get_end_func())
        self.start_dot.move_to(self.get_start_func())
        self.end_dot.move_to(self.get_end_func())
