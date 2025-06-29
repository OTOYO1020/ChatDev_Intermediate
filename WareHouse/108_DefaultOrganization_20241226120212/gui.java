package com.example.workflow;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface (GUI) for the web application.
 * It creates a window with buttons and handles user interactions.
 */
public class GUI extends JFrame {
    private WorkflowManager workflowManager;
    private JButton createTemplateButton;
    private JButton assignTaskButton;
    private JButton updateProgressButton;
    private JButton generateReportButton;
    public GUI(WorkflowManager workflowManager) {
        this.workflowManager = workflowManager;
        // Set up the window
        setTitle("Business Workflow Automation");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());
        // Create buttons
        createTemplateButton = new JButton("Create Workflow Template");
        assignTaskButton = new JButton("Assign Task");
        updateProgressButton = new JButton("Update Task Progress");
        generateReportButton = new JButton("Generate Report");
        // Add action listeners to the buttons
        createTemplateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                handleCreateTemplateButtonClick();
            }
        });
        assignTaskButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                handleAssignTaskButtonClick();
            }
        });
        updateProgressButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                handleUpdateProgressButtonClick();
            }
        });
        generateReportButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                handleGenerateReportButtonClick();
            }
        });
        // Add the buttons to the window
        add(createTemplateButton);
        add(assignTaskButton);
        add(updateProgressButton);
        add(generateReportButton);
    }
    public void start() {
        // Display the window
        setVisible(true);
    }
    private void handleCreateTemplateButtonClick() {
        // Prompt the user to enter the template name
        String templateName = JOptionPane.showInputDialog(this, "Enter the template name:");
        if (templateName != null && !templateName.isEmpty()) {
            // Create a new workflow template
            workflowManager.createWorkflowTemplate(templateName);
            JOptionPane.showMessageDialog(this, "Workflow template created successfully!");
        } else {
            JOptionPane.showMessageDialog(this, "Invalid template name!");
        }
    }
    private void handleAssignTaskButtonClick() {
        // Prompt the user to enter the template name, task name, assignee, and deadline
        String templateName = JOptionPane.showInputDialog(this, "Enter the template name:");
        String taskName = JOptionPane.showInputDialog(this, "Enter the task name:");
        String assignee = JOptionPane.showInputDialog(this, "Enter the assignee:");
        String deadline = JOptionPane.showInputDialog(this, "Enter the deadline:");
        if (templateName != null && !templateName.isEmpty() &&
                taskName != null && !taskName.isEmpty() &&
                assignee != null && !assignee.isEmpty() &&
                deadline != null && !deadline.isEmpty()) {
            // Assign the task to the assignee with the deadline
            workflowManager.assignTask(templateName, taskName, assignee, deadline);
            JOptionPane.showMessageDialog(this, "Task assigned successfully!");
        } else {
            JOptionPane.showMessageDialog(this, "Invalid input!");
        }
    }
    private void handleUpdateProgressButtonClick() {
        // Prompt the user to enter the template name and task name
        String templateName = JOptionPane.showInputDialog(this, "Enter the template name:");
        String taskName = JOptionPane.showInputDialog(this, "Enter the task name:");
        if (templateName != null && !templateName.isEmpty() &&
                taskName != null && !taskName.isEmpty()) {
            // Prompt the user to select the task progress
            String[] options = {"Completed", "Not Completed"};
            int choice = JOptionPane.showOptionDialog(this, "Select the task progress:", "Update Task Progress",
                    JOptionPane.DEFAULT_OPTION, JOptionPane.QUESTION_MESSAGE, null, options, options[0]);
            boolean isCompleted = (choice == 0);
            // Update the task progress
            workflowManager.updateTaskProgress(templateName, taskName, isCompleted);
            JOptionPane.showMessageDialog(this, "Task progress updated successfully!");
        } else {
            JOptionPane.showMessageDialog(this, "Invalid input!");
        }
    }
    private void handleGenerateReportButtonClick() {
        // Prompt the user to enter the template name
        String templateName = JOptionPane.showInputDialog(this, "Enter the template name:");
        if (templateName != null && !templateName.isEmpty()) {
            // Generate a report for the workflow template
            workflowManager.generateReport(templateName);
            JOptionPane.showMessageDialog(this, "Report generated successfully!");
        } else {
            JOptionPane.showMessageDialog(this, "Invalid template name!");
        }
    }
}