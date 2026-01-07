from manim import *

class ImplicitFunctionExample(Scene):
    def construct(self):
        graph = ImplicitFunction(
            lambda x, y: x ** y, 
            color=YELLOW
        )
        self.add(NumberPlane(), graph)
        self.play(Create(graph))
        self.wait(2)