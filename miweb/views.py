from django.shortcuts import render, HttpResponse
from .models import Vitacura

def inicio(request):
    return render(request, "inicio.html")

def inicio2(request):
    if request.method == 'POST':
        edad = request.POST.get('edad', '')
        fiebre = request.POST.get('fiebre', '')
        tos = request.POST.get('tos', '')
        cansancio = request.POST.get('cansancio', '')
        pecho = request.POST.get('pecho', '')
        cabeza = request.POST.get('cabeza', '')
        respirar = request.POST.get('respirar', '')
        enfermedad = request.POST.get('enfermedad', '')
        return render(request, "inicio2.html")
    else:
        return render(request, "inicio2.html")



def contacto(request):
    return render(request, "contacto.html")

def Lascondes(request):   
    ordcompetidores = ["Clínica Cordillera", "Clínica Las Condes", "Clínica San Carlos de Apoquindo", "Clínica Universidad de los Andes", "Hospital FACH", "Cesfam Apoquindo", "Integramedica Alto las Condes", "Integramedica Los Dominicos", "Integramedica Manquehue", "Hospital Dipreca", "Centro Médico Medicien", "Clínica Psiquiatrica Creser", "Pensionado San José", "Centro Médico y Dental Megasalud Arauco", "Centro Médico y Dental Megasalud Padre Hurtado", "Central Odontológica de la Fuerzas Armadas y de Orden", "Centro Médico Militar Rosa O'Higgins", "Centro Odontológico Uno Salud Dental Las Condes", "Clínica Milano", "Centro de Salud Familiar Apoquindo", "Centro de Salud Familiar Aníbal Ariztía", "Clínica Arauco Salud","Centro Asistencial AChS Las Condes", "Centro Médico y Dental Megasalud Kennedy", "Darvax Salud", "COSAM Las Condes", "SAPU Aníbal Ariztía", "Instituto Oftalmológico Puerta del Sol", "Clínica Paris SpA", "Centro Vida Integra de Las Condes", "VidaIntegra (El Bosque Norte)", "Integramedica  calle Neveria"]
    context = {"Place": ordcompetidores, "numcompetidores": len(ordcompetidores)}
    return render(request, "hlascondes.html", context)

def ubic_lascondes(request):
    ubic = ["Alejandro Fleming 7889", "Estoril 450", "Camino El Alba 12351", "Av Plaza 2501", "Avenida Américo Vespucio, of. 102, Piso 1 100", "Calle Martin de Zamora 4602", "Avenida Alexander Fleming 7885", "Calle Lo Fontecilla 441", "Avenida Cristóbal Colón 5850", "Avenida Las Condes 8631", "Calle Vital Apoquindo 1200", "Calle Camino El Alba 12351", "Avenida Presidente Kennedy 5413", "Avenida Padre 1621", "Avenida Las Condes 8631", "Avenida Américo Vespucio 995", "Avenida Padre Hurtado Sur, Piso 2 Locales 24-25-26, Centro Punto Vivo Padre Hurtado 1621", "Calle Estoril 645", "Calle Cerro Altar 6611", "Calle Paúl Harris 1140", "Avenida Kennedy 5413", "Avenida Kennedy 5735", "Avenida Manquehue 329", "Avenida Cristóbal Colón 3018", "Calle Enrique Foster Sur 153", "Calle La Escuela 1229", "Calle Puerta del Sol 36", "Calle Hernando de Magallanes 142", "Avenida Apoquindo 3281", "Calle Roger 2800", "Calle Nevería 4715", "Avenida Plaza 2501"]
    context = {"Place": ubic, "numcompetidores": len(ubic)}
    return render(request, "ubiclascondes.html", context)


def vitacura(request):
    vitacura = ["Clínica Tabancura", "Clínica Alemana","COSAM Vitacura", "Centro de Salud Familiar Vitacura", "Clínica Lo Curro"] 
    #hosp_vitacura = Vitacura.objects.values('hospital', 'ubicacion')
    ubicacion_vitacura = ["Av. Tabancura 1185 ", "Av Vitacura 5951", "Av Vitacura 7458", "Indiana 1195","Santa María 5950"]
    #context = {"Place": hosp_vitacura, "numcompetidores": len(hosp_vitacura)}
    context = {"Place": vitacura, "numcompetidores": len(vitacura), "ubicacioncomp":ubicacion_vitacura}
    return render(request, "hvitacura.html", context)

