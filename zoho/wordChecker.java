import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

class GFG {
  // Helper funtion takes in a word and a String Array
  // If the word is present in all the elements of array,
  // it will return the word, else null string.
  static String wordChecker(String word,String [] arr){
    for(String sentence:arr){
      try{
        if(sentence.contains(word)){
        continue;
      }
      else{
        return "";
      }
      }catch(NullPointerException e){
        continue;
      }
    }
    return word + ' ';
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String[] arr = new String[in.nextInt()];
    in.nextLine();
    String first = in.nextLine();
    for(int i = 1; i < arr.length; i++){
      arr[i] = in.nextLine();
    }
    // End of input section
    
    // Splitting first sentence into array of words
    String[] words = first.split("\\s+");
    String result = "";
    
    // Every word in first sentence is checked
    // if present it will be added to string.
    for(String word:words){
      result += wordChecker(word,arr);
    }

    System.out.println(result.trim());
  }
}
