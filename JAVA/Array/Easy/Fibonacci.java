import java.util.Scanner;

class Fibonacci{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Number: ");
        int num = sc.nextInt();

        int series = fib(num);

        System.out.println("Series: "+ series);

        sc.close();
    }

    static int fib(int n){
        if (n == 0) {
            return 0;
        }
        else if (n == 1) {
            return 1;
        }

        return fib(n - 1) + fib(n - 2);
    }
}