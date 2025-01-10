import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    /*
     * Complete the timeConversion function below.
     */
    static String timeConversion(String s) {
        /*
         * Write your code here.
         
        if(s.charAt(8)=='P'){
            int hours = Integer.parseInt(s.substring(0,2));
            hours +=12;
            if (hours == 24) return "00"+s.substring(2,8);
            return hours+s.substring(2,8);
        } else return s.substring(0,8);
        */
        for (int i=0; i<s.length();i++){
            if (s.charAt(i)=='P'){
                s = s.substring(0,i);
                String[] ar = s.split(":");
                int[] arI = new int[ar.length];
                for(int j=0;j<ar.length;j++){
                    arI[j] = Integer.parseInt(ar[j]);
                }
                arI[0]+=12;
                if(arI[0]==24){
                    return "00:"+arI[1]+":"+arI[2];
                } else return arI[0]+":"+arI[1]+":"+arI[2];
            } else if (s.charAt(i)=='A'){
                return s.substring(0,i);
            }
        }
        return null;

    }

    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = scan.nextLine();

        String result = timeConversion(s);

        bw.write(result);
        bw.newLine();

        bw.close();
    }
}
