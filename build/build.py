#!/usr/bin/env python3
"""Gera o site estático da Jusante em ../ (raiz do repositório).
O e-mail de contato vem da variável de ambiente JUSANTE_EMAIL (opcional)."""
import json, os, shutil, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
BASE = 'https://jusante.com.br'
TODAY = datetime.date.today().isoformat()
WA = 'https://wa.me/5511986489818?text=Ol%C3%A1%2C%20gostaria%20de%20falar%20sobre%20assist%C3%AAncia%20t%C3%A9cnica%20pericial.'
EMAIL = os.environ.get('JUSANTE_EMAIL', '').strip()
_cf = os.path.join(os.path.dirname(__file__), 'contato.txt')
if not EMAIL and os.path.exists(_cf):
    EMAIL = open(_cf).read().strip()
TEL = '(11) 98648-9818'

SERVICOS = [
    ('/assistencia-tecnica-pericia-trabalhista/', 'Assistência técnica em perícia trabalhista'),
    ('/pericia-insalubridade/', 'Perícia de insalubridade (NR-15)'),
    ('/pericia-periculosidade/', 'Perícia de periculosidade (NR-16)'),
    ('/acidente-de-trabalho-e-ergonomia/', 'Acidente de trabalho e ergonomia'),
    ('/ltcat-ppp-extemporaneo/', 'LTCAT e PPP extemporâneo'),
    ('/consultoria-ssma/', 'Consultoria SSMA, PGR e treinamentos'),
]

ORG = {
    "@type": "ProfessionalService", "@id": BASE + "/#org",
    "name": "Jusante Perícias e SSMA", "alternateName": "Jusante Engenharia",
    "url": BASE + "/", "logo": BASE + "/assets/img/icon-512.png", "image": BASE + "/assets/img/og.jpg",
    "telephone": "+55-11-98648-9818",
    "address": {"@type": "PostalAddress", "addressLocality": "São Paulo", "addressRegion": "SP", "addressCountry": "BR"},
    "areaServed": ["São Paulo", "Brasil"],
    "founder": {"@id": BASE + "/eng-clayton-mendel/#person"},
    "sameAs": ["https://www.instagram.com/jusantessma/", "https://www.linkedin.com/company/jusante"],
    "knowsAbout": ["Assistência técnica pericial", "Perícia trabalhista", "Insalubridade", "Periculosidade",
                   "Ergonomia", "LTCAT", "PPP", "Higiene ocupacional", "Segurança do Trabalho"],
}
if EMAIL:
    ORG["email"] = EMAIL
PERSON = {
    "@type": "Person", "@id": BASE + "/eng-clayton-mendel/#person",
    "name": "Clayton Wallace Mendel Martins", "alternateName": "Eng. Clayton Mendel",
    "jobTitle": "Engenheiro de Segurança do Trabalho", "image": BASE + "/assets/img/clayton-mendel.webp",
    "url": BASE + "/eng-clayton-mendel/", "worksFor": {"@id": BASE + "/#org"},
    "hasCredential": {"@type": "EducationalOccupationalCredential", "name": "CREA-SP 5070143507"},
    "sameAs": ["https://www.linkedin.com/in/clayton-mendel"],
}

ICON_WA = '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.6c-2 0-4-.6-5.7-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.6 10.6 0 1 1 16 26.6zm5.8-7.9c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2l-1 1.2c-.2.2-.4.2-.7.1a8.7 8.7 0 0 1-4.3-3.8c-.3-.6.3-.5.9-1.7.1-.2 0-.4 0-.5l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.8s1.2 3.3 1.4 3.5c.2.2 2.4 3.7 5.8 5.1 2.2.9 3 1 4.1.8.7-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.1-.3-.2-.6-.3z"/></svg>'


def email_link(prefix=''):
    if not EMAIL:
        return ''
    return f'{prefix}<a href="mail' + f'to:{EMAIL}">{EMAIL}</a>'


def head(title, desc, path, extra_ld=None):
    ld = {"@context": "https://schema.org", "@graph": [ORG, PERSON] + (extra_ld or [])}
    url = BASE + path
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#0a181d">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Jusante Perícias e SSMA">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/montserrat-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#conteudo">Ir para o conteúdo</a>
'''


def header():
    svc = ''.join(f'<a href="{u}">{n}</a>' for u, n in SERVICOS)
    return f'''<header class="site"><div class="wrap">
<a class="brand" href="/" aria-label="Jusante Perícias e SSMA – início"><img src="/assets/img/logo.webp" alt="Jusante Perícias e SSMA" width="226" height="100"></a>
<nav class="main" aria-label="Principal">
<details class="svc"><summary>Serviços</summary><div class="dd">{svc}</div></details>
<a href="/#metodo">Método</a>
<a href="/eng-clayton-mendel/">Responsável técnico</a>
<a href="/#contato">Contato</a>
<a class="cta" href="{WA}" target="_blank" rel="noopener">Fale no WhatsApp</a>
</nav>
<details class="mob"><summary>Menu</summary><div class="panel">{svc}<a href="/#metodo">Método</a><a href="/eng-clayton-mendel/">Responsável técnico</a><a href="/#contato">Contato</a><a href="{WA}" target="_blank" rel="noopener">WhatsApp {TEL}</a></div></details>
</div></header>
<main id="conteudo">
'''


def cta_band(title='Precisa de apoio técnico em uma perícia?', text='Conte brevemente sua necessidade. Retornamos para entender o caso e indicar o melhor caminho.'):
    return f'''<section><div class="wrap"><div class="cta-band">
