#!/usr/bin/env python3
"""Genera las páginas por producto (roller-blackout.html, etc.) a partir de PRODUCTOS.

Uso:  python3 build-productos.py
Cada página comparte header, footer, estilos y medición con index.html.
Para cambiar un texto, editalo acá y volvé a correr el script.
"""
import json, html, datetime, pathlib

SITE = "https://entreluz.casa"
WSP = "5491166776019"
HOY = datetime.date.today().isoformat()

PRODUCTOS = [
    {
        "slug": "roller-blackout",
        "nombre": "Cortinas Roller Blackout",
        "title": "Cortinas Roller Blackout a Medida en Buenos Aires | Entre Luz Home",
        "description": "Cortinas roller blackout a medida para dormitorios, cuartos de chicos y home cinema. Bloqueo total de luz, medición sin cargo a domicilio e instalación propia en CABA y GBA.",
        "h1": "Cortinas roller blackout a medida",
        "lead": "Para dormir a oscuras aunque afuera sea mediodía. Medimos en tu casa, confeccionamos en taller propio e instalamos en Buenos Aires y Gran Buenos Aires.",
        "hero": "cortina-roller-blackout-dormitorio",
        "hero_alt": "Cortina roller blackout a medida instalada en un dormitorio",
        "hero_pos": "50% 40%",
        "intro_titulo": "Oscuridad completa, terminación prolija",
        "intro": [
            "La cortina roller blackout es la opción más pedida para dormitorios: una tela opaca enrollada en un tubo de aluminio que baja hasta el antepecho y bloquea el paso de la luz. A diferencia de una roller estándar de tienda, la hacemos exactamente al ancho y alto de tu ventana, así que no quedan franjas de luz a los costados ni tela sobrante enrollada.",
            "Trabajamos telas blackout en varios colores y texturas, desde lisas hasta con trama tipo lino, con muestras físicas que llevamos a tu casa. Te recomendamos el sistema de accionamiento (cadena o motorizado) según el tamaño de la ventana y cómo la usás.",
        ],
        "intro_img": "cortina-roller-blackout-bajada",
        "intro_img_alt": "Cortina roller blackout completamente bajada",
        "datos": [
            ("Bloqueo de luz", "Tela opaca, ideal para dormir de día o con luz de calle"),
            ("A medida real", "Ancho y alto exactos de tu ventana, sin filtraciones laterales"),
            ("Plazo", "10 a 15 días hábiles desde que confirmás tela y presupuesto"),
        ],
        "usos_titulo": "Dónde conviene una roller blackout",
        "usos": [
            ("Dormitorios", "Para descansar bien en departamentos con luz de calle o ventanas al este. Es la cortina que más instalamos."),
            ("Cuartos de chicos", "Siestas de día sin pelear con la luz. La tela es lavable con un paño húmedo y el sistema de cadena puede llevar traba de seguridad."),
            ("Home cinema y oficinas", "Oscurecimiento total para proyector o pantalla, y para reuniones sin reflejos."),
        ],
        "galeria": [
            ("cortina-roller-blackout-combinado", "Cortina roller blackout con cortinado de tela en sistema combinado"),
            ("cortina-roller-dormitorio-noche", "Cortina roller blackout en dormitorio con luz nocturna"),
            ("cortina-roller-blackout-bajada", "Roller blackout bajada en dormitorio"),
        ],
        "faqs": [
            ("¿Una roller blackout bloquea toda la luz?", "La tela bloquea el 100% de la luz. Lo que puede filtrarse es por los costados, entre la tela y la pared. Por eso medimos en tu casa y te recomendamos dónde instalarla (dentro del vano o sobre la pared) para minimizar ese borde. Si necesitás oscuridad absoluta, el sistema combinado roller más cortinado de tela lo resuelve del todo."),
            ("¿Sirve para ventanas grandes o ventanales?", "Sí. Para anchos grandes evaluamos el peso de la tela y el tubo, y a veces conviene dividir en dos paños o motorizar. Te lo decimos en la visita."),
            ("¿Cuánto cuesta una cortina roller blackout a medida?", "Depende de las medidas y de la tela que elijas. Después de la visita te enviamos el presupuesto por escrito, con tela, sistema, accesorios e instalación incluidos. La visita y la medición no tienen cargo."),
            ("¿Cómo se limpia?", "Con un paño apenas húmedo o un plumero. No se lava en lavarropas ni se plancha."),
        ],
        "wsp_msg": "Hola Entre Luz Home! Me interesa una cortina roller blackout a medida. ¿Pueden asesorarme?",
        "cta": "Consultar roller blackout",
    },
    {
        "slug": "roller-screen",
        "nombre": "Cortinas Roller Screen",
        "title": "Cortinas Roller Screen a Medida en Buenos Aires | Entre Luz Home",
        "description": "Cortinas roller screen a medida que filtran el sol y el calor sin perder la vista al exterior. Ideales para living, comedor y oficinas. Medición sin cargo e instalación propia en CABA y GBA.",
        "h1": "Cortinas roller screen a medida",
        "lead": "Filtran el sol y el calor, cortan los reflejos y dejan ver hacia afuera. La cortina más versátil para living, comedor, cocina y oficina.",
        "hero": "cortina-roller-screen-estudio",
        "hero_alt": "Cortina roller screen filtrando la luz en un estudio",
        "hero_pos": "50% 50%",
        "intro_titulo": "Luz sin sol directo",
        "intro": [
            "La tela screen es una malla técnica que deja pasar parte de la luz y el aire visual, pero frena los rayos UV y buena parte del calor. Desde adentro seguís viendo el jardín o la calle; desde afuera, de día, no se ve hacia adentro. Por eso es la elección habitual para ambientes de estar y para oficinas con muchas pantallas.",
            "Se fabrica en distintos grados de apertura (cuánto se ve y cuánto filtra) y en colores neutros que combinan con casi cualquier decoración. En la visita te mostramos las muestras contra tu ventana, con la luz real del ambiente, que es la única forma seria de elegir.",
        ],
        "intro_img": "cortina-roller-screen-azul",
        "intro_img_alt": "Cortina roller screen azul en una ventana con vista a la calle",
        "datos": [
            ("Control solar", "Reduce calor y reflejos sin oscurecer el ambiente"),
            ("Vista al exterior", "Ves hacia afuera y de día conserva la privacidad"),
            ("Plazo", "10 a 15 días hábiles desde que confirmás tela y presupuesto"),
        ],
        "usos_titulo": "Dónde conviene una roller screen",
        "usos": [
            ("Living y comedor", "Bajás el sol de la tarde sin cerrar la vista ni apagar el ambiente."),
            ("Oficinas y estudios", "Sin reflejos en las pantallas y con menos calor en verano. Es la cortina más usada en obras y oficinas."),
            ("Cocinas y lavaderos", "Tela lavable, sin pliegues, que no acumula grasa ni humedad como una tela común."),
        ],
        "galeria": [
            ("cortina-roller-screen-detalle", "Detalle de cortina roller screen filtrando luz"),
            ("cortina-roller-screen-estudio", "Roller screen en estudio con luz natural"),
            ("cortina-roller-screen-azul", "Roller screen azul a medida"),
        ],
        "faqs": [
            ("¿La screen da privacidad de noche?", "De día sí: con más luz afuera que adentro, desde la calle no se ve. De noche, con la luz prendida, se invierte y se ve hacia adentro. Si necesitás privacidad nocturna, se combina con una blackout o con un cortinado."),
            ("¿Cuál es la diferencia entre screen y blackout?", "La screen filtra y deja ver; la blackout bloquea y oscurece. Para dormitorios va blackout; para ambientes de estar, screen. Muchas veces la mejor solución es una de cada una, o el sistema combinado en el mismo carril."),
            ("¿Cuánto cuesta una cortina roller screen a medida?", "Depende de las medidas y del tipo de tela screen. Te pasamos el presupuesto por escrito después de medir, sin cargo por la visita."),
        ],
        "wsp_msg": "Hola Entre Luz Home! Me interesa una cortina roller screen a medida. ¿Qué opciones tienen?",
        "cta": "Consultar roller screen",
    },
    {
        "slug": "cortinados-de-tela",
        "nombre": "Cortinados de Tela",
        "title": "Cortinados de Tela a Medida en Buenos Aires: Lino, Voile y Gasas | Entre Luz Home",
        "description": "Cortinados de tela a medida en lino, voile, gasas y telas naturales. Confección en taller propio, caída perfecta e instalación en CABA y GBA. Medición y asesoramiento sin cargo.",
        "h1": "Cortinados de tela a medida",
        "lead": "Lino, voile, gasas y telas naturales confeccionadas en taller propio, con la caída que solo tiene una cortina hecha para esa ventana.",
        "hero": "cortinas-tela-living-amplio",
        "hero_alt": "Cortinado de tela natural a medida en living con techo de madera",
        "hero_pos": "50% 45%",
        "intro_titulo": "La tela le da calidez a la casa",
        "intro": [
            "Un cortinado de tela cambia un ambiente más que cualquier otro elemento: suma textura, suaviza la luz y le da terminación a la ventana. Trabajamos con lino, voile, gasas y mezclas naturales, en cortinados livianos tipo sheer que dejan pasar la luz o en telas con más cuerpo para tapar y abrigar.",
            "La diferencia con una cortina comprada está en la confección: tomamos las medidas en tu casa, definimos el tipo de pliegue (tabla, americano, ollado o riel oculto), el largo exacto hasta el piso y el sistema de riel o barral. Eso es lo que hace que la cortina caiga perfecta y no quede ni corta ni arrastrando.",
        ],
        "intro_img": "cortina-tela-sheer-detalle",
        "intro_img_alt": "Detalle de cortina sheer con luz natural filtrada",
        "datos": [
            ("Telas", "Lino, voile, gasas y naturales, con muestras físicas en tu casa"),
            ("Confección", "Taller propio: pliegue, largo y terminaciones a medida"),
            ("Plazo", "10 a 15 días hábiles desde que confirmás tela y presupuesto"),
        ],
        "usos_titulo": "Dónde conviene un cortinado de tela",
        "usos": [
            ("Living y comedor", "Sheer de voile o lino para tamizar la luz y darle marco al ventanal, con o sin una cortina más pesada por detrás."),
            ("Dormitorios", "Tela con cuerpo para abrigar y dar intimidad, o combinada con una roller blackout para oscurecer."),
            ("Obras y hoteles", "Cortinados para varias habitaciones con el mismo criterio, medidos en obra y entregados con plazos coordinados."),
        ],
        "galeria": [
            ("cortinado-tela-natural-living", "Cortinado de tela natural en living con sofá"),
            ("living-cortina-sheer-terraza", "Cortinados sheer en living con puertas al jardín"),
            ("cortina-tela-luz-natural", "Cortina de tela dejando pasar la luz natural"),
            ("suite-cortinados-tela-gris", "Suite con cortinados de tela gris y sheer"),
        ],
        "faqs": [
            ("¿Qué tela conviene para un living?", "Para tamizar la luz sin cerrar el ambiente, voile o lino liviano. Si además querés tapar, se suma un paño con más cuerpo o una roller detrás. Lo definimos en la visita, viendo la luz real de tu living."),
            ("¿Cortinado de tela o roller?", "No compiten: la roller resuelve la luz y la tela resuelve la estética. Lo más pedido hoy es el sistema combinado, roller blackout o screen más cortinado de tela en el mismo carril."),
            ("¿Los cortinados se lavan?", "Depende de la tela. El voile y muchas gasas se lavan en casa con programa delicado; el lino conviene lavarlo en seco o con cuidado para que no encoja. Te lo indicamos con la tela elegida."),
            ("¿Cuánto cuesta un cortinado de tela a medida?", "Depende de los metros de tela, el tipo de pliegue y el sistema de riel o barral. Después de medir te enviamos el presupuesto por escrito, sin cargo por la visita."),
        ],
        "wsp_msg": "Hola Entre Luz Home! Quiero consultar por cortinados de tela a medida. ¿Qué telas trabajan?",
        "cta": "Consultar cortinados",
    },
    {
        "slug": "sistemas-combinados",
        "nombre": "Sistemas Combinados",
        "title": "Cortinas Combinadas Roller + Cortinado de Tela a Medida | Entre Luz Home",
        "description": "Sistema combinado: cortina roller blackout o screen más cortinado de tela en un mismo carril. Oscurecimiento y diseño en una sola instalación, a medida, en CABA y GBA.",
        "h1": "Sistemas combinados: roller más cortinado de tela",
        "lead": "Una roller blackout o screen para manejar la luz y un cortinado de tela para vestir la ventana, instalados juntos en un mismo carril.",
        "hero": "cortina-combinada-roller-tela",
        "hero_alt": "Sistema combinado de cortina roller y cortinado de tela a medida",
        "hero_pos": "50% 45%",
        "intro_titulo": "Lo funcional y lo estético, en una sola instalación",
        "intro": [
            "El sistema combinado resuelve el dilema clásico: la roller es práctica pero fría, el cortinado es lindo pero no oscurece. Con un carril doble o un soporte especial, instalamos la roller pegada al vidrio y el cortinado de tela por delante. De día abrís todo y entra la luz; de noche bajás la blackout y cerrás la tela.",
            "Se puede armar con roller blackout (dormitorios) o roller screen (living), y con cualquier tela del cortinado: sheer de voile, lino, gasa. Medimos ambos elementos juntos para que los largos coincidan y el conjunto se vea como una sola pieza.",
        ],
        "intro_img": "cortina-combinada-dormitorio-jardin",
        "intro_img_alt": "Sistema combinado roller y tela en dormitorio con salida al jardín",
        "datos": [
            ("Dos cortinas", "Roller blackout o screen más cortinado de tela"),
            ("Un solo carril", "Instalación integrada, sin soportes a la vista"),
            ("Plazo", "10 a 15 días hábiles desde que confirmás telas y presupuesto"),
        ],
        "usos_titulo": "Dónde conviene un sistema combinado",
        "usos": [
            ("Dormitorios", "Blackout para dormir y un sheer para el día. Es la combinación que más instalamos en suites."),
            ("Living con ventanal", "Screen contra el sol de la tarde y cortinado de lino para darle marco al ventanal."),
            ("Departamentos a la calle", "Privacidad de día con la screen, de noche con la tela, y la vista intacta cuando querés."),
        ],
        "galeria": [
            ("cortina-combinada-tela-roller", "Sistema combinado roller y cortinado con vista al jardín"),
            ("cortina-roller-blackout-combinado", "Roller blackout con cortinado de tela"),
            ("cortina-combinada-dormitorio-jardin", "Sistema combinado en dormitorio"),
        ],
        "faqs": [
            ("¿Se puede instalar un combinado donde ya hay una roller?", "En general sí: sumamos el riel del cortinado por delante de la roller existente, siempre que haya espacio en el vano o la pared. Lo vemos en la visita."),
            ("¿Oscurece del todo?", "Es la solución que más oscurece: la blackout bloquea la luz y la tela tapa el borde lateral por donde una roller sola deja pasar una franja."),
            ("¿Cuánto cuesta un sistema combinado?", "Es la suma de la roller y el cortinado, más el carril doble. Te enviamos el presupuesto por escrito después de medir, con la visita sin cargo."),
        ],
        "wsp_msg": "Hola Entre Luz Home! Me interesa el sistema combinado de roller y cortinado. ¿Pueden contarme cómo funciona?",
        "cta": "Consultar sistema combinado",
    },
    {
        "slug": "venezianas",
        "nombre": "Cortinas Venezianas de Madera",
        "title": "Cortinas Venezianas de Madera a Medida en Buenos Aires | Entre Luz Home",
        "description": "Cortinas venezianas de madera a medida para cocinas, livings y oficinas. Lamas que regulan la luz con precisión. Medición sin cargo e instalación propia en CABA y GBA.",
        "h1": "Cortinas venezianas de madera a medida",
        "lead": "Lamas de madera que giran para regular la luz con precisión. Carácter y textura para cocinas, livings y estudios.",
        "hero": "cortina-veneziana-madera-detalle",
        "hero_alt": "Cortina veneziana de madera oscura con luz filtrando entre las lamas",
        "hero_pos": "50% 50%",
        "intro_titulo": "Luz regulable, lama por lama",
        "intro": [
            "La veneziana de madera es la cortina que más control da sobre la luz: girás las lamas y pasás de sol pleno a penumbra sin levantar la cortina. Y a diferencia de las venezianas de aluminio de oficina, la madera suma calidez y se lleva bien con pisos, muebles y marcos de madera.",
            "Las hacemos a medida del vano, con lamas de 25 o 50 mm según el tamaño de la ventana, en tonos naturales, nogal, wengué o laqueadas en blanco. Van instaladas dentro del vano para una terminación limpia o sobre la pared cuando el vano no tiene profundidad.",
        ],
        "intro_img": "cortina-veneziana-madera-cocina",
        "intro_img_alt": "Cortina veneziana de madera en cocina",
        "datos": [
            ("Regulación", "Lamas giratorias: luz plena, tamizada o cerrada"),
            ("Madera", "Tonos naturales, nogal, wengué o laqueado blanco"),
            ("Plazo", "10 a 15 días hábiles desde que confirmás modelo y presupuesto"),
        ],
        "usos_titulo": "Dónde conviene una veneziana de madera",
        "usos": [
            ("Cocinas", "Regulás la luz sobre la mesada sin tela que junte grasa. Se limpia con un paño."),
            ("Livings y estudios", "Un cambio de estilo fuerte para ventanas medianas: el juego de luz entre lamas es parte de la decoración."),
            ("Oficinas y consultorios", "Privacidad graduable y un aspecto más cálido que la veneziana metálica."),
        ],
        "galeria": [
            ("cortina-veneziana-madera-cocina", "Veneziana de madera en cocina"),
            ("cortina-veneziana-madera-detalle", "Detalle de veneziana de madera"),
        ],
        "faqs": [
            ("¿La madera se arruina con la humedad?", "En baños o lavaderos con mucho vapor no la recomendamos. En cocinas normales funciona bien; las lamas vienen con terminación protectora y se limpian con paño seco o apenas húmedo."),
            ("¿Sirve para ventanas grandes?", "Para anchos grandes usamos lama de 50 mm y a veces dividimos en dos paños para que el mecanismo no sufra. Te lo indicamos en la medición."),
            ("¿Cuánto cuesta una veneziana de madera a medida?", "Depende de las medidas y del tipo de madera o laqueado. Te enviamos el presupuesto por escrito después de medir, sin cargo por la visita."),
        ],
        "wsp_msg": "Hola Entre Luz Home! Me interesa una cortina veneziana de madera a medida. ¿Qué materiales y colores tienen?",
        "cta": "Consultar venezianas",
    },
    {
        "slug": "ropa-de-cama",
        "nombre": "Ropa de Cama a Medida",
        "title": "Ropa de Cama a Medida: Sábanas, Acolchados y Almohadones | Entre Luz Home",
        "description": "Ropa de cama a medida confeccionada en taller propio: sábanas, acolchados, fundas y almohadones para colchones de medidas especiales, con las mismas telas premium de nuestros cortinados.",
        "h1": "Ropa de cama a medida",
        "lead": "Sábanas, acolchados, almohadones y fundas confeccionados en taller propio, con las mismas telas de nuestros cortinados. Para que el dormitorio hable un solo idioma.",
        "hero": "dormitorio-roller-blanco-amplio",
        "hero_alt": "Dormitorio con ropa de cama a medida y cortina roller blanca",
        "hero_pos": "50% 55%",
        "intro_titulo": "Dormitorios con un mismo lenguaje textil",
        "intro": [
            "Nació como un pedido de clientes de cortinas: querían almohadones y un pie de cama con la misma tela del cortinado. Hoy confeccionamos ropa de cama completa a medida: sábanas para colchones de medidas especiales, acolchados y cubrecamas, fundas de almohadones y pies de cama, en lino, algodón y mezclas.",
            "Es la solución cuando el colchón no es estándar (king, sommier grande, cuchetas, camas de obra o de hotel) o cuando querés que las cortinas, los almohadones y la cama combinen de verdad y no a ojo.",
        ],
        "intro_img": "cortinado-tela-clasica",
        "intro_img_alt": "Almohadones y acolchado de tela natural a medida",
        "datos": [
            ("Medidas especiales", "King, sommier, cuchetas, camas de obra y hotel"),
            ("Telas", "Lino, algodón y mezclas, las mismas de los cortinados"),
            ("Plazo", "10 a 15 días hábiles desde que confirmás tela y presupuesto"),
        ],
        "usos_titulo": "Qué confeccionamos",
        "usos": [
            ("Sábanas y fundas", "Juegos de sábanas y fundas de almohada al tamaño exacto del colchón, en algodón o lino."),
            ("Acolchados y pies de cama", "Cubrecamas, acolchados y pies de cama en la tela que elijas, coordinados con el cortinado."),
            ("Almohadones", "Fundas y almohadones para cama, sillones y bancos, con cierre invisible."),
        ],
        "galeria": [
            ("dormitorio-roller-blanco-ratan", "Dormitorio con ropa de cama a medida y roller blanca"),
            ("dormitorio-cucheta-cortina-gris", "Dormitorio con cuchetas, ropa de cama y cortina gris"),
            ("cortinado-tela-clasica", "Almohadones de tela natural"),
        ],
        "faqs": [
            ("¿Hacen sábanas para colchones de medidas raras?", "Sí, es el caso más habitual: king de importación, sommier con pillow, cuchetas angostas o camas de obra. Nos pasás las medidas del colchón (largo, ancho y alto) y las confeccionamos exactas."),
            ("¿Puedo combinar con las cortinas?", "Es la idea. Si hacés el cortinado con nosotros, los almohadones o el pie de cama salen de la misma tela o de una que combine, y lo coordinamos en una sola visita."),
            ("¿Cuánto cuesta la ropa de cama a medida?", "Depende de las piezas, las medidas y la tela. Te enviamos el presupuesto por escrito, sin cargo por el asesoramiento."),
        ],
        "wsp_msg": "Hola Entre Luz Home! Me interesa la ropa de cama a medida. ¿Qué opciones tienen?",
        "cta": "Consultar ropa de cama",
    },
]

