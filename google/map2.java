/*
Given an array of strings, return a Map<String, Integer> containing a key for every different string in the array, and the value is that string's length.

wordLen(["a", "bb", "a", "bb"]) → {"bb": 2, "a": 1}
wordLen(["this", "and", "that", "and"]) → {"that": 4, "and": 3, "this": 4}
wordLen(["code", "code", "code", "bug"]) → {"code": 4, "bug": 3}
*/

import java.util.*;
class map2 {
  public static void main(String[] args) {
    String[] strings = {"a","b","c"};
    System.out.println(wordLen(strings)); // {"a": 0, "b": 0, "c": 0}
  }
  /*
    Function will solve the problem above following the specification.
    Time complexity is going to be O(n)  n = number of strings in array
    space complexity is goign to be O(n) where n = number of strings in array,
    space of map increases linearly.
  */
  public static Map<String, Integer> wordLen(String[] strings) {
    Map<String, Integer> map = new HashMap<String, Integer>();
    for (String c : strings) {
      if(!map.containsKey(c)){
        map.put(c,c.length()); // stores the length of the string
      }
    }
    return map;
  }

}
