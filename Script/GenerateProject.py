import sys
import os
import argparse

def is_already_exist_vs_project(root_directory, project_name):
    target_project_path = f"{root_directory}{project_name}"
    target_project_file = f"{target_project_path}/{project_name}.csproj"

    if not os.path.isdir(target_project_path):
        return False
    
    if not os.path.isfile(target_project_file):
        return False
    
    return True
    
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

    # 인자로 전달받은 프로젝트가 이미 존재한다면.


    print(f"{project_name} 프로젝트 생성 시작.\n")
    command = f"dotnet new console --language \"C#\" --name {project_name}"
    os.system(command)