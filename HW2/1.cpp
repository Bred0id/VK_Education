#include "List.hpp"

Node* ReverseList(Node* head) {
  Node* prev = nullptr;
  while (head != nullptr) {
    Node* next = head->next;
    head->next = prev;
    prev = head;
    head = next;
  }
  return prev;
}
