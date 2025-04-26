non_complaent = {
    "a": ["железо"],
    "b": ["цинк"],
    "c": ["магний", "железо"],
    "магний": ["c"],
    "цинк": ["c", "железо"],
    "железо": ["цинк", "a"],
    "full_list": ["a", "b", "c", "железо", "цинк", "магний"]
}


def is_complaent (a: dict, vit1: str, vit2: str)->bool:
    if(vit1 == vit2):
        print("Переданы одинаковые витамины")
        return False
    if(not(vit1 in a["full_list"]) or not(vit2 in a["full_list"])):
        print("Неизвестный витамин")
        return False
    if(vit2 in a[vit1]):
        print(f"{vit1} и {vit2} НЕ СОВМЕСТИМЫ")
        return False
    print(f"{vit1} и {vit2} совместимы")
    return True



def divide_groupps (non_complaent: dict, vit_list: list)->list:
    if(len(vit_list)==0):
        return None
    can_be_added = True
    is_added = False
    result = [[vit_list[0]]]
    for new_vitamin in vit_list:
        new_vitamin = new_vitamin.strip()
        new_vitamin = new_vitamin.lower()
        if(not new_vitamin in non_complaent["full_list"]):
            print(f"Неизвестный витамин {new_vitamin}")
            continue
        is_added = False
        for group in result:
            can_be_added = True
            if(new_vitamin in group):
                can_be_added = False
                continue
            for already_el in group:
                if already_el in non_complaent[new_vitamin]:
                    can_be_added = False
            if(can_be_added):
                group.append(new_vitamin)
                is_added = True
                break
        if(not is_added):
            result.append([new_vitamin])
    return result

def print_result(groups: list):
    if(len(groups)==0):
        print("Нет принимаемых витаминов\n")
    for i in range(len(groups)):
        print(f"Прием {i+1}:")
        for vitamin in groups[i]:
            print(vitamin, end="\t")
        print()


vit1 = input("Введите 1 витамин\n")
vit2 = input("Введите 2 витамин\n")
my_vitamins = ["a", "b", "c", "железо", "цинк", "магний"]
is_complaent(non_complaent, vit1, vit2)
print_result(divide_groupps(non_complaent, my_vitamins))
