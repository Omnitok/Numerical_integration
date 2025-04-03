from .locate import find_setup, find_input_file, Path
from configparser import ConfigParser


def parse_setupfile() -> ConfigParser:
    """Parses the content of the setting.ini file

    Args:
        file: Path to settings.ini

    Returns:
        ConfigParser object with content from setting.ini
    """
    file = find_setup()
    setup = ConfigParser()
    setup.read(file)
    return setup


def parse_inputfile(file: Path):
    pass
