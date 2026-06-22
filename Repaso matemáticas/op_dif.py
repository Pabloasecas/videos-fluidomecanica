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
        radio_curva_nivel = np.sqrt((3 - z_punto) / 2)

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
            checkerboard_colors=[azul, azul],
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
        etiqueta_yz = MathTex(
            r"\frac{\partial z}{\partial y}",
            color=azul,
            font_size=48,
        )
        etiqueta_yz.move_to(RIGHT * 1.7 + UP * 1.35)
        grafica_yz = VGroup(axes_yz, axes_yz_labels, parabola_yz, punto_yz, tangente_yz, etiqueta_yz)

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
        etiqueta_xz = MathTex(
            r"\frac{\partial z}{\partial x}",
            color=azul,
            font_size=48,
        )
        etiqueta_xz.move_to(RIGHT * 1.7 + DOWN * 1.45)

        escala_gradiente = 0.18
        vector_gradiente = Arrow3D(
            start=axes.c2p(x_punto, y_punto, z_punto),
            end=axes.c2p(
                x_punto + escala_gradiente * pendiente_xz,
                y_punto + escala_gradiente * pendiente_yz,
                z_punto,
            ),
            color=naranja,
            thickness=0.025,
            height=0.18,
            base_radius=0.06,
        )

        axes_xy = Axes(
            x_range=[-1.35, 1.35, 0.5],
            y_range=[-1.35, 1.35, 0.5],
            x_length=5.0,
            y_length=5.0,
            axis_config={"color": WHITE, "include_numbers": False, "tip_width": 0.12, "tip_height": 0.12},
            tips=True,
        )
        axes_xy.move_to(ORIGIN + DOWN * 0.25)
        axes_xy_labels = axes_xy.get_axis_labels(
            MathTex("x", color=WHITE, font_size=36),
            MathTex("y", color=WHITE, font_size=36),
        )
        curva_xy = ParametricFunction(
            lambda theta: axes_xy.c2p(
                radio_curva_nivel * np.cos(theta),
                radio_curva_nivel * np.sin(theta),
            ),
            t_range=[0, TAU],
            color=azul,
            stroke_width=6,
        )
        punto_xy = Dot(
            axes_xy.c2p(x_punto, y_punto),
            radius=0.08,
            color=YELLOW,
        )
        escala_vector_xy = 0.18
        vector_xy = Arrow(
            axes_xy.c2p(x_punto, y_punto),
            axes_xy.c2p(
                x_punto + escala_vector_xy * pendiente_xz,
                y_punto + escala_vector_xy * pendiente_yz,
            ),
            buff=0,
            color=naranja,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.22,
        )
        etiqueta_vector_xy = MathTex(
            r"\left(\frac{\partial z}{\partial x},\frac{\partial z}{\partial y}\right)",
            color=naranja,
            font_size=42,
        )
        etiqueta_vector_xy.to_edge(DOWN, buff=0.35)
        nombre_gradiente_xy = MathTex(
            r"\nabla z",
            color=naranja,
            font_size=36,
        )
        nombre_gradiente_xy.next_to(punto_xy, UR, buff=0.12)
        etiqueta_curva_xy = MathTex(
            r"z=\frac{3}{4}",
            color=azul,
            font_size=38,
        )
        etiqueta_curva_xy.next_to(curva_xy, LEFT, buff=0.25)

        grafica = VGroup(axes, axes_labels, paraboloide, punto, curva_nivel, curva_nivel_xz, vector_gradiente)
        grafica.scale(1.425)
        grafica.move_to(LEFT * 3.0 + DOWN * 1.15)

        self.add_fixed_in_frame_mobjects(
            axes_yz,
            axes_yz_labels,
            parabola_yz,
            punto_yz,
            tangente_yz,
            etiqueta_yz,
            axes_xz,
            axes_xz_labels,
            parabola_xz,
            punto_xz,
            tangente_xz,
            etiqueta_xz,
            axes_xy,
            axes_xy_labels,
            curva_xy,
            punto_xy,
            vector_xy,
            etiqueta_vector_xy,
            nombre_gradiente_xy,
            etiqueta_curva_xy,
        )
        axes_yz.set_opacity(0)
        axes_yz_labels.set_opacity(0)
        parabola_yz.set_stroke(opacity=0)
        punto_yz.set_opacity(0)
        tangente_yz.set_stroke(opacity=0)
        etiqueta_yz.set_opacity(0)
        axes_xz.set_opacity(0)
        axes_xz_labels.set_opacity(0)
        parabola_xz.set_stroke(opacity=0)
        punto_xz.set_opacity(0)
        tangente_xz.set_stroke(opacity=0)
        etiqueta_xz.set_opacity(0)
        axes_xy.set_opacity(0)
        axes_xy_labels.set_opacity(0)
        curva_xy.set_stroke(opacity=0)
        punto_xy.set_opacity(0)
        vector_xy.set_opacity(0)
        etiqueta_vector_xy.set_opacity(0)
        nombre_gradiente_xy.set_opacity(0)
        etiqueta_curva_xy.set_opacity(0)

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
        self.play(
            etiqueta_yz.animate.set_opacity(1),
            etiqueta_xz.animate.set_opacity(1),
            run_time=1.5,
        )
        self.play(Create(vector_gradiente), run_time=2)
        self.wait(2)
        self.play(
            FadeOut(grafica),
            axes_yz.animate.set_opacity(0),
            axes_yz_labels.animate.set_opacity(0),
            parabola_yz.animate.set_stroke(opacity=0),
            punto_yz.animate.set_opacity(0),
            tangente_yz.animate.set_stroke(opacity=0),
            etiqueta_yz.animate.set_opacity(0),
            axes_xz.animate.set_opacity(0),
            axes_xz_labels.animate.set_opacity(0),
            parabola_xz.animate.set_stroke(opacity=0),
            punto_xz.animate.set_opacity(0),
            tangente_xz.animate.set_stroke(opacity=0),
            etiqueta_xz.animate.set_opacity(0),
            run_time=2,
        )
        self.play(
            axes_xy.animate.set_opacity(1),
            axes_xy_labels.animate.set_opacity(1),
            curva_xy.animate.set_stroke(opacity=1),
            punto_xy.animate.set_opacity(1),
            vector_xy.animate.set_opacity(1),
            etiqueta_vector_xy.animate.set_opacity(1),
            nombre_gradiente_xy.animate.set_opacity(1),
            etiqueta_curva_xy.animate.set_opacity(1),
            run_time=2,
        )
        self.wait(5)

























