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

class Stack
{
    node *top;

public:
    Stack() { top = NULL; }
    void push(int value)
    {
        node *n1 = createNode(value);
        if (top == NULL)
        {
            top = n1;
            return;
        }
        n1->next = top;
        top = n1;
    }
    void pop()
    {
        if (top == NULL)
        {
            cout << "UnderFlow\n";
            return;
        }
        node *temp = top;
        top = top->next;
        free(temp);
    }
    void displayAll()
    {
        if (top == NULL)
        {
            cout << "UnderFlow\n";
            return;
        }
        node *ptr = top;
        while (ptr != NULL)
        {
            cout << ptr->value << "->";
            ptr = ptr->next;
        }
        cout << endl;
    }
};

int main()
{
    Stack s;
    s.push(1);
    s.push(2);
    s.push(3);
    s.displayAll();
    s.pop();
    s.displayAll();
    return 0;
}