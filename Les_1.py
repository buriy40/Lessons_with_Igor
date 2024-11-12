# a = 4**4**4
# print(a)
#
# print(int('4-2'))

# def pos_add(a,b):
#     return abs(a+b)
# print(pos_add(7, -7))
#
# print(pos_add(7, -5))
# print(pos_add(-2, -3))

# def foo(a):
# #    return divmod(a, -11)
#     return a//-11, a%-11
#
# print(foo(22))
# print(foo(-47))
# print(foo(111))

def num_sum(a):
    # 1. Определяем принадлежность значения 'a' к целому числу, но не к булеву типу
    if isinstance(a, int) and not isinstance(a, bool):
        # 2. Преобразуем число в положительное, а потом - строку
        a_to_str = str(abs(a))
        # 3. Задаем начальную сумму 0
        s = 0
        # 4. В цикле складываем все числа
        for i in a_to_str:
            s += int(i)
        return s
    return 'Это не целое число'
# Тесты
print(num_sum(-146))
print(num_sum('-11'))
print(num_sum(True))