#include<iostream>
using namespace std;
void swap(int &, int &); // function decleration 

int main()
{
    int x,y;
    cout<< "Enter the first  number ";   // taking input 
    cin >> x;
    cout<< "Enter the second number :";
    cin >> y ;

    // before swap print  value 
    cout << "Before swap "<< endl;    
    cout<< "x = " << x << endl 
        << "y = " << y << endl;
    
    swap(x,y);  // function call 
    
    cout << "After swap = "<< endl ;
    cout<< "x = " << x << endl 
        << "y = " << y << endl;
}

void swap (int &m , int &n ) // function define  
{  // using reference variable swap two number 
     int temp ;
     temp = m ;
     m = n ;
     n = temp ; 
}
