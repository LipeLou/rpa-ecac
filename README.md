# 🤖 Automação EFD-REINF

> Sistema completo para automatizar o preenchimento de declarações de imposto de renda (plano de saúde) da Receita Federal com assinatura eletrônica automática.

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-4.15.2-green.svg)](https://selenium.dev)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


## 🚀 Características

- ✅ **100% Automático** - Assinatura eletrônica automatizada
- ✅ **Sistema de Checkpoints** - Retoma de onde parou
- ✅ **Gestão Inteligente** - Pula CPFs já processados e grupos sem valor
- ✅ **Validação Automática** - Ignora titulares/dependentes sem plano ativo
- ✅ **Tratamento de Erros** - Registra erros no checkpoint para análise
- ✅ **Relatórios Detalhados** - Acompanhamento completo


## 📋 Pré-requisitos

- Python 3.13+
- Google Chrome
- Assinador Serpro (ou equivalente)


## ⚡ Instalação

### Windows
```bash
# Execução rápida (recomendado)
.\executar.bat

# Ou manualmente
venv\Scripts\activate
python automacao_efd.py
```

### Linux/Mac
```bash
# Execução rápida
source venv/bin/activate
python automacao_efd.py
```


## 🎯 Como Usar

1. **Configure** os dados da empresa em `config.py` (use o `config-template.py` e substitua para **config.py**)
2. **Adicione** a planilha `dados.xlsx` com os CPFs
3. **Execute** o sistema
4. **Faça login** manual no site da Receita (apenas uma vez)
5. **Aguarde** o processamento automático

### Fluxo Automático
```
📂 Lê Excel → 🌐 Abre Chrome → 🔐 Login Manual → 🤖 Processa Todos → 📊 Gera Relatórios
```


## ⚙️ Configuração

### Configurações Básicas (`config.py`)

Edite o `config.py` para configurar os dados da empresa e comportamento:

```python
# Dados da empresa
PERIODO_APURACAO = "00/0000"
CNPJ_EMPRESA = "00.000.000/0000-00"
CNPJ_OPERADORA_PADRAO = "00.000.000/0000-00"

# Planilha Excel
PLANILHA = "MÊS - ANO"  # Nome da aba no Excel (sheet)

# Comportamento
VERIFICACAO_MANUAL_PADRAO = False    # True = pausa para revisar
METODO_ASSINATURA_PADRAO = 2         # 1=Apenas teclado, 2=Mouse + teclado
CHROME_VERSION = 141                  # Versão do Chrome instalada
```


## 🔐 Métodos de Assinatura

### Método A - Teclado
```
Sequência: ↑ + ↑ + Enter
```

### Método B - Mouse + Teclado
```
Sequência: Click(x,y) + Enter
```
> Requer configuração de coordenadas após login no ECAC


## 📋 Formato da Planilha

**Arquivo:** `dados.xlsx` **| Aba:** Configurável em `config.py` (variável `PLANILHA`)

### Estrutura da Planilha

A planilha deve conter pelo menos as seguintes colunas:

| NOME | CPF | DEPENDENCIA | VALOR |
|------|-----|-------------|-------|
| João Silva | 000.000.000-00 | TITULAR | 150,00 |
| Maria Silva | 111.111.111-11 | ESPOSA | 150,00 |

**Observações:**
- A primeira linha pode ser um cabeçalho (será ignorada com `skiprows=1`) 
- Cada grupo deve começar com um `TITULAR`
- Dependentes devem estar logo após o titular correspondente
- Valores zero ou nulos são automaticamente ignorados (dependentes sem plano ativo)

### 🔗 Mapeamento de Dependências

O sistema mapeia automaticamente os valores da coluna `DEPENDENCIA` da planilha Excel para os códigos do formulário da Receita Federal. O mapeamento está definido no arquivo `automacao_efd.py` na constante `MAPEAMENTO_DEPENDENCIAS`.

#### Valores Padrão do Mapeamento

| Dependência no Excel | Código | Descrição |
|----------------------|--------|-----------|
| `TITULAR` | `None` | Titular não é dependente |
| `ESPOSA` / `ESPOSO` / `CONJUGE` | `1` | Cônjuge |
| `COMPANHEIRO(A)` / `COMPANHEIRO` / `COMPANHEIRA` / `UNIAO ESTAVEL` | `2` | Companheiro(a) com filho ou união estável |
| `FILHO` / `FILHA` / `ENTEADO` / `ENTEADA` | `3` | Filho(a) ou enteado(a) |
| `IRMAO` / `IRMA` / `NETO` / `NETA` / `BISNETO` / `BISNETA` | `6` | Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais |
| `PAI` / `MAE` / `MÃE` / `AVO` / `AVÔ` / `BISAVO` / `BISAVÔ` | `9` | Pais, avós e bisavós |
| `MENOR POBRE` / `GUARDA JUDICIAL` | `10` | Menor pobre do qual detenha a guarda judicial |
| `TUTOR` / `TUTORA` / `CURADOR` / `CURADORA` | `11` | Pessoa absolutamente incapaz, da qual seja tutor ou curador |
| `EX ESPOSA` / `EX ESPOSO` / `EX CONJUGE` | `12` | Ex-cônjuge |
| `AGREGADO` / `OUTRA DEPENDENCIA` / `SOGRO` / `SOGRA` / `OUTROS` | `99` | Agregado/Outros |

**Observações importantes:**
- O sistema faz busca **case-insensitive** (não diferencia maiúsculas/minúsculas)
- Se uma dependência não for encontrada, o sistema usa automaticamente `'99'` (Agregado/Outros)
- Você pode usar variações do mesmo tipo (ex: `'MAE'`, `'MÃE'`) - todas serão mapeadas para o mesmo código
- O mapeamento já está completo com todas as opções do formulário da Receita Federal


## 📊 Gerenciar Progresso

```bash
# Windows
.\gerenciar_db.bat

# Linux/Mac  
python gerenciar_checkpoint.py
```

**Funcionalidades disponíveis:**
- Ver status geral e estatísticas
- Buscar CPFs específicos
- Limpar dados e resetar progresso
- Exportar relatórios em Excel
- Alterar checkpoint atual
- Visualizar grupos com erro ou pulados


## 📁 Estrutura do Projeto

```
rpa-dirf/
├── main.py        # Automação principal
├── manage.py # Gerenciador de progresso  
├── config.py               # Configurações
├── dados.xlsx              # Planilha com dados
├── requirements.txt        # Dependências
├── executar.bat           # Atalho Windows (opcional)
└── gerenciar_db.bat       # Atalho Windows (opcional)
```


## 🛡️ Segurança

- **🔒 FAILSAFE**: Mover mouse para canto superior esquerdo cancela tudo
- **👤 Login manual**: Certificado digital sempre requer interação manual
- **💾 Dados locais**: Todas as informações permanecem no seu computador


## ❓ Problemas Comuns

| Problema | Solução |
|----------|---------|
| Erro de assinatura | Verificar se Assinador Serpro está rodando |
| CPF não encontrado | Verificar formato da planilha Excel |
| Certificado não funciona | Fazer login manual no navegador normal primeiro |
| Erro de versão ChromeDriver | Atualizar `CHROME_VERSION` no `config.py` com sua versão do Chrome |


## 🔄 Dependências

```txt
selenium==4.15.2
selenium-stealth>=1.0.6
pandas==2.3.3
openpyxl==3.1.5
undetected-chromedriver==3.5.5
PyAutoGUI==0.9.54
```


## 📞 Suporte

1. Verificar logs no terminal
2. Consultar checkpoints no gerenciador
3. Analisar relatórios gerados
4. Resetar progresso se necessário

---

**Desenvolvido para o SINTUNIFEI** | Sistema de envio de declarações no e-cac
