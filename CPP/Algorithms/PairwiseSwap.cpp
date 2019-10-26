#include <iostream>
using namespace std;

struct node
{
    int value;
    struct node *next;
};

node *createNode(int value)
{
    node *n1 = new node;
    n1->value = value;
    n1->next = NULL;
    return n1;
};

class LinkedList
{
    node *head;

public:
    LinkedList()
    {
        head = NULL;
    }
    void insertStart(int value)
    {
        node *n1 = createNode(value);
        if (head == NULL)
        {
            head = n1;
            return;
        }
        n1->next = head;
        head = n1;
    }
    void insertback(int value)
    {
        node *n1 = createNode(value);
        if (head == NULL)
        {
            head = n1;
            return;
        }
        node *ptr = head;
        while (ptr->next != NULL)
        {
            ptr = ptr->next;
        }
        ptr->next = n1;
    }

    void pairWiseSwap()
    {
        node *temp = head;
        while (temp != NULL && temp->next != NULL)
        {

            swap(temp->value,
                 temp->next->value);
            temp = temp->next->next;
        }
    }

    void displayAll()
    {
        if (head == NULL)
            cout << "UnderFlow\n";
        else
        {
            node *ptr = head;
            while (ptr != NULL)
            {
                cout << ptr->value << "->";
                ptr = ptr->next;
            }
            cout << endl;
        }
    }
};

// Test Code

int main()
{
    LinkedList L;

    L.insertStart(5);
    L.insertback(4);
    L.insertback(3);
    L.insertback(2);
    L.insertback(1);

    L.displayAll();
    L.pairWiseSwap();
    L.displayAll();

    return 0;
}
