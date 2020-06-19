from ..ValoresDefecto import ValoresDefecto
from django.conf import settings
from settings.models import Zonas
#from utils.permissions import get_settings


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
