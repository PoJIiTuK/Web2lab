from math import ceil, floor


def get_min_size_of_square(n, w, h):
    left = 1
    right = max(w, h) * n
    while True:
        if right <= left:
            ans = right
            break
        middle = floor((right - left) / 2 + left)
        count_in_row = floor(middle / w)
        count_in_column = floor(middle / h)
        count_of_rectangles = count_in_row * count_in_column
        if count_of_rectangles < n:
            left = middle + 1
        elif count_of_rectangles > n:
            right = middle
        else:
            ans = middle
            break
    return ans


if __name__ == '__main__':
    print(get_min_size_of_square(10, 10056760000, 6788699999))
