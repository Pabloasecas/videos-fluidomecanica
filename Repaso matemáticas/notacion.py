from manim import *
naranja="#FF5900"
azul="#00AEEF"

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

class producto_escalar(Scene):
    def construct(self):
        prod_esc1 = MathTex(
            r"\mathbf{u}\cdot\mathbf{v}",
            r"=",
            r"u_xv_x+u_yv_y+u_zv_z",
            color=naranja,
            font_size=72,
        )
        self.play(Write(prod_esc1))
        self.wait(2)

        prod_esc2 = MathTex(
            r"\mathbf{u}\cdot\mathbf{v}",
            r"=",
            r"\lVert\mathbf{u}\rVert",
            r"\lVert\mathbf{v}\rVert",
            r"\cos(\theta)",
            color=naranja,
            font_size=72,
        )
        self.play(TransformMatchingTex(prod_esc1, prod_esc2))
        self.wait(2)

        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[-1, 4, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": azul, "include_numbers": True},
            tips=True,
        )
        axes_labels = axes.get_axis_labels(
            MathTex("x", color=azul),
            MathTex("y", color=azul),
        )

        vector_u = Arrow(
            axes.c2p(0, 0),
            axes.c2p(1, 3),
            buff=0,
            color=naranja,
        )
        vector_v = Arrow(
            axes.c2p(0, 0),
            axes.c2p(3, 1),
            buff=0,
            color=naranja,
        )
        label_u = MathTex(r"\mathbf{u}", color=naranja).next_to(
            vector_u.get_end(), RIGHT
        )
        label_v = MathTex(r"\mathbf{v}", color=naranja).next_to(
            vector_v.get_end(), UP
        )

        self.play(FadeOut(prod_esc2))
        self.play(Write(axes), Write(axes_labels))
        self.play(GrowArrow(vector_u), GrowArrow(vector_v))
        self.play(Write(label_u), Write(label_v))
        self.wait(2)
