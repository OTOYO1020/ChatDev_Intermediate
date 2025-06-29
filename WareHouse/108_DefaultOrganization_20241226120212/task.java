package com.example.workflow;
/**
 * This class represents a task in a workflow template.
 */
public class Task {
    private String name;
    private String assignee;
    private String deadline;
    private boolean isCompleted;
    public Task(String name, String assignee, String deadline) {
        this.name = name;
        this.assignee = assignee;
        this.deadline = deadline;
        this.isCompleted = false;
    }
    public String getName() {
        return name;
    }
    public void setCompleted(boolean completed) {
        isCompleted = completed;
    }
}