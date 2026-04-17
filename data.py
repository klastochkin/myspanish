PRONOUNS = ["yo", "tú", "él/ella", "nosotros", "vosotros", "ellos/ellas"]

TENSE_NAMES = {
    "present":               "Presente",
    "preterite":             "Pretérito",
    "imperfect":             "Imperfecto",
    "future":                "Futuro",
    "pluperfect_subjunctive": "Pluscuamperfecto de Subjuntivo",
}

# ── Vocabulary ────────────────────────────────────────────────────────────────

VOCABULARY = {
    "el baile": ["dance"], "la danza": ["dance"], "el boleto": ["ticket"],
    "la canción": ["song"], "el concierto": ["concert"], "la comedia": ["comedy"],
    "el cuento": ["story", "short story"], "la cultura": ["culture"],
    "el drama": ["drama"], "la tragedia": ["tragedy"], "la escultura": ["sculpture"],
    "el espectáculo": ["show", "spectacle", "performance"], "la estatua": ["statue"],
    "el festival": ["festival"], "la historia": ["history", "story"],
    "la música": ["music"], "la obra": ["work", "play"], "el crítico": ["critic"],
    "la crítica": ["criticism", "critique", "review"], "la obra maestra": ["masterpiece"],
    "la ópera": ["opera"], "la zarzuela": ["musical", "spanish musical"],
    "la orquesta": ["orchestra"], "el personaje": ["character"],
    "el protagonista": ["protagonist", "main character"], "la pintura": ["painting"],
    "la poesía": ["poetry"], "el público": ["audience", "public"],
    "el teatro": ["theater", "theatre"], "la taquilla": ["ticket booth", "box office"],
    "el papel": ["role", "paper"], "los instrumentos": ["instruments"],
    "artístico": ["artistic"], "clásico": ["classic", "classical"],
    "dramático": ["dramatic"], "extranjero": ["foreign"],
    "folclórico": ["folkloric", "folk"], "moderno": ["modern"],
    "romántico": ["romantic"], "talentoso": ["talented"],
    "la cerámica": ["ceramics", "pottery"], "el tejido": ["knitting", "weaving", "fabric"],
    "la fotografía": ["photography"], "el bailarín": ["dancer", "male dancer"],
    "la bailarina": ["dancer", "female dancer", "ballerina"],
    "el/la cantante": ["singer"], "el/la compositor/a": ["composer"],
    "el/la director/a": ["director"], "el/la dramaturgo/a": ["playwright"],
    "el/la escritor/a": ["writer", "author"],
    "la estrella de cine": ["movie star", "film star"], "el músico": ["musician"],
    "el poeta": ["poet"], "la poetisa": ["poetess", "poet"],
    "el/la artesano/a": ["artisan", "craftsperson"],
    "el actor / la actriz": ["actor", "actress"], "el canal": ["channel"],
    "el concurso": ["competition", "contest", "game show"],
    "los dibujos animados": ["cartoons", "animations"],
    "el documental": ["documentary"], "el premio": ["award", "prize"],
    "la realidad": ["reality"],
    "el programa de entrevistas": ["talk show", "interview show"],
    "la telenovela": ["soap opera"], "de acción": ["action"],
    "de aventuras": ["adventure"], "de terror": ["horror", "terror"],
    "de horror": ["horror"], "de ciencia ficción": ["science fiction", "sci-fi"],
    "de vaqueros": ["western", "cowboy"], "romántica": ["romantic"],
    "histórica": ["historical", "historic"],
    "basada en un hecho real": ["based on a true story"],
    "dibujar": ["to draw"], "bailar": ["to dance"], "cantar": ["to sing"],
    "escribir": ["to write"], "declamar": ["to recite", "to declaim"],
    "pintar": ["to paint"], "esculpir": ["to sculpt"],
    "aburrirse": ["to get bored", "to be bored"],
    "divertirse": ["to have fun", "to enjoy oneself"],
    "aplaudir": ["to applaud", "to clap"], "apreciar": ["to appreciate"],
    "criticar": ["to criticize"], "dirigir": ["to direct"],
    "hacer el papel de": ["to play the role of"],
    "interpretar": ["to perform", "to interpret"], "presentar": ["to present"],
    "publicar": ["to publish"], "tocar": ["to play (instrument)", "to touch"],
    "dramatizar": ["to dramatize"], "actuar": ["to act"],
    "componer": ["to compose"], "tejer": ["to knit", "to weave"],
}

# ── Conjugation verbs ─────────────────────────────────────────────────────────

