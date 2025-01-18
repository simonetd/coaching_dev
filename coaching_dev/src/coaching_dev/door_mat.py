
def draw_mat_door(size):

    if not isinstance(size, int) or size % 2 == 0:
        raise ValueError("Input must be an odd integer.")

    n = size
    m = 3 * n

    # Top half pattern
    for i in range(n // 2):
        pattern = '.|.' * (2 * i + 1)
        print(pattern.center(m, '-'))

    # Center 'WELCOME'
    print('WELCOME'.center(m, '-'))

    # Bottom half pattern
    for i in range(n // 2 - 1, -1, -1):
        pattern = '.|.' * (2 * i + 1)
        print(pattern.center(m, '-'))

if __name__ == "__main__":
    try:
        size = int(input("Enter an odd integer for the door mat size: "))
        draw_mat_door(size)
    except ValueError as e:
        print(e)