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

class Queue
{
    node *front, *rear;

public:
    Queue() { front = rear = NULL; }
    void enQueue(int value)
    {
        node *newNode = createNode(value);
        if (front == NULL)
        {
            front = rear = newNode;
            return;
        }
        rear->next = newNode;
        rear = newNode;
    }
    int deQueue()
    {
        if (front == NULL)
        {
            cout << "Underflow\n";
            return NULL;
        }
        int temp = front->value;
        if (front == rear)
            front = rear = NULL;
        else
            front = front->next;
        return temp;
    }
    void displayAll()
    {
        if (front == NULL)
        {
            cout << "Underflow\n";
            return;
        }
        node *ptr = front;
        while (ptr)
        {
            cout << ptr->value << "->";
            ptr = ptr->next;
        }
        cout << endl;
    }
};

// Test Code

int main()
{
    Queue Q;
    Q.enQueue(1);
    Q.enQueue(2);
    Q.enQueue(3);
    Q.displayAll();
    Q.deQueue();
    Q.displayAll();
    Q.deQueue();
    Q.displayAll();
    return 0;
}
