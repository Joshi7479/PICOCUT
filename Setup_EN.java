import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Scanner;


void main() throws IOException, InterruptedException {
    System.out.println("= = =   =    = =  =     =  = = = ©");
    System.out.println("=    =  =  =      =     =    =  ");
    System.out.println("= = =   =  =      =     =    =  ");
    System.out.println("=       =    = =    = =      =  ");
    System.out.println("\n\nWelcome to PICUT©-Setup!");



    int a = 1;
    while (a == 1) {
        Path pfad = Path.of("config.txt");
        List<String> zeilen = Files.readAllLines(pfad, StandardCharsets.UTF_8);
        var scan = new Scanner(System.in);

        System.out.println("Which Button do you want to configure? (Please type in the GP Number. Only the Pins from 1 - 22 on any Pi Pico are supported!\nhttps://www.elektronik-kompendium.de/sites/raspberry-pi/2611051.htm");
        int button = scan.nextInt();

        scan.nextLine();
        if (button > 22) {
            System.exit(5);
        }
        if (button < 1) {
            System.exit(5);
        }
        int button2 = button + 5;
        System.out.println("What should the Button do?");
        var text = scan.nextLine();

        if (button2 >= 5 && button < zeilen.size()) {
            zeilen.set(button2, text);
            Files.write(pfad, zeilen, StandardCharsets.UTF_8);
            System.out.println("Config updatet!");
        } else {
            System.out.println("Sorry. Something went wrong! Please Try again!");
        }
        System.out.println("Configure another Button? (0=No, 1=Yes)");
        a = scan.nextInt();

    }
    System.out.println("= = =   =    = =  =     =  = = = ©");
    System.out.println("=    =  =  =      =     =    =  ");
    System.out.println("= = =   =  =      =     =    =  ");
    System.out.println("=       =    = =    = =      =  ");
    System.out.println("\n\nCU!");

    try {
        // Pausiert den aktuellen Thread für 1 Sekunde
        TimeUnit.SECONDS.sleep(1);
    } catch (InterruptedException e) {
        // Behandlung der Ausnahme, falls der Schlaf unterbrochen wird
        Thread.currentThread().interrupt();
    }
}