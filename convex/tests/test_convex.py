from pytest import approx
from math import sqrt
from r2point import R2Point
from convex import Figure, Void, Point, Segment, Polygon


class TestVoid:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Void()

    # Нульугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Void (нульугольник)
    def test_void(self):
        assert isinstance(self.f, Void)

    # Периметр нульугольника нулевой
    def test_perimeter(self):
        assert self.f.perimeter() == 0.0

    # Площадь нульугольника нулевая
    def test_аrea(self):
        assert self.f.area() == 0.0

    # При добавлении точки нульугольник превращается в одноугольник
    def test_add(self):
        assert isinstance(self.f.add(R2Point(0.0, 0.0)), Point)


class TestPoint:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Point(R2Point(0.0, 0.0))

    # Одноугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Point (одноугольник)
    def test_point(self):
        assert isinstance(self.f, Point)

    # Периметр одноугольника нулевой
    def test_perimeter(self):
        assert self.f.perimeter() == 0.0

    # Площадь одноугольника нулевая
    def test_аrea(self):
        assert self.f.area() == 0.0

    # При добавлении точки одноугольник может не измениться
    def test_add1(self):
        assert self.f.add(R2Point(0.0, 0.0)) is self.f

    # При добавлении точки одноугольник может превратиться в двуугольник
    def test_add2(self):
        assert isinstance(self.f.add(R2Point(1.0, 0.0)), Segment)


class TestSegment:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Segment(R2Point(0.0, 0.0), R2Point(1.0, 0.0))

    # Двуугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Segment (двуугольник)
    def test_segment(self):
        assert isinstance(self.f, Segment)

    # Периметр двуугольника равен удвоенной длине отрезка
    def test_perimeter(self):
        assert self.f.perimeter() == approx(2.0)

    # Площадь двуугольника нулевая
    def test_аrea(self):
        assert self.f.area() == 0.0

    # При добавлении точки двуугольник может не измениться
    def test_add1(self):
        assert self.f.add(R2Point(0.5, 0.0)) is self.f

    # При добавлении точки двуугольник может превратиться в другой двуугольник
    def test_add2(self):
        assert isinstance(self.f.add(R2Point(2.0, 0.0)), Segment)

    # При добавлении точки двуугольник может превратиться в треугольник
    def test_add2(self):
        assert isinstance(self.f.add(R2Point(0.0, 1.0)), Polygon)


