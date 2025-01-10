import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        int i = 1;
        Scanner scanner = new Scanner(System.in);
        while(scanner.hasNextLine()){
            System.out.format("%d %s\n", i, scanner.nextLine());
            i++;
        }
    }
}