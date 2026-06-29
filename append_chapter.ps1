$sep = "`r`n`r`n---`r`n`r`n"
$content = Get-Content 'C:\Users\Admin\.openclaw\workspace\novel\_new_chapter.md' -Encoding UTF8 -Raw
Add-Content -Path 'C:\Users\Admin\.openclaw\workspace\novel\正文.md' -Value ($sep + $content) -Encoding UTF8
Remove-Item 'C:\Users\Admin\.openclaw\workspace\novel\_new_chapter.md'
Write-Host 'OK'
