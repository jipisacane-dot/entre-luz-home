# Entre Luz Home — sitio web

Sitio estático ultraliviano (HTML + CSS + JS vanilla). Sin frameworks ni build step.
Publicado en Vercel: **https://entreluz.casa** (proyecto `entre-telas`, alias `entre-telas-liard.vercel.app`).

## Estructura

```
entre-luz-home/
├── index.html      # única página, con JSON-LD (LocalBusiness, WebSite, WebPage, FAQPage)
├── styles.css
├── script.js       # WhatsApp links, header, menú mobile, reveal, lightbox
├── robots.txt
├── sitemap.xml     # con extensión de imágenes
├── vercel.json     # cache de imágenes + headers de seguridad
├── LEEME.md
└── images/         # fotos en .jpg + .webp, logo en variantes, og-cover.jpg, favicons
```

## Cosas que se editan seguido

- **Número de WhatsApp:** `WSP_NUMERO` en [script.js](script.js).
- **Horarios / zona:** en el JSON-LD (`openingHoursSpecification`, `address`, `areaServed`) y en el texto de la sección Contacto.
- **Preguntas frecuentes:** están dos veces, en el HTML visible (`<section class="faq">`) y en el JSON-LD `FAQPage`. Mantener ambas iguales.
- **Instagram:** `@entre_telashome` aparece en el JSON-LD (`sameAs`), en la galería y en el footer.

## Logo

- `images/logo.jpg` — original con fondo lino (se usa para el `logo` del JSON-LD).
- `images/logo-dark.png/.webp` — sin fondo, tinta oscura. Header al hacer scroll.
- `images/logo-light.png/.webp` — sin fondo, crema. Header sobre el hero y footer.
- `images/apple-touch-icon.png` (180px) y `images/favicon-32.png`.

## Imágenes

Cada foto tiene versión `.jpg` (fallback) y `.webp` (se sirve primero vía `<picture>`).
Para sumar una foto nueva: exportar a ~1600px de lado mayor, generar el `.webp`, agregarla con `<picture>`, `alt` descriptivo, `width`/`height`, `loading="lazy"` y sumarla a `sitemap.xml`.

## Probar localmente

```bash
python3 -m http.server 8000
# abrir http://localhost:8000
```

## Publicar

Con la CLI de Vercel desde esta carpeta (ya está linkeada al proyecto en `.vercel/`):

```bash
npx vercel --prod
```

## SEO implementado

- Title y meta description con keyword + ciudad
- Canonical, Open Graph (imagen 1200×630) y Twitter Card
- JSON-LD: `LocalBusiness` + `WebSite` + `WebPage` + `FAQPage` (con FAQ visible en la página)
- robots.txt + sitemap.xml con imágenes
- HTML semántico, un solo `h1`, `h2` por sección con keywords
- `alt` descriptivo en todas las fotos, `width`/`height` para evitar CLS, `loading="lazy"`
- WebP con fallback JPG, preload del hero, `fetchpriority="high"`
- Headers de cache e inmutabilidad para imágenes (vercel.json)
