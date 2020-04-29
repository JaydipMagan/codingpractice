/*
Return an array that contains the sorted values from the input array with duplicates removed.

sort([]) → []
sort([1]) → [1]
sort([1, 1]) → [1]
*/

import java.util.*;
class sort{
  public static void main(String[] args) {
    int[] test = {2,1,4,6,3};
    System.out.println(Arrays.toString(sort(test)));
  }

  /*
  When given a array of ints, function creates a set of the numbers so
  that only unique numbers remain. This takes O(1) property of hashset.
  So for all elements it takes O(n). Now the elements are sorted automatically
  so we can just get the array and convert them to int objects. This takes
  O(m)  m = number of unique ints. Hence total time taken is O(n+m) = O(n)
  since m <= n.
  */
  public static int[] sort(int[] a) {

    Set<Integer> uniqueValues = new HashSet<Integer>();
    for(int i = 0; i < a.length; i++) {
      if(!uniqueValues.contains(a[i])){
        uniqueValues.add(a[i]);
      }
    }
    int [] newA = new int[uniqueValues.size()];
    int i = 0;
    for (Object x : uniqueValues.toArray()) {
      newA[i++] = (int) x;
    }
    return newA;
  }

}