LAZY = 'loading="lazy" decoding="async"'
ICO_WSP = '<svg viewBox="0 0 24 24" width="{s}" height="{s}" aria-hidden="true"><use href="#ico-wsp"/></svg>'

SYMBOLS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <symbol id="ico-wsp" viewBox="0 0 24 24"><path fill="currentColor" d="M.057 24l1.687-6.163a11.867 11.867 0 0 1-1.587-5.946C.157 5.335 5.493 0 12.05 0a11.82 11.82 0 0 1 8.413 3.488 11.82 11.82 0 0 1 3.48 8.414c-.003 6.557-5.338 11.892-11.893 11.892a11.9 11.9 0 0 1-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884a9.86 9.86 0 0 0 1.51 5.26l-.999 3.648 3.978-1.607zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.149-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.247-.694.247-1.289.173-1.413z"/></symbol>
  <symbol id="ico-ig" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" d="M7 2.5h10A4.5 4.5 0 0 1 21.5 7v10a4.5 4.5 0 0 1-4.5 4.5H7A4.5 4.5 0 0 1 2.5 17V7A4.5 4.5 0 0 1 7 2.5Z"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.6"/><circle cx="17.5" cy="6.5" r="1.1" fill="currentColor"/></symbol>
</svg>"""

def e(s):
    return html.escape(s, quote=True)

def picture(name, alt, extra="", w="", h=""):
    dims = f' width="{w}" height="{h}"' if w else ""
    return (f'<picture><source srcset="/images/{name}.webp" type="image/webp">'
            f'<img src="/images/{name}.jpg" alt="{e(alt)}"{dims} {extra}></picture>')

def nav_links(slug):
    items = [
        ("/#productos", "Productos"), ("/#galeria", "Galería"), ("/ropa-de-cama", "Ropa de cama"),
        ("/#proceso", "Proceso"), ("/#faq", "Preguntas"), ("/#contacto", "Contacto"),
    ]
    return "\n".join(f'        <li><a href="{h}">{t}</a></li>' for h, t in items)

def product_links_html(current):
    lis = []
    for p in PRODUCTOS:
        if p["slug"] == current:
            continue
        lis.append(f'        <li><a href="/{p["slug"]}">{e(p["nombre"])}</a></li>')
    return "\n".join(lis)

def jsonld(p):
    url = f"{SITE}/{p['slug']}"
    graph = [
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Inicio", "item": f"{SITE}/"},
                {"@type": "ListItem", "position": 2, "name": "Productos", "item": f"{SITE}/#productos"},
                {"@type": "ListItem", "position": 3, "name": p["nombre"], "item": url},
            ],
        },
        {
            "@type": "Service",
            "@id": f"{url}#service",
            "name": f"{p['nombre']} a medida",
            "serviceType": f"Confección e instalación de {p['nombre'].lower()} a medida",
            "description": p["description"],
            "url": url,
            "image": f"{SITE}/images/{p['hero']}.jpg",
            "provider": {"@id": f"{SITE}/#business"},
            "areaServed": [
                {"@type": "City", "name": "Buenos Aires"},
                {"@type": "AdministrativeArea", "name": "Gran Buenos Aires"},
            ],
        },
        {
            "@type": "WebPage",
            "@id": f"{url}#webpage",
            "url": url,
            "name": p["title"],
            "isPartOf": {"@id": f"{SITE}/#website"},
            "about": {"@id": f"{url}#service"},
            "primaryImageOfPage": f"{SITE}/images/{p['hero']}.jpg",
            "inLanguage": "es-AR",
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in p["faqs"]
            ],
        },
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)

def render(p):
    url = f"{SITE}/{p['slug']}"
    hero_img = f"{SITE}/images/{p['hero']}.jpg"
    intro_ps = "\n".join(f"        <p>{e(t)}</p>" for t in p["intro"])
    datos = "\n".join(f"          <li><strong>{e(k)}</strong><span>{e(v)}</span></li>" for k, v in p["datos"])
    usos = "\n".join(
        f'        <li>\n          <h3>{e(t)}</h3>\n          <p>{e(d)}</p>\n        </li>' for t, d in p["usos"])
    gal = "\n".join(
        f'        <figure>{picture(n, a, LAZY)}</figure>' for n, a in p["galeria"])
    faqs = "\n".join(
        f'        <details class="faq-item">\n          <summary>{e(q)}</summary>\n          <p>{e(a)}</p>\n        </details>'
        for q, a in p["faqs"])
    related = "\n".join(
        f'        <li><a href="/{o["slug"]}">{picture(o["hero"], o["nombre"], LAZY)}<span>{e(o["nombre"])}</span></a></li>'
        for o in PRODUCTOS if o["slug"] != p["slug"])
    wsp = e(p["wsp_msg"])

    return f"""<!DOCTYPE html>
