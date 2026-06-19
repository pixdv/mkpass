#!/usr/bin/env python3
# mkpass.py


import arguments
import generator
import output_path
import errors
import tomllib

def main() -> None:
    parser = arguments.get_parser()
    args = parser.parse_args()

    if args.help:
        with open("README.md") as f:
            print("\n" + f.read() + "\n")
            exit()

    if args.version:
        with open("pyproject.toml", "rb") as f:
            toml = tomllib.load(f)
            print(toml["project"]["name"] + f" v{toml['project']['version']}")
            exit()

    all_args = {
        "lowercase": not args.no_lower or True,
        "uppercase": not args.no_upper or True,
        "digits_": not args.no_digits or True,
        "special": not args.no_special or True,
        "exclude": args.exclude or None,
        "length": args.length or None,
        "min_length": args.min_length or 12,
        "max_length": args.max_length or 20,
        "number": args.number or 1
    }

    if args.no_lower and args.no_upper and args.no_digits and args.no_special:
        print(
            errors.OUTPUT_ERRORS["template"] +
            "\nCannot use both --no-lower --no-upper --no-digits --no-special. Nothing will be generated."
        )
        exit()

    if args.exclude and set(generator.__symbols__()).issubset(set(args.exclude)):
        print(
            errors.OUTPUT_ERRORS["template"] +
            "\nCannot use --exclude more than 93 characters. Nothing will be generated."
        )
        exit()

    if args.length and args.length > 10000:
        print(
            errors.OUTPUT_ERRORS["template"] +
            "\nCannot use --length more than 10000 characters. Too long password will be generated."
        )
        exit()

    if args.length and args.length <= 0:
        print(
            errors.OUTPUT_ERRORS["template"] +
            "\nCannot use --length less or equals 0. Nothing will be generated."
        )
        exit()

    if args.number and args.number <= 0:
        print(
            errors.OUTPUT_ERRORS["template"] +
            "\nCannot use --number more than 0. Nothing will be generated."
        )
        exit()

    if args.min_length and args.min_length <= 0:
        print(
            errors.OUTPUT_ERRORS["template"] +
            "\nCannot use --min_length less than 0. Nothing will be generated."
        )
        exit()

    if args.max_length and args.max_length >= 10000000:
        print(
            errors.OUTPUT_ERRORS["template"] +
            "\nCannot use --max_length more than 10000000 characters. Too long password will be generated."
        )
        exit()

    if all_args["min_length"] > all_args["max_length"]:
        print(
            errors.OUTPUT_ERRORS["template"] +
            "\n--min-length must be less than or equal to --max-length."
        )
        exit()

    passwords = generator.passwords(**all_args)
    if passwords:
        if args.output:
            path = output_path.get_output_path(args.output, force=args.force)
            if path and not path in errors.OUTPUT_ERRORS.values():
                with open(path, "w") as f:
                    f.write("\n".join(passwords))
            elif path in errors.OUTPUT_ERRORS.values():
                parser.error(
                    path
                )
            else:
                parser.error(
                    "Unknown error's happen"
                )
        if not args.quiet:
            text = "\n    ━ /// mkpass /// ━\n"
            for password in passwords:
                text += f"\n ┏ Password: {password}"
                text += f"\n ┗ Length: {len(password)}\n"
            print(text)
    else:
        print("Error: No password generated.")



if __name__ == "__main__":
    main()
