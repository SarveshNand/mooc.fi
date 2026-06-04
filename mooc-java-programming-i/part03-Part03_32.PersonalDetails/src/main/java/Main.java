import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String longest = "";
        int sum = 0;
        int count = 0;

        while (true) {
            String input = scanner.nextLine();

            if (input.equals("")) {
                break;
            }

            String[] parts = input.split(",");

            String name = parts[0];
            int year = Integer.valueOf(parts[1]);

            if (name.length() > longest.length()) {
                longest = name;
            }

            sum += year;
            count++;
        }

        System.out.println("Longest name: " + longest);
        System.out.println("Average of the birth years: " + (double) sum / count);
    }
}