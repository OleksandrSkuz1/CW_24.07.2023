# Виведення головного меню з наступними опціями:
# Створити новий рахунок.
# Зняти кошти з рахунку.
# Поповнити рахунок.
# Перевести кошти з одного рахунку на інший.
# Перевірити баланс рахунку.
# Вийти з програми.

# def bank_account(balance):
#     balance >= 0
#
#     name = input("Введіть ім'я власника рахунку: ")
#     balance = float(input("Введіть початковий баланс: "))
#     with_account = float(input("Введіть кошти які ви хочете зняти: "))

# Словник для збереження рахунків і їх балансів
accounts = {}


# Функція створення нового рахунку
def create_account():
    owner_name = input("Введіть ім'я власника рахунку: ")
    initial_balance = float(input("Введіть початковий баланс: "))
    account_id = len(accounts) + 1  # Унікальний ідентифікатор - просто порядковий номер
    accounts[account_id] = initial_balance
    print(f"Створено новий рахунок для {owner_name} з ідентифікатором {account_id}.")
    print(f"Початковий баланс: {initial_balance}")


# Функція зняття коштів з рахунку
def withdraw_amount():
    account_id = int(input("Введіть ідентифікатор рахунку: "))
    if account_id not in accounts:
        print("Рахунок з таким ідентифікатором не існує.")
    else:
        amount = float(input("Введіть суму для зняття: "))
        balance = accounts[account_id]
        if amount > balance:
            print("Недостатньо коштів на рахунку.")
        else:
            accounts[account_id] -= amount
            print(f"Знято {amount} з рахунку з ідентифікатором {account_id}. Залишок: {accounts[account_id]}")


# Головне меню
while True:
    print("Головне меню:")
    print("1. Створити новий рахунок.")
    print("2. Зняти кошти з рахунку.")
    print("3. Поповнити рахунок.")
    print("4. Перевести кошти з одного рахунку на інший.")
    print("5. Перевірити баланс рахунку.")
    print("6. Вийти з програми.")

    choice = int(input("Виберіть опцію (введіть відповідний номер): "))

    if choice == 1:
        create_account()
    elif choice == 2:
        withdraw_amount()
    elif choice == 3:
        # Додатковий код для опції "Поповнити рахунок" можна розмістити тут
        pass
    elif choice == 4:
        # Додатковий код для опції "Перевести кошти з одного рахунку на інший" можна розмістити тут
        pass
    elif choice == 5:
        # Додатковий код для опції "Перевірити баланс рахунку" можна розмістити тут
        pass
    elif choice == 6:
        print("До побачення! Завершення програми.")
        break
    else:
        print("Невідома опція. Спробуйте ще раз.")











