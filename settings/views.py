from django.shortcuts import render
from .models import Settings
from .models import Zonas
from utils.permissions import verificar_permiso_usuario, get_permisos_usuario
from utils.fechas import get_periodos, get_date_db
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

# clases por modulo
from clases.settings.ZonasClass import ZonasClass


@user_passes_test(lambda user: verificar_permiso_usuario(user, 15, 'lista'), 'without_permission')
def settings_index(request):
    # settings = Settings.objects.order_by('-list_date').filter(is_published=True)
    permisos = get_permisos_usuario(request.user, 15)

    if request.method == 'POST':
        if permisos.modificar:
            settings = Settings.objects.get(pk=1)

            empresa = request.POST['empresa']
            direccion = request.POST['direccion']
            ciudad = request.POST['ciudad']
            telefonos = request.POST['telefonos']
            actividad = request.POST['actividad']
            fecha_sistema = get_date_db(request.POST['fecha_sistema'])
            costo_m3 = request.POST['costo_m3']

            settings.empresa = empresa
            settings.direccion = direccion
            settings.ciudad = ciudad
            settings.telefonos = telefonos
            settings.actividad = actividad
            settings.usar_fecha_servidor = request.POST['usar_fecha_servidor']
            settings.fecha_sistema = fecha_sistema
            settings.cant_per_page = request.POST['cant_per_page']
            settings.cant_lista_cobranza = request.POST['cant_lista_cobranza']
            settings.costo_m3 = costo_m3
            settings.costo_minimo = request.POST['costo_minimo']
            settings.unidad_minima_m3 = request.POST['unidad_minima_m3']
            settings.multa_pasivo = request.POST['multa_pasivo']
            settings.periodo_ini = request.POST['periodo_ini']
            settings.periodo_fin = request.POST['periodo_fin']
            #settings.costo_m3 = 525.55

            #settings.save(update_fields=['empresa', 'direccion', 'ciudad', 'telefonos', 'actividad', 'usar_fecha_servidor', 'fecha_sistema', 'cant_per_page', 'cant_lista_cobranza', 'costo_m3'])
            settings.save()

            # mensaje en pantalla
            messages.add_message(request, messages.SUCCESS, {'type': 'success', 'title': 'Configuraciones!', 'description': 'Datos guardados correctamente'})

        else:
            # no tiene permiso
            # mensaje en pantalla
            messages.add_message(request, messages.SUCCESS, {'type': 'danger', 'title': 'Configuraciones!', 'description': 'No tiene permiso para realizar esta operacion'})

    settings = Settings.objects.get(pk=1)
    periodos = get_periodos()
    context = {
        'settings': settings,
        'periodos': periodos,
        'permisos': permisos
    }
    return render(request, 'settings/settings.html', context)


# zonas
@user_passes_test(lambda user: verificar_permiso_usuario(user, 14, 'lista'), 'without_permission')
def zonas_index(request):
    # request.session['modulo'] = 'zonas'
    # modulo_actual = request.session['modulo']

    # restricciones = {'zona_id__gte': 1, 'zona_id__lte': 20000}
    # print(restricciones)
    # #zonas = Zonas.objects.filter(zona_id__gte=2, zona_id__lte=4)
    # zonas = Zonas.objects.filter(**restricciones)[4:6]
    # # print(zonas)

    zonas_class = ZonasClass()
    #id_max = zonas_class.getMaxId()
    #print('id_max', id_max)
    zonas = zonas_class.index(request)
    zonas_session = request.session[zonas_class.modulo_session]
    print(zonas_session)
    context = {
        'zonas': zonas,
        'session': zonas_session,
    }
    return render(request, 'settings/zonas.html', context)
