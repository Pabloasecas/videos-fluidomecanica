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

        x_punto = 3 / 4
        y_punto = -3 / 4
        z_punto = 3 / 4
        radio_corte = np.sqrt(3 / 2)
        radio_nivel = np.sqrt((3 - 2 * x_punto**2) / 2)
        radio_nivel_xz = np.sqrt((3 - 2 * y_punto**2) / 2)

        axes = ThreeDAxes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            z_range=[0, 3.5, 0.5],
            x_length=4.4,
            y_length=4.4,
            z_length=3.0,
            axis_config={"color": WHITE},
        )
        axes_labels = axes.get_axis_labels(
            MathTex("x", color=WHITE, font_size=30),
            MathTex("y", color=WHITE, font_size=30),
            MathTex("z", color=WHITE, font_size=30),
        )

        paraboloide = Surface(
            lambda r, theta: axes.c2p(
                r * np.cos(theta),
                r * np.sin(theta),
                3 - 2 * r**2,
            ),
            u_range=[0, radio_corte],
            v_range=[0, TAU],
            resolution=(12, 32),
            fill_color=azul,
            fill_opacity=0.75,
            checkerboard_colors=[azul, verde],
            stroke_color=WHITE,
            stroke_width=0.35,
        )

        punto = Dot3D(
            point=axes.c2p(x_punto, y_punto, z_punto),
            radius=0.08,
            color=YELLOW,
        )

        curva_nivel = ParametricFunction(
            lambda y: axes.c2p(
                x_punto,
                y,
                3 - 2 * x_punto**2 - 2 * y**2,
            ),
            t_range=[-radio_nivel, radio_nivel],
            color=naranja,
            stroke_width=5,
        )

        curva_nivel_xz = ParametricFunction(
            lambda x: axes.c2p(
                x,
                y_punto,
                3 - 2 * x**2 - 2 * y_punto**2,
            ),
            t_range=[-radio_nivel_xz, radio_nivel_xz],
            color=naranja,
            stroke_width=5,
        )

        axes_yz = Axes(
            x_range=[-1.35, 1.35, 0.5],
            y_range=[-0.1, 2.25, 0.5],
            x_length=3.1,
            y_length=2.6,
            axis_config={"color": WHITE, "include_numbers": False, "tip_width": 0.12, "tip_height": 0.12},
            tips=True,
        )
        axes_yz.to_corner(UR, buff=0.6).shift(DOWN * 0.65)
        axes_yz_labels = axes_yz.get_axis_labels(
            MathTex("y", color=WHITE, font_size=32),
            MathTex("z", color=WHITE, font_size=32),
        )
        parabola_yz = axes_yz.plot(
            lambda y: 3 - 2 * x_punto**2 - 2 * y**2,
            x_range=[-radio_nivel, radio_nivel],
            color=naranja,
            stroke_width=5,
        )
        parabola_yz.set_fill(opacity=0)
        punto_yz = Dot(
            axes_yz.c2p(y_punto, z_punto),
            radius=0.07,
            color=YELLOW,
        )
        pendiente_yz = -4 * y_punto
        tangente_yz = axes_yz.plot(
            lambda y: z_punto + pendiente_yz * (y - y_punto),
            x_range=[y_punto - 0.32, y_punto + 0.32],
            color=azul,
            stroke_width=5,
        )
        tangente_yz.set_fill(opacity=0)
        grafica_yz = VGroup(axes_yz, axes_yz_labels, parabola_yz, punto_yz, tangente_yz)

        axes_xz = Axes(
            x_range=[-1.35, 1.35, 0.5],
            y_range=[-0.1, 2.25, 0.5],
            x_length=3.1,
            y_length=2.6,
            axis_config={"color": WHITE, "include_numbers": False, "tip_width": 0.12, "tip_height": 0.12},
            tips=True,
        )
        axes_xz.to_corner(DR, buff=0.6).shift(UP * 0.55)
        axes_xz_labels = axes_xz.get_axis_labels(
            MathTex("x", color=WHITE, font_size=32),
            MathTex("z", color=WHITE, font_size=32),
        )
        parabola_xz = axes_xz.plot(
            lambda x: 3 - 2 * x**2 - 2 * y_punto**2,
            x_range=[-radio_nivel_xz, radio_nivel_xz],
            color=naranja,
            stroke_width=5,
        )
        parabola_xz.set_fill(opacity=0)
        punto_xz = Dot(
            axes_xz.c2p(x_punto, z_punto),
            radius=0.07,
            color=YELLOW,
        )
        pendiente_xz = -4 * x_punto
        tangente_xz = axes_xz.plot(
            lambda x: z_punto + pendiente_xz * (x - x_punto),
            x_range=[x_punto - 0.32, x_punto + 0.32],
            color=azul,
            stroke_width=5,
        )
        tangente_xz.set_fill(opacity=0)

        grafica = VGroup(axes, axes_labels, paraboloide, punto, curva_nivel, curva_nivel_xz)
        grafica.scale(0.95)
        grafica.move_to(LEFT * 3.0 + DOWN * 1.15)

        self.add_fixed_in_frame_mobjects(
            axes_yz,
            axes_yz_labels,
            parabola_yz,
            punto_yz,
            tangente_yz,
            axes_xz,
            axes_xz_labels,
            parabola_xz,
            punto_xz,
            tangente_xz,
        )
        axes_yz.set_opacity(0)
        axes_yz_labels.set_opacity(0)
        parabola_yz.set_stroke(opacity=0)
        punto_yz.set_opacity(0)
        tangente_yz.set_stroke(opacity=0)
        axes_xz.set_opacity(0)
        axes_xz_labels.set_opacity(0)
        parabola_xz.set_stroke(opacity=0)
        punto_xz.set_opacity(0)
        tangente_xz.set_stroke(opacity=0)

        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES, zoom=0.8)
        self.play(Write(titulo))
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(paraboloide), run_time=3)
        self.play(FadeIn(punto, scale=1.5), run_time=1)
        self.play(Create(curva_nivel), run_time=2)
        self.wait(1)
        self.play(
            axes_yz.animate.set_opacity(1),
            axes_yz_labels.animate.set_opacity(1),
            parabola_yz.animate.set_stroke(opacity=1),
            punto_yz.animate.set_opacity(1),
            run_time=2,
        )
        self.wait(2)
        self.play(Create(curva_nivel_xz), run_time=2)
        self.wait(1)
        self.play(
            axes_xz.animate.set_opacity(1),
            axes_xz_labels.animate.set_opacity(1),
            parabola_xz.animate.set_stroke(opacity=1),
            punto_xz.animate.set_opacity(1),
            run_time=2,
        )
        self.wait(1)
        self.play(
            tangente_yz.animate.set_stroke(opacity=1),
            tangente_xz.animate.set_stroke(opacity=1),
            run_time=2,
        )
        self.wait(5)

















