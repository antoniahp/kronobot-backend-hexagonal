from dataclasses import dataclass
from cqrs.commands.command import Command


@dataclass(frozen=True)
class ImportKronoliveEventsCommand(Command):
    days_to_import_events: int
