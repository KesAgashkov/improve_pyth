

def get_common_and_unic_items():
    data = {"Вася": ("Палатка", "Котелок", "Спички", "Шашлык", "Топор", "Мазик"),
            "Петя": ("Палатка", "Котелок", "Топор"),
            "Саша": ("Палатка", "Котелок", "Топор", "Спирт", "Масло", "Топор"),
            "Костя": ("Веревка", "Мыло", "Топор", "Палатка"),
            }
    lst = []
    for k, v in data.items():
        lst.append(set(v))

    temp_1 = lst[0]
    res_all = set()
    for i in range(1, len(lst)):
        temp_1 = temp_1.intersection(lst[i])
    print(temp_1)

    temp = set()
    res_unic = set()
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                temp.update(lst[j])
        temp = lst[i] - temp
        res_unic.update(temp)
        temp = set()
    print(res_unic)


# get_common_and_unic_items()


# Задание 1
# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

def get_list_double_el():
    lst = [9, 1, 1, 2, 2, 3, 3, 3, 5, 8, 8]
    res = []
    for el_1 in lst:
        count = 0
        for el_2 in lst:
            if el_1 == el_2:
                count += 1
        if count == 2:
            res.append(el_1)
            count = 0
    print(list(set(res)))


# get_list_double_el()

# Задание 2
# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.

def get_ten_most_frequent_words():
    dct = {}
    text = """
            Хотя лонгрид как жанр еще только складывается, многие аспекты работы над материалами данного типа разобраны
            как в российской, так и в зарубежной учебно-методической литературе. Например, М. Григорян выделяет
            в качестве отдельного жанра «длинные статьи» объемом в 800−2000 слов. Темой для таких материалов может
            стать «анализ ситуации, рассказ о необычном человеке и повествование о том, как живут люди
            в странных местах». При подготовке материала М. Григорян рекомендует использовать композиционную схему 
            «зигзаг» чередуя примеры и репортажные фрагменты («краски») с информационными вставками («факты»). 
            Начинать текст следует с человеческой истории, отражающей проблему, завершать материал – другой историей, 
            которая «оставила бы у читателя запоминающийся образ» Аналогичный подход предлагает О.Р. Самарцев, 
            который противопоставляет новостным текстам, где информация подается в порядке убывания важности 
            (композиционная схема «перевернутая пирамида»), историйные тексты, представляющие собой исследование 
            ситуации в какой-то сфере и выстраиваемые как последовательность историй, соединенных авторскими связками. 
            В качестве композиционных схем подобных материалов упомянуты «параллельный рассказ», когда «истории 
            связаны между собой только на уровне темы», «лейтмотивный рассказ», когда «истории объединены сквозной 
            историей и пересекаются с ней в ключевых точках», и «перекрестный рассказ», когда «истории пересекаются 
            как в отдельных точках, так и по всему тексту». Также одним из приемов названо «закольцовывание», 
            когда «начавшаяся в первом абзаце материала история завершается в последнем абзаце, охватывая другие 
            истории своеобразным сюжетным кольцом Близкий к лонгриду жанр описан А.В. Колесниченко под названием 
            «трендовая статья»15. Предметом отображения здесь является значимое изменение, происходящее в обществе, 
            новое явление, тенденция. Например, то, что благодаря распространению цифровой фототехники 
            фотографы-любители начали конкурировать с профессиональными папарацци, продавая в СМИ фотографии «звезд», 
            случайно встреченных в различных местах16. Метод отображения – уже упомянутая выше композиционная схема 
            «зигзаг», когда материал подается в виде чередования примеров, иллюстрирующих тренд, и обобщений, 
            раскрывающих значение этих примеров и вписывающих их в контекст. Целью является доказательство того, 
            что данный тренд действительно имеет место, а также новое, более глубокое понимание происходящего и 
            его возможных последствий.
            """
    text = text.replace(".", '').replace(",", "").replace("«", "").replace("»", "")
    words = text.split()
    for el in words:
        dct[el] = words.count(el)

    print(f"Простой вариант: {Counter(words).most_common(10)}")

    res = sorted(dct.items(), key=lambda x: x[1], reverse=True)
    print(f"Вариант посложнее: {res[:10]}")



# get_ten_most_frequent_words()

# Задание 3
# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.


def get_camp_set_1():
    bag = {"лопата": 20, "фонарик": 1, "палатка": 18, "сапоги": 10, "котелок": 5, "спальник": 7, }
    limit = 45
    weight = 0
    lst = []
    for key, el in bag.items():
        if weight + el > limit:
            continue
        else:
            lst.append(key)
            weight += el
    print(f"Общий вес = {weight}. В рюкзаке следующие вещи: {lst}")
    weight = 0
    res = []


# get_camp_set_1()
def get_camp_set_all_var():
    bag = {"лопата": 20, "фонарик": 1, "палатка": 18, "сапоги": 10, "котелок": 5, "спальник": 7, }
    limit = 45
    weight = 0
    res = []
    flag = False
    for key, el_1 in bag.items():
        weight = el_1
        res.append(key)
        for key, el_2 in bag.items():
            if weight + el_2 > limit:
                continue
            elif el_1 == el_2:
                continue
            else:
                res.append(key)
                weight += el_2
        print(f"Общий вес = {weight}. В рюкзаке следующие вещи: {res}")
        weight = 0
        res = []


# get_camp_set_all_var()

