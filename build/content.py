# Conteúdo das páginas. Executado dentro de build.py (usa as funções de lá).

ICONS = [
 '<path d="M12 3v18M7 21h10M5 7h14M5 7l-3 7a3 3 0 0 0 6 0zM19 7l-3 7a3 3 0 0 0 6 0z"/>',
 '<path d="M14 14.8V4a2 2 0 1 0-4 0v10.8a4 4 0 1 0 4 0zM12 9v7"/>',
 '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
 '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M12 8v5M12 16h0"/>',
 '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
 '<path d="M3 21h18M5 21V8l7-5 7 5v13M9 21v-6h6v6"/>',
]
home_cards = ''.join(f'''<a class="card" href="{u}"><span class="ico-b"><svg viewBox="0 0 24 24">{ICONS[i-1]}</svg></span><h3>{n}</h3><p>{d}</p><span class="more">Saiba mais →</span></a>'''
    for i, ((u, n), d) in enumerate(zip(SERVICOS, [
        'Análise dos autos, quesitos, acompanhamento da diligência, parecer técnico e análise crítica do laudo.',
        'Agentes físicos, químicos e biológicos avaliados pela atividade real, tempo de exposição, EPC e EPI.',
        'Inflamáveis, explosivos, energia elétrica, motocicleta e segurança pessoal, com análise de área de risco e frequência.',
        'Investigação das condições operacionais, organização do trabalho, fatores de risco e nexo técnico.',
        'Reconstrução técnica das condições de trabalho em períodos passados, para PPP e aposentadoria especial.',
        'PGR, LTCAT, inspeções, NR-13 e treinamentos presenciais ou EAD para empresas.',
    ]), start=1))

home = head('Assistência Técnica em Perícia Trabalhista em São Paulo | Jusante',
            'Assistência técnica em perícias trabalhistas de insalubridade, periculosidade, acidente de trabalho, ergonomia, LTCAT e PPP. Para escritórios de advocacia e empresas, em São Paulo e todo o Brasil.',
            '/')
