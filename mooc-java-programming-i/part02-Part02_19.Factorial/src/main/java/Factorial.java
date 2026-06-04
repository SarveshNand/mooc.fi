
import java.util.Scanner;

public class Factorial {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Give a number: ");
        int number = Integer.valueOf(scanner.nextLine());
        int factNumber = 1;
        for (int i = 1; number >= i; i++) {
            factNumber = factNumber * i;
        }
        System.out.print("Factorial: " + factNumber);
    }
}
