# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Guy Rosen")

init:
    image phishing = "phishing-screenshot.jpg"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Guy Rosen happy

    # These display lines of dialogue.

    e "Dies ist eine Änderung."

    e "Hallo und willkommen in meiner Welt der Cybersicherheit. Mein Name ist Guy Rosen und ich bin Chief Information Security Officer bei Meta."

    e "Meine Aufgaben sind die Überwachung der Sicherheitsmaßnahmen des Unternehmens, die Abwehr von Cyberbedrohungen und der Schutz von Nutzerdaten."

    e "Im Laufe eures Praktikums habt ihr bei meinen Kollegen schon einen kleinen Einblick in Netzwerksicherheit und die Entwicklung von Sicherheitsrichtlinien bekommen."

    e "Heute habe ich eine neue Aufgabe für euch. Kennt ihr die Autorin Julia Kuhn? Sie hat die Fantasy-Dilogie „Ravenhall Academy“ geschrieben und ihre Debütromane sind ein voller Erfolg."

    e "Demnach sind auch die Follower-Zahlen ihrer Profile abrupt gestiegen. Sie hat sich eben an uns gewendet, da ihr Profil gehackt wurde. Julia Kuhn hat uns gebeten sie dabei zu unterstützen,
    ihre Daten zurückzubekommen."

    e "Sie ist wohl auf eine Phishing-Direkt-Nachricht reingefallen. Einige ihrer Follower haben sie darauf aufmerksam gemacht, da diese von ihr komische Nachrichten mit Login-Links bekommen haben."

    e "Ich habe das Profil bereits vorläufig gesperrt, da auf diesem Weg die persönlichen Daten vieler Personen bereits an die Hacker gelangt sind."

    e "Bevor Frau Kuhn den Zugriff auf ihren Account vollkommen verloren hat, hat sie noch den vermutlichen Auslöser gefunden."

    show phishing
    e  "So sieht eine typische Phishing Nachricht aus."
    hide phishing

    e "Durch das Eingeben ihrer Login-Daten auf der Webseite, die sie über die URL erreichte, haben die Hacker den direkten Zugriff auf ihr Profil bekommen."

    e "Aber nun zu eurer Aufgabe: Bitte probiert die Daten zurück zu bekommen und den Hacker zu identifizieren. Weil das für mich eine alltägliche Aufgabe ist, möchte ich, dass ihr diese Herausforderung
    erstmal weitgehend alleine angeht."

    e "Natürlich könnt ihr mich jederzeit um Hilfe bitten. Zusätzlich werde ich euch ab und zu über die Schulter schauen und euch Hinweise geben. Also frohes Schaffen und unterstützt euch bitte gegenseitig!"

    # new Scene

    e "Zunächst müsst ihr diese Nachricht entziffern, um dem Hacker einen Schritt näher zu kommen. Hierfür könnt ihr die ??-Methode anwenden. Falls euch das nichts sagt, könnt ihr euch gerne einen Hinweis einholen."

    menu: 
        "Bitte gib mir einen Hinweis zur Aufgabe.":
            e "placeholder für Aufgabe 1"
            jump aufgabe_1
        "Ich möchte direkt mit der Aufgabe starten":
            jump aufgabe_1


    # new Scene

    # menü einfügen

    e "Das habt ihr gut gemacht! Der erste Hinweis führt euch zu einer weiteren Sicherheitsbarriere, die der Hacker eingerichtet hat. Auf dem Bildschirm seht ihr ein Muster von Logikgattern."

    e "Diese hat der Hacker erstellt, um seine Spuren zu verwischen. Ihr müsst die richtige Kombination finden, um die Sicherheitsmaßnahme zu überwinden."

    # new Scene

    menu: 
        "Erklär mir noch einmal, wie man vorgehen muss":
            e "placeholder für Erklärung von Aufgabe 2"
        "Lass mich direkt loslegen":
            jump aufgabe_2

    e "Jetzt wisst ihr, wer der Hacker ist. Jetzt müsst ihr noch das Dokument mit den Anmeldedaten entschlüsseln. Für diesen weiteren Schritt müsst ihr die folgenden Binärzahlen in Dezimalzahlen umwandeln."

    # new Scene
    e "Durch eure gute Zusammenarbeit, habt ihr nun den Hacker gefunden und die Daten gerettet. Das war eine solide Leistung! Ich denke, dass euch dieser Auftrag einen guten Einblick in meinen Beruf gegeben hat. 
    Hoffentlich hattet ihr Spaß dabei."

    e "Phishing-Nachrichten sind nicht selten und jedem kann so etwas mal passieren, aber denkt bitte daran jegliche Nachrichten und URLs zu überprüfen. 
    Durch eine Zwei-Faktor-Authentifizierung und sichere Passwörter macht ihr es den Hackern deutlich schwerer."

    e "Aufgrund dessen werde ich allen Profilen, die auf den Hackerangriff reingefallen sind eine Mail mit den eben genannten Schutzmaßnahmen zukommen lassen."

    e "Das haben viele Personen mit kleineren Profilen oft gar nicht auf dem Schirm und so wie es scheint hat sich Julia Kuhn bis jetzt auch noch nicht ausreichend damit beschäftigt."

    e "Ich hoffe ihr habt heute einiges gelernt. Nicht nur über Cybersecurity, sondern auch für euren Alltag. Für heute möchte ich euch nun entlassen, gut gemacht!"

    e "Bis bald und noch viel Spaß bei eurem Praktikum, wir laufen uns sicher noch einmal über den Weg."

    # This ends the game.

    return

