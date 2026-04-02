#include "List.hpp"

Node* MergeSortedLists(Node* a, Node* b) {
  Node dummy;
  Node* tail = &dummy;
  while (a != nullptr && b != nullptr) {
    if (a->value <= b->value) {
      tail->next = a;
      a = a->next;
    } else {
      tail->next = b;
      b = b->next;
    }
    tail = tail->next;
  }
  if (a != nullptr) {
    tail->next = a;
  } else {
    tail->next = b;
  }
  return dummy.next;
}
