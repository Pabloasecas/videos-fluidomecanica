from manim import *
naranja="#FF5900"

class latex(Scene):
    def construct(self):
        latex = Tex(r"\LaTeX", font_size=144)
        self.play(Write(latex))
        self.wait(2)

class notacion_vectorial(Scene):
    def construct(self):
        vector = MathTex(
            r"\mathbf{v}",
            r"=v_x",
            r"\mathbf{e}_x",
            r"+v_y",
            r"\mathbf{e}_y",
            r"+v_z",
            r"\mathbf{e}_z",
            color=naranja,
            font_size=72,
        )
        self.play(Write(vector))

        vector_circle1 = Circle(color=naranja).surround(vector[0], buffer_factor=1.4)
        vector_circle2 = Circle(color=naranja).surround(vector[2], buffer_factor=1.4)
        vector_circle3 = Circle(color=naranja).surround(vector[4], buffer_factor=1.4)
        vector_circle4 = Circle(color=naranja).surround(vector[6], buffer_factor=1.4)

        self.play(Create(vector_circle1),Create(vector_circle2),Create(vector_circle3),Create(vector_circle4))
        self.wait(2)
