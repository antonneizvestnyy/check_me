#Информация о железе ПК#
$Computer = "NAME_PK"
Invoke-Command -ComputerName $Computer -ScriptBlock {
    $hostName = (Get-WmiObject -Class Win32_ComputerSystem -Property Name).Name
    $Motherboard = Get-CimInstance Win32_BaseBoard
    $Bios = Get-WmiObject win32_bios
    $CPU = Get-WmiObject Win32_Processor
    $OS = Get-WmiObject Win32_OperatingSystem
    
    Write-Host "| $hostName | $($Motherboard.Manufacturer) ($($Motherboard.Product)) | $($Bios.SMBIOSBIOSVersion) | $($CPU.Name) | $($OS.BuildNumber) |"
}
