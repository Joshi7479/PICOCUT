import javax.swing.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.concurrent.TimeUnit;
import java.io.IOException;
import java.io.BufferedWriter;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;


class Eingabefenster {
    public static void main(String[] args) throws IOException {
        try {
            UIManager.setLookAndFeel("com.sun.java.swing.plaf.gtk.GTKLookAndFeel");
        } catch (Exception e) {
            try {
                UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
            } catch (Exception ex) {
                ex.printStackTrace();
            }
        }
        String[] optionen = {"Deutsch", "English"};
        String sprache = (String) JOptionPane.showInputDialog(
                null,
                "Please select your language / Bitte wähle deine Sprache aus:",
                "Sprache/Language",
                JOptionPane.QUESTION_MESSAGE,
                null,
                optionen,
                optionen[0]
        );
        if (sprache == "Deutsch") {
            JOptionPane.showMessageDialog(null, "Sprache Deutsch gewählt!");

            JOptionPane.showMessageDialog(null, "Herzlich willkommen zum interaktiven Setup-Programm für PICOCUT!\nNach ein paar Fargen weisst du genau, welche Dateien du herunterladen musst\nund was du mit ihnen tuen musst!");

            String[] CPIops = {"Ja", "Nein"};
            String CPI = (String) JOptionPane.showInputDialog(
                    null,
                    "Hast du Circuitpython auf deinem Pi Pico installiert?",
                    "Circuitpython installiert?",
                    JOptionPane.QUESTION_MESSAGE,
                    null,
                    CPIops,
                    CPIops[0]);
            if (CPI == "Nein") {
                JOptionPane.showMessageDialog(null, "Dann gehe jetzt auf https://circuitpython.org/downloads und lade die Version für deinen Pi herunter.");
                JOptionPane.showMessageDialog(null, "Super, jetzt stecke deinen Raspberry Pi Pico aus und halte den Knopf gedrückt. \nStecke ihn während du den knopf gedrückt hältst wieder in deinen PC.\nDann die Datei einfach auf den Pi kopieren.");
                   JOptionPane.showMessageDialog(null, "Das wars schon, jetzt geht`s weiter.");
            }
            JOptionPane.showMessageDialog(null, "Gespeichert!");
            String[] UPorDOWNops = {"Nein", "Ja: Pull-Up Buttons", "Ja: Pull-Down Buttons"};
            String UPorDOWN = (String) JOptionPane.showInputDialog(
                    null,
                    "Weisst du, welchen Button Typ du hast?",
                    "Button-Typ",
                    JOptionPane.QUESTION_MESSAGE,
                    null,
                    UPorDOWNops,
                    UPorDOWNops[0]);
            if (UPorDOWN == "Nein") {
                JOptionPane.showMessageDialog(null, "Dann gehe jetzt zurück zu github und lade die Datei Test_DE.py \nund führe diese im Editor Thonny auf dem Python des Pi aus!");
                String[] UPorDOWNops2 = {"Pull-Up Buttons", "Pull-Down Buttons"};
                UPorDOWN = (String) JOptionPane.showInputDialog(
                        null,
                        "Jetzt weisst du, welchen Typ du hast!",
                        "Button-Typ",
                        JOptionPane.QUESTION_MESSAGE,
                        null,
                        UPorDOWNops2,
                        UPorDOWNops2[0]);



            }


            JOptionPane.showMessageDialog(null, "Gespeichert!");
            if (UPorDOWN == "Ja, Pull-Up Buttons") {
                JOptionPane.showMessageDialog(null, "Dann lade dir jetzt die Datei cody.py aus dem Ordner code_Pull-Up_DE von Github!");
            }

            if (UPorDOWN == "Pull-Up Buttons") {
                JOptionPane.showMessageDialog(null, "Dann lade dir jetzt die Datei cody.py aus dem Ordner code_Pull-Up_DE von Github!");
            }
            if (UPorDOWN == "Ja, Pull-Down Buttons") {
                JOptionPane.showMessageDialog(null, "Dann lade dir jetzt die Datei cody.py aus dem Ordner code_Pull-Down_DE von Github!");
            }

            if (UPorDOWN == "Pull-Down Buttons") {
                JOptionPane.showMessageDialog(null, "Dann lade dir jetzt die Datei cody.py aus dem Ordner code_Pull-Down_DE von Github!");
            }
            JOptionPane.showMessageDialog(null, "Außerdem brauchst du das Bundle für deine Circuitpython-Version von: https://circuitpython.org/libraries. Darin findest du im ordner Lib den Ordner adafruit_hid. Kopiere diesen in den Lib Ordner\nauf dem Pi. Zusätzlich benötigst du noch die Dateien keyboard_layout_win_de.mpy und keycode_win_de aus dem Repo: keyboard_layout_win_de.mpy. Lege diese auch in den Ordner lib.");
            JOptionPane.showMessageDialog(null, "Fertig?");
            JOptionPane.showMessageDialog(null, "Kopiere jetzt code.py auf den Pi Pico!");
            int a = 1;
            var scan = new Scanner(System.in);
            Path newconfig = Paths.get("config.txt");
            try (BufferedWriter writer = Files.newBufferedWriter(newconfig)) {
                for (int i = 0; i < 30; i++) {
                    writer.newLine();
                }
                System.out.println("\nConfig was generated successfully!.");
            } catch (IOException e) {
                System.out.println("\nSomething went wrong: " + e.getMessage());
            }
            while (a == 1) {
                Path pfad = Path.of("config.txt");
                List<String> zeilen = Files.readAllLines(pfad, StandardCharsets.UTF_8);


                String eingabe = JOptionPane.showInputDialog(null, "Welcher Knopf soll etwas tuen? (Bitte die GP Nummer eingeben) (Hier gibt es den Pin-Belegungs-Planhttps://www.elektronik-kompendium.de/sites/raspberry-pi/2611051.htm)\nNur die Pins 1 - 22 auf jedem Pi Pico werden unterstüzt.)\n");
                int button = Integer.parseInt(eingabe);
                if (button > 22) {
                    System.exit(5);
                }
                if (button < 1) {
                    System.exit(5);
                }
                int button2 = button + 5;
                String text = JOptionPane.showInputDialog(null, "\nWas soll der Knopf tuen?\n");

                if (button2 >= 5 && button < zeilen.size()) {
                    zeilen.set(button2, text);
                    Files.write(pfad, zeilen, StandardCharsets.UTF_8);
                    JOptionPane.showMessageDialog(null, "\nConfig wurde erstellt!\n");
                } else {
                    JOptionPane.showMessageDialog(null,"Ups, da hat etwas nicht geklappt!");
                }
                String[] Weiterops = {"Ja", "Nein"};
                String Weiter = (String) JOptionPane.showInputDialog(
                        null,
                        "Noch einen Knopf konfigurieren?",
                        "Weiter konfigurieren?",
                        JOptionPane.QUESTION_MESSAGE,
                        null,
                        Weiterops,
                        Weiterops[0]);
                if (Weiter == "Nein") {
                    a = 0;
                }

            }
            JOptionPane.showMessageDialog(null, "Jetzt kannst du die frisch erstellte config.txt aus diesem Ordner auf den Pi kopieren!");
            JOptionPane.showMessageDialog(null, "Jetzt ist alles Fertig! Pi ausstecken, wieder einstecken und testen!\n\nProbleme? Schicke mir eine Mail an Joshi7479@proton.me");




        }

        if (sprache == "English") {

            JOptionPane.showMessageDialog(null, "Setup started in English");

            JOptionPane.showMessageDialog(null, "Welcome to this interactive Setup-script for PICOCUT!\nOnly a few questions and you know, which Files you need\nand what you have to do with them!");

            String[] CPIops = {"Yes", "No"};
            String CPI = (String) JOptionPane.showInputDialog(
                    null,
                    "Do you have Circuitpython installed on your Pi?",
                    "Circuitpython installed?",
                    JOptionPane.QUESTION_MESSAGE,
                    null,
                    CPIops,
                    CPIops[0]);
            if (CPI == "No") {
                JOptionPane.showMessageDialog(null, "Then go now on https://circuitpython.org/downloads and download the Version for you´re Pi.");
                JOptionPane.showMessageDialog(null, "Great, now plug out the cable to the Pi.\nOn the Pi is a button. Keep it pressed while you plug the cable in!.\nThen just copy the file onto the Pi.");
                JOptionPane.showMessageDialog(null, "No, the Pi is ready!.");
            }
            JOptionPane.showMessageDialog(null, "Saved!");
            String[] UPorDOWNops = {"No", "Yes: Pull-Up Buttons", "Yes: Pull-Down Buttons"};
            String UPorDOWN = (String) JOptionPane.showInputDialog(
                    null,
                    "Do you know, which Type of Buttons you have?",
                    "Button-Type",
                    JOptionPane.QUESTION_MESSAGE,
                    null,
                    UPorDOWNops,
                    UPorDOWNops[0]);
            if (UPorDOWN == "No") {
                JOptionPane.showMessageDialog(null, "Then go now back to Github and download the file Test_EN.py \nand execute it in the Editor Thonny with the Python of the Pi!");
                String[] UPorDOWNops2 = {"Pull-Up Buttons", "Pull-Down Buttons"};
                UPorDOWN = (String) JOptionPane.showInputDialog(
                        null,
                        "Now you know, which Type of Button you have!",
                        "Button-Type",
                        JOptionPane.QUESTION_MESSAGE,
                        null,
                        UPorDOWNops2,
                        UPorDOWNops2[0]);


            }


            JOptionPane.showMessageDialog(null, "Saved!");
            if (UPorDOWN == "Yes, Pull-Up Buttons") {
                JOptionPane.showMessageDialog(null, "Now download code_Pull-Up_EN in the folder code_Pull-Up_EN from Github!");
            }

            if (UPorDOWN == "Pull-Up Buttons") {
                JOptionPane.showMessageDialog(null, "Now download code_Pull-Up_EN in the folder code_Pull-Up_EN from Github!");
            }
            if (UPorDOWN == "Ja, Pull-Down Buttons") {
                JOptionPane.showMessageDialog(null, "Now download code_Pull-Down_EN in the folder code_Pull-Down_EN from Github!");
            }

            if (UPorDOWN == "Pull-Down Buttons") {
                JOptionPane.showMessageDialog(null, "Now download code_Pull-Down_EN in the folder code_Pull-Down_DE von Github!");
            }
            JOptionPane.showMessageDialog(null, "Also you need the Bundle for you´re Circuitpython-Version from: https://circuitpython.org/libraries. In it, there is the folder adafruit_hid. copy this folder in the lib folder\non the Pi.");
            JOptionPane.showMessageDialog(null, "Ready?");
            JOptionPane.showMessageDialog(null, "Now you can copy code.py onto the Pi!");
            int a = 1;
            var scan = new Scanner(System.in);
            while (a == 1) {
                Path pfad = Path.of("config.txt");
                List<String> zeilen2 = Files.readAllLines(pfad, StandardCharsets.UTF_8);


                String input = JOptionPane.showInputDialog(null, "Which Button do you want to configure? (Please type in the GP Number. Only the Pins from 1 - 22 on any Pi Pico are supported!)\nPinouts: https://www.elektronik-kompendium.de/sites/raspberry-pi/2611051.htm)\n");
                int button3 = Integer.parseInt(input);
                if (button3 > 22) {
                    System.exit(5);
                }
                if (button3 < 1) {
                    System.exit(5);
                }
                int button2 = button3 + 5;
                String text = JOptionPane.showInputDialog(null, "And what should the button do / type?");

                if (button2 >= 5 && button3 < zeilen2.size()) {
                    zeilen2.set(button2, text);
                    Files.write(pfad, zeilen2, StandardCharsets.UTF_8);
                    JOptionPane.showMessageDialog(null, "\nConfig was generated successfully!!\n");
                } else {
                    JOptionPane.showMessageDialog(null, "Sorry, something went wrong!");
                }
                String[] Weiterops2 = {"Yes", "No"};
                String Weiter2 = (String) JOptionPane.showInputDialog(
                        null,
                        "Configure another button?",
                        "",
                        JOptionPane.QUESTION_MESSAGE,
                        null,
                        Weiterops2,
                        Weiterops2[0]);
                if (Weiter2 == "No") {
                    a = 0;
                }
            }
            JOptionPane.showMessageDialog(null, "Jetzt kannst du die frisch erstellte config.txt aus diesem Ordner auf den Pi kopieren!\nNow you can copy the config.txt onto the Pi!");
            JOptionPane.showMessageDialog(null, "Jetzt ist alles Fertig! Pi ausstecken, wieder einstecken und testen!\n\nProbleme? Schicke mir eine Mail an Joshi7479@proton.me\nNow everything is ready! Just reconnect the Pi!\n\nAny problems? Contact me: Joshi7479@proton.me");
        }
    }
}
