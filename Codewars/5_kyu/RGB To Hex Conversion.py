def rgb(r, g, b):
    dec_to_hex = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: "A", 11: "B", 12: "C", 13: "D",
                  14: "E",
                  15: "F"}

    def rgb_size(size):
        if size > 255:
            size = 255
        elif size < 0:
            size = 0
        return size

    def rgb_value(value):
        first = value // 16
        second = value - 16 * first
        return str(dec_to_hex[first]) + str(dec_to_hex[second])

    return "".join(rgb_value(rgb_size(i)) for i in [r, g, b])


print(rgb(148, 0, 211))
