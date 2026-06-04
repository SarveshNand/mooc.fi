
import java.util.Scanner;

public class DifferentTypesOfInput {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        // Write your program here
        System.out.println("Give a string:");
        String message1 = scan.nextLine();
        System.out.println("Give an integer:");
        int message2 = Integer.valueOf(scan.nextLine());
        System.out.println("Give a double:");
        double message3 = Double.valueOf(scan.nextLine());
        System.out.println("Give a boolean:");
        boolean message4 = Boolean.valueOf(scan.nextLine());

        System.out.println("You gave the string " + message1);
        System.out.println("You gave the integer " + message2);
        System.out.println("You gave the double " + message3);
        System.out.println("You gave the boolean " + message4);
    }
}
