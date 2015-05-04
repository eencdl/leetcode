package main;

/**
 Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
 If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
 The replacement must be in-place, do not allocate extra memory.
 Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
 1,2,3 → 1,3,2
 3,2,1 → 1,2,3
 1,1,5 → 1,5,1

 */
public class NextPermutation {
    //This has an algorithm
    //Ex: 6,8,7,4,3,2
    // step 1: find right to left the first digit that violate increase
    //  6 (partition number)
    // step 2: find right to left the first digit that is larger than partition number
    //  7 (change number)
    // step 3: swap the two numbers
    //   7,8,6,4,3,2
    // step 4: reverse all the digit on the right of the partition index
    //   7 (parition index) 8,6,4,3,2
    //   7,2,3,4,6,8 (answer)

    public void nextPermutation(int[] num) {
        if(num.length <= 1)
            return;

        //find partition number
        int i = num.length - 1;
        for(; i>0; i--) {
            if(num[i] > num[i-1])
                break;
        }


        //find change number
        int j = num.length - 1;
        int tmp;
        if(i > 0) {
            i--;
            for(;j>=0;j--){
                if(num[j] > num[i])
                    break;
            }
            //swap
            tmp = num[j];
            num[j] = num[i];
            num[i] = tmp;
            i++; //partition index
        }




        //reverse from partition index
        j = num.length - 1;
        while(i<j) {
            tmp = num[i];
            num[i] = num[j];
            num[j] = tmp;
            i++;
            j--;
        }
    }
}
