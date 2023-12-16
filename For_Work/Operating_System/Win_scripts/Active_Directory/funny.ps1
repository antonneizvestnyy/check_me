#Показать сообщение удаленному пользователю
Invoke-Command -ComputerName <NAME_PK> -ScriptBlock {msg * "Перезагрузка запланирована в течении 1 минуты:)"}
