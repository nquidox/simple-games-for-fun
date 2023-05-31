
def make_field(x, y):
    field = []  # объявляем массив

    for i in range(0, y):   # генерируем двумерный массив
        field.append(['-']*x)   # заполняем его значками пустой клетки

    return field


def print_field(field):
    # print(field)
    for row in field:
        print(row)


def check_horizontal(field, step_y, step_x, side):
    counter = 0
    shift_left = step_x
    while shift_left >= 0:
        if field[step_y][shift_left] == side:
            counter += 1
            shift_left -= 1
        else:
            break

    shift_right = step_x
    while shift_right <= len(field[step_y]) - 1:
        if field[step_y][shift_right] == side:
            counter += 1
            shift_right += 1
        else:
            break

    return counter


def check_vertical(field, step_y, step_x, side):
    counter = 0
    shift_up = step_y
    while shift_up >= 0:
        if field[shift_up][step_x] == side:
            counter += 1
            shift_up -= 1
        else:
            break

    shift_down = step_y
    while shift_down <= len(field) - 1:
        if field[shift_down][step_x] == side:
            counter += 1
            shift_down += 1
        else:
            break
    return counter


def check_left_diagonal(field, step_y, step_x, side):
    counter = 0
    shift_up = step_y
    shift_left = step_x

    while shift_up >= 0 and shift_left >= 0:
        if field[shift_up][shift_left] == side:
            counter += 1
            shift_up -= 1
            shift_left -= 1
        else:
            break

    shift_down = step_y
    shift_right = step_x

    while shift_down <= len(field) - 1 and shift_right <= len(field[step_y]) - 1:
        if field[shift_down][shift_right] == side:
            counter += 1
            shift_down += 1
            shift_right += 1
        else:
            break

    return counter


def check_right_diagonal(field, step_y, step_x, side):
    counter = 0
    shift_up = step_y
    shift_right = step_x

    while shift_up >= 0 and shift_right <= len(field[step_y]) - 1:
        if field[shift_up][shift_right] == side:
            counter += 1
            shift_up -= 1
            shift_right += 1
        else:
            break

    shift_down = step_y
    shift_left = step_x

    while shift_down <= len(field) - 1 and shift_left >= 0:
        if field[shift_down][shift_left] == side:
            counter += 1
            shift_down += 1
            shift_left -= 1
        else:
            break

    return counter


def check_for_win(field, step_y, step_x, side, win_condition):
    # win_condition = 3
    # field = [
    # ['X', '-', '-', '-', 'X'],
    # ['-', 'X', '-', 'X', '-'],
    # ['X', '-', 'X', '-', 'X'],
    # ['-', '-', '-', '-', 'X'],
    # ['X', '-', 'X', 'X', '-'],
    # ]
    # print_field(field)
    # print()
    # step_y = 0
    # step_x = 4
    #
    # side = 'X'

    w1 = check_horizontal(field, step_y, step_x, side)
    w2 = check_vertical(field, step_y, step_x, side)
    w3 = check_left_diagonal(field, step_y, step_x, side)
    w4 = check_right_diagonal(field, step_y, step_x, side)
    # print(f'{w1=}, {w2=}, {w3=}, {w4=}')
    #
    # if w1 >= 4 or w2 >= 4 or w3 >= 4 or w4 >= 4:
    #     print(f"WIN")
    # else:
    #     print(f"NO WIN")
    wc = win_condition +1
    if w1 >= wc or w2 >= wc or w3 >= wc or w4 >= wc:
        return True
    else:
        return False


def main():
    win_condition = 3
    x, y = 5, 5
    step = 0
    step_num = x * y
    field = make_field(x, y)
    side_switch = True

    while step <= step_num:
        print(f'\n \n \nНомер хода: {step}')
        print_field(field)
        inp = input("Введите клетку для хода y, x через запятую: ")
        step_y = int(inp.split(',')[0].strip())
        step_x = int(inp.split(',')[1].strip())

        if side_switch == True:
            print('Ход ноликов')
            field[step_y][step_x] = 'X'
            if check_for_win(field, step_y, step_x, 'X', win_condition):
                print("X победили!")
                break
            side_switch = False
        else:
            print('Ход крестиков')
            field[step_y][step_x] = 'O'
            if check_for_win(field, step_y, step_x, 'O', win_condition):
                print("O победили!")
                break
            side_switch = True
        step += 1


if __name__ == '__main__':
    main()