home += header()
home += f'''<section class="hero home"><img class="mark" src="/assets/img/mark.webp" alt=""><div class="wrap hero-split">
<div><div class="eyebrow">Assistência técnica em perícias trabalhistas</div>
<h1>Segurança do Trabalho aplicada à <em>prova técnica</em>.</h1>
<p class="lead">Assistência técnica pericial para escritórios de advocacia e empresas, para reclamantes e reclamadas, em perícias de insalubridade, periculosidade, acidente de trabalho, ergonomia, LTCAT e PPP.</p>
<div class="actions"><a class="btn pri" href="{WA}" target="_blank" rel="noopener">Falar pelo WhatsApp</a><a class="btn sec" href="#servicos">Ver serviços</a></div></div>
<img class="hero-img" src="/assets/img/equipe.webp" alt="Equipe em treinamento de Segurança do Trabalho conduzido pela Jusante" width="1400" height="1050" fetchpriority="high">
</div></section>
<div class="wrap"><div class="stats">
<div class="stat"><b><small>+</small>410</b><span>assistências técnicas periciais</span></div>
<div class="stat"><b><small>+</small>70</b><span>peritos judiciais acompanhados</span></div>
<div class="stat"><b><small>+</small>15</b><span>anos de atuação em SSMA</span></div>
<div class="stat"><b>360°</b><span>antes, durante e depois da perícia</span></div>
</div></div>

<section id="servicos"><div class="wrap">
<div class="eyebrow">Serviços</div>
<h2>Assistência técnica para cada tipo de perícia.</h2>
<p class="lead">Cada trabalho parte do objeto da demanda, das atividades efetivamente exercidas e dos documentos disponíveis. A exposição se conclui pela atividade real, nunca pelo nome do cargo.</p>
<div class="grid g3">{home_cards}</div>
</div></section>

<section class="soft"><div class="wrap">
<div class="split" style="align-items:start">
<div><div class="eyebrow">Para quem atuamos</div>
<h2>Escritórios de advocacia e empresas.</h2>
<p class="lead">Atuamos para reclamantes e reclamadas, sempre com a mesma régua técnica.</p></div>
<div class="grid g2" style="margin-top:0">
<div class="card"><h3>Escritórios de advocacia</h3><p>Leitura técnica da inicial e da defesa, quesitos, acompanhamento da diligência, parecer e subsídios para manifestação sobre o laudo.</p></div>
<div class="card"><h3>Empresas</h3><p>Preparação documental para a perícia, orientação ao preposto, acompanhamento da diligência e prevenção de novos passivos.</p></div>
</div></div>
<h3 style="margin-top:56px;font-size:20px">O que costuma decidir uma perícia</h3>
<div class="factors">
<div><b>Eficácia do EPI</b><span>CA, vida útil, troca, treinamento e fiscalização do uso.</span></div>
<div><b>Tempo e forma de exposição</b><span>Habitualidade e frequência pela rotina real.</span></div>
<div><b>Área de risco</b><span>Delimitação prevista na NR-16 e ingresso efetivo.</span></div>
<div><b>Metodologia de medição</b><span>NHOs da Fundacentro e registro rastreável.</span></div>
</div>
</div></section>

<section id="metodo" class="dark"><div class="wrap">
<div class="eyebrow">Método Jusante</div>
<h2>Antes, durante e depois da perícia.</h2>
<div class="grid g3">
<div class="card"><span class="num">01 · PREPARAR</span><h3>Antes da perícia</h3><ul class="check"><li>Análise da inicial, da contestação e dos documentos técnicos (PPP, LTCAT, PGR, fichas de EPI)</li><li>Pontos controvertidos e quesitos</li><li>Conversa prévia com a parte assistida sobre a atividade real e a dinâmica da diligência</li></ul></div>
<div class="card"><span class="num">02 · VERIFICAR</span><h3>Na diligência</h3><ul class="check"><li>Acompanhamento da perícia judicial</li><li>Perguntas técnicas ao perito</li><li>Registro fotográfico e medições com equipamento próprio, quando cabível</li></ul></div>
<div class="card"><span class="num">03 · SUSTENTAR</span><h3>Depois do laudo</h3><ul class="check"><li>Análise crítica do laudo pericial</li><li>Parecer técnico assistencial</li><li>Subsídios para manifestação, impugnação e quesitos complementares</li></ul></div>
</div></div></section>

<section><div class="wrap split">
<img src="/assets/img/treinamento.webp" alt="Treinamento de Segurança do Trabalho conduzido pela Jusante" width="1400" height="1051" loading="lazy">
<div><div class="eyebrow">Campo e medições</div>
<h2>Engenheiros em campo, com medição própria.</h2>
<p class="lead">Além das perícias, a Jusante conduz treinamentos e programas de SST em empresas. Isso traz para o processo a leitura de quem conhece a operação por dentro.</p>
<div class="chips"><span class="chip">Ruído – NHO 01</span><span class="chip">Calor/IBUTG – NHO 06</span><span class="chip">Vibração – NHO 09 e 10</span><span class="chip">Iluminamento – NHO 11</span><span class="chip">Químicos com bomba</span><span class="chip">pH de produtos</span></div>
<p style="margin-top:20px">Vivência em indústria, construção civil, logística, alimentos, farmacêutico, hospitalar, cosméticos e varejo.</p>
<a class="btn dark" style="margin-top:22px" href="/consultoria-ssma/">Consultoria SSMA e treinamentos</a>
</div></div></section>

<section class="soft"><div class="wrap person">
<img src="/assets/img/clayton-mendel.webp" alt="Eng. Clayton Mendel, responsável técnico da Jusante" width="900" height="945" loading="lazy">
<div><div class="eyebrow">Responsável técnico</div>
<h2>Eng. Clayton Mendel</h2>
<p style="margin-top:10px;font-weight:600;color:var(--teal)">Engenheiro Ambiental e de Segurança do Trabalho · Pós-graduado em Ergonomia · CREA-SP 5070143507</p>
<p class="lead">Atuação em SSMA desde 2009, em ambientes corporativos e industriais. Mais de 410 assistências técnicas em perícias trabalhistas e cíveis, com experiência em diligências conduzidas por mais de 70 peritos judiciais.</p>
<p class="quote">O jurídico conduz a tese. A Jusante cuida da prova técnica.</p>
<a class="btn dark" style="margin-top:26px" href="/eng-clayton-mendel/">Conheça a trajetória</a></div>
</div></section>
'''

