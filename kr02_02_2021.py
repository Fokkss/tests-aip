def task_1(two_dim_words):
    lst = []
    cnt = 0
    lst1 = len(two_dim_words)
    for i in range(lst1):
        lst += two_dim_words[i]
    for j, string in enumerate(lst):
        lst[j] = "".join(sorted(list(string)))
        lst.sort(key=lambda k: (len(k), k), reverse=True)
    sorted_words = lst
    return sorted_words

def task_4_1(words):
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    return res


def task_4_2(words):  # можно сделать тесты
    words0 = list(words)
    words1 = []
    for i in words0:
        if len(i) > 3:
            words1.append(i)
        else:
            del i
    res = set(words1)
    return res


def task_4_3(words):
   words0 = list(words)
    words1 = []
    v = "aoiuey"
    for i in words0:
        i = i.lower()
        for l in i:
            if l in v and i[-1] == "a":
                i = i.replace(l, " ")
                words1.append(i)
            else:
                del l
    res = words1
    return res


def task_5(lst1, lst2):
    list_m1 = set(lst1)
    list_m2 = set(lst2)
    a = list_m1.difference(list_m2)
    diff = sorted(a)
    return diff


def task_6(lst):
    lst1 = set(lst)
    lst2 = list(lst1)
    res = sorted(lst2, reverse=True)
    return res
#пока не готово

