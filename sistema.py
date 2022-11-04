def fsaldo_conta(renda, data_demissao):
    dia_demissao = str(data_demissao)
    valor_dia = renda / 30
    dia_demissao = dia_demissao[-2:]
    return valor_dia * int(dia_demissao)


def fse_um_ano(data_contratacao, data_recisao):
    tempo = data_recisao - data_contratacao
    tempo_segundos = tempo.total_seconds()
    if ((((tempo_segundos / 60) / 60) / 24) / 30) / 12 > 1:
        return True
    else:
        return False


def calculo_anos_trabalhados(data_contratacao, data_recisao):
    strdata_contratacao = str(data_contratacao)
    strdata_recisao = str(data_recisao)
    return int(strdata_recisao[:4]) - int(strdata_contratacao[:4])


def multa_fgts(saldo_conta):
    return saldo_conta * 0.4


def fcalculo_qtd_dias_avisos(anos_trabalhados):
    qtd = 30 + (anos_trabalhados * 3)
    if qtd > 90:
        qtd = 90
    return qtd


def fvalor_aviso(salario, qtd_dias_aviso):
    return (salario / 30) * qtd_dias_aviso


def fdesconto_inss(salario, saldo_conta, decterceiro):
    if salario < 1212:
        desconto = (saldo_conta * 0.075) + (decterceiro * 0.075)
    elif 1212.01 < salario < 2427.35:
        desconto = (saldo_conta * 0.09) + (decterceiro * 0.09)
    elif 2427.36 < salario < 3641.03:
        desconto = (saldo_conta * 0.12) + (decterceiro * 0.12)
    elif 3641.04 < salario < 7087.22:
        desconto = (saldo_conta * 0.14) + (decterceiro * 0.14)
    else:
        desconto = 0
    return desconto


def desconto_irpf(salario, desconto_inss):
    base = salario - desconto_inss
    if base < 1903.98:
        irpf = 0
    elif 1903.99 < base < 2826.65:
        irpf = base * 0.075
    elif 2826.66 < base < 3751.05:
        irpf = base * 0.15
    elif 3751.06 < base < 4664.68:
        irpf = base * 0.225
    else:
        irpf = base * 0.275
    return irpf


def fdecimo_terceiro(salario, data_demissao):
    strdata_demissao = str(data_demissao)
    return (salario / 12) * int(strdata_demissao[5:7])


def f_valor_ferias(salario, seuumano, data_demissao):
    terco_ferias = salario / 3
    if seuumano:
        valor_ferias = salario + terco_ferias
    else:
        strtatademissao = str(data_demissao)
        valor_ferias = (salario / 12 * int(strtatademissao[4:7])) + terco_ferias
        print(f'Foi demitido no mes {strtatademissao[4:7]}')

    return valor_ferias


def motivo_despensa():
    lista_motivo = ['Sem Justa Causa',
                    'Com Justa Causa',
                    'Fim de Contrato',
                    'Pedido de Demissão',
                    'Recisão Indireta'
                    ]
    return lista_motivo