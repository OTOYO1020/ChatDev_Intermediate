/**
 * This class represents the data model of the web application.
 * It stores and manages the data used by the application.
 */
public class Model {
    private double salesData;
    private double salesTarget;
    public void setSalesData(double salesData) {
        this.salesData = salesData;
    }
    public double getSalesData() {
        return salesData;
    }
    public void setSalesTarget(double salesTarget) {
        this.salesTarget = salesTarget;
    }
    public double getSalesTarget() {
        return salesTarget;
    }
}