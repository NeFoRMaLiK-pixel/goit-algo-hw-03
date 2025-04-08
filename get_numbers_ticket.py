import random

def get_numbers_ticket(min, max, quantity):
    if not isinstance(min, int) or not isinstance(max, int) or not isinstance(quantity, int):
        return []
    if min < 1 or max > 1000 or min > max:
        return []
    if quantity < 1 or quantity > (max - min + 1):
        return []
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)

# Примеры использования функции
print(get_numbers_ticket(1, 49, 6))   
print(get_numbers_ticket("1", 49, 6))  