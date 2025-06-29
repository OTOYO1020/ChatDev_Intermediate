import java.util.ArrayList;
import java.util.List;
/**
 * This class represents the data model of the web application.
 */
public class Model {
    private List<String> expenses;
    public Model() {
        expenses = new ArrayList<>();
    }
    public void addExpense(String expense, String category) {
        expenses.add(expense + " - " + category);
    }
    public String getExpenseList() {
        StringBuilder sb = new StringBuilder();
        for (String expense : expenses) {
            sb.append(expense).append("\n");
        }
        return sb.toString();
    }
}