<img class="mark" src="/assets/img/mark.webp" alt="">
<div><h2>{title}</h2><p>{text}</p></div>
<a class="btn pri" href="{WA}" target="_blank" rel="noopener">Falar no WhatsApp</a>
</div></div></section>
'''


def footer():
    svc = ''.join(f'<a href="{u}">{n}</a>' for u, n in SERVICOS)
    return f'''</main>
<footer class="site" id="contato"><div class="wrap">
<div class="cols">
<div><img src="/assets/img/logo.webp" alt="Jusante Perícias e SSMA" width="181" height="80" style="height:80px;width:auto">
<p style="margin-top:16px;max-width:360px">Engenharia de Segurança do Trabalho aplicada à prova técnica. Assistência técnica pericial para escritórios de advocacia e empresas, para reclamantes e reclamadas.</p></div>
<div><h4>Serviços</h4>{svc}</div>
<div><h4>Contato</h4>
<a href="{WA}" target="_blank" rel="noopener">WhatsApp {TEL}</a>
{email_link()}
<a href="https://www.instagram.com/jusantessma/" target="_blank" rel="noopener">Instagram @jusantessma</a>
<a href="https://www.linkedin.com/company/jusante" target="_blank" rel="noopener">LinkedIn</a>
<p style="margin-top:8px">São Paulo/SP · atendimento em todo o Brasil</p></div>
</div>
<div class="legal">Jusante Perícias e SSMA · CNPJ 55.532.612/0001-17 · Responsável técnico: Eng. Clayton Mendel, CREA-SP 5070143507</div>
</div></footer>
<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="Falar no WhatsApp">{ICON_WA}</a>
</body>
</html>
'''


def hero_page(eyebrow, h1, lead, crumb):
    return f'''<section class="hero page"><img class="mark" src="/assets/img/mark.webp" alt=""><div class="wrap">
<div class="crumbs"><a href="/">Início</a> › {crumb}</div>
<div class="eyebrow">{eyebrow}</div>
<h1>{h1}</h1>
<p class="lead">{lead}</p>
<div class="actions"><a class="btn pri" href="{WA}" target="_blank" rel="noopener">Falar pelo WhatsApp</a></div>
</div></section>
'''


def faq_block(items):
    html = '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + '</div>'
    ld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q,
          "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}
    return html, ld


def crumb_ld(name, path):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Início", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": BASE + path}]}


def side_box():
    return f'''<aside class="box"><h3>Fale com a Jusante</h3>
<p>Conte brevemente o caso. Retornamos para entender a demanda e indicar o melhor caminho.</p>
<a class="btn dark" href="{WA}" target="_blank" rel="noopener">WhatsApp {TEL}</a>
{email_link('<p style="margin-top:14px">') + ('</p>' if EMAIL else '')}
<p style="margin-top:18px;font-size:13px">Atendimento a escritórios de advocacia e empresas, para reclamantes e reclamadas.</p></aside>'''


def service_page(path, title, desc, eyebrow, h1, lead, crumb, body, faqs, related):
    faq_html, faq_ld = faq_block(faqs)
    rel = ''.join(f'<a class="card" href="{u}"><h3>{n}</h3><span class="more" style="margin-top:12px">Ver serviço →</span></a>'
                  for u, n in SERVICOS if u in related)
    html = head(title, desc, path, [crumb_ld(crumb, path), faq_ld,
                {"@type": "Service", "name": crumb, "provider": {"@id": BASE + "/#org"},
                 "areaServed": "BR", "description": desc}])
    html += header() + hero_page(eyebrow, h1, lead, crumb)
    html += f'''<section><div class="wrap aside"><div class="prose">{body}
<h2>Perguntas frequentes</h2>{faq_html}</div>{side_box()}</div></section>
<section class="soft"><div class="wrap"><div class="eyebrow">Serviços relacionados</div><div class="grid g3">{rel}</div></div></section>
'''
    html += cta_band() + footer()
    write(path, html)


def write(path, html):
    if path.endswith('.html'):
        out = os.path.join(ROOT, path.strip('/'))
    elif path == '/':
        out = os.path.join(ROOT, 'index.html')
    else:
        out = os.path.join(ROOT, path.strip('/'), 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(html)
    PAGES.append(path)


PAGES = []
exec(open(os.path.join(os.path.dirname(__file__), 'content.py'), encoding='utf-8').read())

shutil.copy(os.path.join(os.path.dirname(__file__), 'style.css'), os.path.join(ROOT, 'assets', 'style.css'))
open(os.path.join(ROOT, 'CNAME'), 'w').write('jusante.com.br\n')
open(os.path.join(ROOT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n')
urls = ''.join(f'<url><loc>{BASE}{p}</loc><lastmod>{TODAY}</lastmod></url>' for p in PAGES if not p.endswith('.html'))
open(os.path.join(ROOT, 'sitemap.xml'), 'w').write(
    f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
print('\n'.join(PAGES))
