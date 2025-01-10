import java.util.*;
import java.io.*;
import java.lang.Math;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            makeSeries(a,b,n);
        }
        in.close();
    }
    
    private static void makeSeries(int a, int b, int n){
        int result[] = new int[n];
        for(int i=0;i<n;i++){
            if(i==0){
                result[i]=a+1*b;
            } else {
                result[i] = result[i-1]+(int)Math.pow(2,i)*b;
            }
        }
        for(int i:result){
            System.out.print(i);
            System.out.print(" ");
        }
        System.out.println();
        
    }
}
