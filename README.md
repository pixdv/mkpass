ABOUT:
    Simple Password Generator
USAGE:
    python3 mkpass.py [OPTION]...
ARGUMENTS:
    -h, --help              Show this help message and exit
    -v, --version           Show program's version and exit

    -l, --no-lower          Exclude lowercase characters
    -u, --no-upper          Exclude uppercase characters
    -d, --no-digits         Exclude digits
    -s, --no-special        Exclude special
    
    -e, --exclude <CHARS>   Exclude extra characters
    -m, --min-length <N>    Set minimum password length (default: 12)
    -M, --max-length <N>    Set maximum password length (default: 20)
    -L, --length <N>        Set password length (overrides -m and -M)
    -n, --number <N>        Numbers of passwords to generate (default: 1)
    -o, --output <PATH>     Output file
    
    -f, --force             Force output
    -q, --quiet             Suppress output (errors only)