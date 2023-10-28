#Задание №3: Частотный анализ букв в тексте
def count_letters(text):
    text_lower = text.lower()
    letters_count = {}

    for alpha in text_lower:
        if alpha.isalpha():
            if letters_count.get(alpha) is None:
                letters_count[alpha] = 0
            letters_count[alpha] += 1

    return letters_count


def calculate_frequency(letters_dict):
    alpha_sum = sum(letters_dict.values())
    letters_frequency = {}

    for alpha, _ in letters_dict.items():
        letters_frequency[alpha] = (letters_dict[alpha] / alpha_sum)

    return letters_frequency


def print_dict(dictionary):
    for elem, freq in dictionary.items():
        print(elem + ':' + f"{freq: .2f}")


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

count_dict = count_letters(main_str)
frequency_dict = calculate_frequency(count_dict)
print_dict(frequency_dict)
