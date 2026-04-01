"""
Arquivo de Configuração - Automação EFD-REINF
==============================================

Este arquivo centraliza todas as configurações do sistema de automação.
Modifique os valores conforme necessário para seu ambiente e dados.
"""

# ============================================================
# CONFIGURAÇÕES GERAIS
# ============================================================

# URL base do sistema EFD-REINF
URL_BASE = 'https://cav.receita.fazenda.gov.br/ecac/Aplicacao.aspx?id=10019&origem=menu'

# Arquivo Excel com os dados para processamento
ARQUIVO_EXCEL = ''

# Nome da planilha/aba no Excel
PLANILHA = ''

# Arquivo do banco de dados para checkpoints
BANCO_DADOS = ''

# Modo de operação:
# - "inclusao": fluxo atual de inclusão/envio
# - "retificacao": altera valor de titulares já enviados
MODO_OPERACAO = "inclusao"

# ============================================================
# DADOS DA EMPRESA
# ============================================================

# Período de apuração (formato MM/AAAA)
PERIODO_APURACAO = "00/0000"

# CNPJ da empresa (formato 00.000.000/0000-00)
CNPJ_EMPRESA = "00.000.000/0000-00"

# CNPJ padrão da operadora de saúde (formato 00.000.000/0000-00)
CNPJ_OPERADORA_PADRAO = "00.000.000/0000-00"

# ============================================================
# CONFIGURAÇÕES DE TEMPO E ESPERA
# ============================================================

# Tempo de espera para o aplicativo de assinatura (segundos)
TEMPO_ESPERA_ASSINADOR = 10

# Timeout padrão para WebDriverWait (segundos)
TIMEOUT_WEBDRIVER = 10

# Timeout para aguardar alerta de sucesso da assinatura (segundos)
TIMEOUT_ALERTA_SUCESSO = 60

# Timeout para localizar próximo CPF (segundos)
TIMEOUT_PROXIMO_CPF = 15

# Timeout para busca e abertura de evento na retificação (segundos)
RETIFICACAO_TIMEOUT_LISTAR = 15

# Timeout para mensagem de sucesso após concluir retificação (segundos)
RETIFICACAO_TIMEOUT_SUCESSO = 60

# Tempo de espera para cliques (usado nos métodos de assinatura)
TEMPO_ESPERA_CLIQUE = 0.5

# Intervalo aleatório para digitação (min, max em segundos)
INTERVALO_DIGITACAO_MIN = 0.01
INTERVALO_DIGITACAO_MAX = 0.03

# Intervalo aleatório para espera geral (min, max em segundos)
INTERVALO_ESPERA_MIN = 0.2
INTERVALO_ESPERA_MAX = 0.6

# ============================================================
# CONFIGURAÇÕES DO CHROME
# ============================================================

# Versão do Chrome
CHROME_VERSION = 142

# Diretório do perfil Chrome para automação
CHROME_PROFILE_DIR = 'chrome_efd'

# Argumentos do Chrome
CHROME_ARGS = [
    '--disable-blink-features=AutomationControlled',
    '--disable-dev-shm-usage',
    '--no-sandbox',
    '--disable-extensions',
    '--disable-plugins',
    '--disable-images',
    '--disable-javascript',
    '--disable-plugins-discovery',
    '--disable-background-networking',
    '--disable-background-timer-throttling',
    '--disable-backgrounding-occluded-windows',
    '--disable-renderer-backgrounding'
]

# ============================================================
# CONFIGURAÇÕES DO PYAUTOGUI
# ============================================================

# Ativar/desativar failsafe (mover mouse para canto cancela)
PYAUTOGUI_FAILSAFE = True

# Pausa entre ações do PyAutoGUI (segundos)
PYAUTOGUI_PAUSE = 0.1

# Configurações dos métodos de assinatura
ASSINATURA_METODO_A_INTERVALO = 0.3  # Intervalo entre teclas (segundos)
ASSINATURA_METODO_B_INTERVALO = 0.5  # Intervalo entre click e enter (segundos)

