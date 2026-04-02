
#ifndef LIST_HPP
#define LIST_HPP

#include <iostream>
#include <vector>
#include <string>
#include <cstdint>

struct Node {
  int64_t value;
  Node* next = nullptr;
};

struct List {
  Node* head = nullptr;
  Node* tail = nullptr;
  size_t size = 0;

  void PushBack(int64_t value) {
    Node* node = new Node();
    node->value = value;
    if (tail == nullptr) {
      head = node;
      tail = node;
    } else {
      tail->next = node;
      tail = node;
    }
    size++;
  }

  void Clear() {
    Node* cur = head;
    while (cur != nullptr) {
      Node* next = cur->next;
      delete cur;
      cur = next;
    }
    head = nullptr;
    tail = nullptr;
    size = 0;
  }
};

#endif