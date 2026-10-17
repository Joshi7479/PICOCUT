import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

void main() throws IOException {
    System.out.println("= = =   =    = =  =     =  = = = ©");
    System.out.println("=    =  =  =      =     =    =  ");
    System.out.println("= = =   =  =      =     =    =  ");
    System.out.println("=       =    = =    = =      =  ");
    System.out.println("\n\nWillkommen zum PICUT©-Setup!");
    int a = 1;
    while (a == 1) {
        Path pfad = Path.of("config.txt");
        List<String> zeilen = Files.readAllLines(pfad, StandardCharsets.UTF_8);
        var scan = new Scanner(System.in);

        System.out.println("Welcher Knopf soll etwas tuen? (Bitte die GP Nummer (https://www.elektronik-kompendium.de/sites/raspberry-pi/2611051.htm)\nNur die Pins 1 - 22 auf jedem Pi Pico werden unterstüzt.");
        int button = scan.nextInt();

        scan.nextLine();
        if (button > 22) {
            System.exit(5);
        }
        if (button < 1) {
            System.exit(5);
        }
        int button2 = button + 5;
        System.out.println(button2);
        System.out.println("Was soll der Knopf tuen?");
        var text = scan.nextLine();

        if (button2 >= 5 && button < zeilen.size()) {
            zeilen.set(button2, text);
            Files.write(pfad, zeilen, StandardCharsets.UTF_8);
            System.out.println("Config aktualisiert");
        } else {
            System.out.println("Ups, da hat etwas nicht geklappt...");
        }
        System.out.println("Noch einen Button konfigurieren? (0=Nein, 1=Ja)");
        a = scan.nextInt();

    }
    System.out.println("= = =   =    = =  =     =  = = = ©");
    System.out.println("=    =  =  =      =     =    =  ");
    System.out.println("= = =   =  =      =     =    =  ");
    System.out.println("=       =    = =    = =      =  ");
    System.out.println("\n\nBis Bald!");

    try {
        // Pausiert den aktuellen Thread für 1 Sekunde
        TimeUnit.SECONDS.sleep(1);
    } catch (InterruptedException e) {
        // Behandlung der Ausnahme, falls der Schlaf unterbrochen wird
        Thread.currentThread().interrupt();
    }
}