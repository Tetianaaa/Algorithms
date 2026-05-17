import timeit

# Алгоритм Кнута-Морріса-Пратта
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)
    lps = compute_lps(pattern)
    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1


# Алгоритм Боєра-Мура
def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1


# Алгоритм Рабіна-Карпа
def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):
    substring_length = len(substring)
    main_string_length = len(main_string)

    base = 256
    modulus = 101

    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)

    h_multiplier = pow(base, substring_length - 1) % modulus

    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1


def main():
    file1_name = "article1.txt"
    file2_name = "article2.txt"

    try:
        with open(file1_name, "r", encoding="utf-8", errors="ignore") as f:
            text1 = f.read()
        with open(file2_name, "r", encoding="utf-8", errors="ignore") as f:
            text2 = f.read()
    except FileNotFoundError as e:
        print(f"[ПОМИЛКА] Не вдалося знайти файл. Переконайтеся, що файли лежать поруч зі скриптом: {e}")
        return

    tests = {
        "Стаття 1": {
            "text": text1,
            "existing": "найбільш популярних алгоритмів",
            "fake": "hash map",
        },
        "Стаття 2": {
            "text": text2,
            "existing": "linked list",
            "fake": "жадібні алгоритми",
        },
    }

    print(f"{'Текст':<10} | {'Тип':<14} | {'Boyer-Moore(s)':<13} | {'KMP (s)':<14} | {'Rabin-Karp (s)':<14}")
    print("-" * 80)

    for text_name, data in tests.items():
        txt = data["text"]
        for sub_type in ["existing", "fake"]:
            pattern = data[sub_type]

            iterations = 50
            t_bm = timeit.timeit(lambda: boyer_moore_search(txt, pattern), number=iterations)
            t_kmp = timeit.timeit(lambda: kmp_search(txt, pattern), number=iterations)
            t_rk = timeit.timeit(lambda: rabin_karp_search(txt, pattern), number=iterations)

            print(f"{text_name:<10} | {sub_type:<14} | {t_bm:<14.5f} | {t_kmp:<14.5f} | {t_rk:<14.5f}")
        print("-" * 80)


if __name__ == "__main__":
    main()