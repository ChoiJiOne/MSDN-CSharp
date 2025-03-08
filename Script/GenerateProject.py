import sys
import os
import argparse

if __name__ == "__main__":    
    parser = argparse.ArgumentParser()
    parser.add_argument("--project_name", help="Name of the Visual Studio C# console project to create.")
    parser.add_argument("--root_directory", help="MSDN-CSharp directory(Do not touch this directory).")
    args = parser.parse_args()

    root_directory = args.root_directory
    project_name = args.project_name

    # 프로젝트 이름이 비어있다면.
    if not project_name:
        print("\nERROR! Project name not provided.\nUSAGE: GenerateProject.bat <PROJECT_NAME>\n")
        sys.exit(1)

    print(f"{project_name} 프로젝트 생성 시작.\n")
    command = f"dotnet new console --language \"C#\" --name {project_name}"
    os.system(command)