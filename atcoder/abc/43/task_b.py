s = input()


def final_text(s: str) -> str:
    editor_stack = []
    for c in s:
        if c == '0' or c == '1':
            editor_stack.append(c)
        elif c == 'B':
            if editor_stack:
                editor_stack.pop()
    return "".join(editor_stack)

print(final_text(s))
