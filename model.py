import numpy as np

class SmartIrrigationModel:
    def predict(self, temperature, humidity, moisture):
        """
        Simple AI logic:
        If soil moisture < 30% and temperature > 30°C => Need irrigation
        """
        if moisture < 30 and temperature > 30:
            return "Irrigation Needed 🌾"
        elif moisture < 40 and humidity < 50:
            return "Irrigation Recommended 💧"
        else:
            return "No Irrigation Needed ✅"
