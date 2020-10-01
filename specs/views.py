from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponsePermanentRedirect
from .models import Brand
from .models import ValveType
from .models import BellSize
from .models import BellMaterial
from .models import Finish
from .models import OuterSlideMaterial
from .models import BassTrombone
from .models import CustomizableBassTrombone

# Create your views here.

def index(request):
    if request.get_host() == "basstrombonespecs.herokuapp.com":
        return HttpResponsePermanentRedirect('https://www.basstrombonespecs.com')

    # These are the selections the user inputted on the site.
    brand_selection = request.GET.getlist('brand')
    number_of_valves_selection = request.GET.getlist('number_of_valves')
    valve_configuration_selection = request.GET.getlist('valve_configuration')
    valve_type_selection = request.GET.getlist('valve_type')
    wrap_selection = request.GET.getlist('wrap')
    bell_size_selection = request.GET.getlist('bell_size')
    bell_material_selection = request.GET.getlist('bell_material')
    dual_bore_selection = request.GET.getlist('dual_bore')
    finish_selection = request.GET.getlist('finish')
    outer_slide_material_selection = request.GET.getlist('outer_slide_material')

    # These are for listing out the options on the site.
    brand_all = Brand.objects.all()
    valve_type_all = ValveType.objects.all()
    bell_size_all = BellSize.objects.all()
    bell_material_all = BellMaterial.objects.all()
    finish_all = Finish.objects.all()
    outer_slide_material_all = OuterSlideMaterial.objects.all()

    # This is for listing the customizable bass trombones on the site.
    customizable_bass_trombones = CustomizableBassTrombone.objects.all()

    # These are for listing the filtered results as well as for keeping the selected
    # option highlighted after the submit button is clicked.
    bass_trombone_result = BassTrombone.objects.all()
    brand_result = Brand.objects.none()
    number_of_valves_result = []
    valve_configuration_result = []
    valve_type_result = ValveType.objects.none()
    wrap_result = []
    bell_size_result = BellSize.objects.none()
    bell_material_result = BellMaterial.objects.none()
    dual_bore_result = []
    finish_result = Finish.objects.none()
    outer_slide_material_result = OuterSlideMaterial.objects.none()

    # Filter by brand
    bass_trombone_brand_result = BassTrombone.objects.none()
    if len(brand_selection) != 0:
        for brand in brand_selection:
            bass_trombone_brand_result = BassTrombone.objects.filter(
                brand__exact=brand).union(bass_trombone_brand_result)
            brand_result = Brand.objects.filter(
                brand__exact=brand).union(brand_result)
    else:
        bass_trombone_brand_result = BassTrombone.objects.all()
    bass_trombone_result = bass_trombone_result.intersection(
        bass_trombone_brand_result)

    # Filter by number of valves
    bass_trombone_number_of_valves_result = BassTrombone.objects.none()
    if len(number_of_valves_selection) != 0:
        for number_of_valves in number_of_valves_selection:
            bass_trombone_number_of_valves_result = BassTrombone.objects.filter(
                number_of_valves__exact=number_of_valves).union(
                bass_trombone_number_of_valves_result)
            number_of_valves_result.append(number_of_valves)
    else:
        bass_trombone_number_of_valves_result = BassTrombone.objects.all()
    bass_trombone_result = bass_trombone_result.intersection(
        bass_trombone_number_of_valves_result)

    # Filter by valve configuration
    bass_trombone_valve_configuration_result = BassTrombone.objects.none()
    if len(valve_configuration_selection) != 0:
        for valve_configuration in valve_configuration_selection:
            bass_trombone_valve_configuration_result = BassTrombone.objects.filter(
                valve_configuration__exact=valve_configuration).union(
                bass_trombone_valve_configuration_result)
            valve_configuration_result.append(valve_configuration)
    else:
        bass_trombone_valve_configuration_result = BassTrombone.objects.all()
    bass_trombone_result = bass_trombone_result.intersection(
        bass_trombone_valve_configuration_result)

    # Filter by valve type
    bass_trombone_valve_type_result = BassTrombone.objects.none()
    if len(valve_type_selection) != 0:
        for valve_type in valve_type_selection:
            bass_trombone_valve_type_result = BassTrombone.objects.filter(
                valve_type__exact=valve_type).union(
                bass_trombone_valve_type_result)
            valve_type_result = ValveType.objects.filter(
                valve_type__exact=valve_type).union(valve_type_result)
    else:
        bass_trombone_valve_type_result = BassTrombone.objects.all()
    bass_trombone_result = bass_trombone_result.intersection(
        bass_trombone_valve_type_result)

    # Filter by wrap
    bass_trombone_wrap_result = BassTrombone.objects.none()
    if len(wrap_selection) != 0:
        for wrap in wrap_selection:
            bass_trombone_wrap_result = BassTrombone.objects.filter(
                wrap__exact=wrap).union(
                bass_trombone_wrap_result)
            wrap_result.append(wrap)
    else:
        bass_trombone_wrap_result = BassTrombone.objects.all()
    bass_trombone_result = bass_trombone_result.intersection(
        bass_trombone_wrap_result)

    # Filter by bell size
    bass_trombone_bell_size_result = BassTrombone.objects.none()
    if len(bell_size_selection) != 0:
        for bell_size in bell_size_selection:
            bass_trombone_bell_size_result = BassTrombone.objects.filter(
                bell_size__exact=bell_size).union(
                bass_trombone_bell_size_result)
            bell_size_result = BellSize.objects.filter(
                bell_size__exact=bell_size).union(bell_size_result)
    else:
        bass_trombone_bell_size_result = BassTrombone.objects.all()
    bass_trombone_result = bass_trombone_result.intersection(
        bass_trombone_bell_size_result)

    # Filter by bell material
    bass_trombone_bell_material_result = BassTrombone.objects.none()
    if len(bell_material_selection) != 0:
        for bell_material in bell_material_selection:
            bass_trombone_bell_material_result = BassTrombone.objects.filter(
                bell_material__exact=bell_material).union(
                bass_trombone_bell_material_result)
            bell_material_result = BellMaterial.objects.filter(
                bell_material__exact=bell_material).union(bell_material_result)
    else:
        bass_trombone_bell_material_result = BassTrombone.objects.all()
    bass_trombone_result = bass_trombone_result.intersection(
        bass_trombone_bell_material_result)

    # Filter by dual bore
    bass_trombone_dual_bore_result = BassTrombone.objects.none()
    if len(dual_bore_selection) != 0:
        for dual_bore in dual_bore_selection:
            bass_trombone_dual_bore_result = BassTrombone.objects.filter(
                dual_bore__exact=dual_bore).union(
                bass_trombone_dual_bore_result)
            dual_bore_result.append(dual_bore)
    else:
        bass_trombone_dual_bore_result = BassTrombone.objects.all()
    bass_trombone_result = bass_trombone_result.intersection(
        bass_trombone_dual_bore_result)

    # Filter by finish
    bass_trombone_finish_result = BassTrombone.objects.none()
    if len(finish_selection) != 0:
        for finish in finish_selection:
            bass_trombone_finish_result = BassTrombone.objects.filter(
                finish__exact=finish).union(
                bass_trombone_finish_result)
            finish_result = Finish.objects.filter(
                finish__exact=finish).union(finish_result)
    else:
        bass_trombone_finish_result = BassTrombone.objects.all()
    bass_trombone_result = bass_trombone_result.intersection(
        bass_trombone_finish_result)

    # Filter by outer slide material
    bass_trombone_outer_slide_material_result = BassTrombone.objects.none()
    if len(outer_slide_material_selection) != 0:
        for outer_slide_material in outer_slide_material_selection:
            bass_trombone_outer_slide_material_result = BassTrombone.objects.filter(
                outer_slide_material__exact=outer_slide_material).union(
                bass_trombone_outer_slide_material_result)
            outer_slide_material_result = OuterSlideMaterial.objects.filter(
                outer_slide_material__exact=outer_slide_material).union(
                outer_slide_material_result)
    else:
        bass_trombone_outer_slide_material_result = BassTrombone.objects.all()
    bass_trombone_result = bass_trombone_result.intersection(
        bass_trombone_outer_slide_material_result)

    # Order result
    bass_trombone_result = bass_trombone_result.order_by('brand__brand', 'model')

    bass_trombone_result_count = bass_trombone_result.count()

    context = {
        'debug': settings.DEBUG,
        'brand_all': brand_all,
        'valve_type_all': valve_type_all,
        'bell_size_all': bell_size_all,
        'bell_material_all': bell_material_all,
        'finish_all': finish_all,
        'outer_slide_material_all': outer_slide_material_all,
        'customizable_bass_trombones': customizable_bass_trombones,
        'bass_trombone_result': bass_trombone_result,
        'brand_result': brand_result,
        'number_of_valves_result': number_of_valves_result,
        'valve_configuration_result': valve_configuration_result,
        'valve_type_result': valve_type_result,
        'wrap_result': wrap_result,
        'bell_size_result': bell_size_result,
        'bell_material_result': bell_material_result,
        'dual_bore_result': dual_bore_result,
        'finish_result': finish_result,
        'outer_slide_material_result': outer_slide_material_result,
        'bass_trombone_result_count': bass_trombone_result_count,
    }

    return render(request, 'specs/index.html', context)
