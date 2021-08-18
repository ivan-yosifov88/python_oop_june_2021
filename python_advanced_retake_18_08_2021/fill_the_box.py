def fill_the_box(*args):
    height = args[0]
    length = args[1]
    width = args[2]
    cube_size = height * length * width
    for i in range(3, len(args)):
        if args[i] == "Finish":
            return f"There is free space in the box. You could put {cube_size} more cubes."
        if cube_size < args[i]:
            cubes_left = args[i] - cube_size
            for c in range(i + 1, len(args)):
                if args[c] == "Finish":
                    break
                cubes_left += args[c]
            return f"No more free space! You have {cubes_left} more cubes."

        cube_size -= args[i]

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
