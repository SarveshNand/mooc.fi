
import java.util.Scanner;

public class SumOfASequence {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Last number? ");
        int integer = Integer.valueOf(scanner.nextLine());
        int totalNumber = 0;
        for (int i = integer; i >= 1; i--) {
            totalNumber += i;
        }
        System.out.print("The sum is " + totalNumber);
    }
}
