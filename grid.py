from manim import *

class createGrid(Scene):
    def construct(self):
        # square1=Square()
        # square1.set_fill(BLUE,opacity=0.5)
        # self.play(Create(square1))

        # square2=Square()
        # square2.set_fill(BLUE,opacity=0.5)
        # square2.next_to(square1,RIGHT,buff=0)
        # self.play(Create(square2))

        # square3=Square()
        # square3.set_fill(BLUE,opacity=0.5)
        # square3.next_to(square1,DOWN,buff=0)
        # self.play(Create(square3))

        # square4=Square()
        # square4.set_fill(BLUE,opacity=0.5)
        # square4.next_to(square2,DOWN,buff=0)
        # self.play(Create(square4))

        # self.wait(2)

        for i in range(3):
            for j in range(3):
                square=Square()
                square.set_fill(BLUE,opacity=0.5)
                square.move_to([j,-i,0])
                self.play(Create(square))

        self.wait(2)
       
