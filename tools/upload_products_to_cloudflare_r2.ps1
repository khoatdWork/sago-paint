param(
    [Parameter(Mandatory = $true)]
    [string] $Bucket,

    [string] $ProductsDir = "assets/products",

    [string] $Prefix = "assets/products",

    [string] $CacheControl = "public, max-age=31536000, immutable",

    [switch] $DryRun
)

$ErrorActionPreference = "Stop"

$root = Resolve-Path (Join-Path $PSScriptRoot "..")
$sourceDir = Resolve-Path (Join-Path $root $ProductsDir)

$files = Get-ChildItem -LiteralPath $sourceDir -File |
    Where-Object { $_.Extension -match '^\.(avif|gif|jpe?g|png|svg|webp)$' } |
    Sort-Object Name

if (-not $files) {
    throw "No image files found in $sourceDir"
}

function Get-ContentType {
    param([string] $Extension)

    switch ($Extension.ToLowerInvariant()) {
        ".avif" { "image/avif" }
        ".gif"  { "image/gif" }
        ".jpg"  { "image/jpeg" }
        ".jpeg" { "image/jpeg" }
        ".png"  { "image/png" }
        ".svg"  { "image/svg+xml" }
        ".webp" { "image/webp" }
        default  { "application/octet-stream" }
    }
}

Write-Host "Found $($files.Count) image file(s) in $ProductsDir"

foreach ($file in $files) {
    $key = (($Prefix.TrimEnd("/")) + "/" + $file.Name).Replace("\", "/")
    $objectPath = "$Bucket/$key"
    $contentType = Get-ContentType $file.Extension

    if ($DryRun) {
        Write-Host "[dry-run] $($file.FullName) -> r2://$objectPath ($contentType)"
        continue
    }

    Write-Host "Uploading $($file.Name) -> r2://$objectPath"
    npx --yes wrangler@latest r2 object put $objectPath `
        --file $file.FullName `
        --content-type $contentType `
        --cache-control $CacheControl `
        --remote
}

Write-Host "Done."
