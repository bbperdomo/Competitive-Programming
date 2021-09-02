// test.cpp.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;


//algorithm to find the sum of a sequence of numbers
int main()
{

	int  n;
	int ans = 0;

	cout << "Please enter an amount of numbers to sum" << "\n";
	cin >> n;

	//O(n) method
	for (int i=0; i <= n; i++)
	{
		ans += i;
	}

	cout << ans << "\n";

	cout << "Enter another number:" << "\n";
	int n2;
	int ans2;
	cin >> n2;

	//O(1) method - requires several constant operations that DONT scale with n
	ans2 = (n2 * (n2 + 1) / 2);

	cout << ans2;

	

	return(0);
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
