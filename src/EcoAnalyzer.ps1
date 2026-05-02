Import-Module Pode

Start-PodeServer {
    Listen localhost 8080 Http

    # Endpoint principal de análisis
    Add-PodeRoute -Method Get -Path '/analyze' -ScriptBlock {
        $text = $WebEvent.Query['text']
        $env = [System.Environment]::GetEnvironmentVariable("APP_ENV") ?? "PRE"
        
        # Simulación de huella de carbono basada en longitud del texto
        $carbonFootprint = ($text.Length) * 0.002
        
        Write-PodeJsonResponse -Value @{
            'input' = $text
            'environment' = $env
            'estimated_carbon_gco2' = $carbonFootprint
            'status' = 'Success'
        }
    }

    # Health Check
    Add-PodeRoute -Method Get -Path '/health' -ScriptBlock {
        Write-PodeJsonResponse -Value @{ 
            'status' = 'Healthy'
            'version' = '1.1.0'
        }
    }
}
