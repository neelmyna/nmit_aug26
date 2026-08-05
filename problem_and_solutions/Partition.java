import java.util.Arrays;
import java.util.Scanner;

public class Partition {
    private static void partitionArray(int[] diameters) {
        int k = 0;
        int pivot = diameters[diameters.length - 1];
        for (int i = 0; i < diameters.length - 1; i++) {
            if (diameters[i] < pivot) {
                int temp = diameters[i];
                diameters[i] = diameters[k];
                diameters[k] = temp;
                k++;
            } // end of if
        } // end of for
        int temp = diameters[k];
        diameters[k] = diameters[diameters.length - 1];
        diameters[diameters.length - 1] = temp;
    }

    public static void main(String[] args) {
        int inputSize = Integer.parseInt(args[0]);
        int[] diameters = new int[inputSize];
        System.out.print("Enter diameters of " + inputSize + " Oranges: \n");
        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < inputSize; i++) {
            diameters[i] = scanner.nextInt();
        }
        partitionArray(diameters);
        System.out.print("Array after partition is " + Arrays.toString(diameters));
        scanner.close();
    } // end of main
}