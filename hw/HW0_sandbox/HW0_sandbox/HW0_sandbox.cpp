/***********************************************************
Bryan Perdomo	        
Znumber: Z2338668
Due Date: September 1st 11:59PM
Course:  COT4930 - Competitive Programming
Assignment:  Homework 1
Professor: Dr. Feng-Hao Liu

A little note: 
When I tried to sort using one million elements, my program would take forever and would not complete compilation.
I have lowered the number of elements to 10,000, but you can still see the differences in peformance when examining the
sorting algorithms
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <ctime>
#include <ratio>

using namespace std;


int Partition(vector<int> & qVec, int s, int e);
void QuickSort(vector<int> & qVec, int s, int e);


int main()
{
	using namespace std::chrono;

	long total_elements = 10000;
	

	/****************************************************************************
	bubble sort algorithm*
	*****************************************************************************/

	//init vector with 100,000 zeroes
	vector<int> bVec(total_elements);

	//populate vector with rand nums
	generate(bVec.begin(), bVec.end(), []()
	{
		return rand() % 100;
	});


	auto b_start = high_resolution_clock::now();
	//Implementing bubble sort
	for (int i=0; i < bVec.size(); i++)
	{
		for (int j=0; j < (bVec.size() - i - 1); j++)
		{
			if (bVec[j] > bVec[j + 1])
			{
				int temp = bVec[j];
				bVec[j] = bVec[j+1];
				bVec[j + 1] = temp;
			}
		}
	}

	//calculating time elapsed
	auto b_end = high_resolution_clock::now();
	duration<double> b_time_span = duration_cast<duration<double>>(b_end - b_start);
	auto b_time_milliseconds = duration_cast<milliseconds>(b_end - b_start);




	/***********************************************************************************
	quick sort algorithm*
	************************************************************************************/
    
	vector<int> qVec(total_elements);

	generate(qVec.begin(), qVec.end(), []()
	{
		return rand() % 100;
	});


	//Starting qsort timer
	auto q_start = high_resolution_clock::now();

	//Implementing Quick-sort
	int s = 0;
	int e = qVec.size() - 1;

	QuickSort(qVec, s, e);

	//Calculating time elapsed
	auto q_end = high_resolution_clock::now();
	duration<double> q_time_span = duration_cast<duration<double>>(q_end - q_start);
	auto q_time_milliseconds = duration_cast<milliseconds>(q_end - q_start);




	/****************************************************************************************
	C++ STL Sort() algorithm*
	*****************************************************************************************/

	vector<int> myVec(total_elements);

	generate(myVec.begin(), myVec.end(), []()
	{
		return rand() % 100;
	});

	auto start = high_resolution_clock::now();
	
	sort(myVec.begin(), myVec.end());

	auto end = high_resolution_clock::now();
	duration<double> time_span = duration_cast<duration<double>>(end - start);
	auto time_milliseconds = duration_cast<milliseconds>(end - start);




	cout << "\nBubble Sort of elements contained in a vector took "
		<< b_time_span.count() << " seconds, or "
		<< b_time_milliseconds.count() << " milliseconds." << endl
		<< "\Quick Sort of elements contained in a vector took "
		<< q_time_span.count() << " seconds, or "
		<< q_time_milliseconds.count() << " milliseconds." << endl
		<< "\Standard library sort() of elements contained in a vector took "
		<< time_span.count() << " seconds, or "
		<< time_milliseconds.count() << " milliseconds." << endl;


	return(0);
}



//Functions for QuickSort implementation
int Partition(vector<int> & qVec, int s, int e)
{

	int pivot = qVec[e];
	int p_index = s;
	for (int i = s; i < e; i++)
	{
		if (qVec[i] < pivot)
		{
			int temp = qVec[i];
			qVec[i] = qVec[p_index];
			qVec[p_index] = temp;

			p_index++;
		}

	}
	int temp = qVec[e];
	qVec[e] = qVec[p_index];
	qVec[p_index] = temp;

	return p_index;
}


void QuickSort(vector<int> & qVec, int s, int e)
{
	if (s < e)
	{
		int p = Partition(qVec, s, e);
		QuickSort(qVec, s, (p - 1));
		QuickSort(qVec, (p + 1), e);
	}
}
