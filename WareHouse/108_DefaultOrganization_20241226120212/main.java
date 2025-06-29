package com.example.workflow;
/**
 * This is the main class that serves as the entry point for the web application.
 * It initializes the WorkflowManager and starts the application.
 */
public class Main {
    public static void main(String[] args) {
        // Initialize the WorkflowManager
        WorkflowManager workflowManager = new WorkflowManager();
        // Start the application
        workflowManager.start();
    }
}