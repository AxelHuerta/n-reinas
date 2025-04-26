import flet as ft


class Header(ft.Container):
    def __init__(self):
        super().__init__(
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Problema de las N Reinas",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        "Resuelve el problema de las N Reinas en un tablero de ajedrez.",
                        size=16,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.WHITE,
                    ),
                ]
            ),
            margin=10,
        )
