#include "List.hpp"

void RemoveDuplicates(std::vector<int64_t>& nums) {
  if (nums.empty()) {
    return;
  }
  size_t slow = 0;
  for (size_t fast = 1; fast < nums.size(); fast++) {
    if (nums[fast] != nums[slow]) {
      slow++;
      nums[slow] = nums[fast];
    }
  }
  size_t k = slow + 1;
  nums.resize(k);
}
