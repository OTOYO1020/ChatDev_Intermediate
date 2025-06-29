import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.List;
import java.util.ArrayList;
import SalesData;
import SalesDataAnalyzer;
/**
 * This class represents the web application and contains the GUI components.
 */
public class WebApplication {
    private JFrame frame;
    private JPanel panel;
    private JButton button;
    private JLabel label;
    private SalesDataAnalyzer analyzer;
    public WebApplication() {
        // Initialize the GUI components
        frame = new JFrame("Sales Performance Analyzer");
        panel = new JPanel();
        button = new JButton("Analyze Data");
        label = new JLabel("Sales Performance Analyzer");
        // Set the layout and add components to the panel
        panel.setLayout(new FlowLayout());
        panel.add(button);
        panel.add(label);
        // Add the panel to the frame
        frame.getContentPane().add(panel);
        // Set frame properties
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);
        frame.setVisible(true);
        // Initialize the SalesDataAnalyzer
        analyzer = new SalesDataAnalyzer();
    }
    public void run() {
        // Add event listener to the button
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Analyze the sales data and display the results
                List<SalesData> salesData = analyzer.getSalesData();
                // Calculate the total revenue
                double totalRevenue = analyzer.calculateTotalRevenue();
                // Calculate the average quantity
                double averageQuantity = analyzer.calculateAverageQuantity();
                // Identify the best selling product
                String bestSellingProduct = analyzer.identifyBestSellingProduct();
                // Update the label text when the button is clicked
                label.setText("Data Analyzed!\nTotal Revenue: $" + totalRevenue + "\nAverage Quantity: " + averageQuantity + "\nBest Selling Product: " + bestSellingProduct);
            }
        });
    }
}