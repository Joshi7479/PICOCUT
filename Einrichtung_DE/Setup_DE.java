import java.io.IOException;
import java.io.BufferedWriter;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

void main() throws IOException {
    System.out.println("\n\n");
    System.out.println("= = =   =    = =  =     =  = = = ©");
    System.out.println("=    =  =  =      =     =    =  ");
    System.out.println("= = =   =  =      =     =    =  ");
    System.out.println("=       =    = =    = =      =  ");
    var scan = new Scanner(System.in);
    try {
        TimeUnit.SECONDS.sleep(1);
    } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
    }
    System.out.println("\n\nWillkommen zum PICUT©-Setup!\n\n");
    System.out.println("ACHTUNG! Diese Software unterstüzt NUR die Raspberry Pi Pico Familie!\n\n");

    try {
        TimeUnit.SECONDS.sleep(1);
    } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
    }
    int a = 1;
    System.out.println("Du hast noch keine Config Datei? Soll eine automatisch erstellt werden? (0=Nein, 1 =Ja)\n");
    var b = scan.nextInt();
    if (b == 1) {
        File config = new File("config.txt");

        Path newconfig = Paths.get("config.txt");
        try (BufferedWriter writer = Files.newBufferedWriter(newconfig)) {
            for (int i = 0; i < 30; i++) {
                writer.newLine();
            }
            System.out.println("\nConfig wurde automatisch generiert!");
        } catch (IOException e) {
            System.out.println("\nEin Fehler ist aufgetreten: " + e.getMessage());
        }
    }
    while (a == 1) {
        Path pfad = Path.of("config.txt");
        List<String> zeilen = Files.readAllLines(pfad, StandardCharsets.UTF_8);


        System.out.println("\nWelcher Knopf soll etwas tuen? (Bitte die GP Nummer eingeben) (Hier gibt es den Pin-Belegungs-Planhttps://www.elektronik-kompendium.de/sites/raspberry-pi/2611051.htm)\nNur die Pins 1 - 22 auf jedem Pi Pico werden unterstüzt.)");
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
        System.out.println("\nWas soll der Knopf tuen?\n");
        var text = scan.nextLine();

        if (button2 >= 5 && button < zeilen.size()) {
            zeilen.set(button2, text);
            Files.write(pfad, zeilen, StandardCharsets.UTF_8);
            System.out.println("\nConfig aktualisiert\n\n");
        } else {
            System.out.println("Ups, da hat etwas nicht geklappt...");
        }
        System.out.println("Noch einen Button konfigurieren? (0=Nein, 1=Ja)\n");
        a = scan.nextInt();

    }
    System.out.println("\nJetzt kannst du die config.txt auf deinen Pi kopieren.\n\n");
    try {
        TimeUnit.SECONDS.sleep(1);
    } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
    }
    System.out.println("= = =   =    = =  =     =  = = = ©");
    System.out.println("=    =  =  =      =     =    =  ");
    System.out.println("= = =   =  =      =     =    =  ");
    System.out.println("=       =    = =    = =      =  ");
    System.out.println("Made by Joshi7479");
    System.out.println("Support this Project on Github: https://github.com/Joshi7479/PICUT");
    System.out.println("\n\nBis Bald!");

    try {
        TimeUnit.SECONDS.sleep(1);
    } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
    }
}
