/*
Modify and return the given map as follows: if the key "a" has a value,
set the key "b" to have that same value. In all cases remove the key "c",
leaving the rest of the map unchanged.

mapShare({"a": "aaa", "b": "bbb", "c": "ccc"}) → {"a": "aaa", "b": "aaa"}
mapShare({"b": "xyz", "c": "ccc"}) → {"b": "xyz"}
mapShare({"a": "aaa", "c": "meh", "d": "hi"}) → {"a": "aaa", "b": "aaa", "d": "hi"}
*/
import java.util.*;
class mapShare{
  public static void main(String[] args) {
    Map<String, String> map = new HashMap<String, String>();
    map.put("a","aaa");
    map.put("b","bbb");
    map.put("c","aa");
    map.put("d","dddd");
    System.out.println(mapShare(map).values());
  }

  /*
  This function will remove key c, update key b's value with value of key a and
  make no other change.
  */
  public static Map<String, String> mapShare(Map<String, String> map) {
    //check if map is not empty
    if(!map.isEmpty()){
      //check if map contains a value for key = a
      if (map.containsKey("a")) {
        // remove b and add new value
        if(map.containsKey("b")){
          String valueOfKeyA = map.get("a");
          map.remove("b");
          map.put("b",valueOfKeyA);
        }
        else{
          // add b with value
          String valueOfKeyA = map.get("a");
          map.put("b",valueOfKeyA);
        }
      }
      // remove c
      if(map.containsKey("c")){
        map.remove("c");
      }
    }
    return map;
  }

}
