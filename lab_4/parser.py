def read_xml_file(filename):
    # открытие и чтение файла
    with open(filename, 'r', encoding='utf-8') as file:
        xml_data = file.read()
    return xml_data


def parse_xml_to_json(xml_data):
    json_data = '{\n"schedule": {\n"lesson": [\n'
    indent = '    '

    # разделение строк по тегам вручную
    lines = xml_data.splitlines()

    in_lesson = False  # флаг для отслежки lesson

    for line in lines:
        line = line.strip()

        # если начало урока
        if line.startswith('<lesson>'):
            if in_lesson:
                json_data += '},\n'
            json_data += indent + '{\n'
            in_lesson = True
            continue

        # если достигли конца урока
        if line.startswith('</lesson>'):
            json_data += indent + '},\n'
            in_lesson = False
            continue

        # тут парсинг
        if line.startswith('<time>'):
            time = line.replace('<time>', '').replace('</time>', '').strip()
            json_data += f'{indent * 2}"time": "{time}",\n'

        elif line.startswith('<subject>'):
            subject = line.replace('<subject>', '').replace('</subject>', '').strip()
            json_data += f'{indent * 2}"subject": "{subject}",\n'

        elif line.startswith('<teacher>'):
            teacher = line.replace('<teacher>', '').replace('</teacher>', '').strip()
            json_data += f'{indent * 2}"teacher": "{teacher}",\n'

        elif line.startswith('<audience>'):
            audience = line.replace('<audience>', '').replace('</audience>', '').strip()
            json_data += f'{indent * 2}"location": {{\n{indent * 3}"audience": "{audience}",\n'

        elif line.startswith('<address>'):
            address = line.replace('<address>', '').replace('</address>', '').strip()
            json_data += f'{indent * 3}"address": "{address}"\n{indent * 2}}},\n'

    # закрываем структуру json'а
    json_data = json_data.rstrip(',\n') + '\n'
    json_data += ']\n}\n}'

    return json_data


def write_json_file(filename, json_data):
    # тут запись в json
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json_data)


# тут основная часть
xml_filename = 'schedule.xml'
json_filename = 'schedule.json'

# здесь чтение файла
xml_data = read_xml_file(xml_filename)

# здесь конвертация
json_data = parse_xml_to_json(xml_data)
write_json_file(json_filename, json_data)

print(f'Конвертация завершена. Результат сохранён в файле "{json_filename}".')
