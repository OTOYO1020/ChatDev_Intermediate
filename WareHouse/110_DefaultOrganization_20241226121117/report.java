/**
 * Represents a report for a territory.
 */
package com.example.model;
public class Report {
    private int territoryId;
    private String reportData;
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
     * Retrieves the report data for the territory.
     * 
     * @return The report data for the territory.
     */
    public String getReportData() {
        return reportData;
    }
    /**
     * Sets the report data for the territory.
     * 
     * @param reportData The report data to set for the territory.
     */
    public void setReportData(String reportData) {
        this.reportData = reportData;
    }
}