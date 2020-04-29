/*
Write a simple interpreter which understands "+", "-", and "*" operations.
Apply the operations in order using command/arg pairs starting with the
initial value of `value`. If you encounter an unknown command, return -1.

interpret(1, ["+"], [1]) → 2
interpret(4, ["-"], [2]) → 2
interpret(1, ["+", "*"], [1, 3]) → 6

*/

class interpret{
  
  public static void main(String[] args) {
    int[] values = {1,3};
    String[] commands = {"+","*"};
    System.out.println(interpret(1,commands,values)); // should get 6
  }

  /*
    This solves the problem following the specification above.
    The time complexity of this function is O(n)  n = amount of commands.
    The function can execute in O(1) if it finds that the amount of commands
    is not equal to the amount of arguements. Only 2 additional vars are needed,
    first to store the final value and the second to store the arguement that
    will be applied. Hence space complexity is O(2).
  */
  public static int interpret(int value, String[] commands, int[] args) {
    // check if amount of commands is same as arguements
    if (commands.length!=args.length) {
      return -1;
    }

    int outCome = value; // stores the value after applying commands to init value
    int i = 0; // keep track of which arguement to apply next
    for ( String command : commands) {
      // perform operation depending on command
      switch (command) {
        case "+":
          outCome += args[i++];
          break;
        case "-":
          outCome -= args[i++];
          break;
        case "*":
          outCome = outCome * args[i++];
          break;
        default:
          return -1; // return -1 if command is unknown
      }
    }
    return outCome; // return the final value

  }


}
