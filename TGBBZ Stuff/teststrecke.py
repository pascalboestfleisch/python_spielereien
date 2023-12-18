"""
+---------------------------------------+
|              Teststrecke              |
+---------------------------------------+
| -_fahrzeug_position_transrapid: int   |
| -_fahrzeug_position_werkzeugwagen: int|
| -_fahrbahnStatus: int                 |
| -_garage: int                         |
| -_weiche: int                         |
| -_strecke: List[int]                  |
| -_transrapid: int                     |
| -_werkzeugwagen: int                  |
| -_strecken_radius: int                |
| -_transrapid_marker: int              |
| -_werkzeugwagen_marker: int           |
| -_x_werkzeugwagen: int                |
| -_y_werkzeugwagen: int                |
| -_x_transrapid: int                   |
| -_y_transrapid: int                   |
| -num_frames: int                      |
| -interval: int                        |
+---------------------------------------+
| +__init__()                           |
| +__del__()                            |
| +getTransrapid(): int                 |
| +getWerkzeugwagen(): int              |
| +getStatus(): int                     |
| +getWeiche(): int                     |
| +validiereStart(): bool               |
| +getPositionTransrapid(): int         |
| +getPositionWerkzeugwagen(): int      |
| +starteTransrapid()                   |
| +starteWerkzeugwagen()                |
| +ausfahrtTransrapid()                 |
| +ausfahrtWerkzeugwagen()              |
| +betreibenStrecke()                   |
| +getKoordinaten(winkel, radius): int, int]|
| +update(frame)                        |
| +visualize()                          |
+---------------------------------------+
"""

"""
Warum sind Kapselung und Data Hiding in diesem Beispiel wichtig:

    - vor unerwünschten Zugriffen schützen, hier besonders wichtig, da nur ein Fahrzeug auf der Fahrbahn sein kann
    - verbesserte Sicherheit, sprich, dass selbst öffentliche Methoden nicht ohne Überprüfung ausgeführt werden
    - da nur gewünschte Methoden öffentlich sind und die Attribute weiterhin privat bleiben, Schutz vor Änderungen
    - eventuelle Fehlverhalten werden verhindert
    - bessere Gewährleistung zum Schutz sensibler Daten (Position der Fahrzeuge z.B.)
"""


import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import numpy as np


