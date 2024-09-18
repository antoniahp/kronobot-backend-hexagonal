from dataclasses import dataclass

from cqrs.commands.command import Command


@dataclass(frozen=True)
class ImportKronoliveSectionTimeCommand(Command):
    pass