# Método de assinatura padrão (1=Método A, 2=Método B)
METODO_ASSINATURA_PADRAO = 2

# Coordenadas do mouse para Método B (x, y) - None se não configurado
COORDENADAS_MOUSE_METODO_B = None

# ============================================================
# CONFIGURAÇÕES DE VERIFICAÇÃO
# ============================================================

# Opção padrão para verificação manual de dados (True/False)
VERIFICACAO_MANUAL_PADRAO = True

# ============================================================
# TEMPOS DE ESPERA ESPECÍFICOS (valores hardcoded removidos)
# ============================================================

# Tempo de espera ao detectar execução via script (segundos)
TEMPO_ESPERA_SCRIPT = 1

# Tempo de espera para processamento de páginas (segundos)
TEMPO_PROCESSAMENTO_PAGINA = 0.2

# Timeout para WebDriverWait em modais e elementos específicos (segundos)
TIMEOUT_MODAL = 3

# Tempo de espera antes de enviar declaração (segundos)
TEMPO_ANTES_ENVIO = 1

# Tempo de espera após scroll para visibilidade (segundos)
TEMPO_APOS_SCROLL = 0.2

# Tempo de espera após envio da declaração (segundos)
TEMPO_APOS_ENVIO = 2

# Tempo de espera antes de clicar próximo CPF (segundos)
TEMPO_ANTES_PROXIMO_CPF = 0.5

# Tempo de espera após clicar próximo CPF (segundos)
TEMPO_APOS_PROXIMO_CPF = 1

# Tempo de espera entre grupos (segundos)
TEMPO_ENTRE_GRUPOS = 0.5

# Tempo de espera quando confirmação não é detectada (segundos)
TEMPO_CONFIRMACAO_NAO_DETECTADA = 5

# Tempo de espera quando há erro na assinatura (segundos)
TEMPO_ERRO_ASSINATURA = 10

# Tempo de espera em modo automático antes do envio (segundos)
TEMPO_MODO_AUTOMATICO = 1

# Tempo de espera em execução via script durante verificação (segundos)
TEMPO_SCRIPT_VERIFICACAO = 2

# ============================================================
# SELETORES CSS - FLUXO DE RETIFICAÇÃO
# ============================================================
#
# Preencha com "Copy selector" dos elementos da tela de retificação.
# Os valores abaixo são placeholders e devem ser ajustados no config.py.

RETIFICACAO_SELETOR_CAMPO_CPF = '#cpf_beneficiario'
RETIFICACAO_SELETOR_BOTAO_LISTAR = '[data-testid="botao_listar"]'
RETIFICACAO_SELETOR_BOTAO_RETIFICAR = '[data-testid="botao_retificar"]'
RETIFICACAO_SELETOR_BOTAO_ALTERAR_TITULAR = '[data-testid="botao_alterar_titular"]'
RETIFICACAO_SELETOR_CAMPO_VALOR_PAGO = '#vlr_pago_titular'
RETIFICACAO_SELETOR_BOTAO_SALVAR = '[data-testid="botao_salvar"]'
RETIFICACAO_SELETOR_BOTAO_CONCLUIR_ENVIAR = '[data-testid="botao_concluir_enviar"]'
RETIFICACAO_SELETOR_MENSAGEM_SUCESSO = '[data-testid="mensagem_sucesso"]'
RETIFICACAO_SELETOR_BOTAO_VOLTAR_LISTA = '[data-testid="botao_voltar_lista_eventos"]'

# ============================================================
# CONFIGURAÇÕES DE TESTE (para funções de demonstração)
# ============================================================

# Intervalos para testes de métodos de assinatura (segundos)
TESTE_METODO_A_INTERVALO = 0.3
TESTE_METODO_B_INTERVALO_CLICK = 0.5
TESTE_METODO_B_INTERVALO_FINAL = 0.5
