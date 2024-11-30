username = input("Введите имя: ")
title_0 = input("Введите заголовок заметки_0: ")
title_1 = input("Введите заголовок заметки_1: ")
title_2 = input("Введите заголовок заметки_2: ")
title = [title_0 , title_1 , title_2]    # Создали список заголовков заметок
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату создания заметки (ДД.ММ.ГГГГ): ")
issue_date = input("Введите дату истечения заметки (ДД.ММ.ГГГГ): ")
notes = [(username) ,
    (title) ,
    (content) ,
    (status) ,
    (created_date[0:6]) ,  # показать символы от 0 до 6. Показать символы от 0 до 6 с шагом 2 - print(created_date[0:6:2])
    (issue_date[0:6]) ]
print(notes)
