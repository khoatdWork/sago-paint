param(
    [Parameter(Mandatory = $true)]
    [string] $CdnBaseUrl,

    [switch] $DryRun
)

$ErrorActionPreference = "Stop"

$root = Resolve-Path (Join-Path $PSScriptRoot "..")
$base = $CdnBaseUrl.TrimEnd("/")
$replacement = "$base/assets/products/"
$placeholder = "__PRODUCT_IMAGE_CDN_BASE__/"

$htmlFiles = Get-ChildItem -LiteralPath $root -Recurse -File -Filter *.html

$patterns = @(
    "https://sagopaint.vn/assets/products/",
    "../../assets/products/",
    "../assets/products/",
    "assets/products/"
)

$changed = 0

foreach ($file in $htmlFiles) {
    $content = Get-Content -LiteralPath $file.FullName -Raw
    $next = $content

    foreach ($pattern in $patterns) {
        $next = $next.Replace($pattern, $placeholder)
    }

    $next = $next.Replace($placeholder, $replacement)

    if ($next -ne $content) {
        $changed++
        $relative = Resolve-Path -LiteralPath $file.FullName -Relative
        if ($DryRun) {
            Write-Host "[dry-run] would update $relative"
        } else {
            Set-Content -LiteralPath $file.FullName -Value $next -NoNewline
            Write-Host "Updated $relative"
        }
    }
}

Write-Host "Matched $changed HTML file(s)."
