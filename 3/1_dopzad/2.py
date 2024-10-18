f = open('input.txt', 'r')
n = int(f.readline())


def quicksort(arr):  # сортируем в порядке возрастания
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def generate_permutation(n):  # генерируем список чисел от 1 до n (включительно) в порядке возрастания
    return list(range(1, n + 1))


def find_max_comparisons_permutation(
        n):  # находим перестановку чисел от 1 до n, которая приводит к максимальному количеству сравнений при
    # применении алгоритма быстрой сортировки
    permutations = []
    for i in range(1, n + 1):
        permutation = generate_permutation(n)
        permutation.remove(i)
        permutation.insert(0, i)
        permutations.append(permutation)
    max_comparisons = 0
    max_comparisons_permutation = []
    for permutation in permutations:
        comparisons = len(quicksort(permutation)) - 1
        if comparisons > max_comparisons:
            max_comparisons = comparisons
            max_comparisons_permutation = permutation
    return max_comparisons_permutation


max_comparisons_permutation = find_max_comparisons_permutation(n)  # поиск перестановки с максимальным числом сравнений

f = open('output.txt', 'w')
f.write(' '.join(map(str, max_comparisons_permutation)))
