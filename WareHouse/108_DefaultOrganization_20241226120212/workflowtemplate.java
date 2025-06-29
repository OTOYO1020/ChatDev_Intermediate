package com.example.workflow;
import java.util.ArrayList;
import java.util.List;
/**
 * This class represents a workflow template that contains a sequence of tasks.
 */
public class WorkflowTemplate {
    private String name;
    private List<Task> tasks;
    public WorkflowTemplate(String name) {
        this.name = name;
        tasks = new ArrayList<>();
    }
    public String getName() {
        return name;
    }
    public void addTask(Task task) {
        tasks.add(task);
    }
    public Task findTask(String taskName) {
        // Find the task with the given name
        for (Task task : tasks) {
            if (task.getName().equals(taskName)) {
                return task;
            }
        }
        return null;
    }
    public void generateReport() {
        // Generate a report for the workflow template
        System.out.println("Generating report for workflow template: " + name);
        // TODO: Implement report generation logic
    }
}