class TestPolygon:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Polygon(
            R2Point(
                0.0, 0.0), R2Point(
                1.0, 0.0), R2Point(
                0.0, 1.0))

    # Многоугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Polygon (многоугольник)
    def test_polygon(self):
        assert isinstance(self.f, Polygon)

    # Изменение количества вершин многоугольника
    #   изначально их три
    def test_vertexes1(self):
        assert self.f.points.size() == 3
    #   добавление точки внутрь многоугольника не меняет их количества

    def test_vertexes2(self):
        assert self.f.add(R2Point(0.1, 0.1)).points.size() == 3
    #   добавление другой точки может изменить их количество

    def test_vertexes3(self):
        assert self.f.add(R2Point(1.0, 1.0)).points.size() == 4
    #   изменения выпуклой оболочки могут и уменьшать их количество

    def test_vertexes4(self):
        assert self.f.add(
            R2Point(
                0.4,
                1.0)).add(
            R2Point(
                1.0,
                0.4)).add(
                    R2Point(
                        0.8,
                        0.9)).add(
                            R2Point(
                                0.9,
                                0.8)).points.size() == 7
        assert self.f.add(R2Point(2.0, 2.0)).points.size() == 4

    # Изменение периметра многоугольника
    #   изначально он равен сумме длин сторон
    def test_perimeter1(self):
        assert self.f.perimeter() == approx(2.0 + sqrt(2.0))
    #   добавление точки может его изменить

    def test_perimeter2(self):
        assert self.f.add(R2Point(1.0, 1.0)).perimeter() == approx(4.0)

    # Изменение площади многоугольника
    #   изначально она равна (неориентированной) площади треугольника
    def test_аrea1(self):
        assert self.f.area() == approx(0.5)
    #   добавление точки может увеличить площадь

    def test_area2(self):
        assert self.f.add(R2Point(1.0, 1.0)).area() == approx(1.0)

    def count_points_in_triangle1(self):
        p1 = R2Point(2.0, 0.0)
        p2 = R2Point(0.0, 0.0)
        p3 = R2Point(0.0, 100.0)
        p4 = R2Point(10.0, 0.0)
        p5 = R2Point(0.0, 0.0)
        p6 = R2Point(0.0, 10.0)
        test = Polygon(p4, p5, p6)
        assert test.count_points_in_triangle(p1, p2, p3) == 2

    def count_points_in_triangle2(self):
        p1 = R2Point(100.0, 0.0)
        p2 = R2Point(0.0, 0.0)
        p3 = R2Point(0.0, 100.0)
        p4 = R2Point(60.0, 47.0)
        p5 = R2Point(25.0, 76.0)
        p6 = R2Point(10.0, 84.0)
        p7 = R2Point(76.0, 100.0)
        p8 = R2Point(98.0, 28.0)
        p9 = R2Point(17.0, 73.0)
        p10 = R2Point(58.0, 71.0)
        p11 = R2Point(16.0, 22.0)
        p12 = R2Point(25.0, 91.0)
        test = Polygon(p4, p5, p6)
        test.add(p7)
        test.add(p8)
        test.add(p9)
        test.add(p10)
        test.add(p11)
        test.add(p12)
        assert test.count_points_in_triangle(p1, p2, p3) == 2

    def count_points_in_triangle3(self):
        p1 = R2Point(100.0, 0.0)
        p2 = R2Point(100.0, 100.0)
        p3 = R2Point(0.0, 100.0)
        p4 = R2Point(60.0, 47.0)
        p5 = R2Point(25.0, 76.0)
        p6 = R2Point(10.0, 84.0)
        p7 = R2Point(76.0, 100.0)
        p8 = R2Point(98.0, 28.0)
        p9 = R2Point(17.0, 73.0)
        p10 = R2Point(58.0, 71.0)
        p11 = R2Point(16.0, 22.0)
        p12 = R2Point(25.0, 91.0)
        test = Polygon(p4, p5, p6)
        test.add(p7)
        test.add(p8)
        test.add(p9)
        test.add(p10)
        test.add(p11)
        test.add(p12)
        assert test.count_points_in_triangle(p1, p2, p3) == 3

    def count_points_in_triangle4(self):
        p1 = R2Point(33.0, 0.0)
        p2 = R2Point(0.0, 0.0)
        p3 = R2Point(0.0, 33.0)
        p4 = R2Point(1.0, 1.0)
        p5 = R2Point(3.0, 2.0)
        p6 = R2Point(2.0, 3.0)
        p7 = R2Point(4.0, 4.0)
        test = Polygon(p4, p5, p6)
        test.add(p7)
        assert test.count_points_in_triangle(p1, p2, p3) == 4

    def count_points_in_triangle5(self):
        p1 = R2Point(0.0, 0.0)
        p2 = R2Point(10.0, 5.0)
        p3 = R2Point(2.0, 10.0)
        p4 = R2Point(2.0, 4.0)
        p5 = R2Point(0.0, 7.0)
        p6 = R2Point(3.0, 7.0)
        p7 = R2Point(10.0, 9.0)
        p8 = R2Point(7.0, 5.0)
        p9 = R2Point(1.0, 3.0)
        p10 = R2Point(7.0, 2.0)
        test = Polygon(p4, p5, p6)
        test.add(p7)
        test.add(p8)
        test.add(p9)
        test.add(p10)
        assert test.count_points_in_triangle(p1, p2, p3) == 1

    def count_points_in_triangle6(self):
        p1 = R2Point(5.0, 0.0)
        p2 = R2Point(0.0, 5.0)
        p3 = R2Point(5.0, 10.0)
        p4 = R2Point(2.0, 4.0)
        p5 = R2Point(0.0, 7.0)
        p6 = R2Point(3.0, 7.0)
        p7 = R2Point(10.0, 9.0)
        p8 = R2Point(7.0, 5.0)
        p9 = R2Point(1.0, 3.0)
        p10 = R2Point(7.0, 2.0)
        test = Polygon(p4, p5, p6)
        test.add(p7)
        test.add(p8)
        test.add(p9)
        test.add(p10)
        assert test.count_points_in_triangle(p1, p2, p3) == 0
