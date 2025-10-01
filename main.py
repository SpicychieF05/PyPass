#!/usr/bin/env python3
"""
PyPass - Offline Password Generator
Main entry point for the application
"""

import os
import sys

from src.gui import PasswordGeneratorApp


def main():
    """Main entry point for PyPass application"""
    app = PasswordGeneratorApp()
    app.run()


if __name__ == "__main__":
    main()
