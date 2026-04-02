#include "List.hpp"

Node* DeleteValue(Node* head, int64_t value) {
  Node dummy;
  dummy.next = head;
  Node* cur = &dummy;
  while (cur->next != nullptr) {
    if (cur->next->value == value) {
      Node* del = cur->next;
      cur->next = del->next;
      delete del;
    } else {
      cur = cur->next;
    }
  }
  return dummy.next;
}