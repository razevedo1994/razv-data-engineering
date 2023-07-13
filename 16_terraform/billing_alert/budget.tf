variable "email" {
  description = "Endereço de e-mail para receber notificações de faturamento"
  type        = string
  default     = "seu-email@example.com"  # Valor padrão, pode ser substituído na linha de comando ou no arquivo de variáveis
}

resource "aws_budgets_budget" "cost" {
    name                = "account-billing-monitoring"
    budget_type         = "COST"
    limit_amount        = "5"
    limit_unit          = "USD"
    time_period_start   = "2023-07-12_00:00"
    time_period_end     = "2040-12-31_00:00"
    time_unit           = "MONTHLY"


    notification {
    comparison_operator        = "GREATER_THAN"
    threshold                  = 100
    threshold_type             = "PERCENTAGE"
    notification_type          = "FORECASTED"
    subscriber_email_addresses = [var.email]
  }
}