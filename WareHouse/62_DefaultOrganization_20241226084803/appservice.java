'''
This class contains the business logic for the BudgetPlanner application.
'''
import org.springframework.stereotype.Service;
import com.example.Budget;
import com.example.BudgetRepository;
@Service
public class AppService {
    private final BudgetRepository budgetRepository;
    public AppService(BudgetRepository budgetRepository) {
        this.budgetRepository = budgetRepository;
    }
    public String getMessage() {
        return "Welcome to BudgetPlanner!";
    }
    public void depositToBudget(Long budgetId, double amount) {
        Budget budget = budgetRepository.findById(budgetId)
                .orElseThrow(() -> new IllegalArgumentException("Budget not found"));
        budget.setBalance(budget.getBalance() + amount);
        budgetRepository.save(budget);
    }
    public void withdrawFromBudget(Long budgetId, double amount) {
        Budget budget = budgetRepository.findById(budgetId)
                .orElseThrow(() -> new IllegalArgumentException("Budget not found"));
        if (amount <= budget.getBalance()) {
            budget.setBalance(budget.getBalance() - amount);
            budgetRepository.save(budget);
        } else {
            throw new IllegalArgumentException("Insufficient balance");
        }
    }
}