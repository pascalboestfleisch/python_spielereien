"""
+----------------------------------+
|            Teststrecke           |
+----------------------------------+
| -_fahrzeug_position_transrapid   |
| -_fahrzeug_position_werkzeugwagen|
| -_fahrbahnStatus                 |
| -_garage                         |
| -_weiche                         |
| -_strecke: List[int]             |
| -_transrapid                     |
| -_werkzeugwagen                  |
| -_route_radius                    |
| -_transrapid_marker              |
| -_werkzeugwagen_marker           |
| -_x_werkzeugwagen                |
| -_y_werkzeugwagen                |
| -_x_transrapid                   |
| -_y_transrapid                   |
| -_num_frames                      |
| -_interval                        |
+----------------------------------+
| +getTransrapid(): int            |
| +getWerkzeugwagen(): int         |
| +getStatus(): int                |
| +getWeiche(): int                |
| +validiereStart(): bool          |
| +getPositionTransrapid(): int    |
| +getPositionWerkzeugwagen(): int |
| +starteTransrapid(): void        |
| +starteWerkzeugwagen(): void     |
| +ausfahrtTransrapid(): void      |
| +ausfahrtWerkzeugwagen(): void   |
| +betreibenStrecke(): void        |
| +get_cartesian_coordinates(angle, route_radius): Tuple[float, float] |
| +update(frame): Tuple[Line2D, Line2D] |
| +visualize(): void               |
+----------------------------------+
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
        self._fahrbahnStatus: int = 0  # Fahrbahn frei wenn 0
        self._garage: int = -1  # Position der Garage
        self._weiche: int = 0  # Weiche wurde nicht ausgerichtet (0)
        # Laenge der Strecke als Liste von 0 bis 10
        self._strecke = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self._transrapid: int = 0  # Ist Transrapid angeschalten? 0 -> nein
        self._werkzeugwagen: int = 0  # Ist Werkzeugwagen angeschalten? 0 -> nein
        # Radius der Strecke bzw. des Kreises (Kreis ist die Groesse der Strecke)
        self.route_radius: int = 5
        self._transrapid_marker: int = 0
        self._werkzeugwagen_marker: int = 0
        self._x_werkzeugwagen: int = 0  # X-Koordinate von Werkzeugwagen
        self._y_werkzeugwagen: int = 0  # Y-Koordinate von Werkzeugwagen
        self._x_transrapid: int = 0  # X-Koordinate von Transrapid
        self._y_transrapid: int = 0  # Y-Koordinate von Transrapid
        self.num_frames: int = 100  # Nummer der Frames
        self.interval: int = 100  # Groesse des Intervalls in Millisekunden

    def __del__(self):  # Destruktor
        print("Teststrecke zerstört")

    def getTransrapid(self):
        return self._transrapid

    def getWerkzeugwagen(self):
        return self._werkzeugwagen

    def getStatus(self):
        return self._fahrbahnStatus

    def getWeiche(self):
        return self._weiche

    def validiereStart(self):
        if self.getStatus() == 1:
            if self.getTransrapid() == 1 or self.getWerkzeugwagen() == 1:
                raise Exception(
                    "Es befindet sich bereits ein Fahrzeuf auf der Strecke, bitte warten Sie!"
                )
        return True

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
        return 0  # Wenn Position nicht gesetzt, setze den default Wert auf 0

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
        return 0  # Wenn Position nicht gesetzt, setze den default Wert auf 0

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
                print(
                    "Starten nicht möglich, da bereits ein anderes Fahrzeug auf der Strecke ist. Das Fahrzeug befindet sich noch in der Garage "
                )
                self._fahrzeug_position_transrapid = self._garage
        else:
            print("Der Transrapid wurde bereits gestartet")

    def starteWerkzeugwagen(self):
        if self.getWerkzeugwagen() == 0:
            if self.validiereStart():
                self._fahrzeug_position_werkzeugwagen = self._garage
                self._werkzeugwagen = 1
                print("Werkzeugwagen ist gestartet")
            else:
                print(
                    "Starten nicht möglich, da bereits ein anderes Fahrzeug auf der Strecke ist. Das Fahrzeug befindet sich noch in der Garage "
                )
                self._fahrzeug_position_werkzeugwagen = self._garage
        else:
            print("Der Werkzeugwagen wurde bereits gestartet")

    def ausfahrtTransrapid(self):
        if self.validiereStart():
            if self.getTransrapid() == 1:
                if self.getWeiche() == 0:
                    self._weiche = 1
            self._fahrzeug_position_transrapid = (
                self._fahrzeug_position_transrapid + 1
            ) % len(self._strecke)
            print("Transrapid bewegt sich")
            self._fahrbahnStatus = 1

    def ausfahrtWerkzeugwagen(self):
        if self.validiereStart():
            if self.getWerkzeugwagen() == 1:
                if self.getWeiche() == 0:
                    self._weiche = 1
            self._fahrzeug_position_werkzeugwagen = (
                self._fahrzeug_position_werkzeugwagen + 1
            ) % len(self._strecke)
            print("Werkzeugwagen bewegt sich")
            self._fahrbahnStatus = 1

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

    def get_cartesian_coordinates(self, angle, route_radius):
        if angle is None:
            return (
                0,
                0,
            )  # Wenn es keine Angaben zum Winkel bzw. der Position gibt, wird Marker an die Stelle 0,0 in der Visualisierung gesetzt
        x = route_radius * np.cos(np.radians(angle))
        y = route_radius * np.sin(np.radians(angle))
        return x, y

    def update(self, frame):
        self.betreibenStrecke()
        transrapid_pos = self.getPositionTransrapid()
        werkzeugwagen_pos = self.getPositionWerkzeugwagen()

        # Berechnung des Winkels anhand der Position von Transrapid/Werkzeugwagen
        transrapid_angle = (transrapid_pos / len(self._strecke)) * 360
        werkzeugwagen_angle = (werkzeugwagen_pos / len(self._strecke)) * 360

        # Die Position der Marker updaten
        x_transrapid, y_transrapid = self.get_cartesian_coordinates(
            transrapid_angle, self.route_radius
        )
        x_werkzeugwagen, y_werkzeugwagen = self.get_cartesian_coordinates(
            werkzeugwagen_angle, self.route_radius
        )

        # Zusätzlicher Kasten für Position -1
        x_garage, y_garage = self.get_cartesian_coordinates(-1, self.route_radius)

        if self.getTransrapid() == 0:
            # Wenn die Position des nicht benutzten Fahrzeugs -1 ist, setze den Marker in die Box
            x_transrapid, y_transrapid = x_garage, y_garage

        if self.getWerkzeugwagen() == 0:
            # Wenn die Position des nicht benutzten Fahrzeugs -1 ist, setze den Marker in die Box
            x_werkzeugwagen, y_werkzeugwagen = x_garage, y_garage

        # Die Position der Marker in der Garage aktualisieren
        self._transrapid_marker.set_data(x_transrapid, y_transrapid)
        self._werkzeugwagen_marker.set_data(x_werkzeugwagen, y_werkzeugwagen)

        # Lösche vorherige Marker-Positionen in der Box
        if hasattr(self, "_box_marker"):
            self._box_marker.remove()

        # Markiere die Box, wenn Marker in der Box ist
        if (
            self.getTransrapid() == 0 and self.getWerkzeugwagen() == 0
        ):  # Beide Fahrzeuge in der Box
            self._box_marker = plt.plot(
                x_garage, y_garage, "go", label="Fahrzeuge in der Box"
            )[0]

        # Return an empty list to satisfy the blit parameter
        return []

    def visualize(self):
        # Figur und deren Axis erstellen
        fig, ax = plt.subplots()
        ax.set_aspect("equal", "box")

        # Limitiert die Groesse der Figur
        route_radius = 5  # Radius des Kreises, beeinflusst die Groesse
        ax.set_xlim(-route_radius - 2, route_radius + 2)
        ax.set_ylim(-route_radius, route_radius)

        # Eine Strecke um den Kreis erstellen, sodass die Positionen auf der Linie des Kreises erstellt werden
        route_circle = patches.Circle(
            (0, 0), route_radius, fill=False, color="black", linewidth=2
        )
        ax.add_patch(route_circle)

        # Marker für Transrapid in der Visualisierung
        (self._transrapid_marker,) = ax.plot([], [], "ro", label="Transrapid")

        # Marker für Werkzeugwagen in der Visualisierung
        (self._werkzeugwagen_marker,) = ax.plot([], [], "bo", label="Werkzeugwagen")

        # Zusätzlicher Kasten für Position -1
        box_position_minus_1 = patches.Rectangle(
            xy=(route_radius + 0.5, -0.5), width=1, height=1, fill=True, color="grey", label="Garage bei Position: -1"
        )
        ax.add_patch(box_position_minus_1)

        # Legende der Visualisierung
        ax.legend()

        # Animation der Visualisierung
        animation = FuncAnimation(
            fig, self.update, frames=self.num_frames, interval=self.interval, blit=True
        )

        # Display the animation
        plt.show()






# Klasse initialisieren, bzw Hauptprogramm zum Testen der Klasse

if __name__ == "__main__":
    teststrecke = Teststrecke()
    teststrecke.starteTransrapid()
    # teststrecke.starteWerkzeugwagen() # wuerde Exception werfen, da Fahrzeug auf Fahrbahn
    teststrecke.visualize()
    teststrecke.ausfahrtTransrapid()
    # teststrecke.ausfahrtWerkzeugwagen() # wuerde Exception werfen, da Fahrzeug auf Fahrbahn
    teststrecke.betreibenStrecke()
