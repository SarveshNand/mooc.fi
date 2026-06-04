
import java.util.Scanner;

public class AverageOfPositiveNumbers {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int amountNum = 0;
        int amountSum = 0;
        while (true) {
            int number = Integer.valueOf(scanner.nextLine());
            if (number == 0) {
                break;
            } else if (number > 0) {
                amountNum++;
                amountSum = amountSum + number;
            }
        }
        double averagePositive = (double) amountSum / amountNum;
        if (averagePositive > 0) {
            System.out.println(averagePositive);
        } else {
            System.out.println("Cannot calculate the average");
        }
    }
}
