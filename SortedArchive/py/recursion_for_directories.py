import argparse
import shutil
from pathlib import Path

# task 1:
def parse_arguments():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширенням.")

    parser.add_argument("-s", "--source", type=Path, required=True, help="Шлях до вихідної директорії (джерела)")
    parser.add_argument("-d", "--destination", type=Path, nargs="?", default=Path("dist"),
        help="Шлях до директорії призначення (за замовчуванням: dist)")

    return parser.parse_args()


def copy_and_sort_files(source_dir: Path, dest_dir: Path):
    try:
        for item in source_dir.iterdir():
            if item.is_dir():
                copy_and_sort_files(item, dest_dir)
            else:
                target_folder = item.suffix.lower().strip(".") or "no_extension"
                target_folder = dest_dir / target_folder

                try:
                    target_folder.mkdir(parents=True, exist_ok=True)
                    target_file_path = target_folder / item.name
                    shutil.copy2(item, target_file_path)
                    print(f"Успішно скопійовано: {item} -> {target_file_path}")

                except (PermissionError, OSError) as e:
                    print(f"[ПОМИЛКА] Не вдалося скопіювати файл {item.name}: {e}")

    except PermissionError:
        print(f"[ПОМИЛКА] Відмовлено в доступі до директорії: {source_dir}")
    except FileNotFoundError:
        print(f"[ПОМИЛКА] Директорію не знайдено: {source_dir}")
    except Exception as e:
        print(f"[ПОМИЛКА] Непередбачена помилка при обробці {source_dir}: {e}")


def main():
    args = parse_arguments()
    copy_and_sort_files(args.source, args.destination)

if __name__ == "__main__":
    main()