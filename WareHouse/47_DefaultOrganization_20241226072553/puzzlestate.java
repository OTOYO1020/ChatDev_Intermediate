import java.util.ArrayList;
import java.util.List;
/**
 * This class represents the state of the puzzle.
 */
public class PuzzleState {
    private List<GridPosition> gridPositions;
    private List<Piece> availablePieces;
    private List<DesiredEndState> desiredEndStates;
    public PuzzleState() {
        // Initialize the fields
        gridPositions = new ArrayList<>();
        availablePieces = new ArrayList<>();
        desiredEndStates = new ArrayList<>();
    }
    // Add necessary getter and setter methods for the fields
    public List<GridPosition> getGridPositions() {
        return gridPositions;
    }
    public void setGridPositions(List<GridPosition> gridPositions) {
        this.gridPositions = gridPositions;
    }
    public List<Piece> getAvailablePieces() {
        return availablePieces;
    }
    public void setAvailablePieces(List<Piece> availablePieces) {
        this.availablePieces = availablePieces;
    }
    public List<DesiredEndState> getDesiredEndStates() {
        return desiredEndStates;
    }
    public void setDesiredEndStates(List<DesiredEndState> desiredEndStates) {
        this.desiredEndStates = desiredEndStates;
    }
}