# fmt: off
VERBS: dict[str, dict] = {
    "bailar": {
        "english": "to dance", "sentence": "{bailar} en la fiesta del colegio.",
        "present":                {"yo": "bailo",                    "tú": "bailas",                    "él/ella": "baila",                    "nosotros": "bailamos",                    "vosotros": "bailáis",                    "ellos/ellas": "bailan"},
        "preterite":              {"yo": "bailé",                    "tú": "bailaste",                  "él/ella": "bailó",                    "nosotros": "bailamos",                    "vosotros": "bailasteis",                 "ellos/ellas": "bailaron"},
        "imperfect":              {"yo": "bailaba",                  "tú": "bailabas",                  "él/ella": "bailaba",                  "nosotros": "bailábamos",                  "vosotros": "bailabais",                  "ellos/ellas": "bailaban"},
        "future":                 {"yo": "bailaré",                  "tú": "bailarás",                  "él/ella": "bailará",                  "nosotros": "bailaremos",                  "vosotros": "bailaréis",                  "ellos/ellas": "bailarán"},
        "pluperfect_subjunctive": {"yo": "hubiera bailado",          "tú": "hubieras bailado",          "él/ella": "hubiera bailado",          "nosotros": "hubiéramos bailado",          "vosotros": "hubierais bailado",          "ellos/ellas": "hubieran bailado"},
    },
    "cantar": {
        "english": "to sing", "sentence": "{cantar} una canción en el concierto.",
        "present":                {"yo": "canto",                    "tú": "cantas",                    "él/ella": "canta",                    "nosotros": "cantamos",                    "vosotros": "cantáis",                    "ellos/ellas": "cantan"},
        "preterite":              {"yo": "canté",                    "tú": "cantaste",                  "él/ella": "cantó",                    "nosotros": "cantamos",                    "vosotros": "cantasteis",                 "ellos/ellas": "cantaron"},
        "imperfect":              {"yo": "cantaba",                  "tú": "cantabas",                  "él/ella": "cantaba",                  "nosotros": "cantábamos",                  "vosotros": "cantabais",                  "ellos/ellas": "cantaban"},
        "future":                 {"yo": "cantaré",                  "tú": "cantarás",                  "él/ella": "cantará",                  "nosotros": "cantaremos",                  "vosotros": "cantaréis",                  "ellos/ellas": "cantarán"},
        "pluperfect_subjunctive": {"yo": "hubiera cantado",          "tú": "hubieras cantado",          "él/ella": "hubiera cantado",          "nosotros": "hubiéramos cantado",          "vosotros": "hubierais cantado",          "ellos/ellas": "hubieran cantado"},
    },
    "dibujar": {
        "english": "to draw", "sentence": "{dibujar} un retrato en la clase de arte.",
        "present":                {"yo": "dibujo",                   "tú": "dibujas",                   "él/ella": "dibuja",                   "nosotros": "dibujamos",                   "vosotros": "dibujáis",                   "ellos/ellas": "dibujan"},
        "preterite":              {"yo": "dibujé",                   "tú": "dibujaste",                 "él/ella": "dibujó",                   "nosotros": "dibujamos",                   "vosotros": "dibujasteis",                "ellos/ellas": "dibujaron"},
        "imperfect":              {"yo": "dibujaba",                 "tú": "dibujabas",                 "él/ella": "dibujaba",                 "nosotros": "dibujábamos",                 "vosotros": "dibujabais",                 "ellos/ellas": "dibujaban"},
        "future":                 {"yo": "dibujaré",                 "tú": "dibujarás",                 "él/ella": "dibujará",                 "nosotros": "dibujaremos",                 "vosotros": "dibujaréis",                 "ellos/ellas": "dibujarán"},
        "pluperfect_subjunctive": {"yo": "hubiera dibujado",         "tú": "hubieras dibujado",         "él/ella": "hubiera dibujado",         "nosotros": "hubiéramos dibujado",         "vosotros": "hubierais dibujado",         "ellos/ellas": "hubieran dibujado"},
    },
    "pintar": {
        "english": "to paint", "sentence": "{pintar} un cuadro hermoso en el estudio.",
        "present":                {"yo": "pinto",                    "tú": "pintas",                    "él/ella": "pinta",                    "nosotros": "pintamos",                    "vosotros": "pintáis",                    "ellos/ellas": "pintan"},
        "preterite":              {"yo": "pinté",                    "tú": "pintaste",                  "él/ella": "pintó",                    "nosotros": "pintamos",                    "vosotros": "pintasteis",                 "ellos/ellas": "pintaron"},
        "imperfect":              {"yo": "pintaba",                  "tú": "pintabas",                  "él/ella": "pintaba",                  "nosotros": "pintábamos",                  "vosotros": "pintabais",                  "ellos/ellas": "pintaban"},
        "future":                 {"yo": "pintaré",                  "tú": "pintarás",                  "él/ella": "pintará",                  "nosotros": "pintaremos",                  "vosotros": "pintaréis",                  "ellos/ellas": "pintarán"},
        "pluperfect_subjunctive": {"yo": "hubiera pintado",          "tú": "hubieras pintado",          "él/ella": "hubiera pintado",          "nosotros": "hubiéramos pintado",          "vosotros": "hubierais pintado",          "ellos/ellas": "hubieran pintado"},
    },
    "presentar": {
        "english": "to present", "sentence": "{presentar} el espectáculo en el teatro.",
        "present":                {"yo": "presento",                 "tú": "presentas",                 "él/ella": "presenta",                 "nosotros": "presentamos",                 "vosotros": "presentáis",                 "ellos/ellas": "presentan"},
        "preterite":              {"yo": "presenté",                 "tú": "presentaste",               "él/ella": "presentó",                 "nosotros": "presentamos",                 "vosotros": "presentasteis",              "ellos/ellas": "presentaron"},
        "imperfect":              {"yo": "presentaba",               "tú": "presentabas",               "él/ella": "presentaba",               "nosotros": "presentábamos",               "vosotros": "presentabais",               "ellos/ellas": "presentaban"},
        "future":                 {"yo": "presentaré",               "tú": "presentarás",               "él/ella": "presentará",               "nosotros": "presentaremos",               "vosotros": "presentaréis",               "ellos/ellas": "presentarán"},
        "pluperfect_subjunctive": {"yo": "hubiera presentado",       "tú": "hubieras presentado",       "él/ella": "hubiera presentado",       "nosotros": "hubiéramos presentado",       "vosotros": "hubierais presentado",       "ellos/ellas": "hubieran presentado"},
    },
    "apreciar": {
        "english": "to appreciate", "sentence": "{apreciar} la música clásica de la orquesta.",
        "present":                {"yo": "aprecio",                  "tú": "aprecias",                  "él/ella": "aprecia",                  "nosotros": "apreciamos",                  "vosotros": "apreciáis",                  "ellos/ellas": "aprecian"},
        "preterite":              {"yo": "aprecié",                  "tú": "apreciaste",                "él/ella": "apreció",                  "nosotros": "apreciamos",                  "vosotros": "apreciasteis",               "ellos/ellas": "apreciaron"},
        "imperfect":              {"yo": "apreciaba",                "tú": "apreciabas",                "él/ella": "apreciaba",                "nosotros": "apreciábamos",                "vosotros": "apreciabais",                "ellos/ellas": "apreciaban"},
        "future":                 {"yo": "apreciaré",                "tú": "apreciarás",                "él/ella": "apreciará",                "nosotros": "apreciaremos",                "vosotros": "apreciaréis",                "ellos/ellas": "apreciarán"},
        "pluperfect_subjunctive": {"yo": "hubiera apreciado",        "tú": "hubieras apreciado",        "él/ella": "hubiera apreciado",        "nosotros": "hubiéramos apreciado",        "vosotros": "hubierais apreciado",        "ellos/ellas": "hubieran apreciado"},
    },
    "declamar": {
        "english": "to recite / declaim", "sentence": "{declamar} un poema en el festival de arte.",
        "present":                {"yo": "declamo",                  "tú": "declamas",                  "él/ella": "declama",                  "nosotros": "declamamos",                  "vosotros": "declamáis",                  "ellos/ellas": "declaman"},
        "preterite":              {"yo": "declamé",                  "tú": "declamaste",                "él/ella": "declamó",                  "nosotros": "declamamos",                  "vosotros": "declamasteis",               "ellos/ellas": "declamaron"},
        "imperfect":              {"yo": "declamaba",                "tú": "declamabas",                "él/ella": "declamaba",                "nosotros": "declamábamos",                "vosotros": "declamabais",                "ellos/ellas": "declamaban"},
        "future":                 {"yo": "declamaré",                "tú": "declamarás",                "él/ella": "declamará",                "nosotros": "declamaremos",                "vosotros": "declamaréis",                "ellos/ellas": "declamarán"},
        "pluperfect_subjunctive": {"yo": "hubiera declamado",        "tú": "hubieras declamado",        "él/ella": "hubiera declamado",        "nosotros": "hubiéramos declamado",        "vosotros": "hubierais declamado",        "ellos/ellas": "hubieran declamado"},
    },
    "interpretar": {
        "english": "to perform / interpret", "sentence": "{interpretar} el papel del protagonista en la obra.",
        "present":                {"yo": "interpreto",               "tú": "interpretas",               "él/ella": "interpreta",               "nosotros": "interpretamos",               "vosotros": "interpretáis",               "ellos/ellas": "interpretan"},
        "preterite":              {"yo": "interpreté",               "tú": "interpretaste",             "él/ella": "interpretó",               "nosotros": "interpretamos",               "vosotros": "interpretasteis",            "ellos/ellas": "interpretaron"},
        "imperfect":              {"yo": "interpretaba",             "tú": "interpretabas",             "él/ella": "interpretaba",             "nosotros": "interpretábamos",             "vosotros": "interpretabais",             "ellos/ellas": "interpretaban"},
        "future":                 {"yo": "interpretaré",             "tú": "interpretarás",             "él/ella": "interpretará",             "nosotros": "interpretaremos",             "vosotros": "interpretaréis",             "ellos/ellas": "interpretarán"},
        "pluperfect_subjunctive": {"yo": "hubiera interpretado",     "tú": "hubieras interpretado",     "él/ella": "hubiera interpretado",     "nosotros": "hubiéramos interpretado",     "vosotros": "hubierais interpretado",     "ellos/ellas": "hubieran interpretado"},
    },
    "tocar": {
        "english": "to play (instrument)", "sentence": "{tocar} la guitarra en la orquesta.",
        "present":                {"yo": "toco",                     "tú": "tocas",                     "él/ella": "toca",                     "nosotros": "tocamos",                     "vosotros": "tocáis",                     "ellos/ellas": "tocan"},
        "preterite":              {"yo": "toqué",                    "tú": "tocaste",                   "él/ella": "tocó",                     "nosotros": "tocamos",                     "vosotros": "tocasteis",                  "ellos/ellas": "tocaron"},
        "imperfect":              {"yo": "tocaba",                   "tú": "tocabas",                   "él/ella": "tocaba",                   "nosotros": "tocábamos",                   "vosotros": "tocabais",                   "ellos/ellas": "tocaban"},
        "future":                 {"yo": "tocaré",                   "tú": "tocarás",                   "él/ella": "tocará",                   "nosotros": "tocaremos",                   "vosotros": "tocaréis",                   "ellos/ellas": "tocarán"},
        "pluperfect_subjunctive": {"yo": "hubiera tocado",           "tú": "hubieras tocado",           "él/ella": "hubiera tocado",           "nosotros": "hubiéramos tocado",           "vosotros": "hubierais tocado",           "ellos/ellas": "hubieran tocado"},
    },
    "criticar": {
        "english": "to criticize", "sentence": "{criticar} la obra maestra expuesta en el museo.",
        "present":                {"yo": "critico",                  "tú": "criticas",                  "él/ella": "critica",                  "nosotros": "criticamos",                  "vosotros": "criticáis",                  "ellos/ellas": "critican"},
        "preterite":              {"yo": "critiqué",                 "tú": "criticaste",                "él/ella": "criticó",                  "nosotros": "criticamos",                  "vosotros": "criticasteis",               "ellos/ellas": "criticaron"},
        "imperfect":              {"yo": "criticaba",                "tú": "criticabas",                "él/ella": "criticaba",                "nosotros": "criticábamos",                "vosotros": "criticabais",                "ellos/ellas": "criticaban"},
        "future":                 {"yo": "criticaré",                "tú": "criticarás",                "él/ella": "criticará",                "nosotros": "criticaremos",                "vosotros": "criticaréis",                "ellos/ellas": "criticarán"},
        "pluperfect_subjunctive": {"yo": "hubiera criticado",        "tú": "hubieras criticado",        "él/ella": "hubiera criticado",        "nosotros": "hubiéramos criticado",        "vosotros": "hubierais criticado",        "ellos/ellas": "hubieran criticado"},
    },
    "publicar": {
        "english": "to publish", "sentence": "{publicar} un libro de poesía este año.",
        "present":                {"yo": "publico",                  "tú": "publicas",                  "él/ella": "publica",                  "nosotros": "publicamos",                  "vosotros": "publicáis",                  "ellos/ellas": "publican"},
        "preterite":              {"yo": "publiqué",                 "tú": "publicaste",                "él/ella": "publicó",                  "nosotros": "publicamos",                  "vosotros": "publicasteis",               "ellos/ellas": "publicaron"},
        "imperfect":              {"yo": "publicaba",                "tú": "publicabas",                "él/ella": "publicaba",                "nosotros": "publicábamos",                "vosotros": "publicabais",                "ellos/ellas": "publicaban"},
        "future":                 {"yo": "publicaré",                "tú": "publicarás",                "él/ella": "publicará",                "nosotros": "publicaremos",                "vosotros": "publicaréis",                "ellos/ellas": "publicarán"},
        "pluperfect_subjunctive": {"yo": "hubiera publicado",        "tú": "hubieras publicado",        "él/ella": "hubiera publicado",        "nosotros": "hubiéramos publicado",        "vosotros": "hubierais publicado",        "ellos/ellas": "hubieran publicado"},
    },
    "dramatizar": {
        "english": "to dramatize", "sentence": "{dramatizar} la historia en el escenario.",
        "present":                {"yo": "dramatizo",                "tú": "dramatizas",                "él/ella": "dramatiza",                "nosotros": "dramatizamos",                "vosotros": "dramatizáis",                "ellos/ellas": "dramatizan"},
        "preterite":              {"yo": "dramaticé",                "tú": "dramatizaste",              "él/ella": "dramatizó",                "nosotros": "dramatizamos",                "vosotros": "dramatizasteis",             "ellos/ellas": "dramatizaron"},
        "imperfect":              {"yo": "dramatizaba",              "tú": "dramatizabas",              "él/ella": "dramatizaba",              "nosotros": "dramatizábamos",              "vosotros": "dramatizabais",              "ellos/ellas": "dramatizaban"},
        "future":                 {"yo": "dramatizaré",              "tú": "dramatizarás",              "él/ella": "dramatizará",              "nosotros": "dramatizaremos",              "vosotros": "dramatizaréis",              "ellos/ellas": "dramatizarán"},
        "pluperfect_subjunctive": {"yo": "hubiera dramatizado",      "tú": "hubieras dramatizado",      "él/ella": "hubiera dramatizado",      "nosotros": "hubiéramos dramatizado",      "vosotros": "hubierais dramatizado",      "ellos/ellas": "hubieran dramatizado"},
    },
    "actuar": {
        "english": "to act", "sentence": "{actuar} en la telenovela más popular del canal.",
        "present":                {"yo": "actúo",                    "tú": "actúas",                    "él/ella": "actúa",                    "nosotros": "actuamos",                    "vosotros": "actuáis",                    "ellos/ellas": "actúan"},
        "preterite":              {"yo": "actué",                    "tú": "actuaste",                  "él/ella": "actuó",                    "nosotros": "actuamos",                    "vosotros": "actuasteis",                 "ellos/ellas": "actuaron"},
        "imperfect":              {"yo": "actuaba",                  "tú": "actuabas",                  "él/ella": "actuaba",                  "nosotros": "actuábamos",                  "vosotros": "actuabais",                  "ellos/ellas": "actuaban"},
        "future":                 {"yo": "actuaré",                  "tú": "actuarás",                  "él/ella": "actuará",                  "nosotros": "actuaremos",                  "vosotros": "actuaréis",                  "ellos/ellas": "actuarán"},
        "pluperfect_subjunctive": {"yo": "hubiera actuado",          "tú": "hubieras actuado",          "él/ella": "hubiera actuado",          "nosotros": "hubiéramos actuado",          "vosotros": "hubierais actuado",          "ellos/ellas": "hubieran actuado"},
    },
    "escribir": {
        "english": "to write", "sentence": "{escribir} un cuento para el festival literario.",
        "present":                {"yo": "escribo",                  "tú": "escribes",                  "él/ella": "escribe",                  "nosotros": "escribimos",                  "vosotros": "escribís",                   "ellos/ellas": "escriben"},
        "preterite":              {"yo": "escribí",                  "tú": "escribiste",                "él/ella": "escribió",                 "nosotros": "escribimos",                  "vosotros": "escribisteis",               "ellos/ellas": "escribieron"},
        "imperfect":              {"yo": "escribía",                 "tú": "escribías",                 "él/ella": "escribía",                 "nosotros": "escribíamos",                 "vosotros": "escribíais",                 "ellos/ellas": "escribían"},
        "future":                 {"yo": "escribiré",                "tú": "escribirás",                "él/ella": "escribirá",                "nosotros": "escribiremos",                "vosotros": "escribiréis",                "ellos/ellas": "escribirán"},
        "pluperfect_subjunctive": {"yo": "hubiera escrito",          "tú": "hubieras escrito",          "él/ella": "hubiera escrito",          "nosotros": "hubiéramos escrito",          "vosotros": "hubierais escrito",          "ellos/ellas": "hubieran escrito"},
    },
    "aplaudir": {
        "english": "to applaud", "sentence": "{aplaudir} al actor al final del espectáculo.",
        "present":                {"yo": "aplaudo",                  "tú": "aplaudes",                  "él/ella": "aplaude",                  "nosotros": "aplaudimos",                  "vosotros": "aplaudís",                   "ellos/ellas": "aplauden"},
        "preterite":              {"yo": "aplaudí",                  "tú": "aplaudiste",                "él/ella": "aplaudió",                 "nosotros": "aplaudimos",                  "vosotros": "aplaudisteis",               "ellos/ellas": "aplaudieron"},
        "imperfect":              {"yo": "aplaudía",                 "tú": "aplaudías",                 "él/ella": "aplaudía",                 "nosotros": "aplaudíamos",                 "vosotros": "aplaudíais",                 "ellos/ellas": "aplaudían"},
        "future":                 {"yo": "aplaudiré",                "tú": "aplaudirás",                "él/ella": "aplaudirá",                "nosotros": "aplaudiremos",                "vosotros": "aplaudiréis",                "ellos/ellas": "aplaudirán"},
        "pluperfect_subjunctive": {"yo": "hubiera aplaudido",        "tú": "hubieras aplaudido",        "él/ella": "hubiera aplaudido",        "nosotros": "hubiéramos aplaudido",        "vosotros": "hubierais aplaudido",        "ellos/ellas": "hubieran aplaudido"},
    },
    "esculpir": {
        "english": "to sculpt", "sentence": "{esculpir} una estatua de mármol para la exposición.",
        "present":                {"yo": "esculpo",                  "tú": "esculpes",                  "él/ella": "esculpe",                  "nosotros": "esculpimos",                  "vosotros": "esculpís",                   "ellos/ellas": "esculpen"},
        "preterite":              {"yo": "esculpí",                  "tú": "esculpiste",                "él/ella": "esculpió",                 "nosotros": "esculpimos",                  "vosotros": "esculpisteis",               "ellos/ellas": "esculpieron"},
        "imperfect":              {"yo": "esculpía",                 "tú": "esculpías",                 "él/ella": "esculpía",                 "nosotros": "esculpíamos",                 "vosotros": "esculpíais",                 "ellos/ellas": "esculpían"},
        "future":                 {"yo": "esculpiré",                "tú": "esculpirás",                "él/ella": "esculpirá",                "nosotros": "esculpiremos",                "vosotros": "esculpiréis",                "ellos/ellas": "esculpirán"},
        "pluperfect_subjunctive": {"yo": "hubiera esculpido",        "tú": "hubieras esculpido",        "él/ella": "hubiera esculpido",        "nosotros": "hubiéramos esculpido",        "vosotros": "hubierais esculpido",        "ellos/ellas": "hubieran esculpido"},
    },
    "dirigir": {
        "english": "to direct", "sentence": "{dirigir} la orquesta con mucho talento.",
        "present":                {"yo": "dirijo",                   "tú": "diriges",                   "él/ella": "dirige",                   "nosotros": "dirigimos",                   "vosotros": "dirigís",                    "ellos/ellas": "dirigen"},
        "preterite":              {"yo": "dirigí",                   "tú": "dirigiste",                 "él/ella": "dirigió",                  "nosotros": "dirigimos",                   "vosotros": "dirigisteis",                "ellos/ellas": "dirigieron"},
        "imperfect":              {"yo": "dirigía",                  "tú": "dirigías",                  "él/ella": "dirigía",                  "nosotros": "dirigíamos",                  "vosotros": "dirigíais",                  "ellos/ellas": "dirigían"},
        "future":                 {"yo": "dirigiré",                 "tú": "dirigirás",                 "él/ella": "dirigirá",                 "nosotros": "dirigiremos",                 "vosotros": "dirigiréis",                 "ellos/ellas": "dirigirán"},
        "pluperfect_subjunctive": {"yo": "hubiera dirigido",         "tú": "hubieras dirigido",         "él/ella": "hubiera dirigido",         "nosotros": "hubiéramos dirigido",         "vosotros": "hubierais dirigido",         "ellos/ellas": "hubieran dirigido"},
    },
    "tejer": {
        "english": "to knit / weave", "sentence": "{tejer} una manta colorida para el invierno.",
        "present":                {"yo": "tejo",                     "tú": "tejes",                     "él/ella": "teje",                     "nosotros": "tejemos",                     "vosotros": "tejéis",                     "ellos/ellas": "tejen"},
        "preterite":              {"yo": "tejí",                     "tú": "tejiste",                   "él/ella": "tejió",                    "nosotros": "tejimos",                     "vosotros": "tejisteis",                  "ellos/ellas": "tejieron"},
        "imperfect":              {"yo": "tejía",                    "tú": "tejías",                    "él/ella": "tejía",                    "nosotros": "tejíamos",                    "vosotros": "tejíais",                    "ellos/ellas": "tejían"},
        "future":                 {"yo": "tejeré",                   "tú": "tejerás",                   "él/ella": "tejerá",                   "nosotros": "tejeremos",                   "vosotros": "tejeréis",                   "ellos/ellas": "tejerán"},
        "pluperfect_subjunctive": {"yo": "hubiera tejido",           "tú": "hubieras tejido",           "él/ella": "hubiera tejido",           "nosotros": "hubiéramos tejido",           "vosotros": "hubierais tejido",           "ellos/ellas": "hubieran tejido"},
    },
    "componer": {
        "english": "to compose", "sentence": "{componer} una ópera famosa para el teatro nacional.",
        "present":                {"yo": "compongo",                 "tú": "compones",                  "él/ella": "compone",                  "nosotros": "componemos",                  "vosotros": "componéis",                  "ellos/ellas": "componen"},
        "preterite":              {"yo": "compuse",                  "tú": "compusiste",                "él/ella": "compuso",                  "nosotros": "compusimos",                  "vosotros": "compusisteis",               "ellos/ellas": "compusieron"},
        "imperfect":              {"yo": "componía",                 "tú": "componías",                 "él/ella": "componía",                 "nosotros": "componíamos",                 "vosotros": "componíais",                 "ellos/ellas": "componían"},
        "future":                 {"yo": "compondré",                "tú": "compondrás",                "él/ella": "compondrá",                "nosotros": "compondremos",                "vosotros": "compondréis",                "ellos/ellas": "compondrán"},
        "pluperfect_subjunctive": {"yo": "hubiera compuesto",        "tú": "hubieras compuesto",        "él/ella": "hubiera compuesto",        "nosotros": "hubiéramos compuesto",        "vosotros": "hubierais compuesto",        "ellos/ellas": "hubieran compuesto"},
    },
    "aburrirse": {
        "english": "to get bored", "sentence": "{aburrirse} durante el documental muy largo.",
        "present":                {"yo": "me aburro",                "tú": "te aburres",                "él/ella": "se aburre",                "nosotros": "nos aburrimos",               "vosotros": "os aburrís",                 "ellos/ellas": "se aburren"},
        "preterite":              {"yo": "me aburrí",                "tú": "te aburriste",              "él/ella": "se aburrió",               "nosotros": "nos aburrimos",               "vosotros": "os aburrísteis",             "ellos/ellas": "se aburrieron"},
        "imperfect":              {"yo": "me aburría",               "tú": "te aburrías",               "él/ella": "se aburría",               "nosotros": "nos aburríamos",              "vosotros": "os aburríais",               "ellos/ellas": "se aburrían"},
        "future":                 {"yo": "me aburriré",              "tú": "te aburrirás",              "él/ella": "se aburrirá",              "nosotros": "nos aburriremos",             "vosotros": "os aburriréis",              "ellos/ellas": "se aburrirán"},
        "pluperfect_subjunctive": {"yo": "me hubiera aburrido",      "tú": "te hubieras aburrido",      "él/ella": "se hubiera aburrido",      "nosotros": "nos hubiéramos aburrido",     "vosotros": "os hubierais aburrido",      "ellos/ellas": "se hubieran aburrido"},
    },
    "divertirse": {
        "english": "to have fun / enjoy oneself", "sentence": "{divertirse} mucho en el festival de arte.",
        "present":                {"yo": "me divierto",              "tú": "te diviertes",              "él/ella": "se divierte",              "nosotros": "nos divertimos",              "vosotros": "os divertís",                "ellos/ellas": "se divierten"},
        "preterite":              {"yo": "me divertí",               "tú": "te divertiste",             "él/ella": "se divirtió",              "nosotros": "nos divertimos",              "vosotros": "os divertisteis",            "ellos/ellas": "se divirtieron"},
        "imperfect":              {"yo": "me divertía",              "tú": "te divertías",              "él/ella": "se divertía",              "nosotros": "nos divertíamos",             "vosotros": "os divertíais",              "ellos/ellas": "se divertían"},
        "future":                 {"yo": "me divertiré",             "tú": "te divertirás",             "él/ella": "se divertirá",             "nosotros": "nos divertiremos",            "vosotros": "os divertiréis",             "ellos/ellas": "se divertirán"},
        "pluperfect_subjunctive": {"yo": "me hubiera divertido",     "tú": "te hubieras divertido",     "él/ella": "se hubiera divertido",     "nosotros": "nos hubiéramos divertido",    "vosotros": "os hubierais divertido",     "ellos/ellas": "se hubieran divertido"},
    },
}
# fmt: on

