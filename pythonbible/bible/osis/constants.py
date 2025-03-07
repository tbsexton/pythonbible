from typing import Dict

from pythonbible.books import Book
from pythonbible.errors import InvalidBookError

# noinspection SpellCheckingInspection
BOOK_IDS: Dict[Book, str] = {
    Book.GENESIS: "Gen",
    Book.EXODUS: "Exod",
    Book.LEVITICUS: "Lev",
    Book.NUMBERS: "Num",
    Book.DEUTERONOMY: "Deut",
    Book.JOSHUA: "Josh",
    Book.JUDGES: "Judg",
    Book.RUTH: "Ruth",
    Book.SAMUEL_1: "1Sam",
    Book.SAMUEL_2: "2Sam",
    Book.KINGS_1: "1Kgs",
    Book.KINGS_2: "2Kgs",
    Book.CHRONICLES_1: "1Chr",
    Book.CHRONICLES_2: "2Chr",
    Book.EZRA: "Ezra",
    Book.NEHEMIAH: "Neh",
    Book.ESTHER: "Esth",
    Book.JOB: "Job",
    Book.PSALMS: "Ps",
    Book.PROVERBS: "Prov",
    Book.ECCLESIASTES: "Eccl",
    Book.SONG_OF_SONGS: "Song",
    Book.ISAIAH: "Isa",
    Book.JEREMIAH: "Jer",
    Book.LAMENTATIONS: "Lam",
    Book.EZEKIEL: "Ezek",
    Book.DANIEL: "Dan",
    Book.HOSEA: "Hos",
    Book.JOEL: "Joel",
    Book.AMOS: "Amos",
    Book.OBADIAH: "Obad",
    Book.JONAH: "Jonah",
    Book.MICAH: "Mic",
    Book.NAHUM: "Nah",
    Book.HABAKKUK: "Hab",
    Book.ZEPHANIAH: "Zeph",
    Book.HAGGAI: "Hag",
    Book.ZECHARIAH: "Zech",
    Book.MALACHI: "Mal",
    Book.MATTHEW: "Matt",
    Book.MARK: "Mark",
    Book.LUKE: "Luke",
    Book.JOHN: "John",
    Book.ACTS: "Acts",
    Book.ROMANS: "Rom",
    Book.CORINTHIANS_1: "1Cor",
    Book.CORINTHIANS_2: "2Cor",
    Book.GALATIANS: "Gal",
    Book.EPHESIANS: "Eph",
    Book.PHILIPPIANS: "Phil",
    Book.COLOSSIANS: "Col",
    Book.THESSALONIANS_1: "1Thess",
    Book.THESSALONIANS_2: "2Thess",
    Book.TIMOTHY_1: "1Tim",
    Book.TIMOTHY_2: "2Tim",
    Book.TITUS: "Titus",
    Book.PHILEMON: "Phlm",
    Book.HEBREWS: "Heb",
    Book.JAMES: "Jas",
    Book.PETER_1: "1Pet",
    Book.PETER_2: "2Pet",
    Book.JOHN_1: "1John",
    Book.JOHN_2: "2John",
    Book.JOHN_3: "3John",
    Book.JUDE: "Jude",
    Book.REVELATION: "Rev",
    # Book.BARUCH: "Bar",
    # Book.ADDITIONS_TO_DANIEL: "AddDan",
    # Book.PRAYER_OF_AZARIAH: "PrAzar",
    # Book.BEL_AND_THE_DRAGON: "Bel",
    # Book.SONG_OF_THE_THREE_YOUNG_MEN: "SgThree",
    # Book.SUSANNA: "Sus",
    Book.ESDRAS_1: "1Esd",
    # Book.ESDRAS_2: "2Esd",
    # Book.ADDITIONS_TO_ESTHER: "AddEsth",
    # Book.EPISTLE_OF_JEREMIAH: "EpJer",
    # Book.JUDITH: "Jdt",
    Book.MACCABEES_1: "1Macc",
    Book.MACCABEES_2: "2Macc",
    # Book.MACCABEES_3: "3Macc",
    # Book.MACCABEES_4: "4Macc",
    # Book.PRAYER_OF_MANASSEH: "PrMan",
    Book.ECCLESIASTICUS: "Sir",
    Book.TOBIT: "Tobit",
    Book.WISDOM_OF_SOLOMON: "Wis",
}


def get_book_by_id(book_id: str) -> Book:
    for next_book, next_book_id in BOOK_IDS.items():
        if book_id == next_book_id:
            return next_book

    raise InvalidBookError