def ubic_vitacura(request):
    ubic = ["Av. Tabancura 1185 ", "Av Vitacura 5951", "Av Vitacura 7458", "Indiana 1195","Santa María 5950"]
    context = {"Place": ubic, "numcompetidores": len(ubic)}
    return render(request, "ubicvitacura.html", context)

def lobarnechea(request):
    lo_barnechea = ["SAPU Lo Barnechea", "Centro Comunitario de Salud Familiar Bicentenario(Sur)", "Centro Comunitario de Salud Familiar Bicentenario(Norte)", "Centro de Salud Familiar Lo Barnechea", "Clínica Alemana de La Dehesa", "Centro Médico Clínica Santa María La Dehesa"]
    context = {"Place": lo_barnechea, "numcompetidores": len(lo_barnechea)}
    return render(request, "hbarnechea.html", context)

def ubic_lobarnechea(request):
    ubic = ["Avenida El Rodeo 13533", "Calle Getsemani 229", "Calle Circunvalación Norte 5040", "Avenida El Rodeo 13533", "Avenida José Alcalde Délano 12205", "Avenida La Dehesa 1445"]
    context = {"Place": ubic, "numcompetidores": len(ubic)}
    return render(request, "ubiclobarnechea.html", context)


def providencia(request):
    provi = ["Clínica Paris SpA", "Clínica Vida Estética", "Hospital Metropolitano (Ex Militar, Santiago, Providencia)","Centro Metropolitano de Sangre y Tejidos", "Actividades gestionadas por la Dirección del Servicio para apoyo de la Red (S.S Metropolitano Oriente)", "PRAIS (S.S Metropolitano Oriente)", "Vacunatorio Internacional SEREMI de Salud Metropolitana", "Hospital Del Salvador (Santiago, Providencia)", "Hospital de Niños Dr. Luis Calvo Mackenna (Santiago, Providencia)", "Instituto Nacional de Enfermedades Respiratorias y Cirugía Torácica", "Instituto de Neurocirugía Dr. Alfonso Asenjo", "Instituto Nacional Geriátrico Presidente Eduardo Frei Montalva", "Clínica Costanera", "Clínica Psiquiatrica Bretaña", "Clínica Indisa", "Clínica Miguel Claro", "Clínica Servet", "Centro Médico y Dental Megasalud Providencia", "Clínica San Andrés", "Clínica Sara Moncada", "Centro CONIN Credes", "Hospital del Trabajador Santiago", "Clínica Santa Rafaela", "Clínica Europa", "Clínica Santa María", "Clínica Oncológica Arturo López Pérez", "Clínica Colonial", "Departamento de Bienestar Social de la Dirección General de Aeronáutica Civil", "Instituto de Enfermedades Circulatorias", "Centro Médico Pediátrico Integral Mediclown", "Clínica de Medicina y Estética MYE", "Centro Médico Vida Integra Tobalaba", "Consultorio Escuela de Carabineros de Chile", "Centro Comunitario de Salud Familiar Andacollo", "Centro Clínico Integral Las Lilas", "Vacunatorio RENVAC", "Centro Odontológico Uno Salud Dental Providencia", "Centro Odontológico Uno Salud Dental Hernando de Aguirre", "Centro Odontológico Uno Salud Dental La Concepción", "Clínica de Cirugía y Estética Edelweiss", "Vacunatorio Mediclown", "Centro Médico y Dental Antonio Varas del Banco del Estado de Chile", "Centro de Salud Familiar Dr. Hernán Alessandri", "Centro de Salud Familiar Dr. Alfonso Leng", "Centro de Salud Familiar Aguilucho", "Centro Integramédica Barcelona", "Clínica Las Acacias", "Clínica Mella", "Centro Servicios Médicos Santa María", "Clínica Astra Providencia", "Clínica Los Coihues", "Centro Vida Integra", "Clínica Las Lilas", "COSAM Provisam", "Clínica Avansalud Providencia", "Dirección Previsional de Carabineros de Chile", "Laboratorio Clínico Blanco", "Química Clínica Especializada", "Laboratorio Bionet", "Bioánalisis Ltda.", "Dilab", "Elsa", "Megasalud", "Clínica New Clinic", "Barnafi Krause Diagnóstica", "Centro de Salud Mutual CChC Providencia", "Centro de Salud Dial Médica", "Centro Comunitario de Salud Familiar Elena Caffarena", "Diagnóstika", "Mirandes S.P.A.", "SAPU Aguilucho", "Centro de Especialidades Odontológicas Leng", "Clínica WLK", "Centro Médico HTS SpA"]
    context = {"Place": provi, "numcompetidores": len(provi)}
    return render(request, "hprovidencia.html", context)

