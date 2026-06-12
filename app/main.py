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
    elif dog_age < 32:
        dog = 2
    elif dog_age < 36:
        dog = 3
    elif dog_age < 40:
        dog = 4
    elif dog_age < 44:
        dog = 5
    elif dog_age < 48:
        dog = 6
    elif dog_age < 52:
        dog = 7
    elif dog_age < 56:
        dog = 8
    elif dog_age < 60:
        dog = 9
    elif dog_age < 64:
        dog = 10
    elif dog_age < 68:
        dog = 11
    elif dog_age < 72:
        dog = 12
    elif dog_age < 76:
        dog = 13
    elif dog_age < 80:
        dog = 14
    elif dog_age < 84:
        dog = 15
    elif dog_age < 88:
        dog = 16
    elif dog_age < 92:
        dog = 17
    elif dog_age < 96:
        dog = 18
    else:
        dog = 17 + (dog_age - 96) // 4

    return [cat, dog]
