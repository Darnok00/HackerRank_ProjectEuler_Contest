#include <iostream>
#include <vector>
#include <cmath>
#include <unordered_map>

const int MAX_N = 1000;

void print_result(const std::vector<int>& result) {
    for (int element : result) {
        std::cout << element << std::endl;
    }
}

int get_number_dividers(int n) {
    int number_dividers = 2;
    for (int i = 2; i <= static_cast<int>(std::sqrt(n)); i++) {
        if (n % i == 0) {
            number_dividers += 2;
            if (i * i == n) {
                number_dividers -= 1;
            }
        }
    }
    return number_dividers;
}

std::unordered_map<int, int> get_triangle_dividers_dict(int max_n) {
    std::unordered_map<int, int> dict_triangle_dividers;
    int actual_triangle = 1;
    int number_triangle = 1;
    int max_dividers = 1;

    while (max_dividers < max_n) {
        number_triangle += 1;
        actual_triangle += number_triangle;
        int number_dividers = get_number_dividers(actual_triangle);
        if (number_dividers > max_dividers) {
            for (int i = max_dividers; i < number_dividers; i++) {
                dict_triangle_dividers[i] = actual_triangle;
            }
            max_dividers = number_dividers;
        }
    }

    return dict_triangle_dividers;
}

std::vector<int> find_triangles(int t) {
    std::vector<int> output_array;
    std::unordered_map<int, int> dict_triangles_dividers = get_triangle_dividers_dict(MAX_N);

    for (int i = 0; i < t; i++) {
        int n;
        std::cin >> n;
        output_array.push_back(dict_triangles_dividers[n]);
    }

    return output_array;
}

int main() {
    int t;
    std::cin >> t;
    std::vector<int> result = find_triangles(t);
    print_result(result);

    return 0;
}
