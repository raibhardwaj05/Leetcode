// string reverse

import java.util.Arrays;
import java.util.Scanner;

public class Reverse {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter String: ");
        String str = sc.nextLine();

        char[] arr = str.toCharArray();
        
        reverseString(arr);

        sc.close();
    }

    static void reverseString(char [] s){
        reverseHelper(s, s.length - 1, 0);

        System.out.println(Arrays.toString(s));
    }

    static void reverseHelper(char[] s, int right, int left){
        if (left >= right) {
            return;
        }

        char temp = s[right];
        s[right] = s[left];
        s[left] = temp;

        reverseHelper(s, right - 1, left + 1);
    }
}
