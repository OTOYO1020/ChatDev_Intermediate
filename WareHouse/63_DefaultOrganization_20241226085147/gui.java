'''
GUI class for the CashFlowManager application.
'''
import java.util.Scanner;
public class GUI {
    private CashFlowManager cashFlowManager;
    private Scanner scanner;
    public GUI() {
        cashFlowManager = new CashFlowManager();
        scanner = new Scanner(System.in);
    }
    public void displayMenu() {
        System.out.println("Cash Flow Manager");
        System.out.println("1. Add Income");
        System.out.println("2. Add Expense");
        System.out.println("3. Calculate Cash Flow");
        System.out.println("4. Display Cash Flow");
        System.out.println("5. Exit");
    }
    public void getUserInput() {
        int choice = -1;
        while (choice != 5) {
            displayMenu();
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    System.out.print("Enter income amount: ");
                    double incomeAmount = scanner.nextDouble();
                    cashFlowManager.addIncome(incomeAmount);
                    break;
                case 2:
                    System.out.print("Enter expense amount: ");
                    double expenseAmount = scanner.nextDouble();
                    cashFlowManager.addExpense(expenseAmount);
                    break;
                case 3:
                    double cashFlow = cashFlowManager.calculateCashFlow();
                    System.out.println("Cash Flow: $" + cashFlow);
                    break;
                case 4:
                    cashFlowManager.displayCashFlow();
                    break;
                case 5:
                    System.out.println("Exiting Cash Flow Manager");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
        }
    }
}