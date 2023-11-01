# snake_eaterII  

## Powershell script to copy the content of 'folder/'  

```
$sourceFolder = "C:\Users\subject\AppData\Roaming\folder"
$destinationFolder = [Environment]::GetFolderPath("Desktop")

## Check if the source folder exists
if (Test-Path $sourceFolder -PathType Container) {
    while ($true) {
        # List all files in the source folder
        $files = Get-ChildItem $sourceFolder

        # Copy each file to the desktop
        foreach ($file in $files) {
            $destinationPath = Join-Path $destinationFolder $file.Name
            Copy-Item $file.FullName $destinationPath -Force
            Write-Host "Copied $($file.FullName) to $($destinationPath)"
        }

        # Sleep for a specified duration before the next iteration (e.g., 1 minute)
        Start-Sleep -Seconds 0.001
    }
} else {
    Write-Host "Source folder does not exist: $sourceFolder"
}
```  

## Powershell script to execute snake_eaterII.exe  

```
$programPath = "C:\Users\subject\Downloads\snake_eaterII\snake_eaterII.exe"

while ($true) {
    Start-Process $programPath -NoNewWindow
    Write-Host "snake_eaterII.exe started."
    Start-Sleep -Seconds 2  # Sleep for 5 seconds before starting again
}
```  

## CMD command to empty out `/roaming` folder  

```
rmdir /s /q "C:\path\to\folder"
```
