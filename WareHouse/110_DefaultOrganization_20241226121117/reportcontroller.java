/**
 * Controller class for managing report-related operations.
 */
import org.springframework.web.bind.annotation.*;
import com.example.model.Report;
@RestController
@RequestMapping("/reports")
public class ReportController {
    /**
     * Generates a report for a territory based on the provided territory ID.
     * 
     * @param territoryId The ID of the territory to generate a report for.
     * @return The generated report object for the specified territory.
     */
    @GetMapping("/{territoryId}")
    public Report generateReport(@PathVariable int territoryId) {
        // Generate a report for the territory based on performance metrics and other data
        Report report = new Report();
        report.setTerritoryId(territoryId);
        report.setReportData("Sample report data");
        return report;
    }
}