# ── Conditional tense (Lesson 2) ──────────────────────────────────────────────

CONDITIONAL_PRONOUNS = ["yo", "tú", "usted/él/ella", "nosotros/as", "ustedes/ellos/ellas"]
CONDITIONAL_TENSE = {"conditional": "Condicional"}

# fmt: off
CONDITIONAL_VERBS: dict[str, dict] = {
    # ── haber / tener family ───────────────────────────────────────────────────
    "haber": {
        "english": "to have (aux) / there would be",
        "sentence": "Ojalá {haber} más tiempo para practicar el español.",
        "conditional": {"yo": "habría",      "tú": "habrías",      "usted/él/ella": "habría",      "nosotros/as": "habríamos",      "ustedes/ellos/ellas": "habrían"},
    },
    "tener": {
        "english": "to have",
        "sentence": "{tener} que estudiar más para el examen.",
        "conditional": {"yo": "tendría",     "tú": "tendrías",     "usted/él/ella": "tendría",     "nosotros/as": "tendríamos",     "ustedes/ellos/ellas": "tendrían"},
    },
    "abstener": {
        "english": "to abstain",
        "sentence": "{abstener} de votar si no conociera bien al candidato.",
        "conditional": {"yo": "abstendría",  "tú": "abstendrías",  "usted/él/ella": "abstendría",  "nosotros/as": "abstendríamos",  "ustedes/ellos/ellas": "abstendrían"},
    },
    "contener": {
        "english": "to contain",
        "sentence": "El informe {contener} información muy valiosa.",
        "conditional": {"yo": "contendría",  "tú": "contendrías",  "usted/él/ella": "contendría",  "nosotros/as": "contendríamos",  "ustedes/ellos/ellas": "contendrían"},
    },
    "detener": {
        "english": "to stop / detain",
        "sentence": "{detener} el proyecto para revisarlo.",
        "conditional": {"yo": "detendría",   "tú": "detendrías",   "usted/él/ella": "detendría",   "nosotros/as": "detendríamos",   "ustedes/ellos/ellas": "detendrían"},
    },
    "mantener": {
        "english": "to maintain / keep",
        "sentence": "{mantener} la calma en una situación difícil.",
        "conditional": {"yo": "mantendría",  "tú": "mantendrías",  "usted/él/ella": "mantendría",  "nosotros/as": "mantendríamos",  "ustedes/ellos/ellas": "mantendrían"},
    },
    "obtener": {
        "english": "to obtain / get",
        "sentence": "{obtener} mejores notas con más práctica.",
        "conditional": {"yo": "obtendría",   "tú": "obtendrías",   "usted/él/ella": "obtendría",   "nosotros/as": "obtendríamos",   "ustedes/ellos/ellas": "obtendrían"},
    },
    "sostener": {
        "english": "to hold / sustain",
        "sentence": "{sostener} esa opinión con buenos argumentos.",
        "conditional": {"yo": "sostendría",  "tú": "sostendrías",  "usted/él/ella": "sostendría",  "nosotros/as": "sostendríamos",  "ustedes/ellos/ellas": "sostendrían"},
    },
    # ── caber ─────────────────────────────────────────────────────────────────
    "caber": {
        "english": "to fit",
        "sentence": "Toda la ropa {caber} en una maleta pequeña.",
        "conditional": {"yo": "cabría",      "tú": "cabrías",      "usted/él/ella": "cabría",      "nosotros/as": "cabríamos",      "ustedes/ellos/ellas": "cabrían"},
    },
    # ── hacer family ──────────────────────────────────────────────────────────
    "hacer": {
        "english": "to do / make",
        "sentence": "{hacer} la tarea más rápido con mejor concentración.",
        "conditional": {"yo": "haría",       "tú": "harías",       "usted/él/ella": "haría",       "nosotros/as": "haríamos",       "ustedes/ellos/ellas": "harían"},
    },
    "deshacer": {
        "english": "to undo / undo",
        "sentence": "{deshacer} los errores con paciencia y dedicación.",
        "conditional": {"yo": "desharía",    "tú": "desharías",    "usted/él/ella": "desharía",    "nosotros/as": "desharíamos",    "ustedes/ellos/ellas": "desharían"},
    },
    "rehacer": {
        "english": "to redo",
        "sentence": "{rehacer} el ejercicio para mejorar la calificación.",
        "conditional": {"yo": "reharía",     "tú": "reharías",     "usted/él/ella": "reharía",     "nosotros/as": "reharíamos",     "ustedes/ellos/ellas": "reharían"},
    },
    "satisfacer": {
        "english": "to satisfy",
        "sentence": "{satisfacer} todos los requisitos del programa.",
        "conditional": {"yo": "satisfaría",  "tú": "satisfarías",  "usted/él/ella": "satisfaría",  "nosotros/as": "satisfaríamos",  "ustedes/ellos/ellas": "satisfarían"},
    },
    # ── poder ─────────────────────────────────────────────────────────────────
    "poder": {
        "english": "to be able to / can",
        "sentence": "{poder} hablar español con fluidez con más práctica.",
        "conditional": {"yo": "podría",      "tú": "podrías",      "usted/él/ella": "podría",      "nosotros/as": "podríamos",      "ustedes/ellos/ellas": "podrían"},
    },
    # ── poner family ──────────────────────────────────────────────────────────
    "poner": {
        "english": "to put / place",
        "sentence": "{poner} más atención en la pronunciación.",
        "conditional": {"yo": "pondría",     "tú": "pondrías",     "usted/él/ella": "pondría",     "nosotros/as": "pondríamos",     "ustedes/ellos/ellas": "pondrían"},
    },
    "componer": {
        "english": "to compose",
        "sentence": "{componer} una canción en español si supiera música.",
        "conditional": {"yo": "compondría",  "tú": "compondrías",  "usted/él/ella": "compondría",  "nosotros/as": "compondríamos",  "ustedes/ellos/ellas": "compondrían"},
    },
    "exponer": {
        "english": "to expose / present",
        "sentence": "{exponer} las ideas con mayor claridad.",
        "conditional": {"yo": "expondría",   "tú": "expondrías",   "usted/él/ella": "expondría",   "nosotros/as": "expondríamos",   "ustedes/ellos/ellas": "expondrían"},
    },
    "imponer": {
        "english": "to impose",
        "sentence": "{imponer} nuevas reglas para mejorar la disciplina.",
        "conditional": {"yo": "impondría",   "tú": "impondrías",   "usted/él/ella": "impondría",   "nosotros/as": "impondríamos",   "ustedes/ellos/ellas": "impondrían"},
    },
    "oponer": {
        "english": "to oppose",
        "sentence": "{oponer} resistencia a los cambios innecesarios.",
        "conditional": {"yo": "opondría",    "tú": "opondrías",    "usted/él/ella": "opondría",    "nosotros/as": "opondríamos",    "ustedes/ellos/ellas": "opondrían"},
    },
    "proponer": {
        "english": "to propose",
        "sentence": "{proponer} una solución creativa al problema.",
        "conditional": {"yo": "propondría",  "tú": "propondrías",  "usted/él/ella": "propondría",  "nosotros/as": "propondríamos",  "ustedes/ellos/ellas": "propondrían"},
    },
    "suponer": {
        "english": "to suppose / assume",
        "sentence": "{suponer} que ya sabes la respuesta correcta.",
        "conditional": {"yo": "supondría",   "tú": "supondrías",   "usted/él/ella": "supondría",   "nosotros/as": "supondríamos",   "ustedes/ellos/ellas": "supondrían"},
    },
    # ── querer / saber ────────────────────────────────────────────────────────
    "querer": {
        "english": "to want / love",
        "sentence": "{querer} visitar España y aprender más español.",
        "conditional": {"yo": "querría",     "tú": "querrías",     "usted/él/ella": "querría",     "nosotros/as": "querríamos",     "ustedes/ellos/ellas": "querrían"},
    },
    "saber": {
        "english": "to know",
        "sentence": "{saber} la respuesta si hubieras estudiado más.",
        "conditional": {"yo": "sabría",      "tú": "sabrías",      "usted/él/ella": "sabría",      "nosotros/as": "sabríamos",      "ustedes/ellos/ellas": "sabrían"},
    },
    # ── venir family ──────────────────────────────────────────────────────────
    "venir": {
        "english": "to come",
        "sentence": "{venir} a la clase de conversación los viernes.",
        "conditional": {"yo": "vendría",     "tú": "vendrías",     "usted/él/ella": "vendría",     "nosotros/as": "vendríamos",     "ustedes/ellos/ellas": "vendrían"},
    },
    "convenir": {
        "english": "to be convenient / suit",
        "sentence": "{convenir} repasar el vocabulario antes del examen.",
        "conditional": {"yo": "convendría",  "tú": "convendrías",  "usted/él/ella": "convendría",  "nosotros/as": "convendríamos",  "ustedes/ellos/ellas": "convendrían"},
    },
    "prevenir": {
        "english": "to prevent / warn",
        "sentence": "{prevenir} los malentendidos con comunicación clara.",
        "conditional": {"yo": "prevendría",  "tú": "prevendrías",  "usted/él/ella": "prevendría",  "nosotros/as": "prevendríamos",  "ustedes/ellos/ellas": "prevendrían"},
    },
    "provenir": {
        "english": "to come from / originate",
        "sentence": "Las palabras {provenir} de raíces de otros idiomas.",
        "conditional": {"yo": "provendría",  "tú": "provendrías",  "usted/él/ella": "provendría",  "nosotros/as": "provendríamos",  "ustedes/ellos/ellas": "provendrían"},
    },
    # ── decir / salir / valer ─────────────────────────────────────────────────
    "decir": {
        "english": "to say / tell",
        "sentence": "{decir} la verdad aunque fuera difícil.",
        "conditional": {"yo": "diría",       "tú": "dirías",       "usted/él/ella": "diría",       "nosotros/as": "diríamos",       "ustedes/ellos/ellas": "dirían"},
    },
    "salir": {
        "english": "to leave / go out",
        "sentence": "{salir} más a practicar el español si tuviera tiempo.",
        "conditional": {"yo": "saldría",     "tú": "saldrías",     "usted/él/ella": "saldría",     "nosotros/as": "saldríamos",     "ustedes/ellos/ellas": "saldrían"},
    },
    "valer": {
        "english": "to be worth",
        "sentence": "{valer} la pena aprender un nuevo idioma.",
        "conditional": {"yo": "valdría",     "tú": "valdrías",     "usted/él/ella": "valdría",     "nosotros/as": "valdríamos",     "ustedes/ellos/ellas": "valdrían"},
    },
}
# fmt: on

