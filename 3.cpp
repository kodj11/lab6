#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

class Student {
public:
    std::string lastName;
    std::string firstName;
    std::string middleName;
    int group;
    int grades[3];

    friend std::istream& operator>>(std::istream& is, Student& s);
    friend std::ostream& operator<<(std::ostream& os, const Student& s);

    bool operator<(const Student& other) const {
        return getAverageGrade() < other.getAverageGrade();
    }

    bool operator>(const Student& other) const {
        return getAverageGrade() > other.getAverageGrade();
    }

private:
    double getAverageGrade() const {
        int sum = 0;
        for (int grade : grades) {
            sum += grade;
        }
        return sum / 3.0;
    }
};

std::istream& operator>>(std::istream& is, Student& s) {
    is >> s.lastName >> s.firstName >> s.middleName
        >> s.group >> s.grades[0] >> s.grades[1] >> s.grades[2];
    return is;
}

std::ostream& operator<<(std::ostream& os, const Student& s) {
    os << s.lastName << " " << s.firstName << " " << s.middleName
        << " " << s.group << " " << s.grades[0] << " " << s.grades[1] << " " << s.grades[2];
    return os;
}

int main() {
    const int NUM_STUDENTS = 5;
    Student students[NUM_STUDENTS];

    std::ifstream input("students.txt");
    for (int i = 0; i < NUM_STUDENTS; i++) {
        input >> students[i];
    }

    std::sort(students, students + NUM_STUDENTS, std::greater<Student>());

    // סמנעטנמגךא ג פיכ
    std::ofstream output("sorted_students.txt");
    for (const auto& s : students) {
        output << s << "\n";
    }

    std::cout << "Student: " << students[0] << " > "
        << "student: " << students[1] << "? -> " << (students[0] > students[1]) << std::endl;

    return 0;
}