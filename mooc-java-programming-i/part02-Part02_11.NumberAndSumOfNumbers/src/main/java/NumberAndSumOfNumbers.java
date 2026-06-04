
import java.util.Scanner;

public class NumberAndSumOfNumbers {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int amountNum = 0;
        int amountSum = 0;
        while (true) {
            System.out.println("Give a number:");
            int number = Integer.valueOf(scanner.nextLine());
            if (number == 0) {
                break;
            }
            amountSum = amountSum + number;
            amountNum++;
        }
        System.out.println("Number of numbers: " + amountNum);
        System.out.println("Sum of the numbers: " + amountSum);
    }
}
