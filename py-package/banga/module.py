# banga/module.py
import argparse
import pkg_resources

def main_function():
    """
    The main function for the 'banga' command-line tool.

    This function is called when users run the 'banga' command.

    It prints installation success, provides usage information, and
    dynamically displays the version from the installed package.

    Additional functionality specific to the 'banga' command can be
    added below.

    Example:
        $ banga --version
        banga 0.1.0

        $ banga -v
        banga 0.1.0
    """
    # Dynamically retrieve version from setup.py
    version = pkg_resources.get_distribution("banga").version

    # Set up command-line argument parser
    parser = argparse.ArgumentParser(description="'banga' provides unified Bengali tools in a single package.")

    # Add argument for displaying version information
    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {version}')
    
    # Add more arguments as needed here for specific functionality
    # Example:
    # parser.add_argument('--input', help='Input file path')

    # Parse command-line arguments
    args = parser.parse_args()

    # Print installation success message
    print("'banga' installed successfully!")

    # Print usage information
    print("You can use 'banga' to perform various tasks.")
    print("For help, run 'banga --help'")

    # Add the rest of the functionality here


if __name__ == '__main__':
    main_function()
