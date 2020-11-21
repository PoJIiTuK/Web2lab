from math import floor


def find_min_size(n, w, h):

    index = 1
    a = max(h, w) * n

    while True:

        if a <= index:
            result = a
            break
        board = floor((a - index) / 2 + index)
        weight = floor(board / w)
        height = floor(board / h)
        rectangles = height * weight
        if rectangles < n:
            index = board + 1
        elif rectangles > n:
            a = board
        else:
            result = board
            break
    return result




if __name__ == '__main__':
    print(find_min_size(10, 3, 2))
