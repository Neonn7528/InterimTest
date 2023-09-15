from NoteReader import readNotes
from Addition import addingNote
from Deleting import deleteNote
from EditNote import editNote
def main():
    while True:
        choice = input("Выберите номер действия: ")
        print("1 - Вывести список заметок")
        print("2 - Добавить новую заметку")
        print("3 - Редактировать заметку")
        print("4 - Удалить заметку")
        print("5 - Выйти из приложения")

        if choice == "1":
            readNotes()
        elif choice == "2":
            addingNote()
        elif choice == "3":
            editNote()
        elif choice == "4":
            deleteNote()
        elif choice == "5":
            print("Завершение работы...")
            break
        else:
            print("Неверный выбор, повторите попытку.\n")
#проверка, что файл запущен в Main
if __name__ == '__main__':
    main()