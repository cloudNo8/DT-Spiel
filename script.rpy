## The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Guy Rosen")

image phishing: 
    "phishing-screenshot.jpg"
    zoom 0.6

image bg desk: 
    "bg desk.jpeg"
    zoom 3.2

image guy: 
    "guy avatar.png"
    zoom 1.6

image bg exercise2:
    "bg exercise2.jpeg"
    zoom 1.6

image gatter1:
    "Gatter1.png"

image gatter2:
    "Gatter2.png"

image gatter3:
    "Gatter3.png"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg desk

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show guy at right

    # These display lines of dialogue.

    e "Hallo und willkommen in meiner Welt der Cybersicherheit. Mein Name ist Guy Rosen und ich bin Chief Information Security Officer bei Meta."
    e "Meine Aufgaben sind die Überwachung der Sicherheitsmaßnahmen des Unternehmens, die Abwehr von Cyberbedrohungen und der Schutz von Nutzerdaten."
    e "Im Laufe eures Praktikums habt ihr bei meinen Kollegen schon einen kleinen Einblick in Netzwerksicherheit und die Entwicklung von Sicherheitsrichtlinien bekommen."
    e "Heute habe ich eine neue Aufgabe für euch. Kennt ihr die Autorin Julia Kuhn? Sie hat die Fantasy-Dilogie „Ravenhall Academy“ geschrieben und ihre Debütromane sind ein voller Erfolg."
    e "Demnach sind auch die Follower-Zahlen ihrer Profile abrupt gestiegen. Sie hat sich eben an uns gewendet, da ihr Profil gehackt wurde. Julia Kuhn hat uns gebeten sie dabei zu unterstützen,
    ihre Daten zurückzubekommen."
    e "Sie ist wohl auf eine Phishing-Direkt-Nachricht reingefallen. Einige ihrer Follower haben sie darauf aufmerksam gemacht, da diese von ihr komische Nachrichten mit Login-Links bekommen haben."
    e "Ich habe das Profil bereits vorläufig gesperrt, da auf diesem Weg die persönlichen Daten vieler Personen bereits an die Hacker gelangt sind."
    e "Bevor Frau Kuhn den Zugriff auf ihren Account vollkommen verloren hat, hat sie noch den vermutlichen Auslöser gefunden."

    show phishing at top
    e  "So sieht eine typische Phishing Nachricht aus."
    hide phishing

    e "Durch das Eingeben ihrer Login-Daten auf der Webseite, die sie über die URL erreichte, haben die Hacker den direkten Zugriff auf ihr Profil bekommen."
    e "Aber nun zu eurer Aufgabe: Bitte probiert die Daten zurück zu bekommen und den Hacker zu identifizieren. Weil das für mich eine eher alltägliche Aufgabe ist, möchte ich, dass ihr diese Herausforderung
    erst einmal weitgehend alleine angeht."
    e "Natürlich könnt ihr mich jederzeit um Hilfe bitten. Zusätzlich werde ich euch ab und zu über die Schulter schauen und euch Hinweise geben."
    e "Oh, moment. Eine kleine Frage noch, bevor ihr loslegt. Hast du breits etwas Erfahrung gesammelt im Thema Cycbersecurity?"

    menu: 
        "Ich habe bisher noch nicht so viel Erfahrung.":
            jump storyPart1
        "Ich würde mich eher als erfahrener einschätzen.":
            jump storyPart1Schwer
     

label storyPart1:
        e "Verstehe, keine Sorge. Jeder hat einmal angefangen. Ich stehe dir zur Seite und unterstütze dich, wenn du Hilfe brauchst. Gemeinsam werden wir das schon schaffen!"
        e "Zunächst müsst ihr diese Nachricht entschlüsseln, um dem Hacker einen Schritt näher zu kommen. Hierfür sollt ihr die ASCII-Codierung verwenden. Falls euch das nichts sagt, könnt ihr euch gerne einen Hinweis einholen."
        jump aufgabe_1
    
