import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the hackerrankInString function below.
    static String hackerrankInString(String s) {
        boolean [] results = {false, false,false, false,false, false,false, false,false, false};
        String compar = "hackerrank";
        for(int i=0,j=0;(i<10 );i++){
            while(!results[i] && j<s.length()){
                if(compar.charAt(i)==s.charAt(j)){
                    results[i]=true;
                } else {
                    j++;
                }
            }
            if(!results[i]){
                return "NO";
            }
        }
        return "YES";
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int qItr = 0; qItr < q; qItr++) {
            String s = scanner.nextLine();

            String result = hackerrankInString(s);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
