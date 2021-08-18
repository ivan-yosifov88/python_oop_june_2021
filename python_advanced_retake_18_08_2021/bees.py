from collections import deque


working_bees = deque([int(el) for el in input().split()])
nectar_to_collect = [int(el) for el in input().split()]
honey_process = deque(input().split())


total_honey_collect = 0


def get_honey_value(bee, honey, symbol):
    if symbol == "+":
        result = bee + honey
    elif symbol == "-":
        result = bee - honey
    elif symbol == "*":
        result = bee * honey
    elif symbol == "/":
        if honey == 0:
            return 0
        result = bee / honey
    return abs(result)


while working_bees and nectar_to_collect:
    bee = working_bees[0]
    nectar = nectar_to_collect[-1]
    if bee <= nectar:
        symbol = honey_process[0]
        honey_collect = get_honey_value(bee, nectar, symbol)
        total_honey_collect += honey_collect

        working_bees.popleft()
        nectar_to_collect.pop()
        honey_process.popleft()
    else:
        nectar_to_collect.pop()

print(f"Total honey made: {total_honey_collect}")
if working_bees:
    print(f"Bees left: {', '.join(str(b) for b in working_bees)}")
if nectar_to_collect:
    print(f"Nectar left: {', '.join(str(n) for n in nectar_to_collect)}")

