import flet as ft
from components.header import Header


def main(page: ft.Page):
    page.title = "Problema de las N Reinas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    solucion4reinas = [
        [1, 3, 0, 2],
        [2, 0, 3, 1],
    ]

    solucion8reinas = [
        [0, 4, 7, 5, 2, 6, 1, 3],
        [0, 5, 7, 2, 6, 3, 1, 4],
        [0, 6, 3, 5, 7, 1, 4, 2],
        [0, 6, 4, 7, 1, 3, 5, 2],
        [1, 3, 5, 7, 2, 0, 6, 4],
        [1, 4, 6, 0, 2, 7, 5, 3],
        [1, 4, 6, 3, 0, 7, 5, 2],
        [1, 5, 0, 6, 3, 7, 2, 4],
        [1, 5, 7, 2, 0, 3, 6, 4],
        [1, 6, 2, 5, 7, 4, 0, 3],
    ]

    n = len(solucion4reinas[0])
    solution = solucion4reinas
    total_solutions = len(solution)
    current_solution_index = 1
    squares = []
    board = ft.Column()

    def get_n(e):
        nonlocal n
        nonlocal solution
        nonlocal current_solution_index
        nonlocal total_solutions

        n = int(input.value)
        print(f"Input = {n}")

        if n == 4:
            solution = solucion4reinas
            current_solution_index = 1
            total_solutions.value = f"{current_solution_index} / {len(solution)}"
            total_solutions_description.value = (
                f"Se encontraron {len(solution)} soluciones para N = {n}"
            )
            update_board()
        elif n == 8:
            solution = solucion8reinas
            current_solution_index = 1
            total_solutions.value = f"{current_solution_index} / {len(solution)}"
            total_solutions_description.value = (
                f"Se encontraron {len(solution)} soluciones para N = {n}"
            )
            update_board()
        else:
            solution = solucion4reinas
        page.update()

    def update_board():
        squares.clear()  # Limpiar el tablero
        print(f"Valor de n = {n}")
        for i in range(n):
            squares.append([])
            for j in range(n):
                isPar = i % 2
                if isPar == 0:
                    squares[i].append(
                        create_square(
                            "white" if j % 2 == 0 else "black",
                            used=(
                                True
                                if j == solution[current_solution_index - 1][i]
                                else False
                            ),
                        )
                    )
                else:
                    squares[i].append(
                        create_square(
                            # Operador ternario
                            "black" if j % 2 == 0 else "white",
                            used=(
                                True
                                if j == solution[current_solution_index - 1][i]
                                else False
                            ),
                        )
                    )

        board.controls = [ft.Row(controls=row) for row in squares]

    # Funciones para los botones de navegacion
    def prev_btn_clicked(e):
        nonlocal current_solution_index
        nonlocal total_solutions
        if current_solution_index > 1:
            current_solution_index -= 1
            total_solutions.value = f"{current_solution_index} / {len(solution)}"
            update_board()
            print("Previo")
            page.update()

    def next_btn_clicked(e):
        nonlocal current_solution_index
        nonlocal total_solutions
        if current_solution_index < len(solution):
            current_solution_index += 1
            total_solutions.value = f"{current_solution_index} / {len(solution)}"
            update_board()
            print("Siguiente")
            page.update()

    # Botones de navegacion
    prev_btn = ft.IconButton(
        icon=ft.Icons.ARROW_BACK,
        icon_color=ft.Colors.WHITE,
        tooltip="Solución anterior",
        on_click=prev_btn_clicked,
    )

    next_btn = ft.IconButton(
        icon=ft.Icons.ARROW_FORWARD,
        icon_color=ft.Colors.WHITE,
        tooltip="Siguiente solución",
        on_click=next_btn_clicked,
    )

    # Texto de soluciones
    total_solutions = ft.Text(
        f"{current_solution_index} / {len(solucion4reinas)}",
        size=20,
        color=ft.Colors.WHITE,
    )

    # Descripcion de soluciones
    total_solutions_description = ft.Text(
        f"Se encontraron {len(solucion4reinas)} soluciones para N = {n}",
        size=20,
        color=ft.Colors.WHITE,
    )

    queen_logo = ft.Image(src="./queen.png")

    title = Header()
    input = ft.TextField(label="Número de reinas", value="4")
    button = ft.ElevatedButton(
        text="Calcular soluciones",
        bgcolor=ft.Colors.TEAL,
        on_click=get_n,
    )

    def create_square(color: str, used: bool = False):
        return ft.Container(
            width=100,
            height=100,
            bgcolor=color,
            content=(
                ft.Image(
                    src="./queen.png",
                )
                if used
                else None
            ),
        )

    update_board()

    page.add(
        ft.Column(
            [
                ft.Row([title], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(
                    [input, button],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [board],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [prev_btn, total_solutions, next_btn],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [total_solutions_description], alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.ALWAYS,
            expand=True,
        ),
    )


ft.app(main)
