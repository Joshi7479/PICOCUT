import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Scanner;

void main() throws IOException {
    int a = 1;
    boolean ok = a == 1;
    while (ok) {
        Path pfad = Path.of("config.txt");
        List<String> zeilen = Files.readAllLines(pfad, StandardCharsets.UTF_8);
        var scan = new Scanner(System.in);

        System.out.println("Welcher Knopf soll etwas tuen?");
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
}
