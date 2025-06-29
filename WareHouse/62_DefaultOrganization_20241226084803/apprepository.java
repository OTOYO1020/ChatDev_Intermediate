'''
This interface provides the repository for the Budget entity.
'''
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.example.Budget;
@Repository
public interface BudgetRepository extends JpaRepository<Budget, Long> {
}