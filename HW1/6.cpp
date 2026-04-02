#include "Libraries.hpp"

void MoveTwo(std::vector<int64_t>& a) {
  size_t j = 0;
  for (size_t i = 0; i < a.size(); i++) {
    if (a[i] % 2 == 0) {
      std::swap(a[j], a[i]);
      j++;
    }
  }
}