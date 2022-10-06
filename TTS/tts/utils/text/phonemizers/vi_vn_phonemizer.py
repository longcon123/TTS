from typing import Dict

from TTS.tts.utils.text.vietnamese.phonemizer import vietnamese_text_to_phonemes
from TTS.tts.utils.text.phonemizers.base import BasePhonemizer

_DEF_VI_PUNCS = "、.,[]()?!〽~『』「」【】"


class VI_VN_Phonemizer(BasePhonemizer):
    """🐸TTS Vi-Vn phonemizer using functions in `TTS.tts.utils.text.vietnamese.phonemizer`

    Args:
        punctuations (str):
            Set of characters to be treated as punctuation. Defaults to `_DEF_VI_PUNCS`.

        keep_puncs (bool):
            If True, keep the punctuations after phonemization. Defaults to False.

    Example ::

        "Xin chào các bạn" -> `s|i|n|1| |c|a|w|2| |k|a|k|5| |b|a|n|6| |.`

    TODO: someone with Vietnamese knowledge should check this implementation
    """

    language = "vi-vn"

    def __init__(self, punctuations=_DEF_VI_PUNCS, keep_puncs=False, **kwargs):  # pylint: disable=unused-argument
        super().__init__(self.language, punctuations=punctuations, keep_puncs=keep_puncs)

    @staticmethod
    def name():
        return "vi_vn_phonemizer"

    @staticmethod
    def phonemize_vi_vn(text: str, separator: str = "|") -> str:
        ph = vietnamese_text_to_phonemes(text, separator)
        return ph

    def _phonemize(self, text, separator):
        return self.phonemize_vi_vn(text, separator)

    @staticmethod
    def supported_languages() -> Dict:
        return {"vi-vn": "Vietnamese (VietNam)"}

    def version(self) -> str:
        return "0.0.1"

    def is_available(self) -> bool:
        return True


# if __name__ == "__main__":
#     text = "Đây là phiên âm tiếng việt sang IPA"
#     e = VI_VN_Phonemizer()
#     print(e.supported_languages())
#     print(e.version())
#     print(e.language)
#     print(e.name())
#     print(e.is_available())
#     print("`" + e.phonemize(text) + "`")
