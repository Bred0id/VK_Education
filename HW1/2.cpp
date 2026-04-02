#include "Libraries.hpp"

std::vector<int64_t> Merge(const std::vector<int64_t>& a, const std::vector<int64_t>& b) {
  std::vector<int64_t> res;
  size_t i = 0;
  size_t j = 0;
  while (i < a.size() && j < b.size()) {
    if (a[i] <= b[j]) {
      res.push_back(a[i]);
      i++;
    } else {
      res.push_back(b[j]);
      j++;
    }
  }
  while (i < a.size()) {
    res.push_back(a[i]);
    i++;
  }
  while (j < b.size()) {
    res.push_back(b[j]);
    j++;
  }
  return res;
}