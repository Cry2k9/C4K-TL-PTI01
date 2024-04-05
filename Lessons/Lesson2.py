class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        """
        Phương thức tính chu vi của hình chữ nhật
        """
        return 2 * (self.width + self.length)

    def calculate_area(self):
        """
        Phương thức tính diện tích của hình chữ nhật
        """
        return self.width * self.length

width = float(input("Nhập chiều rộng của hình chữ nhật: "))
length = float(input("Nhập chiều cao của hình chữ nhật: "))

rectangle = Rectangle(width, length)

print("Chiều rộng của hình chữ nhật:", rectangle.width)
print("Chiều cao của hình chữ nhật:", rectangle.length)
print("Chu vi của hình chữ nhật:", rectangle.calculate_perimeter())
print("Diện tích của hình chữ nhật:", rectangle.calculate_area())