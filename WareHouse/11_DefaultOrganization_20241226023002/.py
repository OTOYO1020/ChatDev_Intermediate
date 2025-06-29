private void runGame() {
    // Game loop
    while (true) {
        // Check if it's a boss battle
        if (bossBattle) {
            // Handle boss battle logic
            handleBossBattle();
        } else {
            // Handle regular level logic
            handleLevel();
        }
        // Check if the game is over or if the player chooses to exit
        if (isGameOver() || isExitRequested()) {
            break; // Exit the game loop
        }
    }
}