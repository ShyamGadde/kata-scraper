from itertools import cycle


def spiralize(size: int) -> list[list[int]]:
    def collision_in_two_steps() -> bool:
        step_inside_bounds = y + y_inc * 2 in range(size) and x + x_inc * 2 in range(size)
        return step_inside_bounds and grid[y + y_inc * 2][x + x_inc * 2] == 1

    directions = cycle(((1, 0), (0, 1), (-1, 0), (0, -1)))

    grid = [[0] * size for _ in range(size)]
    x, y = 0, 0
    direction_changes = 0

    # Observed that the spiral pattern has a total of size - 1 direction changes
    while direction_changes < size:
        x_inc, y_inc = next(directions)

        while y + y_inc in range(size) and x + x_inc in range(size):
            grid[y][x] = 1

            if collision_in_two_steps():
                break

            y += y_inc
            x += x_inc

        direction_changes += 1

    return grid