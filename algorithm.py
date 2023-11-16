import datetime as dt

# список занятых часов, которые нужно учитывать
busy = [
{'start' : '10:30',
'stop' : '10:50'
},
{'start' : '18:40',
'stop' : '18:50'
},
{'start' : '14:40',
'stop' : '15:50'
},
{'start' : '16:40',
'stop' : '17:20'
},
{'start' : '20:05',
'stop' : '20:20'
}
]

def str_to_time(time_str: str, pattern: str) -> dt:
    '''Функция для перевода строковых объектов в объекты datetime.'''
    return dt.datetime.strptime(time_str, pattern)

def get_free_window(busy: list[dict], slot_length: int) -> list:
    '''Функция для вычисления свободных окон.'''
    pattern = '%H:%M'
    start_job = str_to_time('9:00', pattern)
    end_job = str_to_time('21:00', pattern)

    # список с переведнными входными данными (busy) в объекты datetime
    busy_time = []
    for item in busy:
        start = str_to_time(item['start'], pattern)
        stop = str_to_time(item['stop'], pattern)
        busy_time.append((start, stop))
    busy_time.sort(key=lambda x: x[1])

    # результативный список свободных окон
    free_window = []

    # алгоритм для вычисления свободных окон и добавления в список free_window
    current_time = start_job
    for start, stop in busy_time:
        while current_time < start and (start - current_time >= dt.timedelta(minutes=30)):
            free_window.append(current_time.time())
            current_time += dt.timedelta(minutes=slot_length)
        current_time = stop

    while current_time < end_job and (end_job - current_time > dt.timedelta(minutes=30)):
        free_window.append(current_time.time())
        current_time += dt.timedelta(minutes=slot_length)

    return free_window    



result = get_free_window(busy=busy, slot_length=30)

for slot in result:
    print(slot)



# 9:00 - 9:30
# 9:30 - 10:00
# 10:00 - 10:30
# 10:50 - 11:20
# 11:20 - 11:50
# 11:50 - 12:20
# 12:20 - 12:50
# 12:50 - 13:20
# 13:20 - 13:50
# 13:50 - 14:20
# 15:50 - 16:20
# 17:20 - 17:50
# 17:50 - 18:20
# 18:50 - 19:20
# 19:20 - 19:50
# 20:20 - 20:50