# ── Vocabulary: Un Sinnúmero de Números ──────────────────────────────────────

VOCABULARY_NUMBERS = {
    # ── Cardinal numbers ──────────────────────────────────────────────────────
    "cero":              ["zero", "0"],
    "uno / un":          ["one", "1"],
    "dos":               ["two", "2"],
    "tres":              ["three", "3"],
    "cuatro":            ["four", "4"],
    "cinco":             ["five", "5"],
    "seis":              ["six", "6"],
    "siete":             ["seven", "7"],
    "ocho":              ["eight", "8"],
    "nueve":             ["nine", "9"],
    "diez":              ["ten", "10"],
    "once":              ["eleven", "11"],
    "doce":              ["twelve", "12"],
    "trece":             ["thirteen", "13"],
    "catorce":           ["fourteen", "14"],
    "quince":            ["fifteen", "15"],
    "dieciséis":         ["sixteen", "16"],
    "diecisiete":        ["seventeen", "17"],
    "dieciocho":         ["eighteen", "18"],
    "diecinueve":        ["nineteen", "19"],
    "veinte":            ["twenty", "20"],
    "veintiuno":         ["twenty-one", "21"],
    "veintidós":         ["twenty-two", "22"],
    "veintitrés":        ["twenty-three", "23"],
    "treinta":           ["thirty", "30"],
    "cuarenta":          ["forty", "40"],
    "cincuenta":         ["fifty", "50"],
    "sesenta":           ["sixty", "60"],
    "setenta":           ["seventy", "70"],
    "ochenta":           ["eighty", "80"],
    "noventa":           ["ninety", "90"],
    "cien / ciento":     ["one hundred", "100", "hundred"],
    "doscientos":        ["two hundred", "200"],
    "trescientos":       ["three hundred", "300"],
    "cuatrocientos":     ["four hundred", "400"],
    "quinientos":        ["five hundred", "500"],
    "seiscientos":       ["six hundred", "600"],
    "setecientos":       ["seven hundred", "700"],
    "ochocientos":       ["eight hundred", "800"],
    "novecientos":       ["nine hundred", "900"],
    "mil":               ["one thousand", "1000", "thousand"],
    "dos mil":           ["two thousand", "2000"],
    "tres mil":          ["three thousand", "3000"],
    "diez mil":          ["ten thousand", "10000"],
    "cien mil":          ["one hundred thousand", "100000"],
    "quinientos mil":    ["five hundred thousand", "500000"],
    "un millón":         ["one million", "1000000"],
    # ── Ordinal numbers ───────────────────────────────────────────────────────
    "primero / primer":          ["first", "1st"],
    "segundo":                   ["second", "2nd"],
    "tercero / tercer":          ["third", "3rd"],
    "cuarto":                    ["fourth", "4th"],
    "quinto":                    ["fifth", "5th"],
    "sexto":                     ["sixth", "6th"],
    "séptimo":                   ["seventh", "7th"],
    "octavo":                    ["eighth", "8th"],
    "noveno":                    ["ninth", "9th"],
    "décimo":                    ["tenth", "10th"],
    "undécimo":                  ["eleventh", "11th"],
    "duodécimo":                 ["twelfth", "12th"],
    "decimotercero":             ["thirteenth", "13th"],
    "decimocuarto":              ["fourteenth", "14th"],
    "decimoquinto":              ["fifteenth", "15th"],
    "decimosexto":               ["sixteenth", "16th"],
    "decimoséptimo":             ["seventeenth", "17th"],
    "decimoctavo":               ["eighteenth", "18th"],
    "decimonoveno":              ["nineteenth", "19th"],
    "vigésimo":                  ["twentieth", "20th"],
    "vigésimo primero":          ["twenty-first", "21st"],
    "vigésimo segundo":          ["twenty-second", "22nd"],
    "vigésimo tercero":          ["twenty-third", "23rd"],
    "trigésimo":                 ["thirtieth", "30th"],
    "trigésimo primero":         ["thirty-first", "31st"],
    "trigésimo segundo":         ["thirty-second", "32nd"],
    "trigésimo tercero":         ["thirty-third", "33rd"],
    "cuadragésimo":              ["fortieth", "40th"],
    "quincuagésimo":             ["fiftieth", "50th"],
    "sexagésimo":                ["sixtieth", "60th"],
    "septuagésimo":              ["seventieth", "70th"],
    "octogésimo":                ["eightieth", "80th"],
    "nonagésimo":                ["ninetieth", "90th"],
    "centésimo":                 ["hundredth", "100th"],
    "centésimo primero":         ["one hundred first", "101st"],
    "centésimo segundo":         ["one hundred second", "102nd"],
    "ducentésimo":               ["two hundredth", "200th"],
    "tricentésimo":              ["three hundredth", "300th"],
    "cuadringentésimo":          ["four hundredth", "400th"],
    "quingentésimo":             ["five hundredth", "500th"],
    "sexcentésimo":              ["six hundredth", "600th"],
    "septingentésimo":           ["seven hundredth", "700th"],
    "octingentésimo":            ["eight hundredth", "800th"],
    "noningentésimo":            ["nine hundredth", "900th"],
    "milésimo":                  ["thousandth", "1000th"],
    "milésimo primero":          ["one thousand first", "1001st"],
    "dosmilésimo":               ["two thousandth", "2000th"],
    "tresmilésimo":              ["three thousandth", "3000th"],
    "diezmilésimo":              ["ten thousandth", "10000th"],
    "cienmilésimo":              ["hundred thousandth", "100000th"],
    "quinientosmilésimo":        ["five hundred thousandth", "500000th"],
    "millonésimo":               ["millionth", "1000000th"],
}

