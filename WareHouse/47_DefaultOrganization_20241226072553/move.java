/**
 * This class represents a move in the puzzle.
 */
public class Move {
    private GridPosition fromPosition;
    private GridPosition toPosition;
    private Piece piece;
    public Move(GridPosition fromPosition, GridPosition toPosition, Piece piece) {
        this.fromPosition = fromPosition;
        this.toPosition = toPosition;
        this.piece = piece;
    }
    // Add necessary getter and setter methods for the fields
    public GridPosition getFromPosition() {
        return fromPosition;
    }
    public void setFromPosition(GridPosition fromPosition) {
        this.fromPosition = fromPosition;
    }
    public GridPosition getToPosition() {
        return toPosition;
    }
    public void setToPosition(GridPosition toPosition) {
        this.toPosition = toPosition;
    }
    public Piece getPiece() {
        return piece;
    }
    public void setPiece(Piece piece) {
        this.piece = piece;
    }
}