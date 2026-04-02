#include "Libraries.hpp"

void MergeIn(std::vector<int64_t>& a, std::vector<int64_t>& b) {
  size_t i = a.size() - b.size();
  size_t j = b.size();
  size_t k = a.size();
  while (j > 0) {
    if (i > 0 && a[i - 1] > b[j - 1]) {
      a[k - 1] = a[i - 1];
      i--;
      k--;
    } else {
      a[k - 1] = b[j - 1];
      j--;
      k--;
    }
  }
}