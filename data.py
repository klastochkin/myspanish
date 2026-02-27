PRONOUNS = ["yo", "tú", "él/ella", "nosotros", "vosotros", "ellos/ellas"]

TENSE_NAMES = {
    "present":   "Presente",
    "preterite": "Pretérito",
    "imperfect": "Imperfecto",
    "future":    "Futuro",
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
        "present":   {"yo": "bailo",      "tú": "bailas",      "él/ella": "baila",      "nosotros": "bailamos",      "vosotros": "bailáis",      "ellos/ellas": "bailan"},
        "preterite": {"yo": "bailé",      "tú": "bailaste",    "él/ella": "bailó",      "nosotros": "bailamos",      "vosotros": "bailasteis",   "ellos/ellas": "bailaron"},
        "imperfect": {"yo": "bailaba",    "tú": "bailabas",    "él/ella": "bailaba",    "nosotros": "bailábamos",    "vosotros": "bailabais",    "ellos/ellas": "bailaban"},
        "future":    {"yo": "bailaré",    "tú": "bailarás",    "él/ella": "bailará",    "nosotros": "bailaremos",    "vosotros": "bailaréis",    "ellos/ellas": "bailarán"},
    },
    "cantar": {
        "english": "to sing", "sentence": "{cantar} una canción en el concierto.",
        "present":   {"yo": "canto",      "tú": "cantas",      "él/ella": "canta",      "nosotros": "cantamos",      "vosotros": "cantáis",      "ellos/ellas": "cantan"},
        "preterite": {"yo": "canté",      "tú": "cantaste",    "él/ella": "cantó",      "nosotros": "cantamos",      "vosotros": "cantasteis",   "ellos/ellas": "cantaron"},
        "imperfect": {"yo": "cantaba",    "tú": "cantabas",    "él/ella": "cantaba",    "nosotros": "cantábamos",    "vosotros": "cantabais",    "ellos/ellas": "cantaban"},
        "future":    {"yo": "cantaré",    "tú": "cantarás",    "él/ella": "cantará",    "nosotros": "cantaremos",    "vosotros": "cantaréis",    "ellos/ellas": "cantarán"},
    },
    "dibujar": {
        "english": "to draw", "sentence": "{dibujar} un retrato en la clase de arte.",
        "present":   {"yo": "dibujo",     "tú": "dibujas",     "él/ella": "dibuja",     "nosotros": "dibujamos",     "vosotros": "dibujáis",     "ellos/ellas": "dibujan"},
        "preterite": {"yo": "dibujé",     "tú": "dibujaste",   "él/ella": "dibujó",     "nosotros": "dibujamos",     "vosotros": "dibujasteis",  "ellos/ellas": "dibujaron"},
        "imperfect": {"yo": "dibujaba",   "tú": "dibujabas",   "él/ella": "dibujaba",   "nosotros": "dibujábamos",   "vosotros": "dibujabais",   "ellos/ellas": "dibujaban"},
        "future":    {"yo": "dibujaré",   "tú": "dibujarás",   "él/ella": "dibujará",   "nosotros": "dibujaremos",   "vosotros": "dibujaréis",   "ellos/ellas": "dibujarán"},
    },
    "pintar": {
        "english": "to paint", "sentence": "{pintar} un cuadro hermoso en el estudio.",
        "present":   {"yo": "pinto",      "tú": "pintas",      "él/ella": "pinta",      "nosotros": "pintamos",      "vosotros": "pintáis",      "ellos/ellas": "pintan"},
        "preterite": {"yo": "pinté",      "tú": "pintaste",    "él/ella": "pintó",      "nosotros": "pintamos",      "vosotros": "pintasteis",   "ellos/ellas": "pintaron"},
        "imperfect": {"yo": "pintaba",    "tú": "pintabas",    "él/ella": "pintaba",    "nosotros": "pintábamos",    "vosotros": "pintabais",    "ellos/ellas": "pintaban"},
        "future":    {"yo": "pintaré",    "tú": "pintarás",    "él/ella": "pintará",    "nosotros": "pintaremos",    "vosotros": "pintaréis",    "ellos/ellas": "pintarán"},
    },
    "presentar": {
        "english": "to present", "sentence": "{presentar} el espectáculo en el teatro.",
        "present":   {"yo": "presento",   "tú": "presentas",   "él/ella": "presenta",   "nosotros": "presentamos",   "vosotros": "presentáis",   "ellos/ellas": "presentan"},
        "preterite": {"yo": "presenté",   "tú": "presentaste", "él/ella": "presentó",   "nosotros": "presentamos",   "vosotros": "presentasteis","ellos/ellas": "presentaron"},
        "imperfect": {"yo": "presentaba", "tú": "presentabas", "él/ella": "presentaba", "nosotros": "presentábamos", "vosotros": "presentabais", "ellos/ellas": "presentaban"},
        "future":    {"yo": "presentaré", "tú": "presentarás", "él/ella": "presentará", "nosotros": "presentaremos", "vosotros": "presentaréis", "ellos/ellas": "presentarán"},
    },
    "apreciar": {
        "english": "to appreciate", "sentence": "{apreciar} la música clásica de la orquesta.",
        "present":   {"yo": "aprecio",    "tú": "aprecias",    "él/ella": "aprecia",    "nosotros": "apreciamos",    "vosotros": "apreciáis",    "ellos/ellas": "aprecian"},
        "preterite": {"yo": "aprecié",    "tú": "apreciaste",  "él/ella": "apreció",    "nosotros": "apreciamos",    "vosotros": "apreciasteis", "ellos/ellas": "apreciaron"},
        "imperfect": {"yo": "apreciaba",  "tú": "apreciabas",  "él/ella": "apreciaba",  "nosotros": "apreciábamos",  "vosotros": "apreciabais",  "ellos/ellas": "apreciaban"},
        "future":    {"yo": "apreciaré",  "tú": "apreciarás",  "él/ella": "apreciará",  "nosotros": "apreciaremos",  "vosotros": "apreciaréis",  "ellos/ellas": "apreciarán"},
    },
    "declamar": {
        "english": "to recite / declaim", "sentence": "{declamar} un poema en el festival de arte.",
        "present":   {"yo": "declamo",    "tú": "declamas",    "él/ella": "declama",    "nosotros": "declamamos",    "vosotros": "declamáis",    "ellos/ellas": "declaman"},
        "preterite": {"yo": "declamé",    "tú": "declamaste",  "él/ella": "declamó",    "nosotros": "declamamos",    "vosotros": "declamasteis", "ellos/ellas": "declamaron"},
        "imperfect": {"yo": "declamaba",  "tú": "declamabas",  "él/ella": "declamaba",  "nosotros": "declamábamos",  "vosotros": "declamabais",  "ellos/ellas": "declamaban"},
        "future":    {"yo": "declamaré",  "tú": "declamarás",  "él/ella": "declamará",  "nosotros": "declamaremos",  "vosotros": "declamaréis",  "ellos/ellas": "declamarán"},
    },
    "interpretar": {
        "english": "to perform / interpret", "sentence": "{interpretar} el papel del protagonista en la obra.",
        "present":   {"yo": "interpreto",    "tú": "interpretas",    "él/ella": "interpreta",    "nosotros": "interpretamos",    "vosotros": "interpretáis",    "ellos/ellas": "interpretan"},
        "preterite": {"yo": "interpreté",    "tú": "interpretaste",  "él/ella": "interpretó",    "nosotros": "interpretamos",    "vosotros": "interpretasteis", "ellos/ellas": "interpretaron"},
        "imperfect": {"yo": "interpretaba",  "tú": "interpretabas",  "él/ella": "interpretaba",  "nosotros": "interpretábamos",  "vosotros": "interpretabais",  "ellos/ellas": "interpretaban"},
        "future":    {"yo": "interpretaré",  "tú": "interpretarás",  "él/ella": "interpretará",  "nosotros": "interpretaremos",  "vosotros": "interpretaréis",  "ellos/ellas": "interpretarán"},
    },
    "tocar": {
        "english": "to play (instrument)", "sentence": "{tocar} la guitarra en la orquesta.",
        "present":   {"yo": "toco",       "tú": "tocas",       "él/ella": "toca",       "nosotros": "tocamos",       "vosotros": "tocáis",       "ellos/ellas": "tocan"},
        "preterite": {"yo": "toqué",      "tú": "tocaste",     "él/ella": "tocó",       "nosotros": "tocamos",       "vosotros": "tocasteis",    "ellos/ellas": "tocaron"},
        "imperfect": {"yo": "tocaba",     "tú": "tocabas",     "él/ella": "tocaba",     "nosotros": "tocábamos",     "vosotros": "tocabais",     "ellos/ellas": "tocaban"},
        "future":    {"yo": "tocaré",     "tú": "tocarás",     "él/ella": "tocará",     "nosotros": "tocaremos",     "vosotros": "tocaréis",     "ellos/ellas": "tocarán"},
    },
    "criticar": {
        "english": "to criticize", "sentence": "{criticar} la obra maestra expuesta en el museo.",
        "present":   {"yo": "critico",    "tú": "criticas",    "él/ella": "critica",    "nosotros": "criticamos",    "vosotros": "criticáis",    "ellos/ellas": "critican"},
        "preterite": {"yo": "critiqué",   "tú": "criticaste",  "él/ella": "criticó",    "nosotros": "criticamos",    "vosotros": "criticasteis", "ellos/ellas": "criticaron"},
        "imperfect": {"yo": "criticaba",  "tú": "criticabas",  "él/ella": "criticaba",  "nosotros": "criticábamos",  "vosotros": "criticabais",  "ellos/ellas": "criticaban"},
        "future":    {"yo": "criticaré",  "tú": "criticarás",  "él/ella": "criticará",  "nosotros": "criticaremos",  "vosotros": "criticaréis",  "ellos/ellas": "criticarán"},
    },
    "publicar": {
        "english": "to publish", "sentence": "{publicar} un libro de poesía este año.",
        "present":   {"yo": "publico",    "tú": "publicas",    "él/ella": "publica",    "nosotros": "publicamos",    "vosotros": "publicáis",    "ellos/ellas": "publican"},
        "preterite": {"yo": "publiqué",   "tú": "publicaste",  "él/ella": "publicó",    "nosotros": "publicamos",    "vosotros": "publicasteis", "ellos/ellas": "publicaron"},
        "imperfect": {"yo": "publicaba",  "tú": "publicabas",  "él/ella": "publicaba",  "nosotros": "publicábamos",  "vosotros": "publicabais",  "ellos/ellas": "publicaban"},
        "future":    {"yo": "publicaré",  "tú": "publicarás",  "él/ella": "publicará",  "nosotros": "publicaremos",  "vosotros": "publicaréis",  "ellos/ellas": "publicarán"},
    },
    "dramatizar": {
        "english": "to dramatize", "sentence": "{dramatizar} la historia en el escenario.",
        "present":   {"yo": "dramatizo",   "tú": "dramatizas",   "él/ella": "dramatiza",   "nosotros": "dramatizamos",   "vosotros": "dramatizáis",   "ellos/ellas": "dramatizan"},
        "preterite": {"yo": "dramaticé",   "tú": "dramatizaste", "él/ella": "dramatizó",   "nosotros": "dramatizamos",   "vosotros": "dramatizasteis","ellos/ellas": "dramatizaron"},
        "imperfect": {"yo": "dramatizaba", "tú": "dramatizabas", "él/ella": "dramatizaba", "nosotros": "dramatizábamos", "vosotros": "dramatizabais", "ellos/ellas": "dramatizaban"},
        "future":    {"yo": "dramatizaré", "tú": "dramatizarás", "él/ella": "dramatizará", "nosotros": "dramatizaremos", "vosotros": "dramatizaréis", "ellos/ellas": "dramatizarán"},
    },
    "actuar": {
        "english": "to act", "sentence": "{actuar} en la telenovela más popular del canal.",
        "present":   {"yo": "actúo",      "tú": "actúas",      "él/ella": "actúa",      "nosotros": "actuamos",      "vosotros": "actuáis",      "ellos/ellas": "actúan"},
        "preterite": {"yo": "actué",      "tú": "actuaste",    "él/ella": "actuó",      "nosotros": "actuamos",      "vosotros": "actuasteis",   "ellos/ellas": "actuaron"},
        "imperfect": {"yo": "actuaba",    "tú": "actuabas",    "él/ella": "actuaba",    "nosotros": "actuábamos",    "vosotros": "actuabais",    "ellos/ellas": "actuaban"},
        "future":    {"yo": "actuaré",    "tú": "actuarás",    "él/ella": "actuará",    "nosotros": "actuaremos",    "vosotros": "actuaréis",    "ellos/ellas": "actuarán"},
    },
    "escribir": {
        "english": "to write", "sentence": "{escribir} un cuento para el festival literario.",
        "present":   {"yo": "escribo",    "tú": "escribes",    "él/ella": "escribe",    "nosotros": "escribimos",    "vosotros": "escribís",     "ellos/ellas": "escriben"},
        "preterite": {"yo": "escribí",    "tú": "escribiste",  "él/ella": "escribió",   "nosotros": "escribimos",    "vosotros": "escribisteis", "ellos/ellas": "escribieron"},
        "imperfect": {"yo": "escribía",   "tú": "escribías",   "él/ella": "escribía",   "nosotros": "escribíamos",   "vosotros": "escribíais",   "ellos/ellas": "escribían"},
        "future":    {"yo": "escribiré",  "tú": "escribirás",  "él/ella": "escribirá",  "nosotros": "escribiremos",  "vosotros": "escribiréis",  "ellos/ellas": "escribirán"},
    },
    "aplaudir": {
        "english": "to applaud", "sentence": "{aplaudir} al actor al final del espectáculo.",
        "present":   {"yo": "aplaudo",    "tú": "aplaudes",    "él/ella": "aplaude",    "nosotros": "aplaudimos",    "vosotros": "aplaudís",     "ellos/ellas": "aplauden"},
        "preterite": {"yo": "aplaudí",    "tú": "aplaudiste",  "él/ella": "aplaudió",   "nosotros": "aplaudimos",    "vosotros": "aplaudisteis", "ellos/ellas": "aplaudieron"},
        "imperfect": {"yo": "aplaudía",   "tú": "aplaudías",   "él/ella": "aplaudía",   "nosotros": "aplaudíamos",   "vosotros": "aplaudíais",   "ellos/ellas": "aplaudían"},
        "future":    {"yo": "aplaudiré",  "tú": "aplaudirás",  "él/ella": "aplaudirá",  "nosotros": "aplaudiremos",  "vosotros": "aplaudiréis",  "ellos/ellas": "aplaudirán"},
    },
    "esculpir": {
        "english": "to sculpt", "sentence": "{esculpir} una estatua de mármol para la exposición.",
        "present":   {"yo": "esculpo",    "tú": "esculpes",    "él/ella": "esculpe",    "nosotros": "esculpimos",    "vosotros": "esculpís",     "ellos/ellas": "esculpen"},
        "preterite": {"yo": "esculpí",    "tú": "esculpiste",  "él/ella": "esculpió",   "nosotros": "esculpimos",    "vosotros": "esculpisteis", "ellos/ellas": "esculpieron"},
        "imperfect": {"yo": "esculpía",   "tú": "esculpías",   "él/ella": "esculpía",   "nosotros": "esculpíamos",   "vosotros": "esculpíais",   "ellos/ellas": "esculpían"},
        "future":    {"yo": "esculpiré",  "tú": "esculpirás",  "él/ella": "esculpirá",  "nosotros": "esculpiremos",  "vosotros": "esculpiréis",  "ellos/ellas": "esculpirán"},
    },
    "dirigir": {
        "english": "to direct", "sentence": "{dirigir} la orquesta con mucho talento.",
        "present":   {"yo": "dirijo",     "tú": "diriges",     "él/ella": "dirige",     "nosotros": "dirigimos",     "vosotros": "dirigís",      "ellos/ellas": "dirigen"},
        "preterite": {"yo": "dirigí",     "tú": "dirigiste",   "él/ella": "dirigió",    "nosotros": "dirigimos",     "vosotros": "dirigisteis",  "ellos/ellas": "dirigieron"},
        "imperfect": {"yo": "dirigía",    "tú": "dirigías",    "él/ella": "dirigía",    "nosotros": "dirigíamos",    "vosotros": "dirigíais",    "ellos/ellas": "dirigían"},
        "future":    {"yo": "dirigiré",   "tú": "dirigirás",   "él/ella": "dirigirá",   "nosotros": "dirigiremos",   "vosotros": "dirigiréis",   "ellos/ellas": "dirigirán"},
    },
    "tejer": {
        "english": "to knit / weave", "sentence": "{tejer} una manta colorida para el invierno.",
        "present":   {"yo": "tejo",       "tú": "tejes",       "él/ella": "teje",       "nosotros": "tejemos",       "vosotros": "tejéis",       "ellos/ellas": "tejen"},
        "preterite": {"yo": "tejí",       "tú": "tejiste",     "él/ella": "tejió",      "nosotros": "tejimos",       "vosotros": "tejisteis",    "ellos/ellas": "tejieron"},
        "imperfect": {"yo": "tejía",      "tú": "tejías",      "él/ella": "tejía",      "nosotros": "tejíamos",      "vosotros": "tejíais",      "ellos/ellas": "tejían"},
        "future":    {"yo": "tejeré",     "tú": "tejerás",     "él/ella": "tejerá",     "nosotros": "tejeremos",     "vosotros": "tejeréis",     "ellos/ellas": "tejerán"},
    },
    "componer": {
        "english": "to compose", "sentence": "{componer} una ópera famosa para el teatro nacional.",
        "present":   {"yo": "compongo",   "tú": "compones",    "él/ella": "compone",    "nosotros": "componemos",    "vosotros": "componéis",    "ellos/ellas": "componen"},
        "preterite": {"yo": "compuse",    "tú": "compusiste",  "él/ella": "compuso",    "nosotros": "compusimos",    "vosotros": "compusisteis", "ellos/ellas": "compusieron"},
        "imperfect": {"yo": "componía",   "tú": "componías",   "él/ella": "componía",   "nosotros": "componíamos",   "vosotros": "componíais",   "ellos/ellas": "componían"},
        "future":    {"yo": "compondré",  "tú": "compondrás",  "él/ella": "compondrá",  "nosotros": "compondremos",  "vosotros": "compondréis",  "ellos/ellas": "compondrán"},
    },
    "aburrirse": {
        "english": "to get bored", "sentence": "{aburrirse} durante el documental muy largo.",
        "present":   {"yo": "me aburro",     "tú": "te aburres",     "él/ella": "se aburre",     "nosotros": "nos aburrimos",     "vosotros": "os aburrís",      "ellos/ellas": "se aburren"},
        "preterite": {"yo": "me aburrí",     "tú": "te aburriste",   "él/ella": "se aburrió",    "nosotros": "nos aburrimos",     "vosotros": "os aburrísteis",  "ellos/ellas": "se aburrieron"},
        "imperfect": {"yo": "me aburría",    "tú": "te aburrías",    "él/ella": "se aburría",    "nosotros": "nos aburríamos",    "vosotros": "os aburríais",    "ellos/ellas": "se aburrían"},
        "future":    {"yo": "me aburriré",   "tú": "te aburrirás",   "él/ella": "se aburrirá",   "nosotros": "nos aburriremos",   "vosotros": "os aburriréis",   "ellos/ellas": "se aburrirán"},
    },
    "divertirse": {
        "english": "to have fun / enjoy oneself", "sentence": "{divertirse} mucho en el festival de arte.",
        "present":   {"yo": "me divierto",   "tú": "te diviertes",   "él/ella": "se divierte",   "nosotros": "nos divertimos",    "vosotros": "os divertís",     "ellos/ellas": "se divierten"},
        "preterite": {"yo": "me divertí",    "tú": "te divertiste",  "él/ella": "se divirtió",   "nosotros": "nos divertimos",    "vosotros": "os divertisteis", "ellos/ellas": "se divirtieron"},
        "imperfect": {"yo": "me divertía",   "tú": "te divertías",   "él/ella": "se divertía",   "nosotros": "nos divertíamos",   "vosotros": "os divertíais",   "ellos/ellas": "se divertían"},
        "future":    {"yo": "me divertiré",  "tú": "te divertirás",  "él/ella": "se divertirá",  "nosotros": "nos divertiremos",  "vosotros": "os divertiréis",  "ellos/ellas": "se divertirán"},
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

# ── Lessons ───────────────────────────────────────────────────────────────────

LESSONS = {
    "vocabulary": {
        "1": {
            "title": "Lesson 1",
            "subtitle": "Un Festival de Arte",
            "words": VOCABULARY,
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
    },
}