home += """
<section id="atendimento"><div class="wrap split">
<div><div class="eyebrow">Onde atendemos</div>
<h2>São Paulo, regiões metropolitanas e interior próximo.</h2>
<p class="lead">Diligências presenciais nas áreas do TRT-2 e do TRT-15. Demais localidades sob consulta.</p></div>
<div class="grid g2" style="margin-top:0">
<div class="card"><span class="num">TRT-2</span><h3>Capital e regiões metropolitanas</h3><p>São Paulo (capital), ABC (Santo André, São Bernardo do Campo, São Caetano do Sul, Diadema, Mauá), Guarulhos, Osasco, Barueri, Carapicuíba, Cotia, Taboão da Serra, Mogi das Cruzes, Suzano e Baixada Santista.</p></div>
<div class="card"><span class="num">TRT-15</span><h3>Interior próximo</h3><p>Campinas, Jundiaí, Sorocaba, Indaiatuba, Atibaia, Bragança Paulista e São José dos Campos.</p></div>
</div></div></section>

<section class="soft" id="fale"><div class="wrap split">
<div><div class="eyebrow">Fale com a Jusante</div>
<h2>Conte o caso em poucos cliques.</h2>
<p class="lead">Preencha os campos e a mensagem abre pronta no WhatsApp. Nada é gravado no site.</p></div>
<form class="card waform" id="waform">
<label>Você é<select name="perfil" required><option value="">Selecione</option><option>Advogado(a) do reclamante</option><option>Advogado(a) da reclamada</option><option>Empresa</option><option>Trabalhador(a)</option><option>Outro</option></select></label>
<label>Assunto<select name="assunto" required><option value="">Selecione</option><option>Insalubridade</option><option>Periculosidade</option><option>Acidente de trabalho</option><option>Ergonomia</option><option>LTCAT / PPP</option><option>PGR / consultoria SSMA</option><option>Treinamentos</option><option>Outro</option></select></label>
<label>Cidade<input name="cidade" placeholder="Ex.: Guarulhos"></label>
<label>Mensagem<textarea name="msg" rows="3" placeholder="Conte brevemente a necessidade"></textarea></label>
<button class="btn dark" type="submit">Abrir no WhatsApp</button>
</form>
</div></section>
<script>
document.getElementById('waform').addEventListener('submit',function(e){e.preventDefault();var f=e.target;
var t='Olá, vim pelo site da Jusante.\\nPerfil: '+f.perfil.value+'\\nAssunto: '+f.assunto.value+(f.cidade.value?'\\nCidade: '+f.cidade.value:'')+(f.msg.value?'\\n\\n'+f.msg.value:'');
window.open('https://wa.me/5511986489818?text='+encodeURIComponent(t),'_blank','noopener');});
</script>
"""

home += footer()
write('/', home)

