/**
Submission result:

 - Runtime: 88 ms, faster than 84.93% of C online submissions for Two Sum.
 - Memory Usage: 7.6 MB, less than 35.44% of C online submissions for Two Sum.
 */


#include <stdlib.h>
#include <stdio.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
	int *p1;
	int *p2;
   int *returnArray;
   int found;

	for (p1=nums; p1<nums+numsSize; p1++) {
		found = 0;

		for (p2 = nums+numsSize-1; p2>p1; p2--) {
			if (*p1+*p2 == target) {
				found = 1;
				break;
			}
		}

		if (found == 1) {
			break;
		}
	}

   if (found == 1) {
      returnArray = malloc(2 * sizeof(int) );
      if (returnArray == NULL) {
         *returnSize = 0;
         return NULL;
      }

      *returnArray = p1 - nums;
      *(returnArray + 1) = p2 - nums;

      *returnSize = 2;
      printf("first element: %d\n", *returnArray);
      printf("second element: %d\n", *(returnArray+1));
      return returnArray;
   } else {
      *returnSize = 0;
      return NULL;
   }
}

int main() {
  /* Given nums = [16, 7, 2, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
   */
   int nums[4] = {11, 7, 2, 15};
   int numsSize = 4;
   int target = 9;
   int retSize;

	twoSum(nums, numsSize, target, &retSize);
	return 0;
}


