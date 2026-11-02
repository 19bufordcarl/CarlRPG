param(
    [string]$Name,
    [switch]$All,
    [switch]$NoFold
)

$ErrorActionPreference = "Stop"
$OutputDir = "zines"

function Build-Zine($baseName) {
    $md   = "$baseName.md"
    $tex  = "$baseName.tex"
    $pdf  = "$baseName.pdf"
    $btex = "$baseName-booklet.tex"

    if (-not (Test-Path $md)) {
        Write-Host "Skipping $baseName (no $md)" -ForegroundColor Yellow
        return
    }

    # Strip "Zine" suffix for cleaner output names (WitchZine -> Witch-Zine.pdf)
    $displayName = $baseName -replace 'Zine$', ''
    $jobName = "$displayName-Zine"

    Write-Host "`n=== $baseName ===" -ForegroundColor Cyan

    # Clean stale aux/log so we don't hit the pgfsyspdfmark bug
    Remove-Item "$baseName.aux","$baseName.log","$baseName.out" -ErrorAction SilentlyContinue
    Remove-Item "$baseName-booklet.aux","$baseName-booklet.log" -ErrorAction SilentlyContinue

    Write-Host "  [1/4] pandoc: $md -> $tex"
    pandoc $md --template=dndbook.latex --lua-filter=zine.lua -s -o $tex

    Write-Host "  [2/4] pdflatex pass 1"
    pdflatex -interaction=nonstopmode $tex | Out-Null

    Write-Host "  [3/4] pdflatex pass 2"
    pdflatex -interaction=nonstopmode $tex | Out-Null

    if (-not (Test-Path $pdf)) {
        Write-Host "  ERROR: $pdf not generated. Check $baseName.log" -ForegroundColor Red
        return
    }

    # Generate booklet.tex dynamically
    $foldBlock = if ($NoFold) { "" } else {
@"
\usepackage{eso-pic}
\usepackage{tikz}
\AddToShipoutPictureBG{%
  \begin{tikzpicture}[remember picture, overlay]
    \draw[dashed, gray!40, line width=0.5pt]
      ([yshift=0.5\paperheight]current page.south west) --
      ([yshift=0.5\paperheight]current page.south east);
  \end{tikzpicture}%
}
"@
    }

    $bookletTex = @"
\documentclass{scrartcl}
\usepackage{pdfpages}
$foldBlock
\pagestyle{empty}

\begin{document}
\includepdf[pages=-,booklet,turn=false,landscape]{$pdf}
\end{document}
"@
    $bookletTex | Out-File $btex -Encoding ASCII

    Write-Host "  [4/4] booklet imposition"
    pdflatex -output-directory=$OutputDir -jobname="$jobName" -interaction=nonstopmode $btex | Out-Null
    pdflatex -output-directory=$OutputDir -jobname="$jobName" -interaction=nonstopmode $btex | Out-Null

    Write-Host "  -> $OutputDir\$jobName.pdf" -ForegroundColor Green
}

# Main
New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

if ($All) {
    Get-ChildItem -Filter "*Zine.md" | ForEach-Object {
        Build-Zine ([System.IO.Path]::GetFileNameWithoutExtension($_.Name))
    }
} else {
    if (-not $Name) {
        $Name = Read-Host "Class name (e.g. WitchZine, ViperZine, WizardZine)"
    }
    Build-Zine $Name
}

Write-Host "`nAll done." -ForegroundColor Green