label storyPart1Schwer:
    scene bg desk with fade
    show guy at right
    e "Sehr gut, das wird die Sache sicherlich beschleunigen! Dennoch, auch die Besten brauchen manchmal eine zweite Meinung. Lass uns gemeinsam an die Arbeit gehen und den Fall lösen."
    e "Zunächst müsst ihr diese Nachricht entschlüsseln, um dem Hacker einen Schritt näher zu kommen. Hierfür sollt ihr die ASCII-Codierung verwenden. Falls euch das nichts sagt, könnt ihr euch gerne einen Hinweis einholen."
    jump aufgabe_1Schwer

    # menü einfügen

label storyPart2:
    scene bg desk with fade
    show guy at right
    e "Das habt ihr gut gemacht! Der erste Hinweis führt euch zu einer weiteren Sicherheitsbarriere, die der Hacker eingerichtet hat. Auf dem Bildschirm seht ihr ein Muster von Logikgattern."
    e "Diese hat der Hacker erstellt, um seine Spuren zu verwischen. Ihr müsst die richtige Kombination finden, um die Sicherheitsmaßnahme zu überwinden."

    jump aufgabe_2

label storyPart2Schwer:
    scene bg desk with fade
    show guy at right
    e "Das habt ihr gut gemacht! Der erste Hinweis führt euch zu einer weiteren Sicherheitsbarriere, die der Hacker eingerichtet hat. Auf dem Bildschirm seht ihr ein Muster von Logikgattern."
    e "Diese hat der Hacker erstellt, um seine Spuren zu verwischen. Ihr müsst die richtige Kombination finden, um die Sicherheitsmaßnahme zu überwinden."

    jump aufgabe_2Schwer

label storyPart3:
    scene bg desk with fade
    show guy at right
    e "Jetzt wisst ihr, wer der Hacker ist. Jetzt müsst ihr noch das Dokument mit den Anmeldedaten entschlüsseln. Für diesen weiteren Schritt müsst ihr die folgenden Binärzahlen in Dezimalzahlen umwandeln."

    jump aufgabe_3

label storyPart3Schwer:
    scene bg desk with fade
    show guy at right
    e "Jetzt wisst ihr, wer der Hacker ist. Jetzt müsst ihr noch das Dokument mit den Anmeldedaten entschlüsseln. Für diesen weiteren Schritt müsst ihr die folgenden Binärzahlen in Dezimalzahlen umwandeln."

    jump aufgabe_3Schwer

    # new Scene

label storyPart4:
    scene bg desk with fade
    show guy at right
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

    scene bg exercise2 with fade

    e "Wir haben den Namen des Hackers, aber er ist verschlüsselt. Die verschlüsselte Nachricht lautet: \n\nR8fIsyf/PuecXgTFMHhwePM="
    e "Hierbei handelt es sich um eine Art Verschlüsselung welche sich mit einem Passwort entschlüssen lässt."
    e "Wir müssen nur noch das Passwort herausfinden..."
    
    label passwortAufgabe:
    e "Das Passwort ist leider auch codiert: \n\n112 104 105 115 104 105 110 103"
    e "Zum Glück ist diese Art der Codierung recht einfach: Beim sogenannten Ascii Code ist jede Zahl einem Buchstaben zugewiesen."
    e "Die einzelen Zahlen lassen sich einfach in einer Tabelle ablesen."
    e "Zur Erinnerung: Der Code sieht so aus \n\n112 104 105 115 104 105 110 103"

    $ loesungC = renpy.input("Was ist das Passwort?")
    $ loesungC = loesungC.strip()

    if loesungC == "phishing":
        e "Perfekt, mit diesem Passwort können wir den Code entschlüsseln... Aah der Name des Hackers ist: \n\nBenedikt Dreher"
        e "Sehr gut, diese Information wird uns sehr von Nutzen sein!"
    else:
        e "Das war leider nicht das richtige Passwort, versuche es noch einmal."
        jump passwortAufgabe

    jump storyPart2

