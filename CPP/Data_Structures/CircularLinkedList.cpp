#include <iostream>
using namespace std;
struct node
{
    int value;
    node *next;
};

node *createNode(int value)
{
    node *n1 = new node;
    n1->value = value;
    n1->next = NULL;
    return n1;
}

class CircularLinkedList
{
    node *head;

public:
    CircularLinkedList() { head = NULL; }
    void insertBeginning(int value)
    {
        node *n1 = createNode(value);
        if (head == NULL)
        {
            head = n1;
            n1->next = head;
            return;
        }
        n1->next = head;
        head = n1;
    }
    void insertEnd(int value)
    {
        node *n1 = createNode(value);
        if (head == NULL)
        {
            head = n1;
            n1->next = head;
            return;
        }
        node *ptr = head;
        while (ptr->next != NULL)
            ptr = ptr->next;
        ptr->next = n1;
        n1->next = head;
    }
    void insertMiddle(int value, int pos)
    {
        node *n1 = createNode(value);
        if (head == NULL)
        {
            head = n1;
            head->next = head;
            return;
        }
        node *temp1 = head, *temp2 = head;
        for (int i = 0; i < pos; i++)
        {
            temp2 = temp1;
            temp1 = temp1->next;
        }
        temp2->next = n1;
        n1->next = temp1;
    }
};

int main()
{
    return 0;
}