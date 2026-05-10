Describe "Pruebas de Calidad CI" {
    It "El servicio debe estar saludable" {
        Start-Job -ScriptBlock {
            pwsh ./src/EcoAnalyzer.ps1
        } | Out-Null

        Start-Sleep -Seconds 3

        $response = Invoke-RestMethod -Uri "http://localhost:8080/health"
        $response.status | Should -Be "Healthy"
    }
}
