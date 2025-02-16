import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the plusMinus function below.
    static void plusMinus(int[] arr) {
        int pos = 0;
        int neg = 0;
        int zero = 0;
         for(int i = 0; i<arr.length;i++){
             if(arr[i]>0) {pos++;}
             if(arr[i]<0) {neg++;}
             if(arr[i]==0) {zero++;}
         }
        double posR = (double)pos/arr.length;
        double negR = (double)neg/arr.length;
        double zeroR = (double)zero/arr.length;
    DecimalFormat df = new DecimalFormat("#0.000000");
        
        System.out.println(df.format(posR));
        System.out.println(df.format(negR));
        System.out.println(df.format(zeroR));

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }

        plusMinus(arr);

        scanner.close();
    }
}
