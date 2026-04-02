#include "List.hpp"

bool IsPalindrome(const std::string& s) {
  if (s.empty()) {
    return true;
  }
  size_t left = 0;
  size_t right = s.size() - 1;
  while (left < right) {
    if (s[left] != s[right]) {
      return false;
    }
    left++;
    right--;
  }
  return true;
}
