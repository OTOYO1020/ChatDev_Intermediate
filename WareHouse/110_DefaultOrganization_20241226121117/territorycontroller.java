/**
 * Controller class for managing territory-related operations.
 */
import org.springframework.web.bind.annotation.*;
import com.example.model.Territory;
import com.example.model.User;
@RestController
@RequestMapping("/territories")
public class TerritoryController {
    /**
     * Creates a new territory based on the provided territory object.
     * 
     * @param territory The territory object to create.
     * @return The saved territory object with the generated ID.
     */
    @PostMapping("/")
    public Territory createTerritory(@RequestBody Territory territory) {
        // Save the territory information to the database or any other data source
        // Return the saved territory with the generated ID
        territory.setId(1);
        return territory;
    }
    /**
     * Assigns a territory to a sales representative.
     * 
     * @param territoryId The ID of the territory to assign.
     * @param userId The ID of the sales representative to assign the territory to.
     * @return The updated territory object with the assigned sales representative.
     */
    @PostMapping("/{territoryId}/assign/{userId}")
    public Territory assignTerritory(@PathVariable int territoryId, @PathVariable int userId) {
        // Retrieve the territory and user information from the database or any other data source
        Territory territory = new Territory();
        territory.setId(territoryId);
        territory.setName("Territory 1");
        User user = new User();
        user.setId(userId);
        user.setName("John Doe");
        // Assign the territory to the user
        territory.setAssignedUser(user);
        return territory;
    }
}