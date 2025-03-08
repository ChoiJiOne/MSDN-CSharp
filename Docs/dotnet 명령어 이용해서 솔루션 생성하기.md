# dotnet 명령어를 이용해서 솔루션 생성하기

## 용어
- `.sln`: Visual Studio 솔루션 파일

## 명령어

- 현재 폴더와 이름이 같은 .sln 파일을 생성
    ```PowerShell
    dotnet new sln
    ```
- 지정된 파일 이름을 사용하면 현재 폴더에 .sln 파일 생성
    ```
    dotnet new sln --name {MySolution}
    ```
- 지정된 폴더에 폴더와 이름이 같은 .sln 파일 생성
    ```
    dotnet new sln --output {MySolution}
    ```

## 테스트
- CMD 혹은 PowerShell에서 솔루션 생성 명령어 테스트
- 테스트 디렉토리: `D:\Temp`

### `dotnet new sln`
```PowerShell
D:\Temp>dotnet new sln
"솔루션 파일" 템플릿이 성공적으로 생성되었습니다.

D:\Temp>dir /b
Temp.sln
```

### `dotnet new sln --name {MySolution}`
- 테스트할 솔루션 이름: `Test`
```PowerShell
D:\Temp>dotnet new sln --name Test
"솔루션 파일" 템플릿이 성공적으로 생성되었습니다.

D:\Temp>dir /b
Test.sln
```

### `dotnet new sln --output {MySolution}`
- 테스트할 솔루션 이름: `Test`
```PowerShell
D:\Temp>dotnet new sln --output Test
"솔루션 파일" 템플릿이 성공적으로 생성되었습니다.

D:\Temp>cd Test
D:\Temp\Test>dir /b
Test.sln
```

## 참조
- [dotnet sln](https://learn.microsoft.com/ko-kr/dotnet/core/tools/dotnet-sln)
