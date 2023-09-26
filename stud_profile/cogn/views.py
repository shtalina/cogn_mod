from django.shortcuts import render
from django.http import HttpResponse
from .models import Students, Student, Marks, Faculties, Groups
from io import BytesIO
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import mpld3


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
        name='Cognitive Metrics'
    ))

    # Обновляем макет
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(values) + 10],
            ),
        ),
        showlegend=False,
        #title='Когнитивная модель студента:',


        font=dict(size=12)

    )

    # Преобразуем фигуру в HTML
    graph_html = fig.to_html()

    return render(request, 'cogn/profile.html', {
        'graph_html': graph_html,
        'data': data,
        'student': student,
        'mark': mark,
        'graph_htm': graph_htm,
    })
