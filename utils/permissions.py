from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from permisos.models import Modulos, UsersModulos
from settings.models import Settings

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
    user_modulo = UsersModulos.objects.get(user_id=user.id, modulo_id=modulo_user)
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
