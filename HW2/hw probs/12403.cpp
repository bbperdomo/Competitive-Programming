/* # Input
# The first line of input will contain T (1 ≤ T ≤ 100) denoting the number of operations. Then there will
# be T lines each containing two types of operations as given. You may assume that the input follows
# the restrictions below.
# 1) ‘donate K’ (100 ≤ K ≤ 105), then you have to add K to the account.
# 2) ‘report’, report all the money currently in the account.

# Output
# For each ‘report’ operation, print the total amount of money in the account. */

#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int main ()
{
    //
    int t,a,b,c;

    cin>>t; //reading number of input lines

    long long sum=0; //keep track of total donations for printing

    string s;


    while ( t-- )           //decrement 
    {
        cin>>s;             //reads the 'donate K, report' string
        if(s=="donate")     //
        {
            cin>>a;         //read in int, cin jumps from int to int
            sum=sum+a;      //add donation to current total
        }
        else                //the only other possibility is that the string is 'report'
        {
            cout<<sum<<endl; //print out total donation
        }
    }

    return 0;
}