# ── Vocabulary: Lección 4 — El Mundo del Trabajo ─────────────────────────────

VOCABULARY_L4 = {
    # Las Ocupaciones / los Títulos
    "el/la abogado/a": ["lawyer"], "el actor": ["actor"],
    "la actriz": ["actress"], "el/la arqueólogo/a": ["archaeologist"],
    "el/la arquitecto/a": ["architect"], "el/la bombero/a": ["firefighter"],
    "el/la carpintero/a": ["carpenter"], "el/la científico/a": ["scientist"],
    "el/la cocinero/a": ["cook", "chef"], "el/la consejero/a": ["counselor", "advisor"],
    "el/la contador/a": ["accountant"],
    "el/la corredor/a de bolsa": ["stockbroker"],
    "el/la diseñador/a": ["designer"], "el/la electricista": ["electrician"],
    "el hombre de negocios": ["businessman"],
    "la mujer de negocios": ["businesswoman"],
    "el/la maestro/a": ["teacher"], "el/la profesor/a": ["professor", "teacher"],
    "el/la peluquero/a": ["hairdresser", "barber"],
    "el/la pintor/a": ["painter"], "el/la político/a": ["politician"],
    "el/la psicólogo/a": ["psychologist"], "el/la reportero/a": ["reporter"],
    "el/la periodista": ["journalist"], "el/la secretario/a": ["secretary"],
    "el/la técnico/a": ["technician"], "el/la doctor/a": ["doctor"],
    "el/la enfermero/a": ["nurse"], "el/la dentista": ["dentist"],
    # Campos de Estudio
    "derecho": ["law"], "actuación": ["acting"],
    "arqueología": ["archaeology"], "culinaria": ["culinary arts"],
    "consejería": ["counseling"], "economía": ["economics"],
    "diseño": ["design"], "periodismo": ["journalism"],
    "medicina": ["medicine"], "odontología": ["dentistry"],
    # El Mundo del Trabajo
    "el ascenso": ["promotion", "raise"], "la promoción": ["promotion"],
    "el aumento": ["raise", "increase"],
    "el sueldo": ["salary", "wage"], "el salario": ["salary"],
    "la carrera": ["career"], "la compañía": ["company"],
    "la empresa": ["company", "business"], "la firma": ["firm", "signature"],
    "el empleo": ["job", "employment"], "el puesto": ["position", "job"],
    "el/la gerente": ["manager"], "el/la jefe/a": ["boss"],
    "los negocios": ["business"], "la ocupación": ["occupation"],
    "el oficio": ["trade", "craft"], "el título": ["degree", "title"],
    "la profesión": ["profession"], "la reunión": ["meeting"],
    "el teletrabajo": ["remote work", "telework"],
    "el trabajo": ["work", "job"], "la oficina": ["office"],
    "comercial": ["commercial"], "dentro de": ["within"],
    "próximo": ["next"], "vacaciones": ["vacation"],
    "sobresueldo": ["bonus"],
    # La Entrevista
    "el anuncio": ["advertisement", "announcement"],
    "el/la aspirante": ["applicant", "candidate"],
    "los beneficios": ["benefits"],
    "el currículo": ["résumé", "CV"], "la hoja de vida": ["résumé", "CV"],
    "la entrevista": ["interview"],
    "el entrevistado": ["interviewee"], "el entrevistador": ["interviewer"],
    "la solicitud de trabajo": ["job application"],
    # Verbos
    "ascender": ["to promote", "to rise"], "graduarse": ["to graduate"],
    "contratar": ["to hire"], "entrevistar": ["to interview"],
    "ganar": ["to earn", "to win"], "obtener": ["to obtain", "to get"],
    "solicitar": ["to apply for", "to request"], "defender": ["to defend"],
    "estudiar": ["to study"], "aplicar": ["to apply"],
    "buscar": ["to search", "to look for"],
    "aumentar": ["to increase", "to raise"], "emplear": ["to employ"],
    "negociar": ["to negotiate"],
    "reunirse": ["to meet", "to get together"], "trabajar": ["to work"],
    "dejar": ["to leave", "to quit"], "despedir": ["to fire", "to dismiss"],
    "invertir": ["to invest"], "aceptar": ["to accept"],
    "renunciar": ["to resign", "to give up"],
    "tener éxito": ["to succeed", "to be successful"],
    "comerciar": ["to trade"],
}

