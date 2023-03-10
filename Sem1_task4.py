revenue = int(input('Укажите сумму вашей выручки: '))
costs = int(input('Укажите сумму ваших издержек: '))

if revenue > costs:
    profit = revenue - costs
    print(f"Финансовый результат - прибыль. Ее величина: {profit}")
    stuff = int(input('Укажите количество сотрудников в компании: '))
    print(f"Прибыль фирмы в расчете на одного сотрудника равна: {profit/stuff}")
elif revenue < costs:
    print('Сумма ваших издержек превышает доход')
elif revenue == costs:
    print('Сумма ваших издержек равна доходу')