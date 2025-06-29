/**
 * Controller class for managing performance metrics-related operations.
 */
import org.springframework.web.bind.annotation.*;
import com.example.model.PerformanceMetrics;
@RestController
@RequestMapping("/performancemetrics")
public class PerformanceMetricsController {
    /**
     * Retrieves performance metrics for a territory based on the provided territory ID.
     * 
     * @param territoryId The ID of the territory to retrieve performance metrics for.
     * @return The performance metrics object for the specified territory.
     */
    @GetMapping("/{territoryId}")
    public PerformanceMetrics getPerformanceMetrics(@PathVariable int territoryId) {
        // Retrieve performance metrics for the territory from the database or any other data source
        PerformanceMetrics performanceMetrics = new PerformanceMetrics();
        performanceMetrics.setTerritoryId(territoryId);
        performanceMetrics.setSales(100);
        performanceMetrics.setRevenue(10000);
        return performanceMetrics;
    }
}