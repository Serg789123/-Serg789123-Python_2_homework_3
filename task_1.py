# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

data = [42, 73, 5, 42, 42, 2, 2, 3, 7, 73, 42]
res = []

for i in data:
    if data.count(i) > 1:
        res.append(i)

print(list(set(res)))
