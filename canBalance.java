/*
Given a non-empty array, return true if there is a place to split the array
so that the sum of the numbers on one side is equal to the sum of the numbers
on the other side.

canBalance([1, 1, 1, 2, 1]) → true
canBalance([2, 1, 1, 2, 1]) → false
canBalance([10, 10]) → true
*/

class canBalance{
  public static void main(String[] args) {
    System.out.println("can balance?");
    int[] nums = {1,1,1,3};
    System.out.println(canBalance(nums));
  }

  /*
    Function will return true or false if the array can be balanced at some point.
    The program will work its way from the outside until it meets at some point
    moving the index if the sum of sides aren't equal. This is done in O(n-2) = O(n)
    time since the first and last elements aren't iterated through. Space complexity
    is O(4) if you don't include n which is used for readability sake.
  */
  public static Boolean canBalance(int[] nums){
      int n = nums.length; // number of elements in given array
      // eliminate arrays of size 0 or 1
      if(n==1 || n == 0){
        return false;
      }

      // variables to store the right and left sums
      int rightVal = nums[n-1];
      int leftVal = nums[0];

      // variables to store indexes of left and right side
      int indexLeft = 1;
      int indexRight = n-2;

      // while there are indexes to check
      while(indexLeft<=indexRight){
        //check if the sum of right side is greater than sum of left,
        // checking greater than will mean program won't work with negatives
        if(rightVal>leftVal){
          leftVal += nums[indexLeft++]; //add value to sum
        }
        else{
          rightVal += nums[indexRight--]; //add value sum
        }
      }

      //check if the values were equal on both sides
      if(rightVal==leftVal){
        return true;
      }
      else{
        return false;
      }
  }
}
