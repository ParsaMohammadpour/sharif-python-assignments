def slope(x1, y1, x2, y2):
    return (float(y2 - y1) / float(x2 - x1))
def mabda(x1, y1, x2, y2):
    return ((float(y1)) - slope(x1, y1, x2, y2) * float(x1))
def line(a, b):
    return f'Y={"{:.2f}".format(a)}x+{"{:.2f}".format(b)}'

first = input().split()
second = input().split()

a = slope(float(first[0]), float(first[1]), float(second[0]), float(second[1]))
b = mabda(float(first[0]), float(first[1]), float(second[0]), float(second[1]))
l = line(a, b)

print(f'{"{:.2f}".format(a)}')
print(f'{"{:.2f}".format(b)}')
print(l)