label aufgabe_1Schwer:
    scene bg exercise2 with fade

    e "Wir haben den Namen des Hackers, aber er ist verschlüsselt. Die verschlüsselte Nachricht lautet: \n\nR8fIsyf/PuecXgTFMHhwePM=" 
    e "Hierbei handelt es sich um eine Art Verschlüsselung welche sich mit einem Passwort entschlüssen lässt."
    e "Wir müssen nur noch das Passwort herausfinden..."

    label passwortAufgabeSchwer:
    e "Das Passwort ist leider auch codiert: \n\n83 101 99 117 114 101 33 95 80 97 115 115 119 48 114 100"
    e "Zum Glück ist diese Art der Codierung recht einfach: Beim sogenannten Ascii Code ist jede Zahl einem Buchstaben zugewiesen."
    e "Die einzelen Zahlen lassen sich einfach in einer Tabelle ablesen."
    e "Zur Erinnerung: Der Code sieht so aus \n\n83 101 99 117 114 101 33 95 80 97 115 115 119 48 114 100"

    $ loesungD = renpy.input("Was ist das Passwort?")
    $ loesungD = loesungD.strip()

    if loesungD == "Secure!_Passw0rd":
        e "Perfekt, mit diesem Passwort können wir den Code entschlüsseln... Aah der Name des Hackers ist: \n\nBenedikt Dreher"
        e "Sehr gut, diese Information wird uns sehr von Nutzen sein!"
        jump storyPart2Schwer
    else:
        e "Das war leider nicht das richtige Passwort, versuche es noch einmal."
        jump passwortAufgabeSchwer

    jump storyPart2a


label aufgabe_2:
    scene bg exercise2 with fade

    e "Logikgatter sind die grundlegenden Bausteine digitaler Schaltungen. Sie nehmen einen oder mehrere Eingänge (0 oder 1) und geben basierend auf einer bestimmten Regel einen Ausgang (0 oder 1) aus."
    #vll auch in Bildform, die dann im Hintergrund eingeblendet wird?

    label andGatter:

    e "Hier die erste Aufgabe:"
    e "Es geht um ein AND-Gatter. Ein AND-Gatter gibt nur dann eine 1 aus, wenn beide Eingänge 1 sind. Bestimme den die Ausgabe für die folgenden Eingänge: A=1, B=0 "

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
    e "Es geht um ein OR-Gatter. Das OR-Gatter gibt nur dann eine 1 aus, mindestens ein Eingang 1 ist. Hier die beiden Eingänge: A=0, B=1"

    #if Abfrage nach richtiger Lösung. Lösung: 1

    $ loesung2 = renpy.input("Was ist der Ausgang des OR-Gatters?")
    $ loesung2 = loesung2.strip()

    if loesung2 == "1":
        e "Das ist richtig. Gut gemacht!"
    else: 
        e "Das ist nicht ganz richtig. Versuchs noch einmal."
        jump orGatter

    label nandGatter:

    e "Die nächste Aufgabe handelt von einem NAND-Gatter:"
    e "Ein NAND-Gatter gibt eine 0 aus, wenn beide Eingänge 1 sind. Es ist das Gegenteil eines AND-Gatters. Die beiden Eingänge: A=1, B=1"

    #if Abfrage nach richtiger Lösung. Lösung: 0
    $ loesung3 = renpy.input("Was ist der Ausgang des NAND-Gatters?")
    $ loesung3 = loesung3.strip()

    if loesung3 == "0":
        e "Das ist richtig. Gut gemacht!"
    else:
        e "Das ist nicht ganz richtig. Versuchs noch einmal."
        jump nandGatter

    e "Das hast du super kombiniert bisher. Hier noch die letzte Aufgabe:"

    label norGatter:

    e "Es geht um ein NOR-Gatter, das Gegenteil eines OR-Gatters. Es gibt eine 1 aus, wenn beide Eingänge 0 sind."

    #if Abfrage nach richtiger Lösung. Lösung: 1

    $ loesung4 = renpy.input("Was ist der Ausgang des NOR-Gatters?")
    $ loesung4 = loesung4.strip()

    if loesung4 == "1":
        e "Das ist richtig. Gut gemacht!"
        jump storyPart3
    else: 
        e "Das ist nicht ganz richtig. Versuchs noch einmal."
        jump norGatter
    
    jump storyPart3