def ubic_provi(request):
    ubic = ["Avenida Los Leones 465", "Avenida Eliodoro Yáñez 1759", "Calle Holanda 50", "Avenida Vitacura 115", "Avenida Salvador 364", "Avenida Salvador 364", "Calle José Miguel Infante 551", "Avenida Salvador 364", "Avenida Antonio Varas 360", "Calle José Manuel Infante 717", "Avenida José M. Infante 553", "Calle José Manuel Infante 370", "Calle Antonio Bellet 189", "Avenida Francisco Bilbao 2638", "Avenida Santa María 1810", "Calle Miguel Claro 988", "Calle Almirante Pastene 190", "Calle 11 de Septiembre 1920", "Calle Los Jesuitas 695", "Avenida Pedro de Valdivia 2219", "Avenida Pedro de Valdivia 1880", "Calle Ramón Carnicer 185", "Calle Seminario 580", "Avenida Pedro de Valdivia 483", "Avenida Santa María 410", "Calle Rancagua 878", "Avenida Pedro de Valdivia 2652", "Avenida Eliodoro Yáñez 2394", "Calle Miguel Claro 988", "Avenida Pedro de Valdivia 2219", "Calle Pérez Valenzuela 1551", "Calle Tobalaba 155", "Calle Antonio Varas 1842", "Calle Andacollo 1661", "Avenida Manuel Montt 427", "Calle La Concepción 141", "Avenida Coyancura, Local 6 y 7 2229", "Avenida Hernando de Aguirre, Local 101 215", "Avenida La Concepción, Local 102 201", "Calle Calle Miguel Claro 996", "Calle Collypi 126", "Avenida Providencia 1722", "Calle Los Jesuitas 857", "Avenida Manuel Montt 303", "Calle El Aguilucho 3292", "Calle Barcelona 2116", "Avenida Salvador 537", "Calle Providencia 2608", "Avenida Santa María 410", "Calle Rancagua 701", "Avenida Eliodoro Yáñez 1215", "Avenida 11 de Septiembre 2350", "Avenida Eliodoro Yáñez 2087", "Calle Manuel Montt 2051", "Avenida Salvador 100", "Calle Santa Beatriz 171", "Avenida Salvador 31", "Avenida Salvador 149", "Avenida Vicuña Mackenna, Piso 3 4", "Avenida Bustamante 32", "Avenida Vicuña Mackenna, Piso 1 6", "Avenida Italia 1056", "Calle Salvador 100", "Calle Los Leones 1588", "Avenida Andrés Bello 1195", "Calle Hernán Alessandri 620", "Calle Ricardo Lyon 396", "Calle Marín 520", "Calle Salvador 135", "Avenida Salvador 726", "Calle El Aguilucho 3235", "Avenida Eliodoro Yáñez 1261", "Avenida Los Leones 485", "Avenida Vicuña Mackenna 210"]
    context = {"Place": ubic, "numcompetidores": len(ubic)}
    return render(request, "ubicprovi.html", context)


def lareina(request):
    la_reina = ["Clínica Psicoterapia los Tiempos", "Clínica Instituto El Cedro", "Integramédica Sucursal Plaza Egaña", "Centro Odontológico Uno Salud Dental La Reina", "Vacunatorio Darvax", "Centro de Salud Familiar Ossandon", "Centro de Salud Familiar Juan Pablo II", "Centro Asistencial AChS La Reina", "Hospital Militar de Santiago", "COSAM La Reina","Centro Comunitario de Salud Familiar Dragones de La Reina", "VidaIntegra", "Centro Odontológico La Reina", "SAPU La Reina"]
    context = {"Place": la_reina, "numcompetidores": len(la_reina)}
    return render(request, "hlareina.html", context)

def ubic_lareina(request):
    ubic = ["Avenida José Arrieta 6024", "Calle Julia Berstein 1240", "Avenida Larraín 5862", "Avenida Principe de Gales 6938", "Avenida Francisco Bilbao 6387", "Calle Echenique 8419", "Calle Parinacota 440", "Avenida Jorge 50", "Avenida Larraín 9100", "Calle Quillahua 480", "Calle Dragones de La Reina 616", "Avenida Ossa 345", "Calle Cordillera 25", "Calle Echenique 8419"]
    context = {"Place": ubic, "numcompetidores": len(ubic)}
    return render(request, "ubiclareina.html", context)




