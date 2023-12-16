#поиск пользователя
Get-ADUser -filter {displayName -like "*NAME*"} | select UserPrincipalName
