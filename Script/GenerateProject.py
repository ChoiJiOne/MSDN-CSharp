import sys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project_name", help="Name of the Visual Studio C# console project to create.")

    args = parser.parse_args()

    vs_project_name = args.project_name