# ── Vocabulary: Lección 6 — La Actualidad ────────────────────────────────────

VOCABULARY_L6 = {
    "el acontecimiento": ["event"],
    "la actualidad": ["current events", "present time"],
    "las noticias": ["news"],
    "las noticias de última hora": ["breaking news"],
    "el artículo": ["article"],
    "el diario": ["newspaper", "diary"],
    "el periódico": ["newspaper"],
    "el informe": ["report"],
    "el locutor": ["announcer", "broadcaster"],
    "la locutora": ["announcer", "broadcaster"],
    "el noticiero": ["newscast", "news program"],
    "la prensa": ["press"],
    "el reportaje": ["report", "news story"],
    "el radio": ["radio"],
    "el choque": ["crash", "collision"],
    "el crimen": ["crime"],
    "el desastre natural": ["natural disaster"],
    "el terremoto": ["earthquake"],
    "el maremoto": ["tsunami", "tidal wave"],
    "el sunami": ["tsunami"],
    "la tormenta": ["storm"],
    "el tornado": ["tornado"],
    "el huracán": ["hurricane"],
    "el incendio": ["fire"],
    "el empleo": ["employment"],
    "el desempleo": ["unemployment"],
    "la desigualdad": ["inequality"],
    "la discriminación": ["discrimination"],
    "el ejército": ["army"],
    "la huelga": ["strike"],
    "el paro": ["strike", "unemployment"],
    "el secuestro": ["kidnapping"],
    "la inundación": ["flood"],
    "la libertad": ["freedom", "liberty"],
    "la guerra": ["war"],
    "la paz": ["peace"],
    "el racismo": ["racism"],
    "el sexismo": ["sexism"],
    "el SIDA": ["AIDS"],
    "el soldado": ["soldier"],
    "la violencia": ["violence"],
    "la policía": ["police"],
    "el peligro": ["danger"],
    "el candidato": ["candidate"],
    "la candidata": ["candidate"],
    "el ciudadano": ["citizen"],
    "el deber": ["duty"],
    "los derechos": ["rights"],
    "la dictadura": ["dictatorship"],
    "la opresión": ["oppression"],
    "el atraco": ["holdup", "robbery", "mugging"],
    "el robo": ["heist", "robbery", "theft"],
    "el engaño": ["deception", "deceit"],
    "la decepción": ["disappointment"],
    "el discurso": ["speech"],
    "las elecciones": ["elections"],
    "la encuesta": ["survey", "poll"],
    "la entrevista": ["interview"],
    "los impuestos": ["taxes"],
    "el representante": ["representative"],
    "internacional": ["international"],
    "el voto": ["vote"],
    "anunciar": ["to announce"],
    "comunicarse": ["to communicate"],
    "durar": ["to last"],
    "votar": ["to vote"],
    "elegir": ["to choose", "to elect"],
    "informar": ["to inform"],
    "ocurrir": ["to occur", "to happen"],
    "transmitir": ["to transmit", "to broadcast"],
    "emitir": ["to emit", "to broadcast"],
    "declarar": ["to declare"],
    "luchar": ["to fight", "to struggle"],
    "seguir": ["to follow", "to continue"],
    "cumplir": ["to fulfill", "to comply"],
    "obedecer": ["to obey"],
    "despedirse": ["to say goodbye"],
    "¡Qué gusto!": ["What a pleasure!"],
    "¡Mucho gusto!": ["Nice to meet you!"],
    "¡No tenía ni idea!": ["I had no idea!"],
    "¡Felicidades!": ["Congratulations!"],
    "¡Enhorabuena!": ["Congratulations!"],
    "¡La he pasado de película!": ["I had an amazing time!"],
    "¡Me suena excelente!": ["Sounds great to me!"],
    "Como si …": ["as if"],
}

