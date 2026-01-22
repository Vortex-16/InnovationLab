#include <stdio.h>
#include <stdlib.h>
struct Node {
    int data;
    struct Node* next;
};
struct Node* head = NULL;
void insert(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    if (head == NULL) {
        head = newNode;
        newNode->next = head;
    } else {
        struct Node* temp = head;
        while (temp->next != head) {
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->next = head;
    }
}
void insertAtBeginning(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    if (head == NULL) {
        head = newNode;
        newNode->next = head;
    } else {
        struct Node* temp = head;
        while (temp->next != head) {
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->next = head;
        head = newNode;
    }
}
void insertAtPosition(int data, int position) {
    if (position == 0) {
        insertAtBeginning(data);
        return;
    }
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    struct Node* temp = head;
    for (int i = 0; i < position - 1; i++) {
        temp = temp->next;
        if (temp == head) {
            printf("Position out of bounds\n");
            free(newNode);
            return;
        }
    }
    newNode->next = temp->next;
    temp->next = newNode;
}
void deleteAtPosition(int position) {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    struct Node* temp = head;
    if (position == 0) {
        while (temp->next != head) {
            temp = temp->next;
        }
        if (head->next == head) {
            free(head);
            head = NULL;
        } else {
            struct Node* toDelete = head;
            temp->next = head->next;
            head = head->next;
            free(toDelete);
        }
        return;
    }
    for (int i = 0; i < position - 1; i++) {
        temp = temp->next;
        if (temp->next == head) {
            printf("Position out of bounds\n");
            return;
        }
    }
    struct Node* toDelete = temp->next;
    temp->next = toDelete->next;
    free(toDelete);
}
void display() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    struct Node* temp = head;
    do {
        printf("%d -> ", temp->data);
        temp = temp->next;
    } while (temp != head);
    printf("(head: %d)\n", head->data);
}
int main() {
    insert(10);
    insert(20);
    insertAtBeginning(5);
    insertAtPosition(15, 2);
    display();
    deleteAtPosition(2);
    display();
    deleteAtPosition(0);
    display();
    return 0;
}