label aufgabe_2Schwer:
    #noch einfügen
    scene bg exercise2 with fade
    e "Logikgatter sind die grundlegenden Bausteine digitaler Schaltungen. Sie nehmen einen oder mehrere Eingänge (0 oder 1) und geben basierend auf einer bestimmten Regel einen Ausgang (0 oder 1) aus."
    #vll auch in Bildform, die dann im Hintergrund eingeblendet wird?

    label andOr:

    e "Hier die erste Aufgabe:"
    e "Es geht um eine Kombination aus einem UND und einem ODER-Gatter." 
    e "Ein AND-Gatter gibt nur dann eine 1 aus, wenn beide Eingänge 1 sind. Ein OR-Gatter gibt hingegen dann eine 1 aus, wenn nur mindestens ein Eingang 1 ist."

    show gatter1 at truecenter
    #if Abfrage nach richtiger Lösung. Lösung: 1
    $ loesung1s = renpy.input("Was ist der Ausgang des AND/OR-Gatters?")
    $ loesung1s = loesung1s.strip()

    if loesung1s == "1":
        e "Das ist richtig. Gut gemacht!"
    else: 
        e "Das ist nicht ganz richtig. Versuchs noch einmal"
        jump andOr
    hide gatter1

    label nandNor:

    e "Nun zur zweiten Aufgabe:"
    e "Es geht um ein NAND/NOR-Gatter. Das NAND-Gatter gibt nur dann eine 0 aus, wenn beide Eingänge 1 sind. Das NOR-Gatter gibt nur dann eine 1 aus, wenn beide Eingänge 0 sind."

    show gatter2 at truecenter
    #if Abfrage nach richtiger Lösung. Lösung: 1
    $ loesung2s = renpy.input("Was ist der Ausgang des NAND/NOR-Gatters?")
    $ loesung2s = loesung2s.strip()

    if loesung2s == "1":
        e "Das ist richtig. Gut gemacht!"
    else: 
        e "Das ist nicht ganz richtig. Versuchs noch einmal."
        jump nandNor
    hide gatter2
    
    label orAndNor:

    e "In der letzten Aufgabe geht es um ein kombiniertes OR/AND/NOR-Gatter."
    e "Gib mir Bescheid, wenn ich nochmal die einzelnen Gatter erkären soll."

    menu:
        "Erklär nochmal bitte.":
            e "Das OR-Gatter gibt nur dann eine 1 aus, mindestens ein Eingang 1 ist. Das AND-Gatter gibt wiederum nur dann eine 1 aus, wenn beide Eingänge 1 sind. "
            e "Und das NOR-Gatter gibt zuletzt nur dann eine 1 aus, wenn beide Eingänge 0 sind."
            jump orAndNorA
        "Ich bekomme das hin.":
            jump orAndNorA


    label orAndNorA:
    show gatter3 at truecenter
    #if Abfrage nach richtiger Lösung. Lösung: 0
    $ loesung3s = renpy.input("Was ist der Ausgang des OR/AND/NOR-Gatters?")
    $ loesung3s = loesung3s.strip()

    if loesung3s == "0":
        e "Das ist richtig. Gut gemacht!"
    else:
        e "Das ist nicht ganz richtig. Versuchs noch einmal."
        jump orAndNorA
    hide gatter3

    jump storyPart3Schwer
    