<html lang="es-AR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <meta name="theme-color" content="#faf7f2">
  <meta name="format-detection" content="telephone=no">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <meta name="google-site-verification" content="hC_4qHzH-s5JwuzRbfjRjSebgTMe9a4isv9MP7IivTg">

  <title>{e(p['title'])}</title>
  <meta name="description" content="{e(p['description'])}">
  <meta name="author" content="Entre Luz Home">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <meta name="geo.region" content="AR-B">
  <meta name="geo.placename" content="Buenos Aires">
  <link rel="canonical" href="{url}">

  <meta property="og:type" content="website">
  <meta property="og:locale" content="es_AR">
  <meta property="og:site_name" content="Entre Luz Home">
  <meta property="og:title" content="{e(p['title'])}">
  <meta property="og:description" content="{e(p['description'])}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{hero_img}">
  <meta property="og:image:alt" content="{e(p['hero_alt'])}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{e(p['title'])}">
  <meta name="twitter:description" content="{e(p['description'])}">
  <meta name="twitter:image" content="{hero_img}">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="image" href="/images/{p['hero']}.webp" type="image/webp" fetchpriority="high">
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">

  <!-- Google Ads: etiqueta de Google (medición de conversiones) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=AW-18458130879"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'AW-18458130879');
  </script>

  <link rel="stylesheet" href="/styles.css">
  <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon.png">

  <script type="application/ld+json">
{jsonld(p)}
  </script>
