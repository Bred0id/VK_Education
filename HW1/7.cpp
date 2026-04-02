#include "Libraries.hpp"

void MoveZeroes(std::vector<int64_t>& a) {
  size_t j = 0;
  for (size_t i = 0; i < a.size(); i++) {
    if (a[i] != 0) {
      a[j] = a[i];
      j++;
    }
  }
  while (j < a.size()) {
    a[j] = 0;
    j++;
  }
}