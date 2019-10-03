/*
Author : Ravineel
Title : LIST STL
*/
#include<iostream>
#include<list>
#include<algorithm>
using namespace std;

void disp(list<int> a){

    list<int>::iterator it;
    for(it =a.begin();it!=a.end();++it)
        cout<<*it<<"->";
    cout<<endl;
}


int main(){
  list<int> list1; // creating a list with name as list1

  int n;
  cin>>n ;// to get the initial size of list

  for(int i=0;i<n;++i)
  {
      
      int x;
      cin>>x;
      list1.push_back(x);//Adds a new element ‘x’ at the end of the list.

  }

  //to display list
    disp(list1);

  //to reverse a list
    list1.reverse();
    disp(list1);
    
    //to sort a list
    list1.sort();
    disp(list1);

    //to sort in descending order
    list1.sort(greater<int>());
    disp(list1);

return 0;
}
