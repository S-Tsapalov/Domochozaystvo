from prioritetnost import PriorityScore
import json

# ----Получение списка дел----(приход json файла на сервер)

# ----Получение списка дел из БД

'''
1  Задача ближайших пяти лет
2  Задача на год
3  Задача на квартал
4  Задача на месяц
5  Задача на неделю
6  Задача на день
7  Задача половины дня
8  Задача ближайшего часа
9  Задача ближайших 15 минут
10 Задача требующая немедленного выполнения
'''

def rasschet_balla_srochnosti(time_delta):
    if time_delta == 'Задача на день':
        return 6
    elif time_delta == 'Задача половины дня':
        return 7
    elif time_delta == 'Задача ближайшего часа':
        return 8
    elif time_delta == 'Задача ближайших 15 минут':
        return 9
    elif time_delta == 'Задача требующая немедленного выполнения':
        return 10

cur.execute('''SELECT id, end_data, start_data FROM zadachi WHERE end_data - start_data <= INTERVAL '1 day';''')
result = cur.fetchall() #Список айдишников задач на день
work_lst = []

for i in result:
    cur.execute('''INSERT INTO zadachi_na_den.id_del VALUES(%s);''',(i[0],))

    task = {
        'id':i[0],
        'time_bal':rasschet_balla_srochnosti(i[1]-i[2])
    }
    work_lst.append(task)




# ----------------------------

def sort_work_list(work_list):


    #----Оценка параметров-------

    result = {}
    for work in work_list:
        en = int(input(f'Сколько энергии нужно затратить на задачу от 0 до 10:{work}\n'))
        ur = int(input(f'Насколько срочная задача от 0 до 10:{work}\n'))
        p = PriorityScore(en,ur,1,1)
        result[work] = p.get_score()
    print(result)

    #----------------------------

    #----Сортировка--------------

    result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
    result_list = [i for i in result.keys()]
    print(result_list)
    json_data = json.dumps(result_list)

    #----------------------------

    return json_data