items = {'в': (3, 25),
         'п': (2, 15),
         'б': (2, 15),
         'а': (2, 20),
         'и': (1, 5),
         'н': (1, 15),
         'т': (3, 20),
         'о': (1, 25),
         'ф': (1, 15),
         'д': (1, 10),
         'к': (2, 20),
         'р': (2, 20)
         }

bag_siz = 9
e = items.pop('д')
bag_siz -= 1
item_siz = []
for i in items:
    item_siz.append(items[i][0])
item_health = []
for i in items:
    item_health.append(items[i][1])
n = len(items)
table = [[0 for a in range(bag_siz + 1)] for i in range(n + 1)]
for i in range(n + 1):
    for j in range(bag_siz + 1):
        if i == 0 or j == 0:
            table[i][j] = 0
        elif item_siz[i - 1] <= j:
            table[i][j] = max(item_health[i - 1] + table[i - 1][j - item_siz[i - 1]], table[i - 1][j])
        else:
            table[i][j] = table[i - 1][j]
max_health = table[n][bag_siz]
max_size = bag_siz
list_it = []
for i in range(n, 0, -1):
    if max_health <= 0:
        break
    if max_health == table[i - 1][max_size]:
        continue
    else:
        list_it.append((item_siz[i - 1], item_health[i - 1]))
        max_health -= item_health[i - 1]
        max_size -= item_siz[i - 1]
items_keys = []
health = 0
for item in list_it:
    for t, p in items.items():
        if p == item:
            items_keys.append((t, p[0]))
            items.pop(t)
            health += p[1]
            break
bag = ''.join([i[0] * i[1] for i in items_keys])
bag += 'д'
health += e[1]
health_no = 0
for i in items:
    health_no += items[i][1]
print('Итоговые очки: ', health - health_no)
for i in range(bag_siz + 1):
    print("[", bag[i], "]", end="")
    if (i + 1) % 3 == 0:
        print()
