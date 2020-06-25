from django.shortcuts import get_object_or_404, render
from .models import Settings
from .models import Zonas
from utils.permissions import verificar_permiso_usuario, get_permisos_usuario, get_restricciones_columna
from utils.fechas import get_periodos, get_date_db, get_periodos_mostrar
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
# settings de la app
from django.conf import settings

# clases por modulo
from clases.settings.ZonasClass import ZonasClass

# reverse url
from django.urls import reverse
from django.http import HttpResponseRedirect
from urllib.parse import urlencode


@user_passes_test(lambda user: verificar_permiso_usuario(user, settings.MOD_CONFIGURACIONES_SISTEMA, 'lista'), 'without_permission')
def settings_index(request):
    # settings = Settings.objects.order_by('-list_date').filter(is_published=True)
    permisos = get_permisos_usuario(request.user, settings.MOD_CONFIGURACIONES_SISTEMA)

    if request.method == 'POST':
        if permisos.modificar:
            settings_sistema = Settings.objects.get(pk=1)

            empresa = request.POST['empresa']
            direccion = request.POST['direccion']
            ciudad = request.POST['ciudad']
            telefonos = request.POST['telefonos']
            actividad = request.POST['actividad']
            fecha_sistema = get_date_db(request.POST['fecha_sistema'])
            costo_m3 = request.POST['costo_m3']

            settings_sistema.empresa = empresa
            settings_sistema.direccion = direccion
            settings_sistema.ciudad = ciudad
            settings_sistema.telefonos = telefonos
            settings_sistema.actividad = actividad
            settings_sistema.usar_fecha_servidor = request.POST['usar_fecha_servidor']
            settings_sistema.fecha_sistema = fecha_sistema
            settings_sistema.cant_per_page = request.POST['cant_per_page']
            settings_sistema.cant_lista_cobranza = request.POST['cant_lista_cobranza']
            settings_sistema.costo_m3 = costo_m3
            settings_sistema.costo_minimo = request.POST['costo_minimo']
            settings_sistema.unidad_minima_m3 = request.POST['unidad_minima_m3']
            settings_sistema.multa_pasivo = request.POST['multa_pasivo']
            settings_sistema.periodo_ini = request.POST['periodo_ini']
            settings_sistema.periodo_fin = request.POST['periodo_fin']
            # settings.costo_m3 = 525.55

            # settings.save(update_fields=['empresa', 'direccion', 'ciudad', 'telefonos', 'actividad', 'usar_fecha_servidor', 'fecha_sistema', 'cant_per_page', 'cant_lista_cobranza', 'costo_m3'])
            settings_sistema.save()

            # mensaje en pantalla
            messages.add_message(request, messages.SUCCESS, {'type': 'success', 'title': 'Configuraciones!', 'description': 'Datos guardados correctamente'})

        else:
            # no tiene permiso
            # mensaje en pantalla
            messages.add_message(request, messages.SUCCESS, {'type': 'danger', 'title': 'Configuraciones!', 'description': 'No tiene permiso para realizar esta operacion'})

    settings_sistema = Settings.objects.get(pk=1)
    periodos = get_periodos()
    periodos_mostrar = get_periodos_mostrar(periodos)

    periodos2 = get_periodos()
    periodos2_mostrar = get_periodos_mostrar(periodos2)

    periodos_datos = zip(periodos, periodos_mostrar)
    periodos_datos2 = zip(periodos2, periodos2_mostrar)

    context = {
        'settings': settings_sistema,
        'periodos': periodos,
        'periodos_mostrar': periodos_mostrar,
        'periodos_datos': periodos_datos,
        'periodos_datos2': periodos_datos2,
        'permisos': permisos
    }
    return render(request, 'settings/settings.html', context)


# zonas
@user_passes_test(lambda user: verificar_permiso_usuario(user, settings.MOD_ZONAS, 'lista'), 'without_permission')
def zonas_index(request):
    # request.session['modulo'] = 'zonas'
    # modulo_actual = request.session['modulo']

    # restricciones = {'zona_id__gte': 1, 'zona_id__lte': 20000}
    # print(restricciones)
    # #zonas = Zonas.objects.filter(zona_id__gte=2, zona_id__lte=4)
    # zonas = Zonas.objects.filter(**restricciones)[4:6]
    # # print(zonas)
    permisos = get_permisos_usuario(request.user, settings.MOD_ZONAS)
    zonas_class = ZonasClass()
    # operation
    # request.session[zonas_class.modulo_session]['operation_x'] = ''
    # request.session.modified = True

    if 'operation_x' in request.POST.keys():
        operation = request.POST['operation_x']
        if not operation in ['add', 'modify', 'delete']:
            url = reverse('without_permission')
            return HttpResponseRedirect(url)

        # print('operacion', request.POST.values(), request.POST['operation_x'])
        # request.session[zonas_class.modulo_session]['operation_x'] = request.POST['operation_x']
        # request.session.modified = True

        if operation == 'add':
            url = reverse('zonas_add')
            return HttpResponseRedirect(url)

        if operation == 'modify':
            url = reverse('zonas_modify', kwargs={'zona_id': request.POST['id']})
            return HttpResponseRedirect(url)

        if operation == 'delete':
            url = reverse('zonas_delete', kwargs={'zona_id': request.POST['id']})
            return HttpResponseRedirect(url)

    # verificamos mensajes
    if 'nuevo_mensaje' in request.session.keys():
        messages.add_message(request, messages.SUCCESS, request.session['nuevo_mensaje'])
        del request.session['nuevo_mensaje']
        request.session.modified = True

    # datos por defecto
    url_main = reverse('zonas')
    zonas = zonas_class.index(request)
    zonas_session = request.session[zonas_class.modulo_session]
    # print(zonas_session)
    context = {
        'zonas': zonas,
        'session': zonas_session,
        'permisos': permisos,
        'url_main': url_main,
    }
    return render(request, 'settings/zonas.html', context)


