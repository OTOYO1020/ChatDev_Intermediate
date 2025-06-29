public static void main(String[] args) {
    SwingUtilities.invokeLater(new Runnable() {
        @Override
        public void run() {
            BudgetAssistant budgetAssistant = new BudgetAssistant();
            budgetAssistant.start();
        }
    });
}