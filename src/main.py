import flet as ft
from components.message_bubble import MessageBubble
from components.chat_input import ChatInput
from components.chat_container import ChatContainer
from components.chat_messages_list import ChatMessagesList


def main(page: ft.Page):
    page.title = "Echo Chat"
    page.bgcolor = ft.Colors.WHITE
    
    # Initialize components
    chat_list = ChatMessagesList()
    
    def send_message():
        message_input = None
        # Find the TextField in the input component
        for control in page.controls[0].content.content.controls[1].controls:
            if isinstance(control, ft.TextField):
                message_input = control
                break
        
        if message_input and message_input.value.strip():
            # Add user message using component
            chat_list.controls.append(
                MessageBubble(message_input.value, "You", True)
            )
            
            # Add echo message using component
            chat_list.controls.append(
                MessageBubble(message_input.value, "Echo", False)
            )
            
            message_input.value = ""
            page.update()
    
    # Build UI using components
    chat_input = ChatInput(
        on_send=lambda e: send_message(),
        on_submit=lambda e: send_message()
    )
    
    page.add(
        ChatContainer([
            chat_list,
            chat_input
        ])
    )


ft.app(main)
