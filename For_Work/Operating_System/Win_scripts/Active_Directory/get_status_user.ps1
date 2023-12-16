//проверить статус УЗ
Get-ADUser -Identity <NAME_USER> -Properties LockedOut,DisplayName | Select-Object samaccountName, displayName,Lockedout 
