
# Simple Counter App made on Python using flutter framework (FLET)..
# App Made by: DevJinsar 
# Opensource

import flet
from flet import Page, TextField, Row, IconButton, icons, colors


def main(page: Page):
    page.title = "Counter App With Flet"
    page.vertical_alignment = "center"
    page.bgcolor = colors.ORANGE

    txt_field = TextField(value="0", width=100, text_align="right")

    def minus_clicked(e):
        txt_field.value = int(txt_field.value) - 1
        page.update()

    def plus_clicked(e):
        txt_field.value = int(txt_field.value) + 1
        page.update()

    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus_clicked, icon_color=colors.RED),
                txt_field,
                IconButton(icons.ADD, on_click=plus_clicked, icon_color= colors.GREEN),
            ],
            alignment="center",
        )
    )


flet.app(target=main)