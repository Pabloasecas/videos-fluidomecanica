from manim import *
naranja="#FF5900"
azul="#00AEEF"
verde="#27F5B0"

class latex(Scene):
    def construct(self):
        latex = Tex(r"\LaTeX", font_size=144, color=naranja)
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
        ).shift(LEFT * 0.5 + DOWN * 0.45)

        x_min, x_max = -3, 3
        y_min, y_max = -2, 2
        nx, ny = 42, 28
        dx = (x_max - x_min) / nx
        dy = (y_max - y_min) / ny

        time_tracker = ValueTracker(0)

        def pressure(x, y, t):
            high_center_x = -1.2 + 0.75 * np.sin(1.1 * t)
            high_center_y = 0.6 + 0.35 * np.cos(0.9 * t)
            low_center_x = 1.1 + 0.65 * np.cos(0.8 * t)
            low_center_y = -0.55 + 0.45 * np.sin(1.2 * t)
            high_pressure = 1.4 * np.exp(
                -((x - high_center_x) ** 2 + (y - high_center_y) ** 2) / 0.55
            )
            low_pressure = 0.9 * np.exp(
                -((x - low_center_x) ** 2 + (y - low_center_y) ** 2) / 0.75
            )
            oscillation = 0.25 * np.sin(2.2 * t + 1.4 * x - 0.9 * y)
            gradient = 0.18 * x - 0.08 * y
            return high_pressure - low_pressure + oscillation + gradient

        sample_points = [
            (
                x_min + (i + 0.5) * dx,
                y_min + (j + 0.5) * dy,
            )
            for i in range(nx)
            for j in range(ny)
        ]
        pressure_values = [
            pressure(x, y, t)
            for x, y in sample_points
            for t in np.linspace(0, 5, 26)
        ]
        min_pressure = min(pressure_values)
        max_pressure = max(pressure_values)
        pressure_palette = color_gradient(
            [BLUE_E, azul, verde, YELLOW, naranja, RED_E],
            100,
        )

        def pressure_color(value):
            alpha = inverse_interpolate(min_pressure, max_pressure, value)
            return pressure_palette[int(np.clip(alpha, 0, 0.999) * 100)]

        def update_cell_color(cell, x, y):
            return cell.set_fill(
                pressure_color(pressure(x, y, time_tracker.get_value())),
                opacity=0.92,
            )

        cells = VGroup()
        for x, y in sample_points:
            cell = Rectangle(
                width=axes.x_axis.unit_size * dx,
                height=axes.y_axis.unit_size * dy,
                stroke_width=0,
                fill_color=pressure_color(pressure(x, y, 0)),
                fill_opacity=0.92,
            )
            cell.move_to(axes.c2p(x, y))
            cell.add_updater(lambda mob, x=x, y=y: update_cell_color(mob, x, y))
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

        time_label = MathTex("t=", color=naranja, font_size=36)
        time_value = DecimalNumber(
            time_tracker.get_value(),
            num_decimal_places=1,
            color=naranja,
            font_size=36,
        )
        time_value.add_updater(lambda number: number.set_value(time_tracker.get_value()))
        time_unit = MathTex(r"\mathrm{s}", color=naranja, font_size=36)
        time_marker = VGroup(time_label, time_value, time_unit)
        time_marker.arrange(RIGHT, buff=0.12)

        unsteady_derivative = MathTex(
            r"\frac{\partial p}{\partial t}",
            r"\neq",
            "0",
            color=naranja,
            font_size=34,
        )
        steady_derivative = MathTex(
            r"\frac{\partial p}{\partial t}",
            "=",
            "0",
            color=naranja,
            font_size=34,
        )
        uniform_derivative = MathTex(
            r"\frac{\partial p}{\partial x_i}",
            "=",
            "0",
            r"\quad \forall x_i",
            color=naranja,
            font_size=34,
        ).next_to(title, DOWN, buff=0.12)
        uniform_pressure_color = pressure_color((min_pressure + max_pressure) / 2)
        top_markers = VGroup(time_marker, unsteady_derivative)
        top_markers.arrange(RIGHT, buff=0.65).next_to(title, DOWN, buff=0.12)
        steady_derivative.move_to(unsteady_derivative)

        self.play(Write(title))
        self.play(FadeIn(cells), Write(axes), run_time=2)
        self.play(Write(field_label))
        self.play(FadeIn(legend_group, shift=LEFT * 0.2), Write(time_marker))
        self.play(Write(unsteady_derivative))
        self.play(time_tracker.animate.set_value(5), run_time=5, rate_func=linear)
        cells.clear_updaters()
        time_value.clear_updaters()
        self.play(TransformMatchingTex(unsteady_derivative, steady_derivative))
        self.wait(2)
        self.play(
            FadeOut(time_marker),
            TransformMatchingTex(steady_derivative, uniform_derivative),
            cells.animate.set_fill(uniform_pressure_color, opacity=0.92),
            run_time=2,
        )
        self.wait(2)

