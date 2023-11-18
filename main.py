from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)  # координаты еды
snake = [vector(10, 0)]  # координаты змеи
aim = vector(0, -10)  # направление движения змеи

def change(x, y):
    """
    Функция для изменения направления движения
    Параметры x и y определяют новое направление вектора aim
    """
    aim.x = x
    aim.y = y

def inside(head):
    """
    Функция, проверяющая, находится ли голова змеи в пределах игрового поля
    """
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    """
    Функция, обрабатывающая движение змеи
    """
    head = snake[-1].copy()
    head.move(aim)

    # проверка на столкновение с границами поля или самой собой
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')  # отрисовка красного квадрата
        update()
        return

    snake.append(head)

    # змея съедает еду
    if head == food:
        print('Snake:', len(snake))  # вывод длины змеи
        food.x = randrange(-15, 15) * 10  # новые координаты еды
        food.y = randrange(-15, 15) * 10
    else:
        # удаление хвоста змеи при отсутствии еды
        snake.pop(0)

    clear()

    # отрисовка змеи
    for body in snake:
        square(body.x, body.y, 9, 'black')  # черные квадраты

    square(food.x, food.y, 9, 'green')  # отрисовка еды
    update()
    ontimer(move, 100)  # рекурсивный вызов функции через 100 миллисекунд

setup(420, 420, 370, 0)  # настройка экрана
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')  # назначение клавиш управления
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
