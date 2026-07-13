from prompt_toolkit.key_binding import KeyBindings

quality_key_bind = KeyBindings()


@quality_key_bind.add("<any>")
def _(event):
    current_text = event.app.current_buffer.text
    new_char = event.data

    if not new_char.isdigit():
        return

    if current_text == "" and new_char == "0":
        return

    predicted_text = current_text + new_char

    if int(predicted_text) > 100:
        return

    event.app.current_buffer.insert_text(new_char)
