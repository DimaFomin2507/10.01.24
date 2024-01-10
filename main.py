from functools import reduce


def print_pyramid(n):
    for i2 in range(n, 0, -1):
        start = sum(i
                    for i in range(n - i2 + 1)
                    ) * 2 + 1
        print(f"{'\t' * (i2 - 1)}" 
        f"{'\t\t'.join(
            [str(i)
             for i in range (start, start + (n-i2 + 1
                                             ) * 2, 2)])}")


print(print_pyramid(5))
