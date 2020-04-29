class maxSpan {

  public static void main(String[] args) {
    int[] v = {1, 2, 1, 1, 3};
    System.out.println(maxSpan(v));
  }
  public static int maxSpan(int[] nums) {
  int maxSpan = 0;
  int span = 0;

  for(int i = 0; i<nums.length;i++){
    for(int j = 0; j<nums.length;j++){
      if(nums[i]==nums[j]){
        span = j-i+1;
        maxSpan = Math.max(span,maxSpan);
      }
    }
  }

  return maxSpan;
}
}
