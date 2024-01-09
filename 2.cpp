#include <iostream>

class Rectangle {
private:
    double x = 0;
    double y = 0;
    double width = 1;
    double height = 1;

public:
    friend std::ostream& operator<<(std::ostream& out, const Rectangle& r);

    friend std::istream& operator>>(std::istream& in, Rectangle& r);

    Rectangle(double width, double height) : width(width), height(height) {}

    ~Rectangle() {
        std::cout << "Деструктор для объекта " << *this << std::endl;
    }

    double getArea() const {
        return width * height;
    }

    double left() const { return x; }
    double right() const { return x + width; }
    double bottom() const { return y; }
    double top() const { return y + height; }

    Rectangle operator*(const Rectangle& other) const {
        double x1 = std::max(left(), other.left());
        double y1 = std::max(bottom(), other.bottom());
        double x2 = std::min(right(), other.right());
        double y2 = std::min(top(), other.top());

        if (x2 <= x1 || y2 <= y1) {
            return Rectangle(0, 0); // нет персечения
        }

        return Rectangle(x2 - x1, y2 - y1);
    }

    bool operator>(const Rectangle & other) const {
        return getArea() > other.getArea();
    }

    bool operator<(const Rectangle& other) const {
        return getArea() < other.getArea();
    }
};

int main(void) {
    Rectangle r1(3, 4);
    Rectangle r2(2, 5);
    std::cout << "rectangle 1 (3,4)" << std::endl;
    std::cout << "rectangle 2 (2,5)" << std::endl;

    auto intersection = r1 * r2;
    std::cout << "Peresechenie: " << intersection << std::endl;

    std::cout << "rectangle 1 area: " << r1.getArea() << std::endl;
    std::cout << "rectangle 2 area: " << r2.getArea() << std::endl;

    if (r1 > r2) {
        std::cout << "rectangle 1 area > rectangle 2 area" << std::endl;
    }
    else {
        std::cout << "rectangle 1 area < rectangle 2 area" << std::endl;
    }
}


std::ostream& operator<<(std::ostream& out, const Rectangle& r) {
    out << "Rectangle(" << r.left() << "," << r.bottom() << ","
        << r.width << "," << r.height << ")";
    return out;
}

std::istream& operator>>(std::istream& in, Rectangle& r) {
    in >> r.x >> r.y >> r.width >> r.height;
    return in;
}