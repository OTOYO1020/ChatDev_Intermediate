public class Employee {
    private String name;
    private int performanceScore;
    private int performanceGoal;
    public Employee(String name) {
        this.name = name;
        this.performanceScore = 0;
        this.performanceGoal = 0;
    }
    public String getName() {
        return name;
    }
    public int getPerformanceScore() {
        return performanceScore;
    }
    public void setPerformanceScore(int performanceScore) {
        this.performanceScore = performanceScore;
    }
    public int getPerformanceGoal() {
        return performanceGoal;
    }
    public void setPerformanceGoal(int performanceGoal) {
        this.performanceGoal = performanceGoal;
    }
}