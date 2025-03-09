# PowerShell을 실행할 수 없는 이슈

## 상황

`MainReturnValTest`의 실행 테스트를 위해 PowerShell 스크립트를 작성하여 실행하던 중 다음과 같은 에러가 발생하는 상황

```PowerShell
.\MainReturnValTest.ps1 : 이 시스템에서 스크립트를 실행할 수 없으므로 MainReturnValTest.ps1 파일을 로드할 수 없습니다. 자세한 내용은 about_Execution_Policies(https://go.microsoft.com/fwlink/?LinkID=1
35170)를 참조하십시오.
위치 줄:1 문자:1
+ .\MainReturnValTest.ps1
+ ~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : 보안 오류: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

## 분석

메시지의 내용에서 설명하는 것은 스크립트를 실행할 수 없는 이유를 보안 오류로 표시한다. 즉, 보안 설정 관련 이슈로 추정된다.

> 탐색 결과, 파워셸 스크립트를 실행하기 위해서는 파워셸을 관리자 권한에서 실행하여 파워셸의 실행 정책을 확인해야 한다.

## 해결

우선, 파워셸을 관리자 권한으로 실행한 뒤 다음 명령어를 이용해서 실행 정책을 확인한다.

```PowerShell
PS > Get-ExecutionPolicy -List

        Scope ExecutionPolicy
        ----- ---------------
MachinePolicy       Undefined
   UserPolicy       Undefined
      Process       Undefined
  CurrentUser       Undefined
 LocalMachine       Undefined
```

확인이 되었으면, 다음 명령어를 이용해서 Y키를 입력하고 실행 정책을 변경한다.

```PowerShell
Set-ExecutionPolicy RemoteSigned
```

위 방법으로 동작하지 않는다면 아래의 명령어를 실행하여 Y키를 입력하고 실행 정책을 변경한다.

```PowerShell
Set-ExecutionPolicy AllSigned
```

## 확인

파워셸 스크립트의 정상 작동 여부를 확인한다.

```
PS > .\MainReturnValTest.ps1
Main method return value test.
Execution succeeded
Return value =  0
```

## 참조
- [[Power Shell] 파워쉘 스크립트(.ps1) 실행하는 방법](https://betterinvesting.tistory.com/276)
- [MSDN: 1장 - PowerShell 시작](https://learn.microsoft.com/ko-kr/powershell/scripting/learn/ps101/01-getting-started?view=powershell-7.5)
