from enum import Enum


class StringColor(Enum):
    DEFAULT = "\x01"  # Use Default (Cyan)
    CYAN = "\x02"  # Cyan
    YELLOW = "\x03"  # Yellow
    WHITE = "\x04"  # White
    GREY = "\x05"  # Grey
    RED = "\x06"  # Red
    GREEN = "\x07"  # Green
    RED_P1 = "\x08"  # Red (P1)
    TAB = "\x09"  # Tab
    NEWLINE = "\x0A"  # Newline
    INVISIBLE = "\x0B"  # Invisible
    REMOVE_BEYOND = "\x0C"  # Remove beyond (large font), newline (small font)
    BLUE_P2 = "\x0E"  # Blue (P2)
    TEAL_P3 = "\x0F"  # Teal (P3)
    PURPLE_P4 = "\x10"  # Purple (P4)
    ORANGE_P5 = "\x11"  # Orange (P5)
    RIGHT_ALIGN = "\x12"  # Right Align
    CENTER_ALIGN = "\x13"  # Center Align
    INVISIBLE_2 = "\x14"  # Invisible
    BROWN_P6 = "\x15"  # Brown (P6)
    WHITE_P7 = "\x16"  # White (P7)
    YELLOW_P8 = "\x17"  # Yellow (P8)
    GREEN_P9 = "\x18"  # Green (P9)
    BRIGHTER_YELLOW_P10 = "\x19"  # Brighter Yellow (P10)
    CYAN_2 = "\x1A"  # Cyan
    PINKISH_P11 = "\x1B"  # Pinkish (P11)
    DARK_CYAN_P12 = "\x1C"  # Dark Cyan (P12)
    GREYGREEN = "\x1D"  # Greygreen
    BLUEGREY = "\x1E"  # Bluegrey
    TURQUOISE = "\x1F"  # Turquoise
