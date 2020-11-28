package zoho;

public class string_rotate {
	static boolean areRotations(String str1, String str2) 
    {    
        return (str1.length() == str2.length()) && 
               ((str1 + str1).indexOf(str2) != -1); 
    } 

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str1 = "hello from here"; 
        String str2 = "rehello from he"; 
        str1=str1.replaceAll("\\s", "");
        str2=str2.replaceAll("\\s", "");
        if (areRotations(str1, str2)) 
            System.out.println("Strings are rotations of each other"); 
        else
            System.out.printf("Strings are not rotations of each other");

	}

}
