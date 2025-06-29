import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface (GUI) for the application.
 * It contains the main window and handles user interactions.
 */
public class GUI extends JFrame {
    private JButton button;
    private JButton generateReportsButton; // New button for generating reports
    private JLabel label;
    private JLabel inventoryReportLabel; // Label for displaying inventory report
    private JLabel stockOrderReportLabel; // Label for displaying stock order report
    private Inventory inventory;
    private StockOrder stockOrder;
    private ReportGenerator reportGenerator;
    public GUI() {
        // Set up the main window
        setTitle("Inventory Tracker");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());
        // Create the button
        button = new JButton("Click me");
        // Create the generate reports button
        generateReportsButton = new JButton("Generate Reports");
        // Create the label
        label = new JLabel("Hello, world!");
        // Create instances of Inventory, StockOrder, and ReportGenerator
        inventory = new Inventory();
        stockOrder = new StockOrder();
        reportGenerator = new ReportGenerator(inventory, stockOrder);
        // Add the buttons and label to the main window
        add(button);
        add(generateReportsButton); // Add the generate reports button
        add(label);
        // Add an action listener to the button
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle button click event
                label.setText("Button clicked!");
            }
        });
        // Add an action listener to the generate reports button
        generateReportsButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle generate reports button click event
                generateReports();
            }
        });
        // Create labels for inventory report and stock order report
        inventoryReportLabel = new JLabel();
        stockOrderReportLabel = new JLabel();
        // Add the labels to the main window
        add(inventoryReportLabel);
        add(stockOrderReportLabel);
    }
    public void start() {
        // Show the main window
        setVisible(true);
    }
    /**
     * Generate and display the inventory and stock order history reports.
     */
    public void generateReports() {
        String inventoryReport = reportGenerator.generateInventoryReport();
        String stockOrderReport = reportGenerator.generateStockOrderHistoryReport();
        // Display the reports in the GUI (e.g., using labels or text areas)
        inventoryReportLabel.setText(inventoryReport);
        stockOrderReportLabel.setText(stockOrderReport);
    }
}