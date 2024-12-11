from app.base.user.event.events import UserCreatedEvent


async def log_user_created(event: UserCreatedEvent):
    print(f"[Event] User Created - ID: {event.user_id}, Name: {event.full_name}")
