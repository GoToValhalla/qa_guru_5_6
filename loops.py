
# While - цикл с предусловием
# пока пользователь не введет правильный пароль, ...

actual_password = 12345
password_from_user = 54321

password_incorrect = actual_password == password_from_user

while password_incorrect:
    pass


run_count = 0

while run_count != 10:
    print(1234)
    run_count += 1

# For. Итерируем списки и словари

users = [1, 2, 3, 4, 5]

for user in users:
    print(user)


d = {
    "key": 123,
    "another": 456,
    "third": 789
}

for k in d:
    print(d[k])

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)


# Break/Continue/Else - прерывание цикла

# for i in range - цикл с итератором

for i in range(0):
    if i == 0:
        continue
    if i == 3:
        break

    print(i)
else:
    print("Когда я выполняюсь?")

# enumerate - возвращает пары (индекс, значение)


cities = ["Екатеринбург", "Москва", "Сочи"]

print("///" * 5)

for i, city in enumerate(reversed(cities)):
    print(f"{city} на {i + 1} месте по чистоте воздуха")