# zona add
@user_passes_test(lambda user: verificar_permiso_usuario(user, settings.MOD_ZONAS, 'adicionar'), 'without_permission')
def zona_add(request):
    # url modulo
    url_main = reverse('zonas')
    zonas_class = ZonasClass()

    # guardamos
    existe_error = False
    if 'add_x' in request.POST.keys():
        if zonas_class.add(request):
            # messages.add_message(request, messages.SUCCESS, {'type': 'success', 'title': 'Zonas!', 'description': 'Se agrego la nueva zona'})
            request.session['nuevo_mensaje'] = {'type': 'success', 'title': 'Zonas!', 'description': 'Se agrego la nueva zona: '+request.POST['zona']}
            request.session.modified = True
            return HttpResponseRedirect(url_main)
        else:
            # error al adicionar
            existe_error = True
            messages.add_message(request, messages.SUCCESS, {'type': 'warning', 'title': 'Zonas!', 'description': zonas_class.error_operation})

    # restricciones de columna
    if existe_error:
        db_tags = get_restricciones_columna(Zonas, request, None, 'zona', 'status_id')
    else:
        db_tags = get_restricciones_columna(Zonas, None, None, 'zona', 'status_id')
    context = {
        'url_main': url_main,
        'operation_x': 'add',
        'db_tags': db_tags,
        'control_form': zonas_class.control_form,
        'js_file': zonas_class.modulo_session,
    }
    return render(request, 'settings/zona.html', context)


# zona modify
@ user_passes_test(lambda user: verificar_permiso_usuario(user, settings.MOD_ZONAS, 'modificar'), 'without_permission')
def zona_modify(request, zona_id):
    # url modulo
    url_main = reverse('zonas')
    zona = get_object_or_404(Zonas, pk=zona_id)
    zonas_class = ZonasClass()

    # guardamos
    existe_error = False
    if 'modify_x' in request.POST.keys():
        if zonas_class.modify(request, zona_id):
            # messages.add_message(request, messages.SUCCESS, {'type': 'success', 'title': 'Zonas!', 'description': 'Se agrego la nueva zona'})
            request.session['nuevo_mensaje'] = {'type': 'success', 'title': 'Zonas!', 'description': 'Se modifico la zona: '+request.POST['zona']}
            request.session.modified = True
            return HttpResponseRedirect(url_main)
        else:
            # error al adicionar
            existe_error = True
            messages.add_message(request, messages.SUCCESS, {'type': 'warning', 'title': 'Zonas!', 'description': zonas_class.error_operation})

    # restricciones de columna
    if existe_error:
        db_tags = get_restricciones_columna(Zonas, request, zona, 'zona', 'status_id')
    else:
        db_tags = get_restricciones_columna(Zonas, None, zona, 'zona', 'status_id')

    context = {
        'url_main': url_main,
        'operation_x': 'modify',
        'zona': zona,
        'db_tags': db_tags,
        'control_form': zonas_class.control_form,
        'js_file': zonas_class.modulo_session,
    }
    return render(request, 'settings/zona.html', context)


# zona delete
@ user_passes_test(lambda user: verificar_permiso_usuario(user, settings.MOD_ZONAS, 'eliminar'), 'without_permission')
def zona_delete(request, zona_id):
    # url modulo
    url_main = reverse('zonas')
    zona = get_object_or_404(Zonas, pk=zona_id)
    zonas_class = ZonasClass()

    # restricciones de columna
    db_tags = get_restricciones_columna(Zonas, None, zona, 'zona', 'status_id')

    context = {
        'url_main': url_main,
        'operation_x': 'delete',
        'zona': zona,
        'db_tags': db_tags,
        'control_form': zonas_class.control_form,
        'js_file': zonas_class.modulo_session,
    }
    return render(request, 'settings/zona.html', context)
