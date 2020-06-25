from ..ValoresDefecto import ValoresDefecto
from django.conf import settings
from settings.models import Zonas
from status.models import Status
from django.apps import apps
# from utils.permissions import get_settings


class ZonasClass(ValoresDefecto):
    def __init__(self):
        ValoresDefecto.__init__(self)
        self.modelo_name = 'Zonas'
        self.modelo_id = 'zona_id'
        self.modelo_app = 'settings'
        self.modulo_id = settings.MOD_ZONAS

        # variables de session
        self.modulo_session = "zonas"
        self.columna = "zona"
        self.variable, self.variable_defecto = "ss_zona", ''
        self.variable_page = "ss_page"
        self.variable_page_defecto = "1"
        self.variable_order = "ao_zonas"
        self.variable_order_value = self.columna
        self.variable_order_type = "ao_type"

        # control del formulario
        self.control_form = "txt|2|S|zona|"

    def index(self, request):
        ValoresDefecto.index(self, request)
        self.filtros_modulo.clear()
        self.filtros_modulo['status_id_id__in'] = [self.activo, self.inactivo]
        if self.variable_val != "":
            self.filtros_modulo['zona__icontains'] = self.variable_val

        # paginacion, paginas y definiendo el LIMIT *,*
        self.paginacion()
        # asigamos la paginacion a la session
        request.session[self.modulo_session]['pages_list'] = self.pages_list

        # recuperamos los datos
        return self.getLista()

    def isInDB(self, id, nuevo_valor):
        """verificamos si existe en la base de datos"""
        modelo = apps.get_model(self.modelo_app, self.modelo_name)
        filtros = {}
        filtros['status_id_id__in'] = [self.activo, self.inactivo]
        filtros['zona__iexact'] = nuevo_valor
        if id:
            cantidad = modelo.objects.filter(**filtros).exclude(pk=id).count()
        else:
            cantidad = modelo.objects.filter(**filtros).count()

        # si no existe
        if cantidad > 0:
            return True

        return False

    def add(self, request):
        """aniadimos una nueva zona"""
        if not self.isInDB(None, request.POST['zona']):
            zona_id = self.getMaxId(self)
            status_activo = Status.objects.get(pk=self.activo)
            zona = Zonas.objects.create(zona_id=zona_id, zona=request.POST['zona'], status_id=status_activo, created_at='now', updated_at='now')
            zona.save()
            self.error_operation = ""
            return True
        else:
            self.error_operation = "Ya existe esta zona: " + request.POST['zona']
            return False

    def modify(self, request, id):
        """modificamos la zona"""
        if not self.isInDB(id, request.POST['zona']):

            zona = Zonas.objects.get(pk=id)
            zona.zona = request.POST['zona']
            zona.updated_at = 'now'
            zona.save()
            self.error_operation = ""
            return True
        else:
            self.error_operation = "Ya existe esta zona: " + request.POST['zona']
            return False

    def canDelete(self, id):
        """verificando si se puede eliminar o no la tabla"""
        tablas = ['socios']
        # for tabla in tablas:
        #     datos
