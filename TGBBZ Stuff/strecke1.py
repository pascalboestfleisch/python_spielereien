import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

class Teststrecke:
    def __init__(self, num_frames=10, interval=100):
        self.num_frames = num_frames
        self.interval = interval
        self.route_radius = 5
        self._strecke = list(range(10))  # Eine einfache Strecke von 0 bis 9
        self._transrapid = 0
        self._werkzeugwagen = 0
        self._transrapid_marker = None
        self._werkzeugwagen_marker = None
        self._box_marker = None

    def betreibenStrecke(self):
        self._transrapid = (self._transrapid + 1) % len(self._strecke)
        self._werkzeugwagen = (self._werkzeugwagen + 1) % len(self._strecke)

    def getTransrapid(self):
        return self._transrapid

    def getWerkzeugwagen(self):
        return self._werkzeugwagen

    def getPositionTransrapid(self):
        return self._transrapid

    def getPositionWerkzeugwagen(self):
        return self._werkzeugwagen

    def get_cartesian_coordinates(self, angle, radius):
        x = radius * np.cos(np.radians(angle))
        y = radius * np.sin(np.radians(angle))
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

        # Wenn die Position des nicht benutzten Transrapid -1 ist, setze den Marker in die Box
        if self.getTransrapid() == 0:
            x_transrapid, y_transrapid = x_garage, y_garage

        # Wenn die Position des nicht benutzten Werkzeugwagens -1 ist, setze den Marker in die Box
        if self.getWerkzeugwagen() == 0:
            x_werkzeugwagen, y_werkzeugwagen = x_garage, y_garage

        # Die Position der Marker in der Garage aktualisieren
        self._transrapid_marker.set_data(x_transrapid, y_transrapid)
        self._werkzeugwagen_marker.set_data(x_werkzeugwagen, y_werkzeugwagen)

        # Lösche vorherige Marker-Positionen in der Box
        if self._box_marker:
            self._box_marker.remove()

        # Markiere die Box, wenn Marker in der Box ist
        if self.getTransrapid() == 0 and self.getWerkzeugwagen() == 0:
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


# Beispielaufruf
teststrecke = Teststrecke(num_frames=10, interval=500)
teststrecke.visualize()
