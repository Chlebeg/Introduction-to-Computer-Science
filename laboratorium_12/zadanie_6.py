# Zadanie 6.
# Dany jest zbiór punktów leżących na płaszczyźnie opisany przy pomocy struktury:
# "data = [(x1, y1), (x2, y2), (x3, y3), ..., (xN, yN)]"
# Proszę napisać funkcję, która zwraca wartość True jeżeli w zbiorze istnieją 4
# punkty wyznaczające prostokąt o bokach o długości a i b, takich, że a≠b oraz równoległych do osi układu współrzędnych,
# a wewnątrz tego prostokąta nie ma żadnych innych punktów. Do funkcji należy przekazać strukturę opisującą położenie punktów.

class CartesianGrid:
    def __init__(self, points_list):
        self.points_list = points_list

    def points_sorter(self, starting_point):
        same_on_x = []
        same_on_y = []
        not_connected = []
        for point in self.points_list:
            if point[0] == starting_point[0] and point[1] != starting_point[1]:
                same_on_x.append(point)
            elif point[1] == starting_point[1] and point[0] != starting_point[0]:
                same_on_y.append(point)
            else:
                not_connected.append(point)
        return same_on_x, same_on_y, not_connected

    def get_possible_points(self, starting_point):
        y_value, x_value, not_connected = self.points_sorter(starting_point)
        possible_points = []
        for y_v in y_value:
            for x_v in x_value:
                possible_points.append((x_v[0],y_v[1]))
                print(possible_points)
        return possible_points, not_connected

    def make_rectangle(self, starting_point, rectangle_list):
        class Rectangle:
            def __init__(self, min_x_value, max_x_value, min_y_value, max_y_value):
                self.min_x = min_x_value
                self.max_x = max_x_value
                self.min_y = min_y_value
                self.max_y = max_y_value

        possible_points, not_connected = self.get_possible_points(starting_point)
        for re_point in possible_points:
            if re_point in not_connected:
                x_boundaries = sorted((starting_point[0], re_point[0]))
                y_boundaries = sorted((starting_point[1], re_point[1]))
                if abs(x_boundaries[1]) - abs(x_boundaries[0]) != abs(y_boundaries[1]) - abs(y_boundaries[0]):
                    rectangle_list.append(Rectangle(x_boundaries[0], x_boundaries[1], y_boundaries[0], y_boundaries[1]))
        return rectangle_list

    def is_there_rectangle_without_point_init(self):
        rectangle_list = []
        for point in self.points_list:
            rectangle_list = self.make_rectangle(point,rectangle_list)
        for rectangle in rectangle_list:
            flag = True
            for point in self.points_list:
                print(rectangle.min_x, point, rectangle.max_x)
                if rectangle.min_x < point[0] < rectangle.max_x:
                    print(rectangle.min_y, point, rectangle.max_y)
                    if rectangle.min_y < point[1] < rectangle.max_y:
                        flag = False
            if flag == True:
                return True
        return False


dane = CartesianGrid([(2, 1), (6, 9), (6, 3), (15, 11), (11, 9), (8, 2), (11, 3), (15, 2), (2, 11), (8, 14)])
print(dane.is_there_rectangle_without_point_init())

