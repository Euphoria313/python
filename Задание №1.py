score = int(input("Enter your score: "))
if score < 102:
    print("Счёт не достигнут, не задание выполнено")
elif score == 105:
    print("Счёт достигнут, задание выполнено")
elif score >= 106:
    print("Счёт достигнут, задание перевыполнено")
else:
    print("Счет не достигнут, задание не выполнено")
if score >= 105:
    template = "Поздравляем {} выполнением задания!"
    name = "Дмитрий"
    print(template.format(name))