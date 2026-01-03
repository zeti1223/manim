from manim import *

class TestScene(Scene):
    def construct(self):
        circle = Circle()  # Kör létrehozása
        circle.set_fill(PINK, opacity=0.5)  # Szín beállítása
        
        self.play(Create(circle))  # Animáció lejátszása
        self.wait(2) # Várakozás