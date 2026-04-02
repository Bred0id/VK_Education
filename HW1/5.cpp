#include "Libraries.hpp"

void SortThree(std::vector<int64_t>& a) {
  size_t l = 0;
  size_t m = 0;
  size_t r = a.size();
  while (m < r) {
    if (a[m] == 0) {
      std::swap(a[l], a[m]);
      l++;
      m++;
    } else if (a[m] == 1) {
      m++;
    } else {
      r--;
      std::swap(a[m], a[r]);
    }
  }
}