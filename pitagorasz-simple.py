from manim import *

class PythagorasTetel(Scene):
    def construct(self):
        # Cím
        cim = Text("Pitagorasz-tétel", font_size=48).to_edge(UP)
        
        # Háromszög pontjai
        p1 = [-1, -1, 0] # Derékszögú csúcs
        p2 = [ 2, -1, 0] # b oldal vége
        p3 = [-1, 1, 0]  # a oldal vége
        
        haromszog = Polygon(p1, p2, p3, color=WHITE)
        
        # Oldalak feliratozása
        # A buff=0.1 közelebb viszi a betűt a vonalhoz
        label_a = Text("a").next_to(Line(p1, p3), LEFT, buff=0.2)
        label_b = Text("b").next_to(Line(p1, p2), DOWN, buff=0.2)
        
        # A 'c' betű pozicionálása az átfogó (p2-p3) mentén, kisebb buff-al
        label_c = Text("c").next_to(Line(p2, p3), UR, buff=-0.3).shift(LEFT * 0.2)
        
        # Derékszög jelölése (opcionális, de szebb)
        derekszog = RightAngle(Line(p1, p2), Line(p1, p3), length=0.3, quadrant=(1,1))

        # Egyenlet alul (MathTex-et használtam a szép négyzetre emeléshez)
        egyenlet = MathTex("a^2 + b^2 = c^2", font_size=54).to_edge(DOWN, buff=1)
        
        # Animációk
        self.play(Write(cim))
        self.play(Create(haromszog), Create(derekszog))
        self.play(
            Write(label_a), 
            Write(label_b), 
            Write(label_c)
        )
        self.wait(1)
        self.play(Write(egyenlet))
        self.wait(3)