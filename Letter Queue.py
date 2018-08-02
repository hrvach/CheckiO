def letter_queue(list_of_commands):
    stack = []
    for command in list_of_commands:
        if 'PUSH' in command: stack = [command[-1]] + stack
        else: 
            try: 
                stack.pop()
            except IndexError:
                pass
    return ''.join(stack[::-1])