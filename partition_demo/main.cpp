#include <iostream>
#include "Helper.h"

using namespace std;

/*
 *
给定一个数组 array 和一个数num
1.
给定一个数组arr， 和一个数num， 请把小于等于num的数放在数
组的左边， 大于num的数放在数组的右边。
要求额外空间复杂度O(1)， 时间复杂度O(N)

 * */

template<typename T>
int partition(T arr[], int n, int num) {

    int j;
    j = -1;
    //arr[0,j] <=num , arr[j+1,i) > num
    for (int i = 0; i < n; i++) {

        if (arr[i] <= num) {
            j++;
            swap(arr[i], arr[j]);

        } else {
            // arr[i] >num
            // do nothing

        }

    }
    return j;
}


int main() {

    int arr[9] = {1, 2, 3, 4, 5, 9, 3, 8, 3};

    int num = 5;
    int p = partition(arr, 9, num);

    SortTestHelper::printArray(arr, 9);

    cout << "pov = " << p << ", num = " << num << endl;

    cout << "arr[0..pov]<=" << num << ", arr[pov+1,n]> " << num << endl;
    return 0;
}
