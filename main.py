non_complaent = {
    "a1": ["b12", "k"],
    "b1": ["b2", "b3", "b6", "b12", "c", "mg", "ca"],
    "b2": ["b1", "b12", "fe", "cu"],
    "b3": ["b1"],
    "b5": ["cu"],
    "b6": ["b1", "b12"],
    "b9": ["zn"],
    "b12": ["a", "b1", "b2", "b6", "c", "e", "fe", "cu"],
    "c": ["b1", "b12", "cu"],
    "d": ["e"],
    "e": ["b12", "d", "k", "fe", "mg", "cu", "zn"],
    "k": ["a", "e"],
    "fe": ["b2", "b12", "e", "mg", "ca", "zn"],
    "mg": ["b1", "e", "fe", "p"],
    "cu": ["b2", "b5", "b12", "c", "e", "zn"],
    "ca": ["b1", "p", "zn"],
    "p": ["mg", "ca"],
    "zn": ["b9", "e", "fe", "cu", "ca"]
}


non_complaent["full_list"] = list(non_complaent.keys())


vitamin_translate = {
    "железо": "fe",
    "цинк": "zn",
    "магний": "mg",
    "кальций": "ca",
    "медь": "cu",
    "фосфор": "p",
    "витамин a": "a",
    "витамин b1": "b1",
    "витамин b2": "b2",
    "витамин b3": "b3",
    "витамин b5": "b5",
    "витамин b6": "b6",
    "витамин b9": "b9",
    "витамин b12": "b12",
    "витамин c": "c",
    "витамин d": "d",
    "витамин e": "e",
    "витамин k": "k"
}


def is_complaent(a: dict, vit1: str, vit2: str) -> bool:
    if vit1 == vit2:
        print("Переданы одинаковые витамины.")
        return False
    if vit1 not in a["full_list"] or vit2 not in a["full_list"]:
        print("Один или оба витамина неизвестны.")
        return False
    if vit2 in a[vit1]:
        print(f"{vit1} и {vit2} НЕ СОВМЕСТИМЫ.")
        return False
    print(f"{vit1} и {vit2} совместимы.")
    return True


def divide_groupps(non_complaent: dict, vit_list: list) -> list:
    if len(vit_list) == 0:
        return []
    result = [[vit_list[0]]]
    for new_vitamin in vit_list[1:]:
        new_vitamin = new_vitamin.strip().lower()
        if new_vitamin not in non_complaent["full_list"]:
            print(f"Неизвестный витамин: {new_vitamin}")
            continue
        is_added = False
        for group in result:
            can_be_added = all(
                existing not in non_complaent[new_vitamin]
                for existing in group
            )
            if can_be_added:
                group.append(new_vitamin)
                is_added = True
                break
        if not is_added:
            result.append([new_vitamin])
    return result


def print_result(groups: list):
    if not groups:
        print("Нет витаминов для приёма.\n")
        return
    print("\nРезультат группировки:")
    for i, group in enumerate(groups, 1):
        print(f"Прием {i}: ", end="")
        print(", ".join(group))


def main():
    print("Допустимые названия витаминов: a1, b1, b2, b3, b5, b6, b9, b12, c, d, e, k, fe, mg, cu, ca, p, zn, железо, цинк, магний, кальций, медь, фосфор, витамин a, витамин b1, витамин b2, витамин b3, витамин b5, витамин b6, витамин b9, витамин b12, витамин c, витамин d, витамин e, витамин k")
    vit1 = input("Введите 1 витамин для проверки совместимости: ").strip().lower()
    vit2 = input("Введите 2 витамин для проверки совместимости: ").strip().lower()

    vit1 = vitamin_translate.get(vit1, vit1)
    vit2 = vitamin_translate.get(vit2, vit2)

    is_complaent(non_complaent, vit1, vit2)

    my_vitamins_raw = input("\nВведите список ваших витаминов через запятую: ")
    my_vitamins = [v.strip().lower() for v in my_vitamins_raw.split(",")]
    translated_vitamins = [vitamin_translate.get(v, v) for v in my_vitamins]

    groups = divide_groupps(non_complaent, translated_vitamins)
    print_result(groups)


if __name__ == "__main__":
    main()