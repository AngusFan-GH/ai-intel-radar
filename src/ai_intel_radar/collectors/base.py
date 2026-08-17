from __future__ import annotations

from abc import ABC, abstractmethod

from ..models import Event, Source


class Collector(ABC):
    source_type: str

    @abstractmethod
    def collect(self, source: Source) -> list[Event]:
        raise NotImplementedError
