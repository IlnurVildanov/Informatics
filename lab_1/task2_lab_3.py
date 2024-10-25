import re

def delete_words(text):
    pattern = r'\b(\w+)(\s+\1)+\b'
    result = re.sub(pattern, r'\1', text)
    return result

tests = [
    "Довольно распространённая ошибка ошибка – это лишний повтор повтор слова слова.",
    "Смешно, не не правда ли?",
    "Не нужно портить хор хоровод.",
    "Ошибка повтор повторения это ошибка повтор.",
    "Тест без повторов"
]

for test in tests:
    print("Original text:", test)
    print("Fixed text:", delete_words(test))
    print()
