#include "List.hpp"

bool IsSubstring(const std::string& a, const std::string& b) {
  size_t i = 0;
  size_t j = 0;
  while (i < a.size() && j < b.size()) {
    if (a[i] == b[j]) {
      i++;
    }
    j++;
  }
  if (i == a.size()) {
    return true;
  }
  return false;
}
