/**
 * Controller class for managing user-related operations.
 */
import org.springframework.web.bind.annotation.*;
import com.example.model.User;
@RestController
@RequestMapping("/users")
public class UserController {
    /**
     * Retrieves a user based on the provided ID.
     * 
     * @param id The ID of the user to retrieve.
     * @return The user object with the specified ID.
     */
    @GetMapping("/{id}")
    public User getUser(@PathVariable int id) {
        // Retrieve user information from the database or any other data source
        User user = new User();
        user.setId(id);
        user.setName("John Doe");
        return user;
    }
    /**
     * Creates a new user based on the provided user object.
     * 
     * @param user The user object to create.
     * @return The saved user object with the generated ID.
     */
    @PostMapping("/")
    public User createUser(@RequestBody User user) {
        // Save the user information to the database or any other data source
        // Return the saved user with the generated ID
        user.setId(1);
        return user;
    }
}