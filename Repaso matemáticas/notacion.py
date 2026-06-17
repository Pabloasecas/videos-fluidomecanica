from manim import *
naranja="#FF5900"
azul="#00AEEF"
verde="#27F5B0"

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
            x_range=[-1, 6, 1],
            y_range=[-1, 4, 1],
            x_length=7,
            y_length=5,
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
        perpendicular_line = Line(
            axes.c2p(7 / 3, -1),
            axes.c2p(2 / 3, 4),
            color=WHITE,
        )
        projection_vector = Arrow(
            axes.c2p(0, 0),
            axes.c2p(9 / 5, 3 / 5),
            buff=0,
            color=verde,
        )
        scaled_projection_vector = Arrow(
            axes.c2p(0, 0),
            axes.c2p(9 * np.sqrt(10) / 5, 3 * np.sqrt(10) / 5),
            buff=0,
            color=verde,
        )
        label_w = MathTex(r"\mathbf{w}", color=verde).next_to(
            scaled_projection_vector.get_end(), UP
        )
        product_equality = MathTex(
            r"\lVert\mathbf{w}\rVert",
            r"=",
            r"\mathbf{u}\cdot\mathbf{v}",
            font_size=48,
        ).to_edge(RIGHT)
        product_equality[0].set_color(verde)
        product_equality[2].set_color(naranja)

        self.play(FadeOut(prod_esc2))
        self.play(Write(axes), Write(axes_labels))
        self.play(GrowArrow(vector_u), GrowArrow(vector_v))
        self.play(Write(label_u), Write(label_v))
        self.wait(2)
        self.play(Create(perpendicular_line))
        self.wait(2)
        self.play(GrowArrow(projection_vector))
        self.wait(2)
        self.play(Transform(projection_vector, scaled_projection_vector))
        self.play(Write(label_w))
        self.wait(2)

        graph = VGroup(
            axes,
            axes_labels,
            vector_u,
            vector_v,
            label_u,
            label_v,
            perpendicular_line,
            projection_vector,
            label_w,
        )
        self.play(graph.animate.shift(LEFT * 2))
        self.play(Write(product_equality))
        self.wait(2)

class producto_vectorial(Scene):
    def construct(self):
        prod_vec1 = MathTex(
            r"\mathbf{u}\times\mathbf{v}",
            r"=",
            r"\begin{vmatrix}"
            r"\mathbf{e}_x&\mathbf{e}_y&\mathbf{e}_z\\"
            r"u_x&u_y&u_z\\"
            r"v_x&v_y&v_z"
            r"\end{vmatrix}",
            color=naranja,
            font_size=72,
        )
        self.play(Write(prod_vec1))
        self.wait(2)

        prod_vec2 = MathTex(
            r"\lVert\mathbf{u}\times\mathbf{v}\rVert",
            r"=",
            r"\lVert\mathbf{u}\rVert",
            r"\lVert\mathbf{v}\rVert",
            r"\sin(\theta)",
            color=naranja,
            font_size=72,
        )
        self.play(TransformMatchingTex(prod_vec1, prod_vec2), run_time=3)
        self.wait(2)

        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-1, 4, 1],
            x_length=7,
            y_length=5,
            axis_config={"color": azul, "include_numbers": True},
            tips=True,
        )
        axes_labels = axes.get_axis_labels(
            MathTex("x", color=azul),
            MathTex("y", color=azul),
        )

        u_angle = ValueTracker(0)
        v_angle = ValueTracker(0)
        u_base = np.array([1, 3])
        v_base = np.array([3, 1])

        def rotate_vector(vector, angle):
            rotation_matrix = np.array(
                [
                    [np.cos(angle), -np.sin(angle)],
                    [np.sin(angle), np.cos(angle)],
                ]
            )
            return rotation_matrix @ vector

        def get_u_coords():
            return rotate_vector(u_base, u_angle.get_value())

        def get_v_coords():
            return rotate_vector(v_base, v_angle.get_value())

        def get_cross_product_module():
            u = get_u_coords()
            v = get_v_coords()
            return abs(u[0] * v[1] - u[1] * v[0])

        vector_u = always_redraw(
            lambda: Arrow(
                axes.c2p(0, 0),
                axes.c2p(*get_u_coords()),
                buff=0,
                color=naranja,
            ).set_z_index(2)
        )
        vector_v = always_redraw(
            lambda: Arrow(
                axes.c2p(0, 0),
                axes.c2p(*get_v_coords()),
                buff=0,
                color=naranja,
            ).set_z_index(2)
        )
        label_u = always_redraw(
            lambda: MathTex(r"\mathbf{u}", color=naranja).next_to(
                vector_u.get_end(), RIGHT
            ).set_z_index(3)
        )
        label_v = always_redraw(
            lambda: MathTex(r"\mathbf{v}", color=naranja).next_to(
                vector_v.get_end(), UP
            ).set_z_index(3)
        )
        area = always_redraw(
            lambda: Polygon(
                axes.c2p(0, 0),
                axes.c2p(*get_u_coords()),
                axes.c2p(*(get_u_coords() + get_v_coords())),
                axes.c2p(*get_v_coords()),
                color=WHITE,
                fill_color=WHITE,
                fill_opacity=0.25,
            ).set_z_index(1)
        )
        cross_product_label = MathTex(
            r"\lVert\mathbf{u}\times\mathbf{v}\rVert",
            r"=",
            color=WHITE,
            font_size=44,
        )
        cross_product_value = DecimalNumber(
            get_cross_product_module(),
            num_decimal_places=2,
            font_size=44,
            color=WHITE,
        )
        cross_product_value.previous_value = get_cross_product_module()

        def update_cross_product_value(number):
            current_value = get_cross_product_module()
            number.set_value(current_value)
            if current_value > number.previous_value + 0.01:
                number.set_color(GREEN)
            elif current_value < number.previous_value - 0.01:
                number.set_color(RED)
            number.previous_value = current_value

        cross_product_value.add_updater(update_cross_product_value)
        cross_product_marker = VGroup(
            cross_product_label,
            cross_product_value,
        ).arrange(RIGHT).to_edge(RIGHT)

        self.play(FadeOut(prod_vec2))
        self.play(Write(axes), Write(axes_labels))
        self.play(GrowArrow(vector_u), GrowArrow(vector_v))
        self.play(Write(label_u), Write(label_v))
        self.play(Create(area))
        self.play(Write(cross_product_marker))
        self.play(
            u_angle.animate.set_value(5 * DEGREES),
            v_angle.animate.set_value(-5 * DEGREES),
            run_time=2,
        )
        self.play(
            u_angle.animate.set_value(-5 * DEGREES),
            v_angle.animate.set_value(5 * DEGREES),
            run_time=4,
        )
        self.play(
            u_angle.animate.set_value(0),
            v_angle.animate.set_value(0),
            run_time=2,
        )
        self.wait(2)

class campo_escalar(Scene):
    def construct(self):
        title = Tex("Campo escalar de presiones", font_size=44, color=naranja)
        title.to_edge(UP)

        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=8,
            y_length=4.8,
            axis_config={"color": WHITE, "include_numbers": False},
            tips=True,
        ).shift(LEFT * 0.5 + DOWN * 0.15)

        x_min, x_max = -3, 3
        y_min, y_max = -2, 2
        nx, ny = 42, 28
        dx = (x_max - x_min) / nx
        dy = (y_max - y_min) / ny

        def pressure(x, y):
            high_pressure = 1.4 * np.exp(-((x + 1.2) ** 2 + (y - 0.6) ** 2) / 0.55)
            low_pressure = 0.9 * np.exp(-((x - 1.1) ** 2 + (y + 0.55) ** 2) / 0.75)
            gradient = 0.18 * x - 0.08 * y
            return high_pressure - low_pressure + gradient

        sample_points = [
            (
                x_min + (i + 0.5) * dx,
                y_min + (j + 0.5) * dy,
            )
            for i in range(nx)
            for j in range(ny)
        ]
        pressure_values = [pressure(x, y) for x, y in sample_points]
        min_pressure = min(pressure_values)
        max_pressure = max(pressure_values)

        def pressure_color(value):
            alpha = inverse_interpolate(min_pressure, max_pressure, value)
            return color_gradient(
                [BLUE_E, azul, verde, YELLOW, naranja, RED_E],
                100,
            )[int(np.clip(alpha, 0, 0.999) * 100)]

        cells = VGroup()
        for x, y in sample_points:
            cell = Rectangle(
                width=axes.x_axis.unit_size * dx,
                height=axes.y_axis.unit_size * dy,
                stroke_width=0,
                fill_color=pressure_color(pressure(x, y)),
                fill_opacity=0.92,
            )
            cell.move_to(axes.c2p(x, y))
            cells.add(cell)

        field_label = MathTex(
            r"p(x,y)",
            r"\;[\mathrm{Pa}]",
            color=naranja,
            font_size=44,
        ).next_to(axes, DOWN, buff=0.35)

        legend = VGroup()
        legend_steps = 28
        for i in range(legend_steps):
            value = min_pressure + (max_pressure - min_pressure) * i / (legend_steps - 1)
            bar_cell = Rectangle(
                width=0.28,
                height=4.8 / legend_steps,
                stroke_width=0,
                fill_color=pressure_color(value),
                fill_opacity=1,
            )
            legend.add(bar_cell)
        legend.arrange(UP, buff=0).next_to(axes, RIGHT, buff=0.6)

        legend_title = MathTex("p", color=naranja, font_size=34).next_to(legend, UP, buff=0.15)
        high_label = Tex("alta", color=naranja, font_size=26).next_to(legend, RIGHT, buff=0.18).align_to(legend, UP)
        low_label = Tex("baja", color=naranja, font_size=26).next_to(legend, RIGHT, buff=0.18).align_to(legend, DOWN)
        legend_group = VGroup(legend, legend_title, high_label, low_label)

        self.play(Write(title))
        self.play(FadeIn(cells), Write(axes), run_time=2)
        self.play(Write(field_label))
        self.play(FadeIn(legend_group, shift=LEFT * 0.2))
        self.wait(2)
