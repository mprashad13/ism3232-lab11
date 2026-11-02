# my_tool.py
# Author: Mahendra Prashad


class AppointmentLookup:
    """A tool for checking available service appointment times."""

    def __init__(self, appointments):
        """Store available appointment times by day."""
        self.appointments = appointments

    def find_day(self, text):
        """Find a known appointment day mentioned in the message."""
        for day in self.appointments:
            if day.lower() in text.lower():
                return day
        return None

    def find_times(self, day):
        """Return available times for a day, or None if unknown."""
        return self.appointments.get(day)
