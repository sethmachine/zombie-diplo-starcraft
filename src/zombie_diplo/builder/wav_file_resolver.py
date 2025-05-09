"""Resolve a WavFile enum to its actual path in the CHK."""

from richchk.io.richchk.query.chk_query_util import ChkQueryUtil
from richchk.model.richchk.rich_chk import RichChk
from richchk.model.richchk.wav.rich_wav_section import RichWavSection

from ..model.wav.wav_file import WavFile
from ..util.logger import get_logger


class WavFileResolver:
    def __init__(self, chk: RichChk, wavfile_mapping: dict[WavFile, str]) -> None:
        self._chk = chk
        self.wavfile_mapping = wavfile_mapping
        self._log = get_logger(WavFileResolver.__name__)

    def resolve_exactly(self, wavfile: WavFile) -> str:
        """Resolve a WavFile enum to its string path in the CHK.

        :return:
        """
        richwav = ChkQueryUtil.find_only_rich_section_in_chk(RichWavSection, self._chk)
        wav_basename = self.wavfile_mapping.get(wavfile, None)
        if not wav_basename:
            msg = f"No wav file basename defined for {wavfile}!"
            self._log.error(msg)
            raise KeyError(msg)
        maybe_wav = None
        for wav in richwav.wavs:
            if wav_basename in wav.path_in_chk.value:
                assert isinstance(wav.path_in_chk.value, str)
                return wav.path_in_chk.value
        if not maybe_wav:
            msg = f"Failed to find wav file by its enum value: {wavfile}!"
            self._log.error(msg)
            raise ValueError(msg)
