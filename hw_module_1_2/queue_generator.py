import queue

# task 1:
queue = queue.Queue()
uniq_id_counter = 1

def generate_request():
    global uniq_id_counter
    request = f'Заявка №{uniq_id_counter}'
    queue.put(request)

    print(f'{request} додана до черги.')
    uniq_id_counter+=1

def process_request():
    if not queue.empty():
        current_request = queue.get()
        print(f'{current_request} в процесі обробки.')
    else:
        print(f'Черга пуста.')

def main():
  while True:
    print('\nОберіть команду:')
    print('1: Додати нову заявку в чергу')
    print('2: Обробити наступну заявку')
    print('q: Вихід')

    choice = input('Команда: ').strip()

    if choice == '1':
        generate_request()
    elif choice == '2':
        process_request()
    elif choice == 'q':
        print('До побачення!')
        break
    else:
        print('Спробуйте ще раз.')

if __name__ == "__main__":
    main()