# ---------------------------------------------------------------- ASSISTÊNCIA TÉCNICA
service_page('/assistencia-tecnica-pericia-trabalhista/',
 'Assistência Técnica em Perícia Trabalhista em São Paulo | Jusante',
 'Assistente técnico em perícia trabalhista: análise dos autos, quesitos, acompanhamento da diligência, parecer técnico e análise crítica do laudo. Para escritórios e empresas.',
 'Assistência técnica pericial', 'Assistência técnica em perícia trabalhista',
 'Engenharia de Segurança do Trabalho do início do processo à análise do laudo, para escritórios de advocacia e empresas, reclamantes e reclamadas.',
 'Assistência técnica em perícia trabalhista',
 '''<h2>O que faz o assistente técnico</h2>
<p>Na perícia trabalhista, o juiz nomeia um perito de sua confiança e as partes podem indicar assistentes técnicos. O assistente acompanha os trabalhos, formula quesitos, apresenta parecer e aponta, com fundamento técnico, o que o laudo deixou de considerar. Quando o juiz se afasta da conclusão do perito, costuma ser porque há outro fundamento técnico nos autos. O parecer do assistente é esse fundamento.</p>
<h2>Como trabalhamos</h2>
<ul>
<li><strong>Análise dos autos:</strong> inicial, contestação, documentos técnicos (PPP, LTCAT, PGR, fichas de EPI, FISPQs) e pontos controvertidos.</li>
<li><strong>Quesitos:</strong> objetivos, ligados à atividade real e aos critérios das Normas Regulamentadoras.</li>
<li><strong>Preparação:</strong> conversa prévia com a parte assistida (trabalhador, ou empresa e preposto) sobre a atividade e a dinâmica da diligência.</li>
<li><strong>Diligência:</strong> acompanhamento presencial, perguntas técnicas ao perito, registro fotográfico e medições com equipamento próprio, quando cabível.</li>
<li><strong>Depois do laudo:</strong> análise crítica, parecer técnico assistencial e subsídios para manifestação, impugnação e quesitos complementares.</li>
</ul>
<h2>Temas mais frequentes</h2>
<div class="chips"><span class="chip">Insalubridade</span><span class="chip">Periculosidade</span><span class="chip">Acidente de trabalho</span><span class="chip">Ergonomia</span><span class="chip">Eficácia de EPI</span><span class="chip">LTCAT e PPP</span><span class="chip">Aposentadoria especial</span></div>
<h2>Onde atuamos</h2>
<p>Sede em São Paulo, com atuação na capital, região metropolitana, interior e outros estados, conforme a demanda.</p>''',
 [('Quando contratar o assistente técnico?', 'O ideal é antes da apresentação dos quesitos, para que a perícia já parta das perguntas certas. Também é possível entrar depois do laudo, para análise crítica e parecer.'),
  ('A Jusante atende reclamante e reclamada?', 'Sim. Atuamos para escritórios de advocacia e empresas, tanto pelo reclamante quanto pela reclamada, com o mesmo critério técnico.'),
  ('O que preciso enviar?', 'O número do processo já permite a análise inicial. Se houver, envie também a ata com a nomeação do perito e os documentos técnicos da empresa.'),
  ('Vocês fazem medições na diligência?', 'Sim, quando cabível, com equipamentos próprios para ruído, calor, vibração, iluminamento e amostragem de químicos.')],
 ['/pericia-insalubridade/', '/pericia-periculosidade/', '/acidente-de-trabalho-e-ergonomia/'])

