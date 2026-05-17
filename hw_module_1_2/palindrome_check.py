from collections import deque

#task 2:
def palindrome_check(string):
    string = ''.join(string.split()).lower()

    if not string:
        return False

    deque_char = deque(string)

    while len(deque_char) > 1:
        first_char = deque_char.popleft()
        last_char = deque_char.pop()

        if first_char != last_char:
            return False

    return True


examples = ["Радар", "Козак з казок", "Python", "Шалаш", "Пилип", "School"]
for s in examples:
    result = palindrome_check(s)
    print(f'"{s}" -> {"Паліндром" if result else "Не паліндром"}')