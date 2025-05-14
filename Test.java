import java.io.*;

// Parent class
class FileOperations {
    // Method to write data to a file
    public void writeToFile(String fileName, String content) {
        try (FileWriter writer = new FileWriter(fileName)) {
            writer.write(content);
            System.out.println("Data written to file: " + fileName);
        } catch (IOException e) {
            System.out.println("An error occurred while writing to the file: " + e.getMessage());
        }
    }

    // Method to read data from a file
    public void readFromFile(String fileName) {
        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line;
            System.out.println("Contents of the file:");
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("An error occurred while reading the file: " + e.getMessage());
        }
    }
}

// Child class
public class Test extends FileOperations {
    public static void main(String[] args) {
        // Create an instance of the child class
        Test test = new Test();

        // File name
        String fileName = "example.txt";

        // Write to the file
        String content = "Hello, this is a file handling example in Java.";
        test.writeToFile(fileName, content);

        // Read from the file
        test.readFromFile(fileName); 
    }
}