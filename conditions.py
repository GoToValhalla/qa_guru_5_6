
b = bool

t = True
f = False
n = None

# if/elif/else на примере  кода ответа

if True:
    print('истина')
else:
    print('ложь')



# if 200  <= code < 400 or code == 418:
#     print('хороший ответ')
# else:
#     print('плохой ответ')

# пустые объекты - false
# строки
print(bool("abc"))
print(bool(""))
# числа
print(bool("123"))
print(bool("-123"))
print(bool("0"))
# коллекции
print(bool([0, ""]))
print(bool([]))
# словарь
print(bool({"key": "value"}))
print(bool({}))

