$c = Get-Content 'C:\Users\Admin\.openclaw\workspace\novel\_new_chapter.md' -Encoding UTF8 -Raw
$separator = "`r`n`r`n---`r`n`r`n"
Add-Content -Path 'C:\Users\Admin\.openclaw\workspace\novel\正文.md' -Value ($separator + $c) -Encoding UTF8
Remove-Item 'C:\Users\Admin\.openclaw\workspace\novel\_new_chapter.md' -ErrorAction SilentlyContinue
Write-Output "Done - chapter appended"
