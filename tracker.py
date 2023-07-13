from rasa.core.tracker_store import SQLTrackerStore
from rasa.shared.core.events import UserUttered

class CustomSQLTrackerStore(SQLTrackerStore):
    async def save(self, tracker):
        # Filter out bot messages and other events
        filtered_events = self._filter_user_uttered_events(tracker.events)
        # Update the tracker's events with the filtered events
        tracker.events = filtered_events 
        

        # Call the parent class's save method
        await super().save(tracker)

    @staticmethod
    def _filter_user_uttered_events(events):
        """Filter UserUttered events from a list of events."""
        return [event for event in events if isinstance(event, UserUttered)]