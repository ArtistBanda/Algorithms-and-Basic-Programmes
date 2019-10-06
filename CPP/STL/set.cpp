#include<iostream>
#include<set>
#include<algorithm>

using namespace std;

void disp(set<int> a){

    set<int>::iterator it;
    for(it =a.begin();it!=a.end();++it)
        cout<<*it<<"->";
    cout<<endl;
}

int main(){
/*
Code for implementing SET STL for CPP
A set store data in sorted order , by default from ascending to descending order.
It can only have unique values.
*/

//Creates a set with variable name A
std::set<int> A;

set<int >::iterator it;//creating an iterator for set


int n;
cin>>n; //to get initial size for set

for(int i=0;i<n;++i){
    int x;
    cin>>x;
    A.insert(x); // to insert the element x 

}
//to display a set
disp(A);


//to create a set with reverse order 
set<int, greater<int>()> B; // For descending to Ascending

// to remove a element from set
 int pos;
 cin>>pos;
 A.erase(pos);
 disp(A);

return 0;
}