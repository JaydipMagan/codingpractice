/*
Given a string, return the sum of the numbers appearing in the string, ignoring all other characters.
A number is a series of 1 or more digit chars in a row.
(Note: Character.isDigit(char) tests if a char is one of the chars '0', '1', .. '9'.
Integer.parseInt(string) converts a string to an int.)

sumNumbers("abc123xyz") → 123
sumNumbers("aa11b33") → 44
sumNumbers("7 11") → 18
*/


class sumNumbers{

  public static void main(String[] args) {
    System.out.println(sumNumbers("abc123xyz"));
    System.out.println(sumNumbers("abc123xyz123"));
    System.out.println(sumNumbers("7 11"));
    System.out.println(sumNumbers("aa11bb33"));
  }

  // Function will return sum of numbers found in a string does this by iterating
  // through each character of the string. When a digit is encountered it will check
  // for if next character is a digit too. The while loop executes until a integer
  // is fully discovered. This is then sumed with the existing sum
  // approach will take o(n*w) n = number of characters in the string w = number of digits in string
  public static int sumNumbers(String str) {
    str+=" ";//Pad strings
    int sum = 0;
    int numberFound = 0;
    for (int i = 0; i<str.length(); i++) {
      //check for integer
      if(isInt(str.substring(i,i+1))){
        Boolean stop = false;
        int sizeOfNumber = 0;
        String intFound = "";
        while(!stop){
          if(isInt(str.substring(i,i+sizeOfNumber+1))){
            intFound = str.substring(i,i+sizeOfNumber+1);
            sizeOfNumber++;
          }
          else{
            stop=true;
            i += sizeOfNumber;
            sum += Integer.parseInt(intFound);
          }
        }

      }
    }
    return sum;
  }

  //Function checks if the given string is a integer by iterating through and checking if all chars are digits
  //This approach is taken to avoid the use of exception handling since code bat doesn't allow
  //This approach takes o(n)  n = number of characters in the string
  public static Boolean isInt(String toCheck){
    int x = 0;
    for (int i=0; i<toCheck.length();i++ ) {
      if(Character.isDigit(toCheck.charAt(i))){
        x++;
      }
      else{
        return false;
      }
    }
    if(x==toCheck.length()){
      return true;
    }
    return false;
  }
}
