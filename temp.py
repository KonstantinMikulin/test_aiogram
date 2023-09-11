def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end_signs = ',.!:;?'
    counter = 0
    end = start + size

    if len(text) < end:
        size = len(text) - start
        text = text[start:end]
    else:
        if text[end] == '.' and text[end - 1] in end_signs:
            text = text[start:end - 2]
            size -= 2
        else:
            text = text[start:end]
        for i in range(size - 1, 0, -1):
            if text[i] in end_signs:
                break
            counter = size - i
    page_text = text[:size - counter]
    page_size = size - counter
    return page_text, page_size


text = 'Да? Вы точно уверены? Может быть, вам это показалось?.. Ну, хорошо, приходите завтра, тогда и посмотрим, что можно сделать. И никаких возражений! Завтра, значит, завтра!'
start = 22
size = 145
print(*_get_part_text(text, start, size), sep='\n')
