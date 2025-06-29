/**
 * Represents a user in the system.
 */
package com.example.model;
public class User {
    private int id;
    private String name;
    // Getters and setters
    /**
     * Retrieves the ID of the user.
     * 
     * @return The ID of the user.
     */
    public int getId() {
        return id;
    }
    /**
     * Sets the ID of the user.
     * 
     * @param id The ID to set for the user.
     */
    public void setId(int id) {
        this.id = id;
    }
    /**
     * Retrieves the name of the user.
     * 
     * @return The name of the user.
     */
    public String getName() {
        return name;
    }
    /**
     * Sets the name of the user.
     * 
     * @param name The name to set for the user.
     */
    public void setName(String name) {
        this.name = name;
    }
}