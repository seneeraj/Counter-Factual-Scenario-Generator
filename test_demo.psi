# ============================================
# Divergent Scenario Engine - Instructor Demo
# File: test_demo.ps1
# ============================================

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Divergent Scenario Engine - Test Demo Script" -ForegroundColor Cyan
Write-Host "============================================`n" -ForegroundColor Cyan

# Base API URL
$BASE_URL = "http://127.0.0.1:8000/generate"

# Test concepts
$concepts = @(
    "Cultural Drift",
    "Power Legitimacy",
    "Invisible Consent"
)

foreach ($concept in $concepts) {

    Write-Host "--------------------------------------------" -ForegroundColor Yellow
    Write-Host "Testing Concept: $concept" -ForegroundColor Yellow
    Write-Host "--------------------------------------------" -ForegroundColor Yellow

    try {
        $response = Invoke-RestMethod -Method Post -Uri "$BASE_URL?concept=$concept"

        $count = $response.scenarios.Count

        Write-Host "Scenario Count Returned: $count" -ForegroundColor Green

        if ($count -ne 10) {
            Write-Host "❌ ERROR: Expected exactly 10 scenarios!" -ForegroundColor Red
            continue
        }

        Write-Host "`nGenerated Scenarios:`n" -ForegroundColor Cyan

        $index = 1
        foreach ($scenario in $response.scenarios) {
            Write-Host "$index. $scenario"
            $index++
        }

        Write-Host "`n✅ Test Passed for '$concept'" -ForegroundColor Green
    }
    catch {
        Write-Host "❌ ERROR: Unable to fetch response from API" -ForegroundColor Red
        Write-Host $_
    }

    Write-Host "`nPress Enter to continue to next test..."
    Read-Host
}

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "All demo tests completed successfully." -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
