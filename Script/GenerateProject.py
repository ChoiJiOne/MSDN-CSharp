import sys
import os
import argparse
import re

def check_valid_project_name(project_name):
    if not project_name:
        return False
    
    pattern = r'[\\/:*?"<>|]'
    return not bool(re.search(pattern, project_name))

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

    # 프로젝트 이름이 유효한지 검사.
    # ex. TEST/TEST => 유효한 이름 아님
    # ex. TEST\\TEST => 요효한 이름 아님
    # ex. TEST => 유효한 이름
    # ex. (아무것도 없음) => 유효한 이름 아님
    if not check_valid_project_name(project_name):
        print(f"\nERROR! Project name is invalid: '{project_name}'\n")
        sys.exit(1)

    # 인자로 전달받은 프로젝트가 이미 존재한다면.
    if is_already_exist_vs_project(root_directory, project_name):
        print(f"\nERROR! '{project_name}' C# Visual Studio project is already exist.\n")
        sys.exit(1)

    print(f"'{project_name}' 프로젝트 생성 시작.\n")
    command = f"dotnet new console --language \"C#\" --name {project_name}"
    os.system(command)

    print(f"'{project_name} 프로젝트 솔루션에 추가.\n'")
    add_target_project = f"{project_name}/{project_name}.csproj"
    command = f"dotnet sln add {add_target_project}"
    os.system(command)