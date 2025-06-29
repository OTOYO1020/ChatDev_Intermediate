'''
This class is responsible for handling HTTP requests and returning responses.
'''
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;
import com.example.Budget;
import com.example.BudgetRepository;
@Controller
@RequestMapping("/app")
public class AppController {
    private final AppService appService;
    private final BudgetRepository budgetRepository;
    @Autowired
    public AppController(AppService appService, BudgetRepository budgetRepository) {
        this.appService = appService;
        this.budgetRepository = budgetRepository;
    }
    @GetMapping("/hello")
    @ResponseBody
    public String hello() {
        return "Hello, World!";
    }
    @GetMapping("/message")
    @ResponseBody
    public String getMessage() {
        return appService.getMessage();
    }
    @PostMapping("/budget/deposit")
    @ResponseBody
    public void depositToBudget(@RequestParam("budgetId") Long budgetId, @RequestParam("amount") double amount) {
        appService.depositToBudget(budgetId, amount);
    }
    @PostMapping("/budget/withdraw")
    @ResponseBody
    public void withdrawFromBudget(@RequestParam("budgetId") Long budgetId, @RequestParam("amount") double amount) {
        appService.withdrawFromBudget(budgetId, amount);
    }
}