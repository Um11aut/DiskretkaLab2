def calculate_order_cost(price_list : [], order: []):
    price_dict = {}
    for item in price_list:
        product = item[0].strip().lower() 
        price_dict[product] = (item[1], item[2])

    total_cost = 0

    for order_item in order:
        product_name = order_item[0].strip().lower()
        quantity = order_item[1]

        if product_name in price_dict:
            price, available_quantity = price_dict[product_name]
            if quantity <= available_quantity:
                total_cost += price * quantity
                price_dict[product_name] = (price, available_quantity - quantity)
            else:
                print(f'К-сть на складі: {available_quantity} \nЦе менше ніж {quantity} \n')
                continue
        else:
            print(f'{product_name} не знайдено')
            continue

    return total_cost

def task16():
    price_list = [
    ("хліб", 10, 50),
    ("молоко", 20, 30),
    ("яйця", 5, 100)
    ]

    order = [
        ("хліб", 1),
        ("МОЛОКО", 2)
    ]

    result = calculate_order_cost(price_list, order)

    if result == -1:
        print("Кількість товару в замовленні перевищує наявну.")
    elif result == -2:
        print("Товару із вказаним найменуванням немає в прейскуранті.")
    else:
        print(f"Вартість замовлення: {result} грн.")
