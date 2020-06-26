from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from permisos.models import Modulos, UsersModulos
from settings.models import Settings

from django.db.models.fields import CharField, DecimalField, IntegerField, BooleanField
from utils.custome_dbtypes import DateTimeFieldCustome, DateFieldCustome
from utils.fechas import get_date_from_db, get_datetime_from_db

user_login_required = user_passes_test(
    # lambda user: True if user.email == 'email@email3.com2' else False, login_url='/')
    lambda user: verificar_permiso(user), login_url='/')


def verificar_permiso(user):
    if user.email == 'email@email3.com':
        return True
    else:
        return False


def active_user_required(view_func):
    decorated_view_func = login_required(user_login_required(view_func))
    return decorated_view_func

# permisos del usuario, para el modulo


def get_permisos_usuario(user, modulo):
    modulo_user = Modulos.objects.get(pk=modulo)
    user_modulo = UsersModulos.objects.get(user_id=user.id, modulo_id=modulo_user)

    return user_modulo


def verificar_permiso_usuario(user, modulo, operacion):
    # print(user)
    # print(permiso)
    modulo_user = Modulos.objects.get(pk=modulo)
    #print(modulo_user, '\n')
    try:
        user_modulo = UsersModulos.objects.get(user_id=user.id, modulo_id=modulo_user)
    except UsersModulos.DoesNotExist:
        user_modulo = None
    if user_modulo:
        if operacion == 'lista':
            if user_modulo.enabled:
                return True

        if operacion == 'adicionar':
            if user_modulo.adicionar:
                return True

        if operacion == 'modificar':
            if user_modulo.modificar:
                return True

        if operacion == 'eliminar':
            if user_modulo.eliminar:
                return True

        if operacion == 'anular':
            if user_modulo.anular:
                return True

        if operacion == 'imprimir':
            if user_modulo.imprimir:
                return True

        if operacion == 'permiso':
            if user_modulo.permiso:
                return True

    # sino tiene permiso false
    return False


def get_settings():
    settings_sistema = Settings.objects.get(pk=1)
    #retorno = {}
    retorno = settings_sistema.__dict__
    # print(retorno)

    # for attr, value in settings_sistema.__dict__.iteritems():
    #     retorno[attr] = value
    #     print("Attribute: " + str(attr or ""))
    #     print("Value: " + str(value or ""))

    return retorno


def get_restricciones_columna(modelo, request, instancia, *args):
    """devuelve las restricciones segun el tipo de columna"""
    retorno = {}
    for arg in args:
        columna = modelo._meta.get_field(arg)
        if isinstance(columna, CharField):
            retorno[arg] = 'maxlength="' + str(columna.max_length) + '" onkeyup="txtValid(this);" onblur="txtValid(this);" '
            if request:
                retorno[arg] += (' value="' + request.POST[arg].replace('"', '&quot;') + '"') + F' id="{arg}"' + F' name="{arg}"'
            else:
                if instancia:
                    retorno[arg] += (' value="' + getattr(instancia, arg).replace('"', '&quot;') + '"' if instancia else '') + F' id="{arg}"' + F' name="{arg}"'
                else:
                    retorno[arg] += F' value="" id="{arg}" name="{arg}" '

        elif isinstance(columna, DecimalField):
            retorno[arg] = 'onkeyup="validarNumeroPunto(this);"'
            if request:
                retorno[arg] += (' value="' + request.POST[arg] + '"') + F' id="{arg}"' + F' name="{arg}"'
            else:
                if instancia:
                    retorno[arg] += (' value="' + str(getattr(instancia, arg)) + '"' if instancia else '') + F' id="{arg}"' + F' name="{arg}"'
                else:
                    retorno[arg] += F' value="" id="{arg}" name="{arg}" '

        elif isinstance(columna, DateFieldCustome):
            retorno[arg] = 'readonly="readonly"' + F' id="{arg}"' + F' name="{arg}" '
            if request:
                retorno[arg] += ' value="' + request.POST[arg] + '" '
            else:
                if instancia:
                    retorno[arg] += ' value="' + get_date_from_db(str(getattr(instancia, arg))) + '" '
                else:
                    retorno[arg] += ' value="" '

        elif isinstance(columna, DateTimeFieldCustome):
            retorno[arg] = 'readonly="readonly"' + F' id="{arg}"' + F' name="{arg}"'
            if request:
                retorno[arg] += ' value="' + request.POST[arg] + '" '
            else:
                if instancia:
                    retorno[arg] += ' value="' + get_date_from_db(str(getattr(instancia, arg))) + '" '
                else:
                    retorno[arg] += ' value="" '

        elif isinstance(columna, BooleanField):
            retorno[arg] = '' + F' id="{arg}"' + F' name="{arg}" '

        elif isinstance(columna, IntegerField):
            retorno[arg] = 'onkeyup="validarNumero(this)" '
            if request:
                retorno[arg] += (' value="' + request.POST[arg] + '"') + F' id="{arg}"' + F' name="{arg}" '
            else:
                if instancia:
                    retorno[arg] += (' value="' + str(getattr(instancia, arg)) + '"' if instancia else '') + F' id="{arg}"' + F' name="{arg}" '
                else:
                    retorno[arg] += F' value="" id="{arg}" name="{arg}" '

        else:
            retorno[arg] = 'sin tipo'

    return retorno
