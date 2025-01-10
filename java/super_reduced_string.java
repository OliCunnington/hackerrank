import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
import java.util.ArrayList;

public class Solution {

    // Complete the superReducedString function below.
    static String superReducedString(String s) {
        boolean[] rmv = new boolean[s.length()];
        char[] lst = s.toCharArray();
        for(int i=0;i<lst.length-1;i++){
            if(lst[i] == lst[i+1]){
                    rmv[i]=true;
                    rmv[i+1]=true;
                    i++;
                
            }
        }
        StringBuilder b = new StringBuilder();
        for(int i=0;i<lst.length;i++){
            if(!rmv[i]){
                b.append(lst[i]);
            }
        }
        String result = b.toString();
        rmv = new boolean[result.length()];
        lst = result.toCharArray();
        for(int i=0;i<lst.length-1;i++){
            if(lst[i] == lst[i+1]){
                    rmv[i]=true;
                    rmv[i+1]=true;
                    i++;    
            }
        }
        if(b.length() > 0){
            for (boolean value : rmv) {
                if (value) {
                    return superReducedString(result);
                }
            }   
            return result;
        }
        return "Empty String";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = bufferedReader.readLine();

        String result = superReducedString(s);

        bufferedWriter.write(result);
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
