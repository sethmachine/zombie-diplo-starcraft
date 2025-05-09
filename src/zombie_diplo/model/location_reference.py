"""Refer to a location by its name alone."""
import dataclasses


@dataclasses.dataclass(frozen=True)
class LocationReference:
    _name: str

    @property
    def name(self) -> str:
        return self._name