# ---------------------------------------------------------------- INSALUBRIDADE
service_page('/pericia-insalubridade/',
 'Perícia de Insalubridade (NR-15): Assistência Técnica | Jusante',
 'Assistência técnica em perícia de insalubridade: ruído, calor, químicos, biológicos, vibração e frio. Análise pela atividade real, exposição, EPC e EPI conforme a NR-15.',
 'NR-15', 'Perícia de insalubridade',
 'Análise da exposição pela atividade real, frequência, agente e medidas de controle (EPC e EPI), com enquadramento nos anexos da NR-15.',
 'Perícia de insalubridade',
 '''<h2>Como a insalubridade é caracterizada</h2>
<p>A caracterização depende de perícia a cargo de engenheiro ou médico do trabalho (CLT, art. 195). A conclusão não sai do nome do cargo nem do produto: sai da atividade efetivamente exercida, do agente, da forma e do tempo de exposição e da eficácia das medidas de proteção.</p>
<h2>Agentes mais discutidos</h2>
<ul>
<li><strong>Ruído (Anexo 1):</strong> avaliação de dose conforme a NHO 01, considerando jornada e atenuação do protetor auditivo.</li>
<li><strong>Calor (Anexo 3):</strong> IBUTG conforme a NHO 06, com análise de taxa metabólica e regime de trabalho.</li>
<li><strong>Agentes químicos (Anexos 11 e 13):</strong> avaliação quantitativa ou qualitativa conforme o agente, com análise das FISPQs e da forma de contato.</li>
<li><strong>Agentes biológicos (Anexo 14):</strong> enquadramento pela atividade e pelo tipo de contato descritos no anexo.</li>
<li><strong>Vibração (Anexo 8), frio (Anexo 9) e umidade (Anexo 10).</strong></li>
</ul>
<h2>EPI e eficácia</h2>
<p>O fornecimento do EPI, por si só, não afasta o adicional. Pesam a adequação ao risco, o Certificado de Aprovação, a vida útil, a periodicidade de troca, o treinamento e a fiscalização do uso. Esses pontos são verificados nos documentos e na diligência.</p>
<h2>Medições próprias</h2>
<p>Quando a avaliação quantitativa é cabível, realizamos medições com equipamentos próprios para ruído, calor, vibração, iluminamento e amostragem de químicos com bomba.</p>''',
 [('A insalubridade depende do cargo?', 'Não. A conclusão depende da atividade real, do agente, da frequência e do tempo de exposição e das medidas de controle. O nome do cargo não define a exposição.'),
  ('O uso de EPI elimina a insalubridade?', 'Pode eliminar ou neutralizar, desde que o EPI seja adequado ao risco, tenha CA válido, seja substituído na periodicidade correta e tenha uso orientado e fiscalizado.'),
  ('Quais documentos ajudam na perícia?', 'PPP, LTCAT, PGR, fichas de entrega de EPI, FISPQs dos produtos e laudos ambientais anteriores.')],
 ['/assistencia-tecnica-pericia-trabalhista/', '/pericia-periculosidade/', '/ltcat-ppp-extemporaneo/'])

# ---------------------------------------------------------------- PERICULOSIDADE
service_page('/pericia-periculosidade/',
 'Perícia de Periculosidade (NR-16): Assistência Técnica | Jusante',
 'Assistência técnica em perícia de periculosidade: inflamáveis, explosivos, energia elétrica, motocicleta e segurança pessoal. Análise de área de risco, atividade e frequência conforme a NR-16.',
 'NR-16', 'Perícia de periculosidade',
 'Análise da atividade, da área de risco e da frequência de exposição, com enquadramento nos anexos da NR-16.',
 'Perícia de periculosidade',
 '''<h2>O que define a periculosidade</h2>
<p>A periculosidade é caracterizada por perícia (CLT, art. 195) e depende do enquadramento da atividade nos anexos da NR-16. Na prática, o debate costuma girar em torno de três pontos: se a atividade está prevista no anexo, se o trabalhador ingressava na área de risco e com que frequência.</p>
<h2>Situações mais comuns</h2>
<ul>
<li><strong>Inflamáveis (Anexo 2):</strong> abastecimento, armazenamento, áreas de risco e quantidades.</li>
<li><strong>Explosivos (Anexo 1).</strong></li>
<li><strong>Energia elétrica (Anexo 4):</strong> atividades em instalações ou equipamentos elétricos energizados.</li>
<li><strong>Segurança pessoal e patrimonial (Anexo 3).</strong></li>
<li><strong>Atividades em motocicleta (Anexo 5).</strong></li>
</ul>
<h2>Frequência de exposição</h2>
<p>O contato eventual ou fortuito, ou o habitual por tempo extremamente reduzido, tem tratamento diferente do contato permanente ou intermitente. Por isso a descrição precisa da rotina, com tempos e locais, é decisiva para a conclusão.</p>''',
 [('Basta trabalhar perto de inflamáveis?', 'Não. É preciso verificar se o local é área de risco nos termos do anexo, as quantidades envolvidas e se havia ingresso na área, com que frequência.'),
  ('A periculosidade depende de medição?', 'Em geral, não. A análise é principalmente qualitativa: atividade, local, área de risco e frequência.'),
  ('O que levar para a diligência?', 'A descrição da rotina real, com locais e tempos, além de plantas, licenças e documentos de SST da empresa.')],
 ['/assistencia-tecnica-pericia-trabalhista/', '/pericia-insalubridade/', '/acidente-de-trabalho-e-ergonomia/'])

