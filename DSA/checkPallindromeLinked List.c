#include <stdlib.h>
#include <stdio.h>
struct Node {
    int data;
    struct Node* next;
};
struct Node* head = NULL;
void insert(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = head;
    head = newNode;
}
int isPalindrome() {
    struct Node* slow = head;
    struct Node* fast = head;
    struct Node* prev = NULL;
    struct Node* next = NULL;

    // Find the middle of the linked list
    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }

    // If the number of nodes is odd, skip the middle node
    if (fast != NULL) {
        slow = slow->next;
    }

    // Compare the two halves
    struct Node* firstHalf = prev;
    struct Node* secondHalf = slow;
    while (firstHalf != NULL && secondHalf != NULL) {
        if (firstHalf->data != secondHalf->data) {
            return 0; // Not a palindrome
        }
        firstHalf = firstHalf->next;
        secondHalf = secondHalf->next;
    }
    return 1; // Is a palindrome
}
void display() {
    struct Node* temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}
void freeList() {
    struct Node* temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
}
void main() {
    insert(1);
    insert(2);
    insert(3);
    insert(2);
    insert(1);
    display();
    if (isPalindrome()) {
        printf("The linked list is a palindrome.\n");
    } else {
        printf("The linked list is not a palindrome.\n");
    }
    freeList();
}