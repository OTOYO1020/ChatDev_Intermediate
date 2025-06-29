'''
CashFlowManager class for the CashFlowManager application.
'''
public class CashFlowManager {
    private double cashFlow;
    public CashFlowManager() {
        cashFlow = 0.0;
    }
    public void addIncome(double amount) {
        cashFlow += amount;
    }
    public void addExpense(double amount) {
        cashFlow -= amount;
    }
    public double calculateCashFlow() {
        return cashFlow;
    }
    public void displayCashFlow() {
        System.out.println("Cash Flow: $" + cashFlow);
    }
}