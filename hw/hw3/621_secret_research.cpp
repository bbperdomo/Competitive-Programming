#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>

using namespace std;


int main(){
    string s;

    int t;
    cin>>t;
    while(t--){
        cin>>s;
        int len= s.size();

        if(s == "1" || s == "4" || s == "78"){
            cout<<"+\n";
        }
        else if(s[len-1] == '5' && s[len-2] == '3'){
            cout<<"-\n";
        }
        else if(s[0]=='1' && s[1]=='9' && s[2]=='0'){
            cout<<"?\n";
        }
        else cout<<"*\n";


    }



    return 0;

}