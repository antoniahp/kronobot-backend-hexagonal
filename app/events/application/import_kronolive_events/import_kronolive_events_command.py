from dataclasses import dataclass
from cqrs.commands.command import Command


@dataclass(frozen=True)
class ImportKronoliveEventsCommand(Command):
    pass
