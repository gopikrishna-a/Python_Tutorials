def bubble_sort(lst):
    passes = 0
    swaps = 0
    for j in range(len(lst) - 1):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                swaps += 1
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        passes += 1
    return lst, passes, swaps


if __name__ == "__main__":
    n = int(input("No. of inputs: "))
    lst = list(map(int, input("Eter array values: ").split(" ")))
    if len(lst) == n:
        print(bubble_sort(lst))
    else:
        print("Input array size should be equal to no. of inputs")


def bubble_sort(lst):
    passes = 0
    swaps = 0
    srt = False
    while not srt:
        srt = True
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                srt = False
                swaps += 1
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        passes += 1
    return "{} {}".format(passes, swaps)


if __name__ == "__main__":
    n = int(input("No. of inputs: "))
    lst = list(map(int, input("Eter array values: ").split(" ")))
    if len(lst) == n:
        print(bubble_sort(lst))
    else:
        print("Input array size should be equal to no. of inputs")
