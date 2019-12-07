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
    void addToEmpty(int value)
    {
        node *newNode = createNode(value);
        newNode->next = newNode;
        last = newNode;
    }
    void insertBeginning(int value)
    {
        if (last == NULL)
        {
            addToEmpty(value);
            return;
        }
        node *newNode = createNode(value);
        newNode->next = last->next;
        last->next = newNode;
    }
    void insertEnd(int value)
    {
        if (last == NULL)
        {
            addToEmpty(value);
            return;
        }
        node *newNode = createNode(value);
        newNode->next = last->next;
        last->next = newNode;
        last = newNode;
    }
    void deleteBeginning()
    {
        if (last == NULL)
        {
            cout << "Underflow\n";
            return;
        }
        node *ptr = last->next;
        last->next = ptr->next;
        free(ptr);
    }
    void displayAll()
    {
        if (last == NULL)
        {
            cout << "Underflow\n";
            return;
        }
        node *ptr = last->next;
        while (true)
        {
            cout << ptr->value << ' ';
            ptr = ptr->next;
            if (ptr == last)
            {
                cout << ptr->value;
                break;
            }
        }
        cout << endl;
    }
};

// Test Code

int main()
{
    CircularLinkedList CLL;
    CLL.insertBeginning(1);
    CLL.insertBeginning(2);
    CLL.insertBeginning(3);
    CLL.displayAll();
    CLL.insertEnd(4);
    CLL.displayAll();
    CLL.deleteBeginning();
    CLL.displayAll();
    return 0;
}