</head>
<body class="page-producto">

<a class="skip-link" href="#contenido">Saltar al contenido</a>

{SYMBOLS}

<header class="site-header" id="top">
  <div class="container header-inner">
    <a href="/" class="brand" aria-label="Entre Luz Home — inicio">
      <picture class="logo-dark">
        <source srcset="/images/logo-dark.webp" type="image/webp">
        <img src="/images/logo-dark.png" alt="Entre Luz Home — Estudio textil para obras y espacios" class="logo-img" width="800" height="220">
      </picture>
      <picture class="logo-light" aria-hidden="true">
        <source srcset="/images/logo-light.webp" type="image/webp">
        <img src="/images/logo-light.png" alt="" class="logo-img" width="800" height="220">
      </picture>
    </a>
    <nav class="site-nav" id="primary-nav" aria-label="Navegación principal">
      <ul>
{nav_links(p['slug'])}
        <li class="nav-cta">
          <a class="cta-wsp" href="#contacto" data-wsp data-wsp-msg="{wsp}">
            {ICO_WSP.format(s=18)}
            <span>Pedir asesoramiento</span>
          </a>
        </li>
      </ul>
    </nav>
    <a class="cta-wsp header-cta" href="#contacto" data-wsp data-wsp-msg="{wsp}" aria-label="Pedir presupuesto por WhatsApp">
      {ICO_WSP.format(s=18)}
      <span>WhatsApp</span>
    </a>
    <button class="nav-toggle" aria-controls="primary-nav" aria-expanded="false" aria-label="Abrir menú">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<main id="contenido">

  <section class="hero page-hero" aria-labelledby="hero-title">
    <div class="hero-image">
      {picture(p['hero'], p['hero_alt'], 'fetchpriority="high" decoding="async" style="object-position:' + p['hero_pos'] + '"')}
    </div>
    <div class="hero-overlay" aria-hidden="true"></div>
    <div class="container hero-content">
      <nav class="crumbs" aria-label="Estás en"><a href="/">Inicio</a><span>/</span><a href="/#productos">Productos</a><span>/</span><span aria-current="page">{e(p['nombre'])}</span></nav>
      <h1 id="hero-title">{e(p['h1'])}</h1>
      <p class="hero-sub">{e(p['lead'])}</p>
      <div class="hero-actions">
        <a class="cta-primary" href="#contacto" data-wsp data-wsp-msg="{wsp}">
          {ICO_WSP.format(s=18)}
          Pedir asesoramiento sin cargo
        </a>
        <a class="cta-secondary" href="#detalle">Ver detalles</a>
      </div>
      <ul class="hero-meta" aria-label="Beneficios principales">
        <li>Medición a domicilio sin cargo</li>
        <li>Taller e instalación propios</li>
        <li>CABA y Gran Buenos Aires</li>
      </ul>
    </div>
  </section>

  <section class="intro" id="detalle" aria-labelledby="intro-title">
    <div class="container intro-grid">
      <div class="intro-text">
        <p class="eyebrow">{e(p['nombre'])}</p>
        <h2 id="intro-title">{e(p['intro_titulo'])}</h2>
{intro_ps}
        <ul class="intro-facts" aria-label="Datos del producto">
{datos}
        </ul>
      </div>
      <figure class="intro-figure">
        {picture(p['intro_img'], p['intro_img_alt'], LAZY)}
      </figure>
    </div>
  </section>

  <section class="usos" aria-labelledby="usos-title">
    <div class="container">
      <header class="section-head">
        <p class="eyebrow">Usos</p>
        <h2 id="usos-title">{e(p['usos_titulo'])}</h2>
      </header>
      <ul class="usos-grid">
{usos}
      </ul>
    </div>
  </section>

  <section class="gallery" aria-labelledby="gallery-title">
    <div class="container">
      <header class="section-head">
        <p class="eyebrow">Trabajos</p>
        <h2 id="gallery-title">{e(p['nombre'])} en casas reales</h2>
      </header>
      <div class="gallery-grid gallery-simple">
{gal}
      </div>
      <p class="gallery-more">
        <a href="/#galeria" class="text-link">Ver la galería completa</a>
      </p>
    </div>
  </section>

  <section class="faq" aria-labelledby="faq-title">
    <div class="container faq-inner">
      <header class="section-head">
        <p class="eyebrow">Preguntas frecuentes</p>
        <h2 id="faq-title">Lo que nos preguntan sobre {e(p['nombre'].lower())}</h2>
      </header>
      <div class="faq-list">
{faqs}
      </div>
    </div>
  </section>

  <section class="related" aria-labelledby="related-title">
    <div class="container">
      <header class="section-head">
        <p class="eyebrow">También a medida</p>
        <h2 id="related-title">Otros productos</h2>
      </header>
      <ul class="related-grid">
{related}
      </ul>
    </div>
  </section>

  <section class="contact" id="contacto" aria-labelledby="contact-title">
    <div class="container contact-inner">
      <p class="eyebrow light">Contacto</p>
      <h2 id="contact-title">Pedí tu asesoramiento sin cargo</h2>
      <p class="contact-sub">Escribinos por WhatsApp con una foto de la ventana, las medidas aproximadas y el estilo que te imaginás. En el día te contestamos.</p>
      <a class="cta-wsp big" href="#" data-wsp data-wsp-msg="{wsp}" aria-label="Abrir conversación de WhatsApp con Entre Luz Home">
        {ICO_WSP.format(s=22)}
        <span>{e(p['cta'])}</span>
      </a>
      <p class="contact-fine">Atención de lunes a sábados, de 8 a 19 hs · Buenos Aires y alrededores</p>
    </div>
  </section>

