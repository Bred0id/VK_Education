#include "Libraries.hpp"

void Sort(std::vector<int64_t>& a) {
  size_t l = 0;
  size_t r = a.size();
  while (l < r) {
    if (a[l] == 0) {
      l++;
    } else {
      r--;
      std::swap(a[l], a[r]);
    }
  }
}