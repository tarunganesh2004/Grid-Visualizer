from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle=Circle() # Create a circle
        circle.set_fill(PINK,opacity=0.5) # Set color and transparency
        self.play(Create(circle)) # show the circle

        # Create a circle with a specific radius
        c=Circle(radius=0.2)
        c.set_fill(BLUE,opacity=1)
        self.play(Create(c))

class CreateSquare(Scene):
    def construct(self):
        circle=Circle()
        circle.set_fill(PINK,opacity=0.5)

        # Transform a circle into a square
        square=Square()
        square.rotate(PI/4) # rotate square
        self.play(Create(circle))
        self.play(Transform(circle, square))

        self.play(Create(square)) # create square
        self.play(Transform(square,circle)) # transform square into circle
        self.play(FadeOut(square)) # fade out square
        self.play(FadeOut(circle))
