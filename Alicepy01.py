def decompress_string(s):
    stack = []
    num = 0
    current_str = ""

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '(':
            stack.append((current_str, num))
            current_str = ""
            num = 0
        elif char == ')':
            prev_str, repeat_count = stack.pop()
            current_str = prev_str + current_str * repeat_count
        else:
            current_str += char

    return current_str