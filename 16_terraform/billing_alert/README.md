# Alerta de Budget AWS com Terraform

Este repositório contém o código Terraform necessário para configurar um alerta de budget na AWS utilizando o serviço AWS Budgets. O alerta notificará por e-mail quando o orçamento definido for atingido.

## Pré-requisitos

Antes de executar o código Terraform, você precisa ter o seguinte:

- Terraform instalado (versão >= 1.5.1). Consulte as instruções de instalação em: [Instalando o Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli)
- AWS CLI instalado. Consulte as instruções de instalação em: [Instalando a AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
- Credenciais da AWS configuradas no AWS CLI. Você pode configurá-las executando o comando `aws configure` e fornecendo a chave de acesso e a chave secreta da sua conta da AWS. Para mais informações, consulte: [Configuração do AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)

## Uso

Após atender aos pré-requisitos, siga estas etapas para executar o código Terraform e criar o alerta de budget:

1.  Clone este repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd <DIRETORIO_DO_REPOSITORIO>
```

2. Execute o seguinte comando para verificar as alterações que serão realizadas:

```
terraform plan -var="email=seu-email@example.com"
```

3. Se as alterações planejadas estiverem corretas, execute o seguinte comando para aplicar as alterações, substituindo `seu-email@example.com` pelo seu endereço de e-mail:

```
terraform apply -var="email=seu-email@example.com"
```

4. Confirme a execução digitando `yes` quando solicitado.

O Terraform criará o alerta de budget na AWS. Quando o orçamento definido for atingido, você receberá uma notificação por e-mail no endereço fornecido.

# Limpeza dos recursos criados

Se você deseja remover o alerta de budget e os recursos criados por este código do Terraform, execute o seguinte comando:

```
terraform destroy
```

Isso irá destruir o alerta de budget e os recursos gerenciados pelo Terraform na AWS.