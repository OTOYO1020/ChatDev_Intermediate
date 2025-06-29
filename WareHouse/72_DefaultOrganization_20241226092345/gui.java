import javax.swing.JButton;
import javax.swing.JOptionPane;
import javax.swing.JTextField;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.data.general.DefaultPieDataset;
public class GUI {
    private JFrame frame;
    private JPanel panel;
    private JTextField incomeField;
    private JTextField expenseField;
    private JButton addButton;
    private JButton goalButton;
    private ChartPanel chartPanel;
    public void createAndShowGUI() {
        frame = new JFrame("Budget Planner Lite");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        panel = new JPanel();
        panel.setLayout(new BorderLayout());
        incomeField = new JTextField();
        expenseField = new JTextField();
        addButton = new JButton("Add");
        addButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Add income or expense logic
            }
        });
        goalButton = new JButton("Set Goal");
        goalButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Set goal logic
            }
        });
        panel.add(incomeField, BorderLayout.NORTH);
        panel.add(expenseField, BorderLayout.CENTER);
        panel.add(addButton, BorderLayout.WEST);
        panel.add(goalButton, BorderLayout.EAST);
        DefaultPieDataset dataset = new DefaultPieDataset();
        dataset.setValue("Income", 1000);
        dataset.setValue("Expenses", 500);
        JFreeChart chart = ChartFactory.createPieChart("Budget Breakdown", dataset);
        chartPanel = new ChartPanel(chart);
        panel.add(chartPanel, BorderLayout.SOUTH);
        frame.getContentPane().add(panel);
        frame.pack();
        frame.setVisible(true);
    }
}