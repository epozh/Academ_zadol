f = open('input.txt')
n, k = map(int, f.readline().split())
points = [list(map(int, line.split())) for line in f]


def distance(point):
    x, y = point
    return x ** 2 + y ** 2


def quick_sort(a):
    if len(a) <= 1:
        return a
    elem = a[len(a) // 2][1]
    left = [x for x in a if x[1] < elem]
    middle = [x for x in a if x[1] == elem]
    right = [x for x in a if x[1] > elem]
    return quick_sort(left) + middle + quick_sort(right)


def close(points, k):
    sorted_points = quick_sort(points)
    return sorted_points[:k]


points_closest_to_k = close(points, k)

f = open('output.txt', 'w')
for i, point in enumerate(points_closest_to_k):
    f.write(f"[{point[0]}, {point[1]}]")
