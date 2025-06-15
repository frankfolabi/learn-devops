def show_messages(messages):
    """Display a list of short messages from a list."""
    for message in messages:
        print(message.title())

greetings = ['hi', 'bye', 'hello', 'gracias', 'thanks']

show_messages(greetings)

