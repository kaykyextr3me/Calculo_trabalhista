import sistema


def principal(nome, sal, data_ass, data_rec, validar_ferias, motivo):
    import datetime

    data_assinatura = datetime.datetime.strptime(data_ass, '%Y-%m-%d').date()
    data_recisao = datetime.datetime.strptime(data_rec, '%Y-%m-%d').date()
    salario = int(sal)

    seumano = sistema.fse_um_ano(data_assinatura, data_recisao)
    anos_trabalhados = sistema.calculo_anos_trabalhados(data_assinatura, data_recisao)
    saldo_conta = sistema.fsaldo_conta(salario, data_recisao)
    if validar_ferias == 1:
        valor_ferias = sistema.f_valor_ferias(salario, seumano, data_recisao)
    else:
        valor_ferias = 0
    if seumano:
        valor_13salario = sistema.fdecimo_terceiro(salario, data_recisao)
    else:
        valor_13salario = salario
    desconto_inss = sistema.fdesconto_inss(salario, saldo_conta, valor_13salario)
    desconto_irpf = sistema.desconto_irpf(salario, desconto_inss)
    qtd_dias_aviso = sistema.fcalculo_qtd_dias_avisos(anos_trabalhados)
    valor_aviso = sistema.fvalor_aviso(salario, qtd_dias_aviso)
    multa_fgts = sistema.multa_fgts(saldo_conta)

    if motivo == 1:
        multa_fgts = sistema.multa_fgts(saldo_conta)
        acerto = (saldo_conta + multa_fgts + valor_ferias + valor_aviso + valor_13salario) - (
                desconto_inss + desconto_irpf)

    elif motivo == 2:
        multa_fgts = 0
        acerto = (saldo_conta + valor_ferias) - (desconto_inss + desconto_irpf)

    elif motivo == 3:
        multa_fgts = 0
        acerto = saldo_conta + valor_13salario + valor_ferias

    elif motivo == 4:
        multa_fgts = 0
        acerto = (saldo_conta + valor_ferias + valor_13salario + valor_aviso) - (desconto_inss + desconto_irpf)

    else:
        acerto = (saldo_conta + multa_fgts + valor_ferias + valor_13salario + valor_aviso) - (
                desconto_inss + desconto_irpf)

    return acerto