# ── Compound tenses (Lessons 3 & 4) ──────────────────────────────────────────

COMPOUND_TENSE_NAMES = {
    "present_perfect":             "Presente Perfecto de Indicativo",
    "pluperfect_indicative":       "Pluscuamperfecto de Indicativo",
    "future_perfect":              "Futuro Perfecto de Indicativo",
    "conditional_perfect":         "Condicional Perfecto",
    "present_perfect_subjunctive": "Presente Perfecto del Subjuntivo",
    "pluperfect_subjunctive":      "Pluscuamperfecto del Subjuntivo",
}

_HABER: dict[str, list[str]] = {
    "present_perfect":             ["he",      "has",      "ha",      "hemos",      "habéis",    "han"],
    "pluperfect_indicative":       ["había",   "habías",   "había",   "habíamos",   "habíais",   "habían"],
    "future_perfect":              ["habré",   "habrás",   "habrá",   "habremos",   "habréis",   "habrán"],
    "conditional_perfect":         ["habría",  "habrías",  "habría",  "habríamos",  "habríais",  "habrían"],
    "present_perfect_subjunctive": ["haya",    "hayas",    "haya",    "hayamos",    "hayáis",    "hayan"],
    "pluperfect_subjunctive":      ["hubiera", "hubieras", "hubiera", "hubiéramos", "hubierais", "hubieran"],
}
_REFLEXIVE_PRONOUNS = ["me", "te", "se", "nos", "os", "se"]


def _compound(participle: str, reflexive: bool = False) -> dict[str, dict[str, str]]:
    """Generate all 6 compound-tense conjugations from a past participle."""
    result: dict[str, dict[str, str]] = {}
    for tense, forms in _HABER.items():
        d: dict[str, str] = {}
        for i, p in enumerate(PRONOUNS):
            if reflexive:
                d[p] = f"{_REFLEXIVE_PRONOUNS[i]} {forms[i]} {participle}"
            else:
                d[p] = f"{forms[i]} {participle}"
        result[tense] = d
    return result


# ── Lección 4 compound-tense verbs ──────────────────────────────────────────

L4_COMPOUND_VERBS: dict[str, dict] = {
    "ascender": {
        "english": "to promote / rise",
        "sentence": "{ascender} a un puesto más alto en la empresa.",
        **_compound("ascendido"),
    },
    "graduarse": {
        "english": "to graduate",
        "sentence": "{graduarse} de la universidad con honores.",
        **_compound("graduado", reflexive=True),
    },
    "contratar": {
        "english": "to hire",
        "sentence": "{contratar} a un nuevo empleado para la oficina.",
        **_compound("contratado"),
    },
    "entrevistar": {
        "english": "to interview",
        "sentence": "{entrevistar} a los aspirantes para el puesto.",
        **_compound("entrevistado"),
    },
    "ganar": {
        "english": "to earn / win",
        "sentence": "{ganar} un buen sueldo en la compañía.",
        **_compound("ganado"),
    },
    "obtener": {
        "english": "to obtain / get",
        "sentence": "{obtener} el título de abogado después de estudiar derecho.",
        **_compound("obtenido"),
    },
    "solicitar": {
        "english": "to apply for / request",
        "sentence": "{solicitar} el empleo en la empresa internacional.",
        **_compound("solicitado"),
    },
    "defender": {
        "english": "to defend",
        "sentence": "{defender} los derechos de los trabajadores.",
        **_compound("defendido"),
    },
    "estudiar": {
        "english": "to study",
        "sentence": "{estudiar} economía en la universidad.",
        **_compound("estudiado"),
    },
    "aplicar": {
        "english": "to apply",
        "sentence": "{aplicar} los conocimientos en el trabajo.",
        **_compound("aplicado"),
    },
    "buscar": {
        "english": "to search / look for",
        "sentence": "{buscar} un puesto mejor en otra compañía.",
        **_compound("buscado"),
    },
    "aumentar": {
        "english": "to increase / raise",
        "sentence": "{aumentar} la producción de la empresa.",
        **_compound("aumentado"),
    },
    "emplear": {
        "english": "to employ",
        "sentence": "{emplear} a más técnicos en la firma.",
        **_compound("empleado"),
    },
    "negociar": {
        "english": "to negotiate",
        "sentence": "{negociar} un mejor salario con el gerente.",
        **_compound("negociado"),
    },
    "reunirse": {
        "english": "to meet / get together",
        "sentence": "{reunirse} con el equipo para la videoconferencia.",
        **_compound("reunido", reflexive=True),
    },
    "trabajar": {
        "english": "to work",
        "sentence": "{trabajar} desde casa con el teletrabajo.",
        **_compound("trabajado"),
    },
    "dejar": {
        "english": "to leave / quit",
        "sentence": "{dejar} el puesto para aceptar una oferta mejor.",
        **_compound("dejado"),
    },
    "despedir": {
        "english": "to fire / dismiss",
        "sentence": "{despedir} al empleado por bajo rendimiento.",
        **_compound("despedido"),
    },
    "invertir": {
        "english": "to invest",
        "sentence": "{invertir} en los negocios internacionales.",
        **_compound("invertido"),
    },
    "aceptar": {
        "english": "to accept",
        "sentence": "{aceptar} la oferta de trabajo después de la entrevista.",
        **_compound("aceptado"),
    },
    "renunciar": {
        "english": "to resign / give up",
        "sentence": "{renunciar} al empleo para empezar su propia empresa.",
        **_compound("renunciado"),
    },
    "comerciar": {
        "english": "to trade",
        "sentence": "{comerciar} con empresas de otros países.",
        **_compound("comerciado"),
    },
}

