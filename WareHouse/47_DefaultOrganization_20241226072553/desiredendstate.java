/**
 * This class represents a desired end state of the puzzle.
 */
public class DesiredEndState {
    private GridPosition position;
    private Piece piece;
    public DesiredEndState(GridPosition position, Piece piece) {
        this.position = position;
        this.piece = piece;
    }
    // Add necessary getter and setter methods for the fields
    public GridPosition getPosition() {
        return position;
    }
    public void setPosition(GridPosition position) {
        this.position = position;
    }
    public Piece getPiece() {
        return piece;
    }
    public void setPiece(Piece piece) {
        this.piece = piece;
    }
}