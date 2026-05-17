import random
import timeit


# task 3:
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def tim_sort(arr):
    data = arr.copy()
    data.sort()
    return data

def time_testing():
    sizes = [100, 1000, 5000]

    print(
        f"{'Розмір':<8} | {'Тип':<12} | {'insertion_sort (s)':<12} | {'merge_sort (s)':<12} | {'tim_sort (s)':<12}"
    )
    print("-" * 75)

    for size in sizes:
        datasets = {
            "Random": [random.randint(0, size * 10) for _ in range(size)],
            "Sorted": list(range(size)),
            "Reversed": list(range(size, 0, -1)),
        }

        for type, data in datasets.items():
            t_insertion = timeit.timeit(lambda: insertion_sort(data), number=1)
            t_merge = timeit.timeit(lambda: merge_sort(data), number=1)
            t_timsort = timeit.timeit(lambda: tim_sort(data), number=1)

            print(
                f"{size:<8} | {type:<12} | {t_insertion:<18.5f} | {t_merge:<14.5f} | {t_timsort:<12.5f}"
            )
        print("-" * 75)

if __name__ == "__main__":
    time_testing()