import requests
from src.classes.phone import Phone

BASE_URL = 'http://127.0.0.1:5000/phones'

def get_phones():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        phones_data = response.json()
        phones = [Phone(id_phone=phone[0], name_phone=phone[1], os_phone=phone[2]) for phone in phones_data]
        print("Список телефонов:")
        for phone in phones:
            print(phone)
    else:
        print("Ошибка при получении данных")

def add_phone():
    name = input("Введите название телефона: ")
    os = input("Введите операционную систему: ")
    phone = Phone(id_phone=None, name_phone=name, os_phone=os)
    response = requests.post(BASE_URL, json=phone.to_dict())
    if response.status_code == 201:
        print("Телефон добавлен:", response.json())
    else:
        print("Ошибка при добавлении")

def update_phone():
    id_phone = input("Введите ID телефона для обновления: ")
    name = input("Введите новое название телефона: ")
    os = input("Введите новую операционную систему: ")
    phone = Phone(id_phone=id_phone, name_phone=name, os_phone=os)
    response = requests.put(f'{BASE_URL}/{id_phone}', json=phone.to_dict())
    if response.status_code == 200:
        print("Телефон обновлен")
    else:
        print("Ошибка при обновлении")

def delete_phone():
    id_phone = input("Введите ID телефона для удаления: ")
    response = requests.delete(f'{BASE_URL}/{id_phone}')
    if response.status_code == 200:
        print("Телефон удален")
    else:
        print("Ошибка при удалении")

def main():
    while True:
        print("\nМеню:")
        print("1. Показать все телефоны")
        print("2. Добавить телефон")
        print("3. Обновить телефон")
        print("4. Удалить телефон")
        print("5. Выйти")

        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            get_phones()
        elif choice == '2':
            add_phone()
        elif choice == '3':
            update_phone()
        elif choice == '4':
            delete_phone()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие от 1 до 5.")

if __name__ == '__main__':
    main()
