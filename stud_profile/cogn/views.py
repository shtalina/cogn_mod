from django.shortcuts import render
from django.http import HttpResponse
from .models import Students, Student, Marks, Faculties, Groups, Comp
from io import BytesIO

import plotly.graph_objects as go



def Stud(request):
    data = Students.objects.all()

    return render(request, 'cogn/stud.html', {'data': data})

def faculties(request):
    facultie = Faculties.objects.all()
    grouped_faculties = []

    for faculty in facultie:
        groups = Groups.objects.filter(fak_id=faculty.fak_id).order_by('course')
        grouped_faculties.append({'faculty': faculty, 'groups': groups})

    return render(request, 'cogn/faculties.html', {'grouped_faculties': grouped_faculties})
def profile(request, id):
    data = Students.objects.get(pk=id)
    student = Student.objects.get(pk=id)
    mark = Marks.objects.filter(id=id)
    comp = Comp.objects.all()
    # Получите все записи экзаменов для данного студента

    # Создайте списки для хранения данных о семестрах и средних баллах
    semesters = []
    average_scores = []

    # Итерируйтесь по записям экзаменов и вычисляйте средний балл для каждой сессии
    current_semester = 0
    current_scores = []
    for record in mark:
        if record.is_examen == 1:
            if record.number_of_semester != current_semester:
                if current_scores:
                    # Рассчитайте средний балл для текущей сессии и добавьте данные в списки
                    average_score = sum(current_scores) / len(current_scores)
                    semesters.append(current_semester)
                    average_scores.append(average_score)

                # Сбросьте текущие данные для новой сессии
                current_semester = record.number_of_semester
                current_scores = [record.mark]
            else:
                current_scores.append(record.mark)

    # Добавьте последнюю сессию, если есть данные
    if current_scores:
        average_score = sum(current_scores) / len(current_scores)
        semesters.append(current_semester)
        average_scores.append(average_score)

    # Создайте график для траектории изменения среднего балла
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=semesters, y=average_scores, mode='lines+markers'))
    fig.update_layout(xaxis_title='Семестр', yaxis_title='Средний балл')

    # Преобразуйте график в HTML и передайте его в шаблон
    graph_htm = fig.to_html(full_html=False)

    #Тут уже пентагон
    cognitive_data = {
        "Логическое мышление": student.metric1,
        "Математические навыки": student.metric2,
        "Визуальное восприятие": student.metric3,
        "Речевые способности": student.metric4,
        "Пространственное мышление": student.metric5,
    }

    # Убедитесь, что у вас есть ровно 5 категорий и значений
    categories = list(cognitive_data.keys())

    # Получение списка значений для каждой категории
    values = list(cognitive_data.values())

    # Создаем фигуру для пентагонального графика
    fig = go.Figure()

    # Добавляем границы пентагона
    fig.add_trace(go.Scatterpolar(
        r=values + values[:1],
        theta=categories + categories[:1],
        fill='toself',
        name='Cognitive Metrics',
        line=dict(color='rgb(118, 138, 204)'),


    ))

    # Добавляем значения на точки
    for i, (category, value) in enumerate(zip(categories, values)):
        fig.add_trace(go.Scatterpolar(
            r=[value, value, value, value, value, value],  # Позиционируем значение на соответствующей категории
            theta=[category, category, category, category, category, category],  # 6 точек вокруг категории
            mode='markers+text',  # Включаем маркеры и текст
            text=[f'{value }' + 'ㅤ'],  # Устанавливаем текст метки
            textposition='top right' if i % 2 == 0 else 'top left',  # Располагаем текст в нижней части точки
              # Устанавливаем размер маркера
            name=category,  # Устанавливаем имя категории
            marker = dict(color='rgb(64, 83, 145)')
        ))

    # Обновляем макет
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(values) + 15],
                showline=False,  # Устанавливаем showline в False
                showticklabels=False
            ),
        ),
        showlegend=False,
        # title='Когнитивная модель студента:',

        font=dict(size=12)
    )

    # Преобразуем фигуру в HTML
    graph_html = fig.to_html()


    # А тут будет когнитивная моделька

    values = [student.intro_extro, student.adapt, student.social, student.refl, student.motivation]
    intro_extro_value = student.intro_extro
    adapt_value = student.adapt
    social_value = student.social
    refl_value = student.refl
    motivation_value = student.motivation

    # Задайте имена шкал
    scales = ['Стрессоустойчивость', 'Адаптивность', 'Уровень общительности', 'Способность к рефлексии', 'Самомотивация']

    # Создайте бар-график для каждой шкалы
    fig = go.Figure()
    fig.add_trace(go.Bar(x=[intro_extro_value], y=[scales[0]], orientation='h', name=scales[0],  marker = dict(color='rgb(108, 134, 217)')))
    fig.add_trace(go.Bar(x=[adapt_value], y=[scales[1]], orientation='h', name=scales[1],  marker = dict(color='rgb(85, 110, 189)')))
    fig.add_trace(go.Bar(x=[social_value], y=[scales[2]], orientation='h', name=scales[2],  marker = dict(color='rgb(79, 105, 189)')))
    fig.add_trace(go.Bar(x=[refl_value], y=[scales[3]], orientation='h', name=scales[3],  marker = dict(color='rgb(104, 124, 189)')))
    fig.add_trace(go.Bar(x=[motivation_value], y=[scales[4]], orientation='h', name=scales[4],  marker = dict(color='rgb(79, 98, 158)')))

    # Настройте внешний вид графика
    fig.update_layout(
        barmode='relative',
        xaxis_title='Значение',
        yaxis_title='Шкала',

    )

    # Преобразуйте график в HTML
    graph_ht = fig.to_html(full_html=False)

    return render(request, 'cogn/profile.html', {
        'graph_html': graph_html,
        'data': data,
        'student': student,
        'mark': mark,
        'graph_htm': graph_htm,
        'graph_ht': graph_ht,
        'comp': comp,
    })

def contacts(request):
    return render(request, 'cogn/contacts.html')


