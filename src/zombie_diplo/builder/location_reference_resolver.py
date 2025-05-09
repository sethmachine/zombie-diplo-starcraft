"""Resolve a location reference name to an actual RichLocation."""

from richchk.io.richchk.query.chk_query_util import ChkQueryUtil
from richchk.io.richchk.query.mrgn_query_util import MrgnQueryUtil
from richchk.model.richchk.mrgn.rich_location import RichLocation
from richchk.model.richchk.mrgn.rich_mrgn_section import RichMrgnSection
from richchk.model.richchk.rich_chk import RichChk

from ..model.location_reference import LocationReference
from ..util.logger import get_logger


class LocationReferenceResolver:
    def __init__(self, chk: RichChk) -> None:
        self._chk = chk
        self._log = get_logger(LocationReferenceResolver.__name__)

    def resolve_exactly(
        self, locref: LocationReference, ignorecase: bool = True
    ) -> RichLocation:
        """Attempt to resolve a location reference by its name to an actual RichLocation
        in the CHK.

        :param locref:
        :return:
        """
        mrgn = ChkQueryUtil.find_only_rich_section_in_chk(RichMrgnSection, self._chk)
        maybe_loc = MrgnQueryUtil.find_location_by_name(
            location_name=locref.name, mrgn=mrgn, ignorecase=ignorecase
        )
        if not maybe_loc:
            msg = f"Failed to find location by exact name: {locref.name}!"
            self._log.error(msg)
            raise ValueError(msg)
        return maybe_loc
