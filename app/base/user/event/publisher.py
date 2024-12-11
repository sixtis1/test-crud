from typing import Callable, Dict, List, Type


class EventPublisher:
    def __init__(self):
        self._subscribers: Dict[Type, List[Callable]] = {}

    def subscribe(self, event_type: Type, handler: Callable):
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(handler)

    async def publish(self, event):
        event_type = type(event)
        handlers = self._subscribers.get(event_type, [])
        for handler in handlers:
            await handler(event)
