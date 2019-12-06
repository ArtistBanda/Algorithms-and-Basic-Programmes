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
    node *last;

public:
    CircularLinkedList() { last = NULL; }
    void insertBeginning(int value)
    {
    }
    void insertEnd(int value)
    {
    }
};

int main()
{
    return 0;
}