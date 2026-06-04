
import java.util.Scanner;

public class AverageOfNumbers {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int amountNum = 0;
        int amountSum = 0;
        while (true) {
            System.out.println("Give a number:");
            int input = Integer.valueOf(scanner.nextLine());
            if (input == 0) {
                break;
            }
            amountNum++;
            amountSum = amountSum + input;
        }
        double average = (double) amountSum / amountNum;
        System.out.println("Average of the numbers: " + average);
    }
}
