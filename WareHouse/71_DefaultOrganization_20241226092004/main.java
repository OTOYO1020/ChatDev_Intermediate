import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class Main {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGUI();
            }
        });
    }
    private static void createAndShowGUI() {
        // Create and set up the main frame
        JFrame frame = new JFrame("BudgetOptimizer");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());
        // Create and set up the content panel
        JPanel contentPanel = new JPanel();
        contentPanel.setLayout(new BorderLayout());
        // Create and add components to the content panel
        JLabel titleLabel = new JLabel("BudgetOptimizer");
        titleLabel.setFont(new Font("Arial", Font.BOLD, 24));
        titleLabel.setHorizontalAlignment(JLabel.CENTER);
        contentPanel.add(titleLabel, BorderLayout.NORTH);
        // Create and add buttons to the content panel
        JButton analyzeButton = new JButton("Analyze");
        JButton generateReportButton = new JButton("Generate Report");
        JPanel buttonPanel = new JPanel();
        buttonPanel.add(analyzeButton);
        buttonPanel.add(generateReportButton);
        contentPanel.add(buttonPanel, BorderLayout.CENTER);
        // Add action listeners to the buttons
        analyzeButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Perform analysis logic here
                JOptionPane.showMessageDialog(frame, "Analysis performed!");
            }
        });
        generateReportButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Perform report generation logic here
                JOptionPane.showMessageDialog(frame, "Report generated!");
            }
        });
        // Add the content panel to the frame
        frame.getContentPane().add(contentPanel);
        // Pack and display the frame
        frame.pack();
        frame.setVisible(true);
    }
}