</main>

<footer class="site-footer">
  <div class="container footer-inner">
    <div class="footer-brand">
      <picture>
        <source srcset="/images/logo-light.webp" type="image/webp">
        <img src="/images/logo-light.png" alt="Entre Luz Home" class="footer-logo" width="800" height="220" loading="lazy" decoding="async">
      </picture>
      <p>Cortinas, cortinados y ropa de cama a medida.<br>Estudio textil para obras y espacios.</p>
    </div>
    <nav aria-label="Productos a medida">
      <ul>
{product_links_html('')}
      </ul>
    </nav>
    <nav aria-label="Pie de página">
      <ul>
        <li><a href="/#galeria">Galería</a></li>
        <li><a href="/#proceso">Proceso</a></li>
        <li><a href="/#faq">Preguntas</a></li>
        <li><a href="/#contacto">Contacto</a></li>
      </ul>
    </nav>
    <ul class="footer-social" aria-label="Redes y contacto">
      <li>
        <a href="https://www.instagram.com/entre_telashome/" target="_blank" rel="noopener" aria-label="Seguinos en Instagram">
          <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><use href="#ico-ig"/></svg>
          <span>@entre_telashome</span>
        </a>
      </li>
      <li>
        <a href="#" data-wsp data-wsp-msg="{wsp}" aria-label="Escribir por WhatsApp">
          {ICO_WSP.format(s=20)}
          <span>WhatsApp</span>
        </a>
      </li>
    </ul>
    <p class="footer-legal">© <span id="year">2026</span> Entre Luz Home. Todos los derechos reservados.</p>
  </div>
