package zoho;

public class acii_count {

	public static void main(String[] args) {
		String s ="zz";
		char srr[]=s.toCharArray();
		int arr[] = new int[26];
		int ans=0;
		for(char i:srr) {
			int j;
			if(Character.isLowerCase(i)) {
			j = ((int)i)-97;
			}
			else {
				j=((int)i)-65;
			}
			arr[j]++;
		}
		for(int i=0;i<arr.length;i++) {
			ans+=arr[i]*(i+1);
		}
		System.out.println(ans);

	}

}
