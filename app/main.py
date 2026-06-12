def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    # CAT
    if cat_age < 15:
        cat = 0
    elif cat_age < 24:
        cat = 1
    elif cat_age < 28:
        cat = 2
    else:
        cat = 3 + (cat_age - 28) // 4

    # DOG
    if dog_age < 15:
        dog = 0
    elif dog_age < 24:
        dog = 1
    elif dog_age < 28:
        dog = 2
    else:
        dog = 2 + (dog_age - 28) // 5

    return [cat, dog]