# ── Lección 6 compound-tense verbs ──────────────────────────────────────────

L6_COMPOUND_VERBS: dict[str, dict] = {
    "anunciar": {
        "english": "to announce",
        "sentence": "{anunciar} las noticias de última hora en el noticiero.",
        **_compound("anunciado"),
    },
    "comunicarse": {
        "english": "to communicate",
        "sentence": "{comunicarse} con los ciudadanos por la prensa.",
        **_compound("comunicado", reflexive=True),
    },
    "durar": {
        "english": "to last",
        "sentence": "{durar} mucho tiempo la huelga de los trabajadores.",
        **_compound("durado"),
    },
    "votar": {
        "english": "to vote",
        "sentence": "{votar} en las elecciones presidenciales.",
        **_compound("votado"),
    },
    "elegir": {
        "english": "to choose / elect",
        "sentence": "{elegir} al mejor candidato en las elecciones.",
        **_compound("elegido"),
    },
    "informar": {
        "english": "to inform",
        "sentence": "{informar} al público sobre el desastre natural.",
        **_compound("informado"),
    },
    "ocurrir": {
        "english": "to occur / happen",
        "sentence": "{ocurrir} un terremoto en la región.",
        **_compound("ocurrido"),
    },
    "transmitir": {
        "english": "to transmit / broadcast",
        "sentence": "{transmitir} el discurso del representante por la radio.",
        **_compound("transmitido"),
    },
    "emitir": {
        "english": "to emit / broadcast",
        "sentence": "{emitir} un informe sobre la violencia en el país.",
        **_compound("emitido"),
    },
    "declarar": {
        "english": "to declare",
        "sentence": "{declarar} la paz después de la guerra.",
        **_compound("declarado"),
    },
    "luchar": {
        "english": "to fight / struggle",
        "sentence": "{luchar} por la libertad y los derechos del ciudadano.",
        **_compound("luchado"),
    },
    "seguir": {
        "english": "to follow / continue",
        "sentence": "{seguir} las noticias sobre la situación internacional.",
        **_compound("seguido"),
    },
    "cumplir": {
        "english": "to fulfill / comply",
        "sentence": "{cumplir} con el deber de votar en las elecciones.",
        **_compound("cumplido"),
    },
    "obedecer": {
        "english": "to obey",
        "sentence": "{obedecer} las leyes del país para mantener la paz.",
        **_compound("obedecido"),
    },
    "despedirse": {
        "english": "to say goodbye",
        "sentence": "{despedirse} de los colegas al final del reportaje.",
        **_compound("despedido", reflexive=True),
    },
}

# ── Flat all-in-one conjugation view ─────────────────────────────────────────

ALL_TENSE_NAMES: dict[str, str] = {
    "present":                     "Presente",
    "preterite":                   "Pretérito",
    "imperfect":                   "Imperfecto",
    "future":                      "Futuro",
    "conditional":                 "Condicional",
    "present_perfect":             "Presente Perfecto de Indicativo",
    "pluperfect_indicative":       "Pluscuamperfecto de Indicativo",
    "future_perfect":              "Futuro Perfecto de Indicativo",
    "conditional_perfect":         "Condicional Perfecto",
    "present_perfect_subjunctive": "Presente Perfecto del Subjuntivo",
    "pluperfect_subjunctive":      "Pluscuamperfecto del Subjuntivo",
}

# Remap conditional pronoun keys to standard 6-pronoun set
_COND_PRON_MAP = {
    "yo":                    "yo",
    "tú":                    "tú",
    "usted/él/ella":         "él/ella",
    "nosotros/as":           "nosotros",
    "ustedes/ellos/ellas":   "ellos/ellas",
}

ALL_CONJUGATION_VERBS: dict[str, dict] = {}

# Merge VERBS, L4_COMPOUND_VERBS, L6_COMPOUND_VERBS (all share standard PRONOUNS)
for _src in (VERBS, L4_COMPOUND_VERBS, L6_COMPOUND_VERBS):
    for _verb, _info in _src.items():
        if _verb not in ALL_CONJUGATION_VERBS:
            ALL_CONJUGATION_VERBS[_verb] = dict(_info)
        else:
            for _k, _v in _info.items():
                ALL_CONJUGATION_VERBS[_verb].setdefault(_k, _v)

# Merge CONDITIONAL_VERBS (remap pronouns + derive vosotros as yo_form + "is")
for _verb, _info in CONDITIONAL_VERBS.items():
    _cond_src = _info["conditional"]
    _cond_std: dict[str, str] = {}
    for _old, _new in _COND_PRON_MAP.items():
        if _old in _cond_src:
            _cond_std[_new] = _cond_src[_old]
    # Derive vosotros: habría → habríais  (yo_form + "is")
    _cond_std["vosotros"] = _cond_src.get("yo", "") + "is"

    if _verb not in ALL_CONJUGATION_VERBS:
        ALL_CONJUGATION_VERBS[_verb] = {
            "english":     _info["english"],
            "sentence":    _info["sentence"],
            "conditional": _cond_std,
        }
    else:
        ALL_CONJUGATION_VERBS[_verb]["conditional"] = _cond_std
        ALL_CONJUGATION_VERBS[_verb].setdefault("english", _info["english"])
        ALL_CONJUGATION_VERBS[_verb].setdefault("sentence", _info["sentence"])

# ── Lessons ───────────────────────────────────────────────────────────────────

LESSONS = {
    "vocabulary": {
        "1": {
            "title": "Lesson 1",
            "subtitle": "Un Festival de Arte",
            "words": VOCABULARY,
        },
        "2": {
            "title": "Lesson 2",
            "subtitle": "El Mundo del Trabajo",
            "words": VOCABULARY_L4,
        },
        "3": {
            "title": "Lesson 3",
            "subtitle": "La Actualidad",
            "words": VOCABULARY_L6,
        },
        "4": {
            "title": "Lesson 4",
            "subtitle": "Un Sinnúmero de Números",
            "words": VOCABULARY_NUMBERS,
        },
    },
    "conjugation": {
        "1": {
            "title": "Lesson 1",
            "subtitle": "Lección 5 — Verbos",
            "verbs": VERBS,
            "pronouns": PRONOUNS,
            "tense_names": TENSE_NAMES,
        },
        "2": {
            "title": "Lesson 2",
            "subtitle": "El Condicional",
            "verbs": CONDITIONAL_VERBS,
            "pronouns": CONDITIONAL_PRONOUNS,
            "tense_names": CONDITIONAL_TENSE,
        },
        "3": {
            "title": "Lesson 3",
            "subtitle": "Tiempos Compuestos — El Trabajo",
            "verbs": L4_COMPOUND_VERBS,
            "pronouns": PRONOUNS,
            "tense_names": COMPOUND_TENSE_NAMES,
        },
        "4": {
            "title": "Lesson 4",
            "subtitle": "Tiempos Compuestos — La Actualidad",
            "verbs": L6_COMPOUND_VERBS,
            "pronouns": PRONOUNS,
            "tense_names": COMPOUND_TENSE_NAMES,
        },
    },
}
