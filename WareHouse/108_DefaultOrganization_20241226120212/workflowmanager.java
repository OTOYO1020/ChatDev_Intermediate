package com.example.workflow;
import java.util.ArrayList;
import java.util.List;
/**
 * This class represents the Workflow Manager that handles the creation and management of workflow templates,
 * task assignments, progress tracking, and report generation.
 */
public class WorkflowManager {
    private List<WorkflowTemplate> workflowTemplates;
    public WorkflowManager() {
        workflowTemplates = new ArrayList<>();
    }
    public void start() {
        // Display the GUI for user interactions
        GUI gui = new GUI(this);
        gui.start();
    }
    public void createWorkflowTemplate(String templateName) {
        // Create a new workflow template
        WorkflowTemplate workflowTemplate = new WorkflowTemplate(templateName);
        // Add the template to the list of workflow templates
        workflowTemplates.add(workflowTemplate);
    }
    public void assignTask(String templateName, String taskName, String assignee, String deadline) {
        // Find the workflow template
        WorkflowTemplate workflowTemplate = findWorkflowTemplate(templateName);
        if (workflowTemplate != null) {
            // Create a new task and assign it to the assignee with the deadline
            Task task = new Task(taskName, assignee, deadline);
            // Add the task to the workflow template
            workflowTemplate.addTask(task);
        }
    }
    public void updateTaskProgress(String templateName, String taskName, boolean isCompleted) {
        // Find the workflow template
        WorkflowTemplate workflowTemplate = findWorkflowTemplate(templateName);
        if (workflowTemplate != null) {
            // Find the task in the workflow template
            Task task = workflowTemplate.findTask(taskName);
            if (task != null) {
                // Update the task progress
                task.setCompleted(isCompleted);
            }
        }
    }
    public void generateReport(String templateName) {
        // Find the workflow template
        WorkflowTemplate workflowTemplate = findWorkflowTemplate(templateName);
        if (workflowTemplate != null) {
            // Generate a report for the workflow template
            workflowTemplate.generateReport();
        }
    }
    private WorkflowTemplate findWorkflowTemplate(String templateName) {
        // Find the workflow template with the given name
        for (WorkflowTemplate workflowTemplate : workflowTemplates) {
            if (workflowTemplate.getName().equals(templateName)) {
                return workflowTemplate;
            }
        }
        return null;
    }
}