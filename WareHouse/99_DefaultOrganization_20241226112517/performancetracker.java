import java.util.ArrayList;
import java.util.List;
public class PerformanceTracker {
    private List<Employee> employees;
    public PerformanceTracker() {
        this.employees = new ArrayList<>();
    }
    public void addEmployee(Employee employee) {
        employees.add(employee);
    }
    public void removeEmployee(Employee employee) {
        employees.remove(employee);
    }
    public void setPerformanceGoal(Employee employee, int performanceGoal) {
        employee.setPerformanceGoal(performanceGoal);
    }
    public void conductEvaluation(Employee employee, int performanceScore) {
        employee.setPerformanceScore(performanceScore);
    }
    public void generatePerformanceReport() {
        System.out.println("Performance Report:");
        for (Employee employee : employees) {
            System.out.println("Employee: " + employee.getName());
            System.out.println("Performance Score: " + employee.getPerformanceScore());
            System.out.println("Performance Goal: " + employee.getPerformanceGoal());
            System.out.println("----------------------");
        }
    }
    public List<Employee> getEmployees() {
        return employees;
    }
}