class campo_vectorial(Scene):
    def construct(self):
        title = Tex("Campo vectorial", font_size=44, color=naranja)
        title.to_edge(UP)

        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=8,
            y_length=4.8,
            axis_config={"color": WHITE, "include_numbers": True},
            tips=True,
        ).shift(LEFT * 0.5 + DOWN * 0.15)
        axes_labels = axes.get_axis_labels(
            MathTex("x", color=WHITE),
            MathTex("y", color=WHITE),
        )

        x_values = np.linspace(-2.6, 2.6, 11)
        y_values = np.linspace(-1.6, 1.6, 7)
        arrow_length = 0.42

        def vector_field(x, y):
            return np.array(
                [
                    -0.85 * y + 0.35 * np.sin(1.4 * x),
                    0.85 * x + 0.35 * np.cos(1.4 * y),
                ]
            )

        sample_points = [(x, y) for x in x_values for y in y_values]
        vector_modules = [
            np.linalg.norm(vector_field(x, y))
            for x, y in sample_points
        ]
        min_module = min(vector_modules)
        max_module = max(vector_modules)
        module_palette = color_gradient(
            [BLUE_E, azul, verde, YELLOW, naranja, RED_E],
            100,
        )

        def module_color(value):
            alpha = inverse_interpolate(min_module, max_module, value)
            return module_palette[int(np.clip(alpha, 0, 0.999) * 100)]

        arrows = VGroup()
        for x, y in sample_points:
            vector = vector_field(x, y)
            module = np.linalg.norm(vector)
            direction = vector / module
            start = np.array([x, y]) - direction * arrow_length / 2
            end = np.array([x, y]) + direction * arrow_length / 2
            arrow = Arrow(
                axes.c2p(*start),
                axes.c2p(*end),
                buff=0,
                color=module_color(module),
                stroke_width=4,
                max_tip_length_to_length_ratio=0.28,
            )
            arrows.add(arrow)

        field_label = MathTex(
            r"\mathbf{v}(x,y)",
            color=naranja,
            font_size=44,
        ).next_to(axes, DOWN, buff=0.35)

        legend = VGroup()
        legend_steps = 28
        for i in range(legend_steps):
            value = min_module + (max_module - min_module) * i / (legend_steps - 1)
            bar_cell = Rectangle(
                width=0.28,
                height=4.8 / legend_steps,
                stroke_width=0,
                fill_color=module_color(value),
                fill_opacity=1,
            )
            legend.add(bar_cell)
        legend.arrange(UP, buff=0).next_to(axes, RIGHT, buff=0.6)

        legend_title = MathTex(r"\lVert\mathbf{v}\rVert", color=naranja, font_size=30).next_to(legend, UP, buff=0.15)
        high_label = Tex("mayor", color=naranja, font_size=26).next_to(legend, RIGHT, buff=0.18).align_to(legend, UP)
        low_label = Tex("menor", color=naranja, font_size=26).next_to(legend, RIGHT, buff=0.18).align_to(legend, DOWN)
        legend_group = VGroup(legend, legend_title, high_label, low_label)

        self.play(Write(title))
        self.play(Write(axes), Write(axes_labels))
        self.play(LaggedStart(*[GrowArrow(arrow) for arrow in arrows], lag_ratio=0.025), run_time=3)
        self.play(Write(field_label), FadeIn(legend_group, shift=LEFT * 0.2))
        self.wait(5)