</footer>

<div class="mobile-cta" aria-label="Contacto rápido">
  <a class="cta-wsp" href="#" data-wsp data-wsp-msg="{wsp}">
    {ICO_WSP.format(s=20)}
    <span>Pedir asesoramiento sin cargo</span>
  </a>
</div>

<a class="wsp-float" href="#" data-wsp data-wsp-msg="{wsp}" aria-label="Escribir por WhatsApp">
  {ICO_WSP.format(s=28)}
</a>

<script src="/script.js" defer></script>
</body>
</html>
"""

def main():
    root = pathlib.Path(__file__).parent
    for p in PRODUCTOS:
        (root / f"{p['slug']}.html").write_text(render(p), encoding="utf-8")
        print("ok", p["slug"] + ".html")
    # sitemap: agregar URLs de producto si faltan
    sm = root / "sitemap.xml"
    xml = sm.read_text(encoding="utf-8")
    add = ""
    for p in PRODUCTOS:
        url = f"{SITE}/{p['slug']}"
        if url + "<" in xml or url + "\n" in xml:
            continue
        add += (f"  <url>\n    <loc>{url}</loc>\n    <lastmod>{HOY}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n"
                f"    <image:image>\n      <image:loc>{SITE}/images/{p['hero']}.jpg</image:loc>\n      <image:caption>{e(p['hero_alt'])}</image:caption>\n    </image:image>\n  </url>\n")
    if add:
        xml = xml.replace("</urlset>", add + "</urlset>")
        sm.write_text(xml, encoding="utf-8")
        print("sitemap actualizado")

if __name__ == "__main__":
    main()
