from manim import *


class gridVisualizer(Scene):
    def construct(self):
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))

        # Define overall grid dimensions
        grid_width = 6
        grid_height = 6

        # Calculate cell width and height so that cells are packed tightly
        cell_width = grid_width / cols
        cell_height = grid_height / rows

        # Collect values for each cell in the matrix
        matrix_values = []
        print("Enter values for the grid (row by row):")
        for i in range(rows):
            row_values = input(f"Row {i + 1} values (separated by spaces): ").split()
            matrix_values.append(row_values)

        # Starting position (top-left corner)
        start_x = -grid_width / 2 + cell_width / 2
        start_y = grid_height / 2 - cell_height / 2

        # Create and animate each cell with its value, tightly packed
        for i in range(rows):
            for j in range(cols):
                # Position for each square based on its row and column
                position_x = start_x + j * cell_width
                position_y = start_y - i * cell_height

                # Create the square for each cell
                cell = Square(side_length=cell_width)
                cell.set_fill(color=RED, opacity=0.1)
                cell.set_stroke(color=WHITE, width=1)
                cell.move_to([position_x, position_y, 0])

                # Get the value for the cell from the matrix and create a text label
                cell_value = matrix_values[i][j]
                label = Text(cell_value, font_size=24).move_to([position_x, position_y, 0])

                # Animate the cell and add the label
                self.play(FadeIn(cell), FadeIn(label), run_time=0.2)

        # Pause to display the final grid with values
        self.wait(1)