from manim import *

class PythagorasTetel(Scene):
    def construct(self):
        # MathTex helyett sima Text-et használunk
        cim = Text("Pitagorasz-tétel", font_size=48).to_edge(UP)
        
        # Háromszög pontjai
        p1 = [ -1, -1, 0]
        p2 = [ 2, -1, 0]
        p3 = [ -1, 1, 0]
        
        haromszog = Polygon(p1, p2, p3, color=WHITE)
        
        # MathTex helyett Text
        label_a = Text("a").next_to(Line(p1, p3), LEFT)
        label_b = Text("b").next_to(Line(p1, p2), DOWN)
        label_c = Text("c").next_to(Line(p2, p3), RIGHT).shift(UP * 0.2)
        
        self.play(Write(cim))
        self.play(Create(haromszog))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(2)