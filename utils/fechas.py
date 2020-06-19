from django.conf import settings
from datetime import datetime


meses_3digitos = {
    'Ene': '01',
    'Feb': '02',
    'Mar': '03',
    'Abr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Ago': '08',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dic': '12'
}

meses_2digitos = {
    '01': 'Ene',
    '02': 'Feb',
    '03': 'Mar',
    '04': 'Abr',
    '05': 'May',
    '06': 'Jun',
    '07': 'Jul',
    '08': 'Ago',
    '09': 'Sep',
    '10': 'Oct',
    '11': 'Nov',
    '12': 'Dic'
}


def get_periodos(anio_final=datetime.now().year):
    periodo_ini = settings.PERIODO_INI_SYSTEM
    anio = str(anio_final+1)
    periodo_fin = anio+'12'

    periodos = []
    while periodo_ini != periodo_fin:
        periodos.append(periodo_ini)
        periodo_ini = next_periodo(periodo_ini)
    periodos.append(periodo_fin)

    return periodos


def next_periodo(periodo):
    anio = int(periodo[0:4])
    mes = int(periodo[4:6])
    if mes == 12:
        return str((anio+1))+'01'
    else:
        new_mes = mes+1
        mes_str = str(new_mes) if new_mes >= 10 else '0' + str(new_mes)
        return str(anio)+mes_str


def previous_periodo(periodo):
    anio = int(periodo[0:4])
    mes = int(periodo[4:6])
    if mes == 1:
        return str((anio-1))+'12'
    else:
        new_mes = mes-1
        mes_str = str(new_mes) if new_mes >= 10 else '0' + str(new_mes)
        return str(anio)+mes_str


def get_date_db(fecha):
    if len(fecha) == 11:
        # formato dd/mmm/yyyy
        dia = fecha[0:2]
        mes = get_mes_2digitos(fecha[3:6])
        anio = fecha[7:11]
        return anio+'-'+mes+'-'+dia


def get_mes_2digitos(mes):
    return meses_3digitos.get(mes, 'error en mes')
