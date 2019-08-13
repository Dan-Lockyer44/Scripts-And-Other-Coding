function PasswordRecovery{
[Windows.Security.Credentials.PasswordVault,Windows.Security.Credentials,ContentType=WindowsRuntime]
    $vault = New-Object Windows.Security.Credentials.PasswordVault 
    $vault.RetrieveAll() | % { $_.RetrievePassword();$_ }
    
}

function GrabTerminal{
Read-Host -Prompt "These Are The Stored Passwords That Were Found (Don't Worry If No Passwords Show/If Only Usernames Show) Press Enter To Exit"
Write-Host "Thanks For Using This Script Created By Dan Lockyer" -ForegroundColor Red -BackgroundColor Yellow
start-sleep -seconds 5
}



PasswordRecovery write-output

GrabTerminal