# ---------------------------------------------------------------- ACIDENTE / ERGONOMIA
service_page('/acidente-de-trabalho-e-ergonomia/',
 'Perícia de Acidente de Trabalho e Ergonomia (NR-17) | Jusante',
 'Assistência técnica em perícias de acidente de trabalho e ergonomia: condições operacionais, organização do trabalho, fatores de risco, medidas preventivas e NR-17.',
 'Prova técnica', 'Acidente de trabalho e ergonomia',
 'Investigação das condições operacionais, da organização do trabalho, dos fatores de risco e das medidas preventivas existentes.',
 'Acidente de trabalho e ergonomia',
 '''<h2>Acidente de trabalho</h2>
<p>A perícia de engenharia em acidente de trabalho reconstrói como a atividade era executada, quais riscos existiam e quais medidas de prevenção estavam implantadas. Analisamos procedimentos, treinamentos, ordens de serviço, análises de risco, proteções de máquinas (NR-12), EPIs e o histórico da investigação do acidente.</p>
<h2>Ergonomia</h2>
<p>Em demandas ergonômicas, a análise considera o posto de trabalho, a organização do trabalho, os ritmos, as pausas e as exigências físicas e cognitivas, com base na NR-17 e na avaliação ergonômica da empresa (AEP e, quando exigida, AET).</p>
<h2>O que entregamos</h2>
<ul>
<li>Quesitos voltados à dinâmica do evento ou à exigência ergonômica real.</li>
<li>Acompanhamento da diligência e registro das condições do posto.</li>
<li>Parecer técnico e análise crítica do laudo, com confronto entre normas, documentos e o que foi verificado em campo.</li>
</ul>
<p>Questões de nexo e incapacidade são médicas. Nessas demandas, atuamos na parte de engenharia e podemos trabalhar ao lado do assistente técnico médico.</p>''',
 [('A engenharia define o nexo causal?', 'O nexo e a incapacidade são temas médicos. A engenharia analisa as condições de trabalho, os riscos e as medidas preventivas, que servem de base para essa discussão.'),
  ('Que documentos são importantes em acidente de trabalho?', 'CAT, relatório de investigação, ordens de serviço, treinamentos, fichas de EPI, análise de risco e documentação das máquinas envolvidas.'),
  ('A AET é sempre obrigatória?', 'Não. A NR-17 prevê a avaliação ergonômica preliminar e exige a AET em situações específicas descritas na norma.')],
 ['/assistencia-tecnica-pericia-trabalhista/', '/pericia-insalubridade/', '/consultoria-ssma/'])

