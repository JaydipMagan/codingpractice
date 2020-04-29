class withoutString {

  public static void main(String[] args) {

    System.out.println(withoutString("Hello therello","llo"));
  }
  public static String withoutString(String base, String remove) {
    String newBase = "";

    for (int i = 0; i<base.length(); i++) {

      String b = base.toLowerCase().substring(i,i+1);
      String r = remove.toLowerCase().substring(0,1);
      // System.out.println(b);
      // System.out.println(r);

      if(i<=base.length()-remove.length()-1){
        if(!b.equals(r)){
          newBase+=base.substring(i,i+1);
        }
        else{
          //check next n chars
          // System.out.println(base.substring(i,remove.length()+2).toLowerCase());
          if(base.substring(i,remove.length()+2).toLowerCase().equals(remove.toLowerCase())){
            i+=remove.length()-1;
          }
          else{
            newBase+=base.substring(i,i+1);
          }
        }
      }
      else{
        if(base.length()-remove.length()==i){
          if(base.substring(i,remove.length()+i).toLowerCase().equals(remove.toLowerCase())){
            i+=remove.length()-1;
          }
          else{
            newBase+=base.substring(i,i+1);
          }
        }
        else{
          newBase+=base.substring(i,i+1);
        }
      }
    }

    return newBase;
  }

}
