# На стандартный поток ввода передается текст в одну строку. Далее подаются правила замены в формате "A->B".
# Необходимо последовательно применить эти правила к тексту (заменить все упоминания A на B).
# После каждой такой замены результат выводится в стандартный поток вывода.

text = input()

while True:
    rule = input()
    text = st.replace(rule[0], rule[3])
    print(text)