import flet as ft


def main(page: ft.Page):
    page.title = "Echo Chat"
    page.bgcolor = ft.Colors.WHITE
    
    chat_list = ft.ListView(expand=True, spacing=10, padding=20)
    message_input = ft.TextField(
        hint_text="Type a message...",
        expand=True,
        on_submit=lambda e: send_message()
    )
    
    def send_message():
        if message_input.value.strip():
            # Add user message
            chat_list.controls.append(
                ft.Container(
                    ft.Text(f"You: {message_input.value}", color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.BLUE,
                    padding=10,
                    border_radius=10,
                    alignment=ft.alignment.center_right
                )
            )
            
            # Add echo message
            chat_list.controls.append(
                ft.Container(
                    ft.Text(f"Echo: {message_input.value}", color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.GREY,
                    padding=10,
                    border_radius=10,
                    alignment=ft.alignment.center_left
                )
            )
            
            message_input.value = ""
            page.update()
    
    page.add(
        ft.Container(
            ft.Container(
                ft.Column([
                    chat_list,
                    ft.Row([
                        message_input,
                        ft.IconButton(
                            icon=ft.Icons.SEND,
                            on_click=lambda e: send_message()
                        )
                    ])
                ]),
                width=700,
            ),
            alignment=ft.alignment.center,
            expand=True
        )
    )


ft.app(main)
