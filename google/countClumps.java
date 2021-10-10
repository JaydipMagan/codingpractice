public class countClumps {
    public static void main(String[] args) {
        System.out.println("Hello World");

        int[] input = new int[] {1, 2, 2, 3, 4, 4};
        int[] input1 = new int[] {1, 1, 2, 1, 1};
        int[] input2 = new int[] {1, 1, 1, 1, 1};

        int res = countClumps(input);
        int res1 = countClumps(input1);
        int res2 = countClumps(input2);
        System.out.println(res);
        System.out.println(res1);
        System.out.println(res2);
    }

    public static int countClumps(int[] nums) {
        
        int MIN_ELEMENTS = 2;
        
        int adjacentElements = 0; // 2; 0; 0; 2
        
        int numberofClumps = 0; // 1
        
        for(int i=0; i<nums.length; i++){
            int current = nums[i]; // 1; 1; 2; 1; 1
            
            int next = i+1<nums.length ? nums[i+1] : -1; // 1; 2; 1 
        
            if(next!=-1){
                if(current==next && adjacentElements==0){
                    adjacentElements+=2;
                }
                else if(current==next && adjacentElements>0){
                    adjacentElements++;
                }
                else{
                    // reset no more adjacent elements
                    
                    if(adjacentElements>=MIN_ELEMENTS){
                        numberofClumps++;
                    }
                    
                    adjacentElements = 0; 
                }
            }
            else{
                // index out of range, current element is the last one
                if(adjacentElements>=MIN_ELEMENTS){
                    numberofClumps++;
                }
            }
        }

        return numberofClumps;
    }
}

