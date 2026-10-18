import java.io.IOException;
import java.io.BufferedWriter;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;


void main() throws IOException, InterruptedException {
    var scan = new Scanner(System.in);
    System.out.println("\n\n");
    System.out.println("= = =   =    = =  =     =  = = = ©");
    System.out.println("=    =  =  =      =     =    =  ");
    System.out.println("= = =   =  =      =     =    =  ");
    System.out.println("=       =    = =    = =      =  ");
    try {
        TimeUnit.SECONDS.sleep(1);
    } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
    }
    System.out.println("\n\nWelcome to PICUT©-Setup!\n\n");
    try {
        TimeUnit.SECONDS.sleep(1);
    } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
    }
    System.out.println("ONLY the Raspberry Pi Pico Family is supported!\n\n");

    try {
        TimeUnit.SECONDS.sleep(1);
    } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
    }

    System.out.println("Do you need a config file? (0=No, 1 =Yes)\n");
    var b = scan.nextInt();
    if (b == 1) {
        File config = new File("config.txt");

        Path newconfig = Paths.get("config.txt");
        try (BufferedWriter writer = Files.newBufferedWriter(newconfig)) {
            for (int i = 0; i < 30; i++) {
                writer.newLine(); // Schreibt den plattformunabhängigen Zeilenumbruch
            }
            System.out.println("\nConfig was generated successfully!.");
        } catch (IOException e) {
            System.out.println("\nSomething went wrong: " + e.getMessage());
        }
    }

    try {
        TimeUnit.SECONDS.sleep(1);
    } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
    }

    int a = 1;
    while (a == 1) {
        Path pfad = Path.of("config.txt");
        List<String> zeilen = Files.readAllLines(pfad, StandardCharsets.UTF_8);


        System.out.println("\nWhich Button do you want to configure? (Please type in the GP Number. Only the Pins from 1 - 22 on any Pi Pico are supported!)\nPinouts: https://www.elektronik-kompendium.de/sites/raspberry-pi/2611051.htm)");
        System.out.println("");
        int button = scan.nextInt();

        scan.nextLine();
        if (button > 22) {
            System.exit(5);
        }
        if (button < 1) {
            System.exit(5);
        }
        int button2 = button + 5;
        System.out.println("\nWhat should the Button do?\n");
        var text = scan.nextLine();

        if (button2 >= 5 && button < zeilen.size()) {
            zeilen.set(button2, text);
            Files.write(pfad, zeilen, StandardCharsets.UTF_8);
            System.out.println("\nConfig updatet!\n");
        } else {
            System.out.println("Sorry. Something went wrong! Please Try again!");
        }
        System.out.println("Configure another Button? (0=No, 1=Yes)\n");
        a = scan.nextInt();
        System.out.println("\n");

    }
    System.out.println("Now you can copy the config.txt from this directory onto your Pi!\n\n");
    try {
        TimeUnit.SECONDS.sleep(1);
    } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
    }
    System.out.println("= = =   =    = =  =     =  = = = ©");
    System.out.println("=    =  =  =      =     =    =  ");
    System.out.println("= = =   =  =      =     =    =  ");
    System.out.println("=       =    = =    = =      =  ");
    System.out.println("\n\nCU!");
    System.out.println("Made by Joshi7479");
    System.out.println("Support this Project on Github: https://github.com/Joshi7479/PICUT");
    try {
        TimeUnit.SECONDS.sleep(1);
    } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
    }
}
