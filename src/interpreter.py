#!/usr/bin/env python3
"""
🐯 TigerByte Interpreter v0.1
A minimal starter interpreter for TigerByte source files (.tb)
-------------------------------------------------------------
This script reads TigerByte source files, validates them,
and executes simple TigerByte commands.

Author: Your Name
Date: October 2025
License: MIT
"""
from debug import Debugger
from config import VERSION, REPO_URL
import sys
import os
import argparse


def run_tigerbyte_file(filepath: str, debug_enabled: bool = False):
    """
    Reads and executes a TigerByte (.tb) source file.

    Steps:
    1. Validate file extension
    2. Ensure file exists
    3. Read contents
    4. Execute line-by-line (currently only print commands)
    """
    # Create debugger instance based on the flag
    debugger = Debugger(enabled=debug_enabled)
    debugger.log(f"Attempting to run file: {filepath}")

    # ✅ Step 1: Validate file type
    if not filepath.endswith(".tb"):
        print("❌ Error: Only .tb (TigerByte) files are supported.")
        # Optionally add debugger.log("File extension check failed.")
        return

    # ✅ Step 2: Check file existence
    if not os.path.exists(filepath):
        print(f"❌ Error: File '{filepath}' not found.")
        # Optionally add debugger.log("File existence check failed.")
        return

    # ✅ Step 3: Read the file contents
    debugger.log(f"Reading file contents from {filepath}...")
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            # Read lines, strip whitespace, remove empty lines and comments
            lines = [
                line.strip() for line in file.readlines()
                if line.strip() and not line.strip().startswith('#') # Basic comment handling
            ]
        debugger.log(f"Read {len(lines)} executable lines.")
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        debugger.log(f"File read failed: {e}")
        return


    if not lines:
        print("⚠️ Warning: The TigerByte file is empty or contains only comments.")
        debugger.log("No executable lines found.")
        return

    print("🐯 Executing TigerByte source...\n")

    # --- Debug Output Placeholders ---
    # In the future, the tokenizer would run here
    debugger.show_tokens(None) # Pass actual tokens when available
    # In the future, the parser would run here
    debugger.show_ast(None) # Pass actual AST when available
    # --- End Placeholders ---

    # ✅ Step 4: Execute each line
    debugger.log("Starting line-by-line execution...")
    for i, line in enumerate(lines):
        debugger.show_line_execution(i + 1, line) # Show line before execution
        execute_command(line, debugger) # Pass debugger to command executor

    debugger.log("Execution finished.")


def execute_command(command: str, debugger):
    """
    Basic command executor.
    Supports: print, version, about
    Future: feed, chase, roar, etc.
    """
    
    clean_command = command.strip().lower() # Normalize command input

    if clean_command == "version" or clean_command == "about":
        # Handle the version/about command
        print(f"🐯 TigerByte Interpreter {VERSION}")
        print("Developed by the TigerByte Community")
        print(f"Repository: {REPO_URL}")

    elif command.startswith("print "):
        # Extract message text
        message = command[len("print "):].strip().strip('"').strip("'")
        print(message)

    else:
        # Placeholder for unrecognized commands
        print(f"⚠️ Unknown command: {command}")


def main():
    """CLI entry point with argument parsing."""
    parser = argparse.ArgumentParser(
        description="🐯 TigerByte Interpreter v0.1 - Executes .tb files. Use '--version' for info.",
    )

    # --- CLI VERSION FLAG (THIS IS THE KEY FIX) ---
    # When this flag is used, argparse will print the version and EXIT before checking for positional arguments.
    parser.add_argument(
        '--version',
        action='version',
        version=f'TigerByte Interpreter {VERSION}\nRepository: {REPO_URL}',
        help="Show program's version number and exit."
    )
    # --- END VERSION FLAG ---

    parser.add_argument(
        'filepath',
        nargs='?',           # Makes the argument OPTIONAL (0 or 1 argument)
        default=None,
        help="Path to the TigerByte (.tb) script to run."
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        help="Enable debug mode to show execution steps."
    )

    # Parse the arguments provided from the command line
    args = parser.parse_args()

    # --- LOGIC TO HANDLE NO FILEPATH (Assuming --version wasn't used, as it exits immediately) ---

    if args.filepath:
        # 1. If a filepath is provided, run the file.
        run_tigerbyte_file(args.filepath, debug_enabled=args.debug)
    
    elif not args.filepath:
        # 2. If NO filepath is provided, print the version/info directly.
        # This handles the case where the user runs 'python interpreter.py' with no arguments.
        print(f"🐯 TigerByte Interpreter {VERSION}")
        print("Developed by the TigerByte Community")
        print(f"Repository: {REPO_URL}")
        print("\nNote: To run a script, use: python src/interpreter.py <filepath>")

if __name__ == "__main__":
    main()