# ---------------------------------------------------------------- LTCAT / PPP
service_page('/ltcat-ppp-extemporaneo/',
 'LTCAT Extemporâneo e PPP para Aposentadoria Especial | Jusante',
 'LTCAT extemporâneo e análise de PPP: reconstrução técnica das condições de trabalho em períodos passados, para aposentadoria especial e revisão de PPP.',
 'Previdenciário', 'LTCAT extemporâneo e PPP',
 'Reconstrução técnica das condições ambientais de trabalho em períodos passados, para aposentadoria especial e revisão de PPP.',
 'LTCAT e PPP extemporâneo',
 '''<h2>Quando o documento não existe ou não retrata a realidade</h2>
<p>O PPP deve se basear no LTCAT (Lei 8.213/91, art. 58). Quando a empresa não tem o laudo do período, o PPP está incompleto ou descreve agentes de forma genérica, é possível reconstruir tecnicamente as condições de trabalho do passado.</p>
<h2>Como reconstruímos</h2>
<ul>
<li>Levantamento do histórico ocupacional: funções, setores, processos e equipamentos de cada período.</li>
<li>Análise de documentos existentes: PPRA/PGR, LTCATs anteriores, laudos ambientais, fichas de EPI e FISPQs.</li>
<li>Avaliação de campo, quando o ambiente ainda existe ou é similar, com medições próprias.</li>
<li>Conclusão fundamentada sobre agentes, intensidade, habitualidade e permanência no período analisado.</li>
</ul>
<div class="chips"><span class="chip">PPP</span><span class="chip">PGR/PPRA</span><span class="chip">LTCAT anterior</span><span class="chip">Fichas de EPI</span><span class="chip">FISPQs</span><span class="chip">Laudos ambientais</span><span class="chip">Histórico ocupacional</span></div>''',
 [('O que é LTCAT extemporâneo?', 'É o laudo elaborado depois do período a que se refere, para reconstruir tecnicamente as condições de trabalho daquela época.'),
  ('Serve para aposentadoria especial?', 'Serve como prova técnica da exposição. A aceitação depende da fundamentação e da análise do INSS ou do Judiciário.'),
  ('E se a empresa fechou?', 'É possível trabalhar com documentos remanescentes, ambientes similares e o histórico ocupacional, com as ressalvas técnicas cabíveis.')],
 ['/pericia-insalubridade/', '/assistencia-tecnica-pericia-trabalhista/', '/consultoria-ssma/'])

# ---------------------------------------------------------------- CONSULTORIA SSMA
service_page('/consultoria-ssma/',
 'Consultoria SSMA, PGR, LTCAT e Treinamentos NR | Jusante',
 'Consultoria em Segurança do Trabalho e meio ambiente: PGR, LTCAT, inspeções, NR-13, avaliações ambientais e treinamentos de NRs presenciais ou EAD.',
 'SSMA', 'Consultoria SSMA, PGR e treinamentos',
 'Da perícia à prevenção: documentação coerente, avaliações ocupacionais e treinamentos para reduzir passivos.',
 'Consultoria SSMA, PGR e treinamentos',
 '''<h2>O trabalho não termina no laudo</h2>
<p>Os achados de uma perícia muitas vezes revelam vulnerabilidades da operação. A consultoria transforma esse diagnóstico em plano de melhoria, com documentos coerentes com a realidade de campo.</p>
<h2>Serviços</h2>
<ul>
<li><strong>PGR (NR-01) e LTCAT:</strong> inventário de riscos, plano de ação e laudo técnico das condições ambientais.</li>
<li><strong>Higiene ocupacional:</strong> ruído, calor/IBUTG, vibração, iluminamento, químicos e pH, com equipamentos próprios.</li>
<li><strong>NR-13:</strong> inspeções, relatórios e diretrizes para vasos de pressão e áreas de compressores.</li>
<li><strong>Inspeções e análise de risco</strong> de máquinas, processos e instalações.</li>
<li><strong>Engenharia ambiental:</strong> ruído e vibração ambiental, resíduos, auditorias e apoio a licenciamento.</li>
</ul>
<h2>Treinamentos</h2>
<p>Treinamentos de Normas Regulamentadoras, presenciais ou EAD, conduzidos por engenheiros de Segurança do Trabalho, com conteúdo adaptado à operação da empresa.</p>
<img src="/assets/img/treinamento.webp" alt="Treinamento de Segurança do Trabalho em empresa" width="1400" height="1051" loading="lazy" style="border-radius:14px;margin-top:22px">''',
 [('A Jusante elabora PGR e LTCAT?', 'Sim, com levantamento de campo e medições próprias quando necessárias.'),
  ('Os treinamentos podem ser na empresa?', 'Sim. Podem ser presenciais, na empresa, ou EAD, conforme a norma e o público.')],
 ['/pericia-insalubridade/', '/ltcat-ppp-extemporaneo/', '/acidente-de-trabalho-e-ergonomia/'])

