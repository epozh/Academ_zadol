def majority(A, left, right):
    if left > right:
        return 0
    if left == right:
        return A[left]

    middle = (left + right) // 2

    left_majority = majority(A, left, middle)
    right_majority = majority(A, middle + 1, right)

    if left_majority == right_majority:
        return left_majority

    left_count = sum(1 for i in range(left, right + 1) if A[i] == left_majority)
    if left_count > (right - left + 1) // 2:
        return left_majority

    right_count = sum(1 for i in range(left, right + 1) if A[i] == right_majority)
    if right_count > (right - left + 1) // 2:
        return right_majority

    return 0


with open("input.txt", "r") as input_file:
    n = int(input_file.readline())
    A = list(map(int, input_file.readline().split()))

result = majority(A, 0, n - 1)

with open("output.txt", "w") as output_file:
    if result != 0:
        output_file.write("1")
    else:
        output_file.write("0")
