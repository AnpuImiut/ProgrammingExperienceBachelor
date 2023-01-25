#include <iostream>
#include <vector>

// ---------------------------------------------------------------
// belongs to own file
// ---------------------------------------------------------------

template<typename T>
class QuadMatrix {
  std::vector<T> matrix_;
  size_t dimension_;

public:
  explicit QuadMatrix(size_t dim, T init_val)
      : dimension_{dim}, matrix_(dim * dim, init_val) {}

  size_t getDimension() {
    return dimension_;
  }

  T &operator()(size_t x, size_t y) {
    return matrix_[y * dimension_ + x];
  }
};

template<typename T>
std::ostream &operator<<(std::ostream &ostr, QuadMatrix<T> &matrix) {
  for (size_t i = 0; i < matrix.getDimension(); ++i) {
    for (size_t j = 0; j < matrix.getDimension(); ++j) {
      ostr << matrix(i, j) << " ";
    }
    ostr << '\n';
  }
  return ostr;
}

struct FileInstance {
  size_t n = 0;
  size_t q = 0;
  std::vector<int> numbers{};

  explicit FileInstance(std::istream &istr) {
    istr >> n;
    if(n == 0)
        q = 0;
    else
    {
        istr >> q;
        numbers.reserve(n);
        for (size_t i = 0; i < n; ++i) {
          int number;
          std::cin >> number;
          numbers.push_back(number);
        }
    }
  }
};

// ---------------------------------------------------------------

void algorithm(const std::vector<int> &numbers, QuadMatrix<int> &qtable) {
  int maxc = 0;
  int c = 1;

  auto n = qtable.getDimension();

  for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
      if (numbers[j] == numbers[j - 1]) {
        c++;
        if (c < maxc)
          qtable(i, j) = maxc;
        else
          qtable(i, j) = c;
      }
      else {
        if (c > maxc) {
          qtable(i, j) = c;
          maxc = c;
          c = 1;
        } else {
          qtable(i, j) = maxc;
          c = 1;
        }
      }
    }
    c = 1;
    maxc = 0;
  }
}

int main() {
    while(true)
    {
            // read data from stdin (std::cin)
      FileInstance data{std::cin};
      if (data.n == 0)
        return 0;

      // create a 0 initialized query table
      auto query_table = QuadMatrix<int>(data.n, 0);

      for (size_t i = 0; i < data.n; ++i)
        query_table(i, i) = 1;

      // do algorithm here
      algorithm(data.numbers, query_table);

      // for debugging you can now use:
      // std::cout << query_table << std::endl;

      // do the printing stuff at the end

      for(int x = 0;x < data.q;x++)
      {
          int i,j;
          std::cin>> i >> j;
          std::cout<< query_table(--i,--j)<< "\n";
      }
    }

}
