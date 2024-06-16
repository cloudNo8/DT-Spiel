# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Guy Rosen")


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

    e "Hallo und willkommen in meiner Welt der Cybersicherheit. Mein Name ist Guy Rosen und ich bin Chief Information Security Officer bei Meta."

    e "Meine Aufgaben sind die Überwachung der Sicherheitsmaßnahmen des Unternehmens, die Abwehr von Cyberbedrohungen und der Schutz von Nutzerdaten."

    e "Im Laufe eures Praktikums habt ihr bei meinen Kollegen schon einen kleinen Einblick in Netzwerksicherheit und die Entwicklung von Sicherheitsrichtlinien bekommen."

    e "Heute habe ich eine neue Aufgabe für euch. Kennt ihr die Autorin Julia Kuhn? Sie hat die Fantasy-Dilogie „Ravenhall Academy“ geschrieben und ihre Debütromane sind ein voller Erfolg."

    e "Demnach sind auch die Follower-Zahlen ihrer Profile abrupt gestiegen. Sie hat sich eben an uns gewendet, da ihr Profil gehackt wurde. Julia Kuhn hat uns gebeten sie dabei zu unterstützen,
    ihre Daten zurückzubekommen."

    e "Sie ist wohl auf eine Phishing-Direkt-Nachricht reingefallen. Einige ihrer Follower haben sie darauf aufmerksam gemacht, da diese von ihr komische Nachrichten mit Login-Links bekommen haben."

    e "Ich habe das Profil bereits vorläufig gesperrt, da auf diesem Weg die persönlichen Daten vieler Personen bereits an die Hacker gelangt sind."

    e "Bevor Frau Kuhn den Zugriff auf ihren Account vollkommen verloren hat, hat sie noch den vermutlichen Auslöser gefunden. So sieht eine typische Phishing Nachricht aus."

    e "Durch das Eingeben ihrer Login-Daten auf der Webseite, die sie über die URL erreichte, haben die Hacker den direkten Zugriff auf ihr Profil bekommen."

    e "Aber nun zu eurer Aufgabe: Bitte probiert die Daten zurück zu bekommen und den Hacker zu identifizieren. Weil das für mich eine alltägliche Aufgabe ist, möchte ich, dass ihr diese Herausforderung
    erstmal weitgehend alleine angeht."

    e "Natürlich könnt ihr mich jederzeit um Hilfe bitten. Zusätzlich werde ich euch ab und zu über die Schulter schauen und euch Hinweise geben. Also frohes Schaffen und unterstützt euch bitte gegenseitig!"

    # new Scene

    e "Zunächst müsst ihr diese Nachricht entziffern, um dem Hacker einen Schritt näher zu kommen. Hierfür könnt ihr die ??-Methode anwenden. Falls euch das nichts sagt, könnt ihr euch gerne einen Hinweis einholen."

    # new Scene

    e "Das habt ihr gut gemacht! Der erste Hinweis führt euch zu einer weiteren Sicherheitsbarriere, die der Hacker eingerichtet hat. Auf dem Bildschirm seht ihr ein Muster von Logikgattern."

    e "Diese hat der Hacker erstellt, um seine Spuren zu verwischen. Ihr müsst die richtige Kombination finden, um die Sicherheitsmaßnahme zu überwinden."

    # new Scene

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
