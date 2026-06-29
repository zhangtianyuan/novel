$content = Get-Content 'C:\Users\Admin\.openclaw\workspace\novel\正文.md' -Encoding UTF8
$total = $content.Count
$start = [Math]::Max(0, $total - 400)
$lines = $content[$start..($total-1)]
Write-Output ($lines -join "`r`n")
