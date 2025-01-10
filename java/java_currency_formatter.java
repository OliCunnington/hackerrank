import java.util.*;
import java.text.*;
import java.text.NumberFormat;
import java.util.Locale;

public class Solution {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        
        // Write your code here.
        NumberFormat numFat = NumberFormat.getCurrencyInstance();
        String us = numFat.format(payment);
        Locale locale = new Locale("en", "IN");
        numFat = NumberFormat.getCurrencyInstance(locale);
        String india = numFat.format(payment);
        numFat = NumberFormat.getCurrencyInstance(Locale.CHINA);
        String china = numFat.format(payment);
        locale = new Locale("fr", "FR");
        numFat = NumberFormat.getCurrencyInstance(locale);
        String france = numFat.format(payment);
        
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}
