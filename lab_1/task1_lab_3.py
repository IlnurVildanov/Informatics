import re

def count_smile(text):
    pattern = r";<{P"
    smile = re.findall(pattern, text)
    return len(smile)

tests = [
    "gigachadgigachadgigachadgigachad;<{Pbanbanbanprivet;<{Psad",  # 2 смайла
    ";<{P ;< ;<{P ;<{P ;<{P",  # 4 смайла
    "[;<{P] ]]];<{P++ c++ вроде норм 408379;<{Pкто в майн",  # 3 смайла
    "ИТМО ТОП;<{PВТ ВТ ВТ ВТ ВТ ВТ",  # 1 смайл
    "none :)",  # 0 смайлов
]

expected_results = [
    2,
    4,
    3,
    1,
    0,
]

for i, test in enumerate(tests):
    result = count_smile(test)
    expected = expected_results[i]
    print(f"Test {i+1}: {test}")
    print(f"Expected: {expected}, Got: {result}")
    print("Тест пройден!" if result == expected else "Тест провален!")
    print()