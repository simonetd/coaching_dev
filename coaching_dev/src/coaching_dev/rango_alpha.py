def draw_rangoli(size):
    """Draw Rangoli square depending on the size asked"""
    import string

    # Alphabet
    alpha = string.ascii_lowercase

    # lignes
    lines = []
    for i in range(size):
        left_part = '-'.join(alpha[size-1:i:-1])
        full_row = left_part + (('-' if left_part else '') + alpha[i] + ('-' if left_part else '') + left_part[::-1])
        lines.append(full_row.center(4 * size - 3, '-'))


    return '\n'.join(lines[::-1] + lines[1:])


if __name__ == "__main__":
    size = 4
    print(draw_rangoli(size))