def send_messages(messages):
    """Display a list of short messages from a list."""
    new_message = list(messages)
    sent_message = []

    while new_message:
        message = new_message.pop()
        print(message)
        sent_message.append(message)
    return new_message


greetings = ['hi', 'bye', 'hello', 'gracias', 'thanks']

result = send_messages(greetings)
print(result)
print(greetings)
