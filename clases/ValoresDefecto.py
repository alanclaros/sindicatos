from django.apps import apps
from django.db.models import Max
from django.conf import settings
from utils.permissions import get_settings


class ValoresDefecto(object):

    def __init__(self):
        # estados
        self.activo = int(settings.STATUS_ACTIVO)
        self.inactivo = int(settings.STATUS_INACTIVO)
        self.eliminado = int(settings.STATUS_ELIMINADO)
        self.apertura = int(settings.STATUS_APERTURA)
        self.apertura_recibe = int(settings.STATUS_APERTURA_RECIBE)
        self.cierre = int(settings.STATUS_CIERRE)
        self.cierre_recibe = int(settings.STATUS_CIERRE_RECIBE)
        self.anulado = int(settings.STATUS_ANULADO)
        self.pasivo = int(settings.STATUS_PASIVO)
        self.cobrado = int(settings.STATUS_COBRADO)
        self.no_aperturado = int(settings.STATUS_NO_APERTURADO)

        # propiedades
        self.modelo_name = 'unknow'
        self.modelo_id = 'unknow'
        self.modelo_app = 'unknow'
        self.modulo_id = 0

        # filtros para el modulo
        self.filtros_modulo = {}

        # paginacion
        self.pages_list = []
        self.pages_limit_botton = 0
        self.pages_limit_top = 0

        # control del formulario
        self.control_form = ""

        # error en las operaciones
        self.error_operation = ""

        # sesiones
        self.modulo_session = "unknow"

        # nombre variables filtros para la busqueda
        self.variable, self.variable_defecto, self.variable_val = '', '', ''
        self.variable2, self.variable2_defecto, self.variable2_val = '', '', ''
        self.variable3, self.variable3_defecto, self.variable3_val = '', '', ''
        self.variable4, self.variable4_defecto, self.variable4_val = '', '', ''
        self.variable5, self.variable5_defecto, self.variable5_val = '', '', ''
        self.variable6, self.variable6_defecto, self.variable6_val = '', '', ''
        self.variable7, self.variable7_defecto, self.variable7_val = '', '', ''
        self.variable8, self.variable8_defecto, self.variable8_val = '', '', ''
        self.variable9, self.variable9_defecto, self.variable9_val = '', '', ''
        self.variable10, self.variable10_defecto, self.variable10_val = '', '', ''

        # nombre variable pagina actual
        self.variable_page, self.variable_page_defecto, self.variable_page_val = '', 1, 1

        # nombre de las variables de orden
        self.variable_order, self.variable_order_value = "", ""
        self.variable_order_type, self.variable_order_type_value = "", ""

        # columnas para el ordenamiento
        self.columna = ""
        self.columna2 = ""
        self.columna3 = ""
        self.columna4 = ""
        self.columna5 = ""
        self.columna6 = ""
        self.columna7 = ""
        self.columna8 = ""
        self.columna9 = ""
        self.columna10 = ""

        # session de orden
        self.order_field = ""
        self.order_type = ""
        self.order_field_value = ""
        self.order_type_value = ""

    def getMaxId(self, *args):
        """return max id table"""
        modelo = apps.get_model(self.modelo_app, self.modelo_name)
        max_id = modelo.objects.all().aggregate(Max(self.modelo_id))
        valor = list(max_id.values())[0]
        #print('max_id:', valor)
        valor += 1

        return valor

    def cantidadRegistros(self):
        """cantidad de registros del modulo"""
        # print(self.filtros_modulo)
        modelo = apps.get_model(self.modelo_app, self.modelo_name)
        # print(modelo)
        #nuevo_filtro = {'status_id_id__in': [1, 2]}
        cantidad = modelo.objects.filter(**self.filtros_modulo).count()
        #cantidad = modelo.objects.filter(status_id_id__in=[1, 2]).count()
        #cantidad = modelo.objects.filter(**nuevo_filtro).count()
        # print(self.filtros_modulo)
        # print(cantidad)

        return cantidad

    def index(self, request):
        """inicializando variables de session del modulo"""
        # self.variable_val = request.session[self.modulo_session][self.variable]
        # self.variable2_val = request.session[self.modulo_session][self.variable2]
        # self.variable3_val = request.session[self.modulo_session][self.variable3]
        # self.variable4_val = request.session[self.modulo_session][self.variable4]
        # self.variable5_val = request.session[self.modulo_session][self.variable5]
        # self.variable6_val = request.session[self.modulo_session][self.variable6]
        # self.variable7_val = request.session[self.modulo_session][self.variable7]
        # self.variable8_val = request.session[self.modulo_session][self.variable8]
        # self.variable9_val = request.session[self.modulo_session][self.variable9]
        # self.variable10_val = request.session[self.modulo_session][self.variable10]
        # # pagina
        # self.variable_page_val = request.session[self.modulo_session][self.variable_page]

        # varibles de session sin iniciar
        #print(request.session.keys(), '...', self.modulo_session)
        if not self.modulo_session in request.session.keys():
            request.session[self.modulo_session] = {}
            request.session[self.modulo_session][self.variable] = self.variable_defecto
            request.session[self.modulo_session][self.variable2] = self.variable2_defecto
            request.session[self.modulo_session][self.variable3] = self.variable3_defecto
            request.session[self.modulo_session][self.variable4] = self.variable4_defecto
            request.session[self.modulo_session][self.variable5] = self.variable5_defecto
            request.session[self.modulo_session][self.variable6] = self.variable6_defecto
            request.session[self.modulo_session][self.variable7] = self.variable7_defecto
            request.session[self.modulo_session][self.variable8] = self.variable8_defecto
            request.session[self.modulo_session][self.variable9] = self.variable9_defecto
            request.session[self.modulo_session][self.variable10] = self.variable10_defecto
            # pagina
            request.session[self.modulo_session][self.variable_page] = self.variable_page_defecto
            request.session[self.modulo_session]['pages_list'] = self.pages_list
            request.session[self.modulo_session]['variable_page'] = self.variable_page
            # columnas
            request.session[self.modulo_session]['columna'] = self.columna
            request.session[self.modulo_session]['columna2'] = self.columna2
            request.session[self.modulo_session]['columna3'] = self.columna3
            request.session[self.modulo_session]['columna4'] = self.columna4
            request.session[self.modulo_session]['columna5'] = self.columna5
            request.session[self.modulo_session]['columna6'] = self.columna6
            request.session[self.modulo_session]['columna7'] = self.columna7
            request.session[self.modulo_session]['columna8'] = self.columna8
            request.session[self.modulo_session]['columna9'] = self.columna9
            request.session[self.modulo_session]['columna10'] = self.columna10
            # variables
            request.session[self.modulo_session]['variable'] = self.variable
            request.session[self.modulo_session]['variable2'] = self.variable2
            request.session[self.modulo_session]['variable3'] = self.variable3
            request.session[self.modulo_session]['variable4'] = self.variable4
            request.session[self.modulo_session]['variable5'] = self.variable5
            request.session[self.modulo_session]['variable6'] = self.variable6
            request.session[self.modulo_session]['variable7'] = self.variable7
            request.session[self.modulo_session]['variable8'] = self.variable8
            request.session[self.modulo_session]['variable9'] = self.variable9
            request.session[self.modulo_session]['variable10'] = self.variable10
            # order nombres variables
            request.session[self.modulo_session]['variable_order'] = self.variable_order
            request.session[self.modulo_session]['variable_order_type'] = self.variable_order_type
            # order
            request.session[self.modulo_session][self.variable_order] = self.columna
            request.session[self.modulo_session][self.variable_order_type] = "ASC"

        # si realiza alguna busqueda
        if 'search_button_x' in request.POST.keys():
            if self.variable.strip() != '':
                request.session[self.modulo_session][self.variable] = request.POST[self.variable]
            if self.variable2.strip() != '':
                request.session[self.modulo_session][self.variable2] = request.POST[self.variable2]
            if self.variable3.strip() != '':
                request.session[self.modulo_session][self.variable3] = request.POST[self.variable3]
            if self.variable4.strip() != '':
                request.session[self.modulo_session][self.variable4] = request.POST[self.variable4]
            if self.variable5.strip() != '':
                request.session[self.modulo_session][self.variable5] = request.POST[self.variable5]
            if self.variable6.strip() != '':
                request.session[self.modulo_session][self.variable6] = request.POST[self.variable6]
            if self.variable7.strip() != '':
                request.session[self.modulo_session][self.variable7] = request.POST[self.variable7]
            if self.variable8.strip() != '':
                request.session[self.modulo_session][self.variable8] = request.POST[self.variable8]
            if self.variable9.strip() != '':
                request.session[self.modulo_session][self.variable9] = request.POST[self.variable9]
            if self.variable10.strip() != '':
                request.session[self.modulo_session][self.variable10] = request.POST[self.variable10]
            # pagina
            request.session[self.modulo_session][self.variable_page] = self.variable_page_defecto

        # si seleccionana una pagina
        if self.variable_page in request.POST.keys():
            request.session[self.modulo_session][self.variable_page] = int(request.POST[self.variable_page])

        # asignamos los valores por defecto o los valores seleccionados
        self.variable_val = request.session[self.modulo_session][self.variable]
        self.variable2_val = request.session[self.modulo_session][self.variable2]
        self.variable3_val = request.session[self.modulo_session][self.variable3]
        self.variable4_val = request.session[self.modulo_session][self.variable4]
        self.variable5_val = request.session[self.modulo_session][self.variable5]
        self.variable6_val = request.session[self.modulo_session][self.variable6]
        self.variable7_val = request.session[self.modulo_session][self.variable7]
        self.variable8_val = request.session[self.modulo_session][self.variable8]
        self.variable9_val = request.session[self.modulo_session][self.variable9]
        self.variable10_val = request.session[self.modulo_session][self.variable10]
        # pagina
        self.variable_page_val = request.session[self.modulo_session][self.variable_page]

        # order request
        if self.variable_order in request.POST.keys():
            request.session[self.modulo_session][self.variable_order] = request.POST[self.variable_order]
            request.session[self.modulo_session][self.variable_order_type] = request.POST[self.variable_order_type]

        # datos del orden
        self.variable_order_value = request.session[self.modulo_session][self.variable_order]
        self.variable_order_type_value = request.session[self.modulo_session][self.variable_order_type]

        # importante establecer que la session se modifico para cuando se vuelva al modulo mantenga los datos
        request.session.modified = True

        # session de orden
        # $smarty -> assign('order_field', $variableOrder)
        # $smarty -> assign('order_type', $variableOrderType)
        # $smarty -> assign('order_field_value', $variableOrderValue)
        # $smarty -> assign('order_type_value', $variableOrderTypeValue)

    def paginacion(self):
        settings_sistema = get_settings()
        cant_per_page = settings_sistema['cant_per_page']
        self.pages_list = []
        cant_total = self.cantidadRegistros()
        j = 1
        i = 0
        while i < cant_total:
            self.pages_list.append(j)
            i = i + cant_per_page
            j += 1
            if j > 15:
                break

        self.pages_limit_botton = (int(self.variable_page_val) - 1) * cant_per_page
        self.pages_limit_top = self.pages_limit_botton + cant_per_page

    def getLista(self):
        # orden
        #print(self.variable_order_value, self.variable_order_type_value)
        orden_enviar = ''
        if self.variable_order_value != '':
            orden_enviar = self.variable_order_value
            if self.variable_order_type_value != '':
                if self.variable_order_type_value == 'DESC':
                    orden_enviar = '-' + orden_enviar
        # print(orden_enviar)

        modelo = apps.get_model(self.modelo_app, self.modelo_name)
        retorno = modelo.objects.filter(**self.filtros_modulo).order_by(orden_enviar)[self.pages_limit_botton:self.pages_limit_top]

        return retorno

    def add(self, request):
        """agregar un elemento al modulo"""
        pass

    def modify(self, request, id):
        """modificar un elemento"""
        pass

    def delete(self, request, id):
        """eliminar un elemento"""
        pass

    def canDelete(self, id):
        """verificando si se puede eliminar la tabla"""
        pass

    def isInDB(self, id, nuevo_valor):
        """verificamos si existe el nuevo valor en la base de datos"""
        """id-> en caso que se este modificando"""
        """nuevo_valor-> columna de la base de datos"""
        pass
