/**
 * Represents a territory in the system.
 */
package com.example.model;
public class Territory {
    private int id;
    private String name;
    private User assignedUser; // Added field for assigning a territory to a sales representative
    // Getters and setters
    /**
     * Retrieves the ID of the territory.
     * 
     * @return The ID of the territory.
     */
    public int getId() {
        return id;
    }
    /**
     * Sets the ID of the territory.
     * 
     * @param id The ID to set for the territory.
     */
    public void setId(int id) {
        this.id = id;
    }
    /**
     * Retrieves the name of the territory.
     * 
     * @return The name of the territory.
     */
    public String getName() {
        return name;
    }
    /**
     * Sets the name of the territory.
     * 
     * @param name The name to set for the territory.
     */
    public void setName(String name) {
        this.name = name;
    }
    /**
     * Retrieves the assigned user for the territory.
     * 
     * @return The assigned user for the territory.
     */
    public User getAssignedUser() {
        return assignedUser;
    }
    /**
     * Sets the assigned user for the territory.
     * 
     * @param assignedUser The user to assign to the territory.
     */
    public void setAssignedUser(User assignedUser) {
        this.assignedUser = assignedUser;
    }
}