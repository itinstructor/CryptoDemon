import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.security.*;
import java.util.*;
import java.io.*;

public class HashyApp {
    private JFrame frame;
    private JPanel panel;
    private JTextArea inputTextArea;
    private JButton calculateButton;
    private JButton saveButton;
    private JComboBox<String> inputSourceComboBox;
    private Map<String, JLabel> hashLabels;
    private JCheckBox[] hashCheckboxes;
    private String generatedHashes;

    public HashyApp() {
        // Create the main frame and panel
        frame = new JFrame("Hash Generator");
        panel = new JPanel(new BorderLayout());

        // Create a text area for user input
        inputTextArea = new JTextArea(10, 40);
        JScrollPane inputScrollPane = new JScrollPane(inputTextArea);
        panel.add(inputScrollPane, BorderLayout.NORTH);

        // Create a control panel for buttons and input source selection
        JPanel controlPanel = new JPanel();
        controlPanel.setLayout(new FlowLayout(FlowLayout.LEFT));

        // Create a combo box for selecting input source (User Input or File Input)
        inputSourceComboBox = new JComboBox<>(new String[] { "User Input", "File Input" });
        controlPanel.add(inputSourceComboBox);

        // Create a button to calculate hashes
        calculateButton = new JButton("Calculate Hashes");
        controlPanel.add(calculateButton);

        // Create a button to save hashes to a file
        saveButton = new JButton("Save to File");
        controlPanel.add(saveButton);

        // Add the control panel to the main panel
        panel.add(controlPanel, BorderLayout.CENTER);

        // Create a panel for displaying checkboxes and labels for hashes
        JPanel checkboxPanel = new JPanel();
        checkboxPanel.setLayout(new GridLayout(0, 2));

        // Create checkboxes for hash algorithms and store labels in a map
        hashCheckboxes = new JCheckBox[] {
                new JCheckBox("MD5"),
                new JCheckBox("SHA-1"),
                new JCheckBox("SHA-224"),
                new JCheckBox("SHA-256"),
                new JCheckBox("SHA-384"),
                new JCheckBox("SHA-512"),
                new JCheckBox("SHA3-224"),
                new JCheckBox("SHA3-256"),
                new JCheckBox("SHA3-384"),
                new JCheckBox("SHA3-512") };

        hashLabels = new HashMap<>();

        // Associate labels with checkboxes
        for (JCheckBox checkbox : hashCheckboxes) {
            checkboxPanel.add(checkbox);
            JLabel label = new JLabel();
            hashLabels.put(checkbox.getText(), label);
            checkboxPanel.add(label);
        }

        // Add the checkbox panel to the main panel
        panel.add(checkboxPanel, BorderLayout.SOUTH);

        // Add the main panel to the frame
        frame.add(panel);

        // Configure frame properties
        frame.pack();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);

        // Add action listeners for buttons and combo box
        calculateButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                generateHashes();
            }
        });

        saveButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                saveHashesToFile();
            }
        });

        inputSourceComboBox.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String selectedOption = (String) inputSourceComboBox.getSelectedItem();
                if (selectedOption.equals("File Input")) {
                    openFile();
                } else {
                    inputTextArea.setText("");
                }
            }
        });
    }

    // Method to generate hashes based on user input
    private void generateHashes() {
        // Retrieve user input
        String input = inputTextArea.getText();
        if (input.isEmpty()) {
            JOptionPane.showMessageDialog(frame, "Please enter some text for hashing.", "Error",
                    JOptionPane.ERROR_MESSAGE);
            return;
        }

        // Create a StringBuilder to store the generated hashes
        StringBuilder result = new StringBuilder();

        // Calculate and display selected hashes
        for (JCheckBox checkbox : hashCheckboxes) {
            if (checkbox.isSelected()) {
                String algorithm = checkbox.getText();
                String hash = calculateHash(input, algorithm);
                result.append(algorithm).append(": ").append(hash).append("\n");
                hashLabels.get(algorithm).setText(algorithm + ": " + hash);
            }
        }

        // Store the generated hashes for saving to a file
        generatedHashes = result.toString();
    }

    // Method to calculate a hash using a specified algorithm
    private String calculateHash(String input, String algorithm) {
        try {
            MessageDigest md = MessageDigest.getInstance(algorithm);
            byte[] hashBytes = md.digest(input.getBytes());

            StringBuilder hexString = new StringBuilder();
            for (byte hashByte : hashBytes) {
                String hex = Integer.toHexString(0xFF & hashByte);
                if (hex.length() == 1) {
                    hexString.append("0");
                }
                hexString.append(hex);
            }

            return hexString.toString();
        } catch (NoSuchAlgorithmException e) {
            return "Error: " + e.getMessage();
        }
    }

    // Method to save hashes to a file
    private void saveHashesToFile() {
        if (generatedHashes == null || generatedHashes.isEmpty()) {
            JOptionPane.showMessageDialog(frame, "No hashes to save.", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        // Create a file chooser dialog
        JFileChooser fileChooser = new JFileChooser();

        // Show the save file dialog
        int choice = fileChooser.showSaveDialog(frame);

        if (choice == JFileChooser.APPROVE_OPTION) {
            File file = fileChooser.getSelectedFile();
            try (PrintWriter writer = new PrintWriter(file)) {
                // Write the generated hashes to the selected file
                writer.println(generatedHashes);
                JOptionPane.showMessageDialog(frame, "Hashes saved successfully.", "Success",
                        JOptionPane.INFORMATION_MESSAGE);
            } catch (IOException e) {
                JOptionPane.showMessageDialog(frame, "Error saving the file.", "Error", JOptionPane.ERROR_MESSAGE);
            }
        }
    }

    // Method to open a file for input
    private void openFile() {
        // Create a file chooser dialog
        JFileChooser fileChooser = new JFileChooser();

        // Show the open file dialog
        int choice = fileChooser.showOpenDialog(frame);

        if (choice == JFileChooser.APPROVE_OPTION) {
            File selectedFile = fileChooser.getSelectedFile();
            try (Scanner scanner = new Scanner(selectedFile)) {
                StringBuilder fileContent = new StringBuilder();
                while (scanner.hasNextLine()) {
                    fileContent.append(scanner.nextLine()).append("\n");
                }
                inputTextArea.setText(fileContent.toString());
            } catch (FileNotFoundException e) {
                JOptionPane.showMessageDialog(frame, "Error reading the selected file.", "Error",
                        JOptionPane.ERROR_MESSAGE);
            }
        }
    }

    // Main method to start the application
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new HashyApp();
            }
        });
    }
}
