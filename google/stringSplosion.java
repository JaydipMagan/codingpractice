// Given a non-empty string like "Code" return a string like "CCoCodCode".
//
// stringSplosion("Code") → "CCoCodCode"
// stringSplosion("abc") → "aababc"
// stringSplosion("ab") → "aab"

class stringSplosion {
  public static void main(String[] args) {
    String string = args[0];
    String output = "";

    // append sub string of string from 0 to i for each character in string
    // should get sequence like 001012 for 012
    // O(n) n = amount of characters in string
    for (int i = 1; i<string.length();i++) {
      output+=string.substring(0,i);
    }
    output+= string; // append final string 
    System.out.println(output);
  }
}
