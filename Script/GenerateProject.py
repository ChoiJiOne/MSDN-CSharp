import sys
import os
import argparse

if __name__ == "__main__":    
    parser = argparse.ArgumentParser()
    parser.add_argument("--project_name", help="Name of the Visual Studio C# console project to create.")
    parser.add_argument("--root_directory", help="MSDN-CSharp directory(Do not touch this directory).")
    args = parser.parse_args()

    root_directory = args.root_directory