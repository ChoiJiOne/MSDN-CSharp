# dotnet 명령어를 이용해서 C# 프로젝트 생성하기

## `dotnet new` 명령어
- 지정된 템플릿을 기반으로 새 프로젝트, 구성 파일 또는 솔루션 생성

## 인자
- `TEMPLATE`: 명령이 호출될 때 인스턴스화할 템플릿
```
dotnet new <TEMPLATE> [--dry-run] [--force] [-lang|--language {"C#"|"F#"|VB}]
    [-n|--name <OUTPUT_NAME>] [-f|--framework <FRAMEWORK>] [--no-update-check]
    [-o|--output <OUTPUT_DIRECTORY>] [--project <PROJECT_PATH>]
    [-d|--diagnostics] [--verbosity <LEVEL>] [Template options]
```

## 템플릿

| 템플릿 | 짧은 이름 | 언어 | 태그 | 도입 |
|--------|----------|------|------|------|
| 콘솔 애플리케이션 | console | [C#], F#, VB | 일반/콘솔 | 1.0 |
| 클래스 라이브러리 | classlib | [C#], F#, VB | 일반/라이브러리 | 1.0 |
| WPF 애플리케이션 | wpf | [C#], VB | 일반/WPF | 3.0(VB의 경우 5.0) |
| WPF 클래스 라이브러리 | wpflib | [C#], VB | 일반/WPF | 3.0(VB의 경우 5.0) |
| WPF 사용자 지정 컨트롤 라이브러리 | wpfcustomcontrollib | [C#], VB | 일반/WPF | 3.0(VB의 경우 5.0) |
| WPF 사용자 컨트롤 라이브러리 | wpfusercontrollib | [C#], VB | 일반/WPF | 3.0(VB의 경우 5.0) |
| Windows Forms(WinForms) 애플리케이션 | winforms | [C#], VB | 일반/WinForms | 3.0(VB의 경우 5.0) |
| Windows Forms(WinForms) 클래스 라이브러리 | winformslib | [C#], VB | 일반/WinForms | 3.0(VB의 경우 5.0) |
| Worker Service | worker | [C#] | 일반/Worker/웹 | 3.0 |
| MSTest 테스트 프로젝트 | mstest | [C#], F#, VB | Test/MSTest | 1.0 |
| MSTest 테스트 클래스 | mstest-class | [C#], F#, VB | Test/MSTest | 1.0 |
| NUnit 3 테스트 프로젝트 | nunit | [C#], F#, VB | Test/NUnit | 2.1.400 |
| NUnit 3 테스트 항목 | nunit-test | [C#], F#, VB | Test/NUnit | 2.2 |
| xUnit 테스트 프로젝트 | xunit | [C#], F#, VB | Test/xUnit | 1.0 |
| Razor 구성 요소 | razorcomponent | [C#] | Web/ASP.NET | 3.0 |
| Razor 페이지 | page | [C#] | Web/ASP.NET | 2.0 |
| MVC ViewImports | viewimports | [C#] | Web/ASP.NET | 2.0 |
| MVC ViewStart | viewstart | [C#] | Web/ASP.NET | 2.0 |
| Blazor 웹앱 | blazor | [C#] | Web/Blazor | 8.0.100 |
| BlazorWebAssembly 독립 실행형 앱 | blazorwasm | [C#] | 웹/Blazor//WebAssemblyPWA | 3.1.300 |
| ASP.NET Core 비어 있음 | web | [C#], F# | Web/Empty | 1.0 |
| ASP.NET Core 웹앱(모델-뷰-컨트롤러) | mvc | [C#], F# | Web/MVC | 1.0 |
| ASP.NET Core 웹앱 | webapp, razor | [C#] | Web/MVC/Razor Pages | 2.2, 2.0 |
| Razor 클래스 라이브러리 | razorclasslib | [C#] | Web/Razor/Library/Razor 클래스 라이브러리 | 2.1 |
| ASP.NET Core 웹 API | webapi | [C#], F# | 웹/웹 API/API/서비스/WebAPI | 1.0 |
| ASP.NET Core API | webapiaot | [C#] | 웹/웹 API/API/서비스 | 8.0 |
| ASP.NET Core API 컨트롤러 | apicontroller | [C#] | Web/ASP.NET | 8.0 |
| ASP.NET Core gRPC 서비스 | grpc | [C#] | Web/gRPC | 3.0 |
| dotnet gitignore 파일 | gitignore |  | Config | 3.0 |
| global.json 파일 | globaljson |  | Config | 2.0 |
| NuGet 구성 | nugetconfig |  | Config | 1.0 |
| Dotnet 로컬 도구 매니페스트 파일 | tool-manifest |  | Config | 3.0 |
| 웹 구성 | webconfig |  | Config | 1.0 |
| 솔루션 파일 | sln |  | 솔루션 | 1.0 |
| 프로토콜 버퍼 파일 | proto |  | Web/gRPC | 3.0 |
| EditorConfig file | editorconfig |  | Config | 6.0 |

## 옵션
- `--dry-run`
  - 지정된 명령이 실행되어 템플릿 만들기로 이어질 경우 발생하는 작업에 대한 요약 표시
  - .NET Core 2.2 SDK부터 사용할 수 있습니다.
- `--force`
  - 기존 파일을 변경할 경우에도 콘텐츠 강제 생성
- `-?|-h|--help`
  - 명령에 대한 도움말 출력
  - ex. `dotnet new mvc --helps`
- `-lang|--language {C#|F#|VB}`
  - 만들 템플릿의 언어
- `-n|--name <OUTPUT_NAME>`
  - 생성된 출력에 대한 이름
- `-f|--framework <FRAMEWORK>`
  - 대상 프레임워크 지정
  - ex. "net6.0", "net7.0-macos"
- `-no-update-check`
  - 템플릿을 인스턴스화할 때 템플릿 패키지 업데이트 확인을 사용하지 않도록 설정
  - .NET SDK 6.0.100부터 사용 가능
- `-o|--output <OUTPUT_DIRECTORY>`
  - 생성된 출력을 배치할 위치
  - 기본값은 현재 디렉터리
- `--project <PROJECT_PATH>`
  - 템플릿이 추가되는 프로젝트
  - 지정하지 않으면 현재 또는 부모 디렉터리의 프로젝트가 사용
  - .NET SDK 7.0.100부터 사용 가능
- `-d|--diagnostics`
  - 진단 출력을 사용
  - .NET SDK 7.0.100부터 사용 가능
- `-v|--verbosity <LEVEL>`
  - 명령의 세부 정보 표시 수준을 설정
  - 허용되는 값: `q[uiet]`, `m[inimal]`, `n[ormal]`, `diag[nostic]`
  - .NET SDK 7.0.100부터 사용 가능

## 예시
- C# 콘솔 애플리케이션 프로젝트를 생성
    ```
    dotnet new console --language "C#"
    ```

## 참조
- [dotnet new <템플릿>](https://learn.microsoft.com/ko-kr/dotnet/core/tools/dotnet-new)
- [dotnet 명령어를 이용해서 솔루션 생성하기](./dotnet%20명령어%20이용해서%20솔루션%20생성하기.md)