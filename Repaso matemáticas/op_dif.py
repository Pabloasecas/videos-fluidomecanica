from manim import *
naranja="#FF5900"
azul="#00AEEF"
verde="#27F5B0"

class nabla(Scene):
    def construct(self):
        titulo = Tex("Operador nabla", color=naranja, font_size=56)
        titulo.to_edge(UP)

        definicion = MathTex(
            r"\nabla",
            r"=",
            r"\frac{\partial}{\partial x}\,\mathbf{e}_x",
            r"+",
            r"\frac{\partial}{\partial y}\,\mathbf{e}_y",
            r"+",
            r"\frac{\partial}{\partial z}\,\mathbf{e}_z",
            color=naranja,
            font_size=66,
        )
        definicion.move_to(ORIGIN)
        definicion[0].set_color(naranja)

        caja = SurroundingRectangle(definicion, color=naranja, buff=0.35)

        self.play(Write(titulo))
        self.play(Write(definicion), run_time=3)
        self.play(Create(caja))
        self.wait(3)

class gradiente(ThreeDScene):
    def construct(self):
        titulo = Tex("Gradiente", color=naranja, font_size=56)
        titulo.to_edge(UP)
        self.add_fixed_in_frame_mobjects(titulo)

        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[0, 5, 1],
            x_length=6,
            y_length=6,
            z_length=4,
            axis_config={"color": WHITE},
        )
        axes_labels = axes.get_axis_labels(
            MathTex("x", color=WHITE),
            MathTex("y", color=WHITE),
            MathTex("z", color=WHITE),
        )

        paraboloide = Surface(
            lambda u, v: axes.c2p(u, v, 0.35 * (u**2 + v**2)),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(32, 32),
            fill_color=azul,
            fill_opacity=0.75,
            checkerboard_colors=[azul, verde],
            stroke_color=WHITE,
            stroke_width=0.35,
        )

        etiqueta_funcion = MathTex(
            r"f(x,y)=x^2+y^2",
            color=naranja,
            font_size=42,
        )
        etiqueta_funcion.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(etiqueta_funcion)

        self.set_camera_orientation(phi=62 * DEGREES, theta=-45 * DEGREES, zoom=0.85)
        self.play(Write(titulo))
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(paraboloide), Write(etiqueta_funcion), run_time=3)
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(5)
        self.stop_ambient_camera_rotation()