label aufgabe_3: 
    scene bg exercise2 with fade

    e "Eine Binärzahl besteht nur aus den Ziffern 0 und 1. Jede Stelle in der Binärzahl steht für eine bestimmte Zahl, basierend auf der Position von rechts nach links."
    e "So geht ihr vor: Schreibt euch die Binärzahl auf."
    e "Dann ordnet ihr jeder Stelle der Binärzahl eine Potenz von 2 zu, beginnend mit 2^0 von rechts nach links." 
    e "Multipliziert jede Binärziffer mit ihrem Wert. Und schließlich addiert alle diese Produkte zusammen, um die gesuchte Dezimalzahl zu erhalten."
    e "Gerne könnt ihr hier euer Notizbuch nutzen um euch die Arbeit zu vereinfachen."

    label binär_1: 
        e "Hier ist eure erste Aufgabe."

        #Abfrage nach richtiger Lösung. Lösung: 10
        $ loesung5 = renpy.input("Welche Dezimalzahl ergibt sich aus der Binärzahl 1010?")
        $ loesung5 = loesung5.strip()

        if loesung5 == "10":
            e "Ihr habt eure erste Herausforderung gut gemeistert! Hier ist eure nächste Aufgabe:" 
            jump binär_2
        else: 
            e "Das ist nicht ganz richtig. Versuchs noch einmal"
            jump binär_1

    label binär_2:

        #Abfrage nach richtiger Lösung. Lösung: 54
        $ loesung6 = renpy.input("Welche Dezimalzahl ergibt sich aus der Binärzahl 110110?")
        $ loesung6 = loesung6.strip()

        if loesung6 == "54":
            e "Super gemacht. Euch steht noch eine letzte Aufgabe bevor"
            jump binär_3
        else: 
            e "Hier stimmt was nicht. Versuchs noch einmal"
            jump binär_2

    label binär_3:

        #Abfrage nach richtiger Lösung. Lösung: 941
        $ loesung7 = renpy.input("Welche Dezimalzahl ergibt sich aus der Binärzahl 1110101101?")
        $ loesung7 = loesung7.strip()

        if loesung7 == "941":
            e "Klasse! Ich muss sagen, ich bin beeindruckt mit eurer Leistung."
            jump storyPart4
        else: 
            e "Das ist nicht ganz richtig. Versuchs noch einmal"
            jump binär_3

    jump storyPart4

label aufgabe_3Schwer:
    scene bg exercise2 with fade

    e "Eine Binärzahl besteht nur aus den Ziffern 0 und 1. Jede Stelle in der Binärzahl steht für eine bestimmte Zahl, basierend auf der Position von rechts nach links."
    e "So geht ihr vor: Schreibt euch die Binärzahl auf."
    e "Dann ordnet ihr jeder Stelle der Binärzahl eine Potenz von 2 zu, beginnend mit 2^0 von rechts nach links." 
    e "Multipliziert jede Binärziffer mit ihrem Wert. Und schließlich addiert alle diese Produkte zusammen, um die gesuchte Dezimalzahl zu erhalten."
    e "Gerne könnt ihr hier euer Notizbuch nutzen um euch die Arbeit zu vereinfachen."

    label binär_1s: 
        e "Hier ist eure erste Aufgabe."

        #Abfrage nach richtiger Lösung. Lösung: 203
        $ loesung5s = renpy.input("Welche Dezimalzahl ergibt sich aus der Binärzahl 11001011?")
        $ loesung5s = loesung5s.strip()

        if loesung5s == "203":
            e "Ihr habt eure erste Herausforderung gut gemeistert! Hier ist eure nächste Aufgabe:" 
            jump binär_2s
        else: 
            e "Das ist nicht ganz richtig. Versuchs noch einmal"
            jump binär_1s

    label binär_2s:

        #Abfrage nach richtiger Lösung. Lösung: 186
        $ loesung6s = renpy.input("Welche Dezimalzahl ergibt sich aus der Binärzahl 10111010?")
        $ loesung6s = loesung6s.strip()

        if loesung6s == "186":
            e "Super gemacht. Euch steht noch eine letzte Aufgabe bevor"
            jump binär_3s
        else: 
            e "Hier stimmt was nicht. Versuchs noch einmal"
            jump binär_2s

    label binär_3s:

        #Abfrage nach richtiger Lösung. Lösung: 237
        $ loesung7s = renpy.input("Welche Dezimalzahl ergibt sich aus der Binärzahl 11101101?")
        $ loesung7s = loesung7s.strip()

        if loesung7s == "237":
            e "Klasse! Ich muss sagen, ich bin beeindruckt mit eurer Leistung."
            jump storyPart4
        else: 
            e "Das ist nicht ganz richtig. Versuchs noch einmal"
            jump binär_3s
    jump storyPart4