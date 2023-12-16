import turtle as t

f = 1

print("Отрезок")
if f == 1:
    print("Координаты должны быть в диапазоне: (-350 <= x <= 350, -300 <= y <= 300)")
    t1 = [int(j) for j in input("Введите координаты первой точки: ").split()]
    if len(t1) != 2:
        raise TypeError("Координата имеет ДВА значения: x y")
    else:
        if t1[0] > 350 or t1[0] < -350 or t1[1] > 300 or t1[1] < -300:
            raise TypeError("Координаты должны быть в диапазоне: (-350 <= x <= 350, -300 <= y <= 300)")
        t2 = [int(j) for j in input("Введите координаты второй точки: ").split()]
        if len(t2) != 2:
            raise TypeError("Координата имеет ДВА значения: x y")
        else:
            if t2[0] > 350 or t2[0] < -350 or t2[1] > 300 or t2[1] < -300:
                raise TypeError("Координаты должны быть в диапазоне: (-350 <= x <= 350, -300 <= y <= 300)")
            t.speed(50)
            t.color("black")
            t.up()
            t.goto(t1[0], t1[1])
            t.down()
            t.goto(t2[0], t2[1])
            f += 1

print("\nПрямоугольник")
if f == 2:
    print("Координаты должны быть в диапазоне: (-350 <= x <= 350, -300 <= y <= 300)")
    t1 = [int(j) for j in input("Введите координаты первой вершины: ").split()]
    if len(t1) != 2:
        raise TypeError("Координата имеет ДВА значения: x y")
    else:
        if t1[0] > 350 or t1[0] < -350 or t1[1] > 300 or t1[1] < -300:
            raise TypeError("Координаты должны быть в диапазоне: (-350 <= x <= 350, -300 <= y <= 300)")
        t2 = [int(j) for j in input("Введите координаты второй вершины: ").split()]
        if len(t2) != 2:
            raise TypeError("Координата имеет ДВА значения: x y")
        else:
            if t2[0] > 350 or t2[0] < -350 or t2[1] > 300 or t2[1] < -300:
                raise TypeError("Координаты должны быть в диапазоне: (-350 <= x <= 350, -300 <= y <= 300)")
            if t1[0] == t2[0] or t1[1] == t2[1]:
                raise TypeError("Прямоугольник не построить по таким координатам")
            t.speed(50)
            t.color("black")
            t.up()
            t.goto(t1[0], t1[1])
            t.down()
            t.goto(t2[0], t1[1])
            t.goto(t2[0], t2[1])
            t.goto(t1[0], t2[1])
            t.goto(t1[0], t1[1])
            f += 1

print("\nОкружность")
if f == 3:
    print("Координаты должны быть в диапазоне: (-350 <= x <= 350, -300 <= y <= 300)")
    t1 = [int(j) for j in input("Введите координаты центра окружности: ").split()]
    if len(t1) != 2:
        raise TypeError("Координата имеет ДВА значения: x y")
    else:
        if t1[0] > 350 or t1[0] < -350 or t1[1] > 300 or t1[1] < -300:
            raise TypeError("Координаты должны быть в диапазоне: (-350 <= x <= 350, -300 <= y <= 300)")
        t2 = int(input("Введите значение радиуса: "))
        if (t2 + abs(t1[0])) > 350 or (t2 + abs(t1[1])) > 300:
            raise TypeError("Недопустимое значение радиуса для данной координаты центра")
        if t2 < 0:
            raise TypeError("Радиус не может быть отрицательным")
        t.speed(50)
        t.color("black")
        t.up()
        t.goto(t1[0], t1[1])
        t.down()
        t.circle(t2)
        f += 1

print("\nРавносторонний треугольник")
if f == 4:
    print("Координаты должны быть в диапазоне: (-350 <= x <= 350, -300 <= y <= 300)")
    t1 = [int(j) for j in input("Введите координаты вершины треугольника: ").split()]
    if len(t1) != 2:
        raise TypeError("Координата имеет ДВА значения: x y")
    else:
        if t1[0] > 350 or t1[0] < -350 or t1[1] > 300 or t1[1] < -300:
            raise TypeError("Координаты должны быть в диапазоне: (-350 <= x <= 350, -300 <= y <= 300)")
        t2 = int(input("Введите значение высоты: "))
        a = (t2 * 2 / (3 ** 0.5))
        if (a + abs(t1[0])) > 350 or (a + abs(t1[1])) > 300:
            raise TypeError("Недопустимое значение высоты для данной координаты вершины")
        if a < 0:
            raise TypeError("Высота не может быть отрицательной")
        t.speed(50)
        t.color("black")
        t.up()
        t.goto(t1[0], t1[1])
        t.down()
        t.forward(a)
        t.left(120)
        t.forward(a)
        t.left(120)
        t.forward(a)
        f += 1

if f == 5:
    print("\nВсе фигуры нарисованы!")

t.mainloop()