class Teststrecke:
    # Konstruktor
    def __init__(self):
        self._fahrzeug_position_transrapid: int = 0  # Position Transrapid
        self._fahrzeug_position_werkzeugwagen: int = 0  # Position Werkzeugwagen
        self._fahrbahnStatus: int = 0  # Fahrbahn frei, wenn 0
        self._garage: int = -1  # Position der Garage
        self._weiche: int = 0  # Weiche wurde nicht ausgerichtet (0)

        # Laenge der Strecke als Liste von 0 bis 10
        self._strecke = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self._transrapid: int = 0  # Ist Transrapid angeschalten? 0 -> nein
        self._werkzeugwagen: int = 0  # Ist Werkzeugwagen angeschalten? 0 -> nein

        # Radius der Strecke bzw. des Kreises (Kreis ist die Groesse der Strecke)
        self._strecken_radius: int = 5
        self._transrapid_marker: int = 0
        self._werkzeugwagen_marker: int = 0
        self._x_werkzeugwagen: int = 0  # X-Koordinate von Werkzeugwagen
        self._y_werkzeugwagen: int = 0  # Y-Koordinate von Werkzeugwagen
        self._x_transrapid: int = 0  # X-Koordinate von Transrapid
        self._y_transrapid: int = 0  # Y-Koordinate von Transrapid
        self.num_frames: int = 100  # Nummer der Frames
        self.interval: int = 250  # Groesse des Intervalls in Millisekunden

    # Destruktor
    def __del__(self):
        print("Teststrecke zerstört")

    def getTransrapid(self):
        return self._transrapid

    def getWerkzeugwagen(self):
        return self._werkzeugwagen

    def getStatus(self):
        return self._fahrbahnStatus

    def getWeiche(self):
        return self._weiche

    def getAusfahrtTransrapid(self):
        return self._ausfahrenTransrapid

    def getAusfahrtWerkzeugwagen(self):
        return self._ausfahrenWerkzeugwagen

    # Ueberpruefung, ob Fahrbahn frei ist und ob bereits ein Fahrzeug gestartet wurde
    def validiereStart(self):
        if self.getStatus() == 1:
            if self.getTransrapid() == 1 or self.getWerkzeugwagen() == 1:
                raise Exception(
                    "Es befindet sich bereits ein Fahrzeug auf der Strecke, bitte warten Sie und stellen Sie das Fahrzeug ab!"
                )
        return True

    # Ermittlung Position Transrapid
    def getPositionTransrapid(self):
        if self._transrapid == 0:
            self._fahrzeug_position_transrapid = self._garage
            print(
                "Der Transrapid befindet sich in der Garage, Position: ",
                self._fahrzeug_position_transrapid,
            )
        else:
            print(self._fahrzeug_position_transrapid)
            if self._fahrzeug_position_transrapid is not None:
                return self._strecke[self._fahrzeug_position_transrapid]
        return 0  # Wenn Position nicht gesetzt, default ausgeben

    # Ermittlung Position Werkzeugwagen
    def getPositionWerkzeugwagen(self):
        if self._werkzeugwagen == 0:
            self._fahrzeug_position_werkzeugwagen = self._garage
            print(
                "Der Werkzeugwagen befindet sich in der Garage, Position: ",
                self._fahrzeug_position_werkzeugwagen,
            )
        else:
            print(self._fahrzeug_position_werkzeugwagen)
            if self._fahrzeug_position_werkzeugwagen is not None:
                return self._strecke[self._fahrzeug_position_werkzeugwagen]
        return 0  # Wenn Position nicht gesetzt, default ausgeben

    # Transrapid starten
    def starteTransrapid(self):
        if self.getTransrapid() == 0:
            if self.validiereStart():
                self._fahrzeug_position_transrapid = self._garage
                self._transrapid = 1
                print(
                    "Transrapid ist gestartet und befindet sich noch in der Garage",
                    self._garage,
                )
        else:
            print("Der Transrapid wurde bereits gestartet")

    # Werkzeugwagen starten
    def starteWerkzeugwagen(self):
        if self.getWerkzeugwagen() == 0:
            if self.validiereStart():
                self._fahrzeug_position_werkzeugwagen = self._garage
                self._werkzeugwagen = 1
                print("Werkzeugwagen ist gestartet")
        else:
            print("Der Werkzeugwagen wurde bereits gestartet")

    # Weiche wird auf "Ausfahrt" gestellt, Transrapid fährt auf Strecke
    def ausfahrtTransrapid(self):
        if self.validiereStart():
            if self.getTransrapid() == 1:
                if self.getWeiche() == 0:
                    self._weiche = 1
                    self._fahrbahnStatus = 1

    # Weiche wird auf "Ausfahrt" gestellt, Werkzeugwagen fährt auf Strecke
    def ausfahrtWerkzeugwagen(self):
        if self.validiereStart():
            if self.getWerkzeugwagen() == 1:
                if self.getWeiche() == 0:
                    self._weiche = 1
                    self._fahrbahnStatus = 1

    # Fahrzeuge fahren Strecke, Berechnung Länge der Strecke -1, in Schleife wird Position stetig berechnet, Position um 1 erhöht
    def betreibenStrecke(self):
        for _ in range(len(self._strecke) - 1):
            if self.getTransrapid() == 1:
                self._fahrzeug_position_transrapid = (
                    self._fahrzeug_position_transrapid + 1
                ) % len(self._strecke)
                print(
                    "befindet sich an Position: ",
                    self._strecke[self._fahrzeug_position_transrapid],
                )

            elif self.getWerkzeugwagen() == 1:
                self._fahrzeug_position_werkzeugwagen = (
                    self._fahrzeug_position_werkzeugwagen + 1
                ) % len(self._strecke)
                print(
                    "befindet sich an Position: ",
                    self._strecke[self._fahrzeug_position_werkzeugwagen],
                )

    # Koordinaten zur weiteren Berechnung für Marker der Visualisierung im Kreis
    def getKoordinaten(self, winkel, _strecken_radius):
        if winkel is None:
            return (
                0,
                0,
            )  # Wenn es keine Angaben zum Winkel bzw. der Position gibt, wird Marker an die Stelle 0,0 in der Visualisierung gesetzt
        x = _strecken_radius * np.cos(np.radians(winkel))
        y = _strecken_radius * np.sin(np.radians(winkel))
        return x, y

    # Aktualisiert stetig die Visualisierung um Änderungen anzuzeigen
    def update(self, frame):
        self.betreibenStrecke()
        transrapid_pos = self.getPositionTransrapid()
        werkzeugwagen_pos = self.getPositionWerkzeugwagen()

        # Berechnung des Winkels anhand der Position von Transrapid/Werkzeugwagen
        transrapid_winkel = (transrapid_pos / len(self._strecke)) * 360
        werkzeugwagen_winkel = (werkzeugwagen_pos / len(self._strecke)) * 360

        # Die Koordinaten von Transrapid und Werkzeugwagen berechnen
        x_transrapid, y_transrapid = self.getKoordinaten(
            transrapid_winkel, self._strecken_radius
        )
        x_werkzeugwagen, y_werkzeugwagen = self.getKoordinaten(
            werkzeugwagen_winkel, self._strecken_radius
        )

        # Updatet die jeweiligen X- und Y-Koordinaten
        self._transrapid_marker.set_xdata(x_transrapid)
        self._transrapid_marker.set_ydata(y_transrapid)

        self._werkzeugwagen_marker.set_xdata(x_werkzeugwagen)
        self._werkzeugwagen_marker.set_ydata(y_werkzeugwagen)

        # Gibt die Koordinaten für Werkzeugwagen und Transrapid aus
        return self._transrapid_marker, self._werkzeugwagen_marker

    # Erstellen der Visualisierung der Klasse
    def visualize(self):
        # Figur und deren Axis erstellen
        fig, ax = plt.subplots()
        # Seitenverhältnis bestimmen, damit der Kreis keine Ellipse wird
        ax.set_aspect("equal", "box")

        # Limitiert die Groesse der Figur (Quadrat)
        _strecken_radius = 5  # Radius des Kreises, beeinflusst die Groesse, Strecke ist 10, daher Radius 5
        ax.set_xlim(-_strecken_radius, _strecken_radius)
        ax.set_ylim(-_strecken_radius, _strecken_radius)

        # Eine Strecke um den Kreis erstellen, sodass die Positionen auf der Linie des Kreises erstellt werden
        strecken_kreis = patches.Circle(
            (0, 0), _strecken_radius, fill=False, color="black", linewidth=2
        )
        # Fügt Kreis auf die Achsen hinzu
        ax.add_patch(strecken_kreis)

        # Marker für Transrapid in der Visualisierung
        (self._transrapid_marker,) = ax.plot([], [], "ro", label="Transrapid")

        # Marker für Werkzeugwagen in der Visualisierung
        (self._werkzeugwagen_marker,) = ax.plot([], [], "bo", label="Werkzeugwagen")

        # Legende der Visualisierung
        ax.legend()

        # Animation der Visualisierung
        # Übergabe der Figur, der Methode Update und frames/intervall
        animation = FuncAnimation(
            fig, self.update, frames=self.num_frames, interval=self.interval, blit=True
        )

        # Animation ausführen
        plt.show()


# Klasse initialisieren, bzw Hauptprogramm zum Testen der Klasse
if __name__ == "__main__":
    teststrecke = Teststrecke()
    try:
        teststrecke.starteTransrapid()
        teststrecke.visualize()
        teststrecke.ausfahrtTransrapid()
        # teststrecke.ausfahrtWerkzeugwagen()  # Wirft Exception
        teststrecke.betreibenStrecke()
    except Exception as e:
        print(f"Fehler aufgetreten!: {e}")
