'''
This class represents the BudgetPlanner application.
'''
import javax.persistence.*;
import java.util.List;
import com.example.Budget;
@Entity
public class App {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
    @OneToMany(mappedBy = "app", cascade = CascadeType.ALL)
    private List<Budget> budgets;
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public List<Budget> getBudgets() {
        return budgets;
    }
    public void setBudgets(List<Budget> budgets) {
        this.budgets = budgets;
    }
}