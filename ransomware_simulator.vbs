' Ransomware Simulator pa' Windows - Solo pa' impresionar
' No encripta ni daña nada, solo muestra mensaje
' Ejecuta con doble clic en Windows

Dim objShell
Set objShell = WScript.CreateObject("WScript.Shell")

' Muestra mensaje de ransomware
objShell.Popup "SISTEMA BLOQUEADO POR HACKER PI" & vbNewLine & _
               "Tus datos han sido encriptados." & vbNewLine & _
               "Pa' desbloquear, desbloqueen todos los Chromebooks por una semana." & vbNewLine & _
               "Contacta al admin de red pa' instrucciones." & vbNewLine & _
               "AVISO: Esto es una simulacion. Nada esta realmente bloqueado.", _
               0, "RANSOMWARE ALERTA", 48

' Crea un archivo de texto en el escritorio pa' parecer real
Dim objFSO, objFile
Set objFSO = CreateObject("Scripting.FileSystemObject")
strDesktop = objShell.SpecialFolders("Desktop")
Set objFile = objFSO.CreateTextFile(strDesktop & "\RANSOM_NOTE.txt", True)
objFile.Write "SISTEMA BLOQUEADO POR HACKER PI" & vbNewLine & _
              "Desbloqueen todos los Chromebooks por una semana pa' recuperar acceso." & vbNewLine & _
              "Esto es una simulacion. Tus datos estan seguros."
objFile.Close

Set objShell = Nothing
Set objFSO = Nothing
Set objFile = Nothing