label aufgabe_1:

    #new scene 
    show Guy Rosen happy

    e "Dies ist Aufgabe 1."

    # if Abfrage noch einfügen, und notfalls sowas wie "schade, versuchs noch einmal"

label aufgabe_2:
    #new scene
    show Guy Rosen happy

    e "Dies ist Aufgabe 2."

    e "Logikgatter sind die grundlegenden Bausteine digitaler Schaltungen. Sie nehmen einen oder mehrere Eingänge (0 oder 1) und geben basierend auf einer bestimmten Regel einen Ausgang (0 oder 1) aus."
    e "Hier sind einige grundlegende Logikgatter:"
    e "AND-Gatter: gibt 1 aus, wenn beide Eingänge 1 sind."
    e "OR-Gatter: gibt 1 aus, wenn mindestens einer der Eingänge 1 sind."
    e "NAND-Gatter: gibt 1 aus, wenn mindestens einer der Eingänge 0 ist. Es ist das Gegenteil eines AND-Gatters."
    e "NOR-Gatter: gibt 1 aus, wenn beide Eingänge 0 sind. Es ist das Gegenteil eines OR-Gatters."
    #vll auch in Bildform, die dann im Hintergrund eingeblendet wird?

    label andGatter:

    e "Hier die erste Aufgabe:"

    e "Es geht um ein AND-Gatter. Die Eingänge: A=0, B=1. Ein AND-Gatter gibt nur dann eine 1 aus, wenn beide Eingänge 1 sind."

    #if Abfrage nach richtiger Lösung. Lösung: 0
    $ loesung1 = renpy.input("Was ist der Ausgang des AND-Gatters?")
    $ loesung1 = loesung1.strip()

    if loesung1 == "0":
        e "Das ist richtig. Gut gemacht!"
    else: 
        e "Das ist nicht ganz richtig. Versuchs noch einmal"
        jump andGatter

    label orGatter:

    e "Nun zur zweiten Aufgabe:"

    e "Nun sind die Eingänge A=1 und B=1. Ein OR-Gatter gibt eine 1 aus, wenn mindestens einer der Eingänge 1 ist."

    #if Abfrage nach richtiger Lösung. Lösung: 1

    $ loesung2 = renpy.input("Was ist der Ausgang des OR-Gatters?")
    $ loesung2 = loesung2.strip()

    if loesung2 == "1":
        e "Das ist richtig. Gut gemacht!"
    else: 
        e "Das ist nicht ganz richtig. Versuchs noch einmal."
        jump orGatter

    label nandGatter:

    e "Hier noch eine weitere Aufgabe:"

    e "Diesmal sind die Eingänge A=1 und B=0. Ein NAND-Gatter gibt eine 1 aus, wenn mindestens einer der Eingänge 0 ist. Es ist das Gegenteil eines AND-Gatters."

    #if Abfrage nach richtiger Lösung. Lösung: 1
    $ loesung3 = renpy.input("Was ist der Ausgang des NAND-Gatters?")
    $ loesung3 = loesung3.strip()

    if loesung3 == "1":
        e "Das ist richtig. Gut gemacht!"
    else:
        e "Das ist nicht ganz richtig. Versuchs noch einmal."
        jump nandGatter

    e "Das hast du super kombiniert bisher. Hier noch die letzte Aufgabe:"

    label norGatter:

    e "Nun geht es um ein NOR-Gatter. Eingänge A=0 und B=0. Ein NOR-Gatter gibt eine 1 aus, wenn beide Eingänge 0 sind. Es ist das Gegenteil eines OR-Gatters."

    #if Abfrage nach richtiger Lösung. Lösung: 1

    $ loesung4 = renpy.input("Was ist der Ausgang des NOR-Gatters?")
    $ loesung4 = loesung4.strip()

    if loesung4 == "1":
        e "Das ist richtig. Gut gemacht!"
    else: 
        e "Das ist nicht ganz richtig. Versuchs noch einmal."
        jump norGatter

