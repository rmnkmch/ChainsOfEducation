import manim


class Chain(manim.Line):
    """Chain"""

    def __init__(self, start_func, end_func):
        super().__init__(start_func(), start_func())

        self.get_start_func = start_func
        self.get_end_func = end_func

        self.set_following()

    def set_following(self):
        def update_chain(chain):
            chain.put_start_and_end_on(self.get_start_func(), self.get_end_func())
        self.add_updater(update_chain)
