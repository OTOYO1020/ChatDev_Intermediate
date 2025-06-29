import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.JPanel;
public class GUI extends JPanel {
    private DiceTower diceTower;
    public GUI(DiceTower diceTower) {
        this.diceTower = diceTower;
        setPreferredSize(new Dimension(400, 400));
        setBackground(Color.WHITE);
        addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                diceTower.rollDice();
                repaint();
            }
        });
    }
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        // Draw the dice tower
        g.setColor(Color.GRAY);
        g.fillRect(100, 100, 200, 200);
        // Draw the dice
        g.setColor(Color.BLACK);
        int diceValue = diceTower.getDiceValue();
        g.drawString("Dice Value: " + diceValue, 150, 200);
    }
}