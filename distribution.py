from manim import *

class MuveletSorrend(Scene):
    def construct(self):
        # 1. Alap képlet
        eq1 = MathTex("(a", "+", "b)^2")
        eq1.scale(1.5)
        self.play(Write(eq1))
        self.wait(1)

        # 2. Átalakítás szorzattá: (a+b)(a+b)
        # Felbontjuk a négyzetet két zárójelre
        eq2 = MathTex("(a", "+", "b)", "(a", "+", "b)")
        eq2.scale(1.5)
        
        # A transzformáció vizuálisan megmutatja a négyzetre emelés jelentését
        self.play(ReplacementTransform(eq1, eq2))
        self.wait(1)

        # 3. Kifejtés: a*a + a*b + b*a + b*b
        # Színezzük be a tagokat, hogy követhető legyen az ív
        eq3 = MathTex("a^2", "+", "ab", "+", "ba", "+", "b^2")
        eq3.scale(1.5)
        
        # Animáljuk a "szétrepülést"
        self.play(ReplacementTransform(eq2, eq3))
        self.wait(1)

        # 4. Összevonás: a^2 + 2ab + b^2
        eq4 = MathTex("a^2", "+", "2ab", "+", "b^2")
        eq4.scale(1.5)
        eq4.set_color(YELLOW)

        # Kiemeljük az ab és ba tagokat mielőtt összeolvadnak
        self.play(
            eq3[2].animate.set_color(ORANGE),
            eq3[4].animate.set_color(ORANGE)
        )
        self.wait(0.5)
        
        # Az ab + ba -> 2ab átmenet
        self.play(ReplacementTransform(eq3, eq4))
        self.wait(1)

        # Végső keretezés
        rect = SurroundingRectangle(eq4, color=BLUE, buff=0.3)
        self.play(Create(rect))
        self.wait(2)