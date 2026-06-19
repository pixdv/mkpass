import argparse

def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(add_help=False)

    parser.add_argument(
        "-l",
        "--no-lower",
        action="store_true",
    )
    parser.add_argument(
        "-u",
        "--no-upper",
        action="store_true",
    )
    parser.add_argument(
        "-d",
        "--no-digits",
        action="store_true",
    )
    parser.add_argument(
        "-s",
        "--no-special",
        action="store_true",
    )
    parser.add_argument(
        "-e",
        "--exclude",
        type=str,
    )

    parser.add_argument(
        "-L",
        "--length",
        type=int,
    )
    parser.add_argument(
        "-m",
        "--min-length",
        type=int,
    )
    parser.add_argument(
        "-M",
        "--max-length",
        type=int,
    )

    parser.add_argument(
        "-n",
        "--number",
        type=int,
    )

    parser.add_argument(
        "-o",
        "--output",
        type=str,
    )

    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
    )

    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
    )

    parser.add_argument(
        "-h",
        "--help",
        action="store_true",
    )

    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
    )

    return parser