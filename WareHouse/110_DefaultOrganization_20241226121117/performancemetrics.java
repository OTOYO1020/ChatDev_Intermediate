/**
 * Represents performance metrics for a territory.
 */
package com.example.model;
public class PerformanceMetrics {
    private int territoryId;
    private int sales;
    private int revenue;
    // Add any other necessary fields
    // Getters and setters
    /**
     * Retrieves the ID of the territory.
     * 
     * @return The ID of the territory.
     */
    public int getTerritoryId() {
        return territoryId;
    }
    /**
     * Sets the ID of the territory.
     * 
     * @param territoryId The ID to set for the territory.
     */
    public void setTerritoryId(int territoryId) {
        this.territoryId = territoryId;
    }
    /**
     * Retrieves the sales for the territory.
     * 
     * @return The sales for the territory.
     */
    public int getSales() {
        return sales;
    }
    /**
     * Sets the sales for the territory.
     * 
     * @param sales The sales to set for the territory.
     */
    public void setSales(int sales) {
        this.sales = sales;
    }
    /**
     * Retrieves the revenue for the territory.
     * 
     * @return The revenue for the territory.
     */
    public int getRevenue() {
        return revenue;
    }
    /**
     * Sets the revenue for the territory.
     * 
     * @param revenue The revenue to set for the territory.
     */
    public void setRevenue(int revenue) {
        this.revenue = revenue;
    }
}