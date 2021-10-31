import functools


@functools.total_ordering
class ClassToNumber:
    def __init__(self, name, class_list):
        self.name = name
        self.class_list = self._get_formatted_class_list(class_list)
        self.number_value = self._get_formatted_number_value()

    def _get_formatted_class_list(self, class_list):
        class_list = class_list.split("-")
        class_list.reverse()
        while len(class_list) < 10:
            class_list.append("middle")
        return class_list

    def _get_formatted_number_value(self):
        number_value_list = map(lambda class_value: self._class_value_to_number(class_value), self.class_list)
        return int("".join(number_value_list))

    def _class_value_to_number(self, class_value):
        if class_value == "upper":
            return '3'
        elif class_value == "middle":
            return '2'
        elif class_value == "lower":
            return '1'
        else:
            raise Exception("invalid class value")

    def __lt__(self, other):
        if self.number_value != other.number_value:
            return self.number_value < other.number_value
        else:
            return self.name > other.name


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        class_list = []
        for _ in range(n):
            name, value, _ = input().split()
            name = name[:-1]
            class_list.append(ClassToNumber(name, value))
        class_list.sort(reverse=True)
        for class_value in class_list:
            print(class_value.name)
        print("==============================")