# ---------------------------------------------------------------- PESSOA
person = head('Eng. Clayton Mendel – Engenheiro de Segurança do Trabalho | Jusante',
              'Eng. Clayton Wallace Mendel Martins, engenheiro ambiental e de segurança do trabalho, pós-graduado em ergonomia, CREA-SP 5070143507. Responsável técnico da Jusante Perícias e SSMA.',
              '/eng-clayton-mendel/', [crumb_ld('Eng. Clayton Mendel', '/eng-clayton-mendel/'),
              {"@type": "ProfilePage", "mainEntity": {"@id": BASE + "/eng-clayton-mendel/#person"}}])
person += header() + hero_page('Responsável técnico', 'Eng. Clayton Mendel',
    'Engenheiro Ambiental e de Segurança do Trabalho, pós-graduado em Ergonomia. CREA-SP 5070143507.', 'Eng. Clayton Mendel')
person += f'''<section><div class="wrap person">
<img src="/assets/img/clayton-mendel.webp" alt="Eng. Clayton Wallace Mendel Martins" width="900" height="945">
<div class="prose">
<h2>Trajetória</h2>
<p>Clayton Wallace Mendel Martins atua em Saúde, Segurança e Meio Ambiente desde 2009, com trajetória em ambientes corporativos e industriais. É fundador e responsável técnico da Jusante Perícias e SSMA.</p>
<p>Atua em perícias trabalhistas e cíveis, com mais de 410 assistências técnicas e experiência em diligências conduzidas por mais de 70 peritos judiciais. Coordena uma equipe de engenheiros de Segurança do Trabalho com registro no CREA-SP.</p>
<p>Mantém atualização contínua em cursos e eventos de instituições como OAB e ESA, com foco na interface entre Engenharia, Segurança do Trabalho e prova pericial.</p>
<h2>Formação</h2>
<ul><li>Engenharia Ambiental</li><li>Pós-graduação em Engenharia de Segurança do Trabalho</li><li>Pós-graduação em Ergonomia</li></ul>
<h2>Áreas de atuação</h2>
<div class="chips"><span class="chip">Insalubridade</span><span class="chip">Periculosidade</span><span class="chip">Acidente de trabalho</span><span class="chip">Ergonomia</span><span class="chip">LTCAT e PPP</span><span class="chip">Higiene ocupacional</span><span class="chip">PGR</span></div>
<p class="quote">Exposição se conclui pela atividade efetivamente exercida, nunca pelo nome do cargo.</p>
<p style="margin-top:22px"><a href="https://www.linkedin.com/in/clayton-mendel" target="_blank" rel="noopener">Perfil no LinkedIn →</a></p>
</div></div></section>
'''
person += cta_band() + footer()
write('/eng-clayton-mendel/', person)

# ---------------------------------------------------------------- 404
nf = head('Página não encontrada | Jusante', 'Página não encontrada.', '/404.html')
nf = nf.replace('<meta name="robots" content="index, follow">', '<meta name="robots" content="noindex">')
nf += header() + f'''<section class="hero page"><img class="mark" src="/assets/img/mark.webp" alt=""><div class="wrap">
<div class="eyebrow">Erro 404</div><h1>Página não encontrada.</h1>
<p class="lead">O endereço pode ter mudado. Veja os serviços ou fale com a Jusante.</p>
<div class="actions"><a class="btn pri" href="/">Ir para o início</a><a class="btn sec" href="{WA}" target="_blank" rel="noopener">WhatsApp</a></div>
</div></section>''' + footer()
write('/404.html', nf)
