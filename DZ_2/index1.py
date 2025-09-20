book = {}

book["название"] = input("Введите название книги: ")
book["автор"] = input("Введите автора книги: ")
book["год_издания"] = input("Введите год издания книги: ")

print("\nИнформация о книге:")
for key, value in book.items():
    print(f"{key}: {value}")