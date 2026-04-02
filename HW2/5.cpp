#include "List.hpp"

bool TwoSumSorted(const std::vector<int64_t>& nums, int64_t target) {
  if (nums.size() < 2) {
    return false;
  }
  size_t left = 0;
  size_t right = nums.size() - 1;
  while (left < right) {
    int64_t sum = nums[left] + nums[right];
    if (sum == target) {
      return true;
    }
    if (sum < target) {
      left++;
    } else {
      right--;
    }
  }
  return false;
}
