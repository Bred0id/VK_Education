#include "Libraries.hpp"

void Reverse(std::vector<int64_t>& a, size_t l, size_t r) {
  while (l < r) {
    std::swap(a[l], a[r]);
    l++;
    r--;
  }
}

void ReverseK(std::vector<int64_t>& a, int64_t k) {
  if (a.empty()) {
    return;
  }
  size_t n = a.size();
  k = k % n;
  if (k == 0) {
    return;
  }
  Reverse(a, 0, n - 1);
  Reverse(a, 0, k - 1);
  Reverse(a, k, n - 1);
}