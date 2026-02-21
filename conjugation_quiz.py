#!/usr/bin/env python3
"""Spanish verb conjugation quiz — Lección 5 verbs."""

import argparse
import json
import random
import sys
import unicodedata
from pathlib import Path

PRONOUNS = ["yo", "tú", "él/ella", "nosotros", "vosotros", "ellos/ellas"]

TENSE_NAMES = {
    "present":   "Presente",
    "preterite": "Pretérito",
    "imperfect": "Imperfecto",
    "future":    "Futuro",
}

# Sentence templates: {verb} marks where the conjugated form goes.
# The subject pronoun is prepended automatically at display time.
# fmt: off
VERBS: dict[str, dict] = {
    # ── Regular -AR ──────────────────────────────────────────────────────────
    "bailar": {
        "english": "to dance",
        "sentence": "{bailar} en la fiesta del colegio.",
        "present":   {"yo": "bailo",      "tú": "bailas",      "él/ella": "baila",      "nosotros": "bailamos",      "vosotros": "bailáis",      "ellos/ellas": "bailan"},
        "preterite": {"yo": "bailé",      "tú": "bailaste",    "él/ella": "bailó",      "nosotros": "bailamos",      "vosotros": "bailasteis",   "ellos/ellas": "bailaron"},
        "imperfect": {"yo": "bailaba",    "tú": "bailabas",    "él/ella": "bailaba",    "nosotros": "bailábamos",    "vosotros": "bailabais",    "ellos/ellas": "bailaban"},
        "future":    {"yo": "bailaré",    "tú": "bailarás",    "él/ella": "bailará",    "nosotros": "bailaremos",    "vosotros": "bailaréis",    "ellos/ellas": "bailarán"},
    },
    "cantar": {
        "english": "to sing",
        "sentence": "{cantar} una canción en el concierto.",
        "present":   {"yo": "canto",      "tú": "cantas",      "él/ella": "canta",      "nosotros": "cantamos",      "vosotros": "cantáis",      "ellos/ellas": "cantan"},
        "preterite": {"yo": "canté",      "tú": "cantaste",    "él/ella": "cantó",      "nosotros": "cantamos",      "vosotros": "cantasteis",   "ellos/ellas": "cantaron"},
        "imperfect": {"yo": "cantaba",    "tú": "cantabas",    "él/ella": "cantaba",    "nosotros": "cantábamos",    "vosotros": "cantabais",    "ellos/ellas": "cantaban"},
        "future":    {"yo": "cantaré",    "tú": "cantarás",    "él/ella": "cantará",    "nosotros": "cantaremos",    "vosotros": "cantaréis",    "ellos/ellas": "cantarán"},
    },
    "dibujar": {
        "english": "to draw",
        "sentence": "{dibujar} un retrato en la clase de arte.",
        "present":   {"yo": "dibujo",     "tú": "dibujas",     "él/ella": "dibuja",     "nosotros": "dibujamos",     "vosotros": "dibujáis",     "ellos/ellas": "dibujan"},
        "preterite": {"yo": "dibujé",     "tú": "dibujaste",   "él/ella": "dibujó",     "nosotros": "dibujamos",     "vosotros": "dibujasteis",  "ellos/ellas": "dibujaron"},
        "imperfect": {"yo": "dibujaba",   "tú": "dibujabas",   "él/ella": "dibujaba",   "nosotros": "dibujábamos",   "vosotros": "dibujabais",   "ellos/ellas": "dibujaban"},
        "future":    {"yo": "dibujaré",   "tú": "dibujarás",   "él/ella": "dibujará",   "nosotros": "dibujaremos",   "vosotros": "dibujaréis",   "ellos/ellas": "dibujarán"},
    },
    "pintar": {
        "english": "to paint",
        "sentence": "{pintar} un cuadro hermoso en el estudio.",
        "present":   {"yo": "pinto",      "tú": "pintas",      "él/ella": "pinta",      "nosotros": "pintamos",      "vosotros": "pintáis",      "ellos/ellas": "pintan"},
        "preterite": {"yo": "pinté",      "tú": "pintaste",    "él/ella": "pintó",      "nosotros": "pintamos",      "vosotros": "pintasteis",   "ellos/ellas": "pintaron"},
        "imperfect": {"yo": "pintaba",    "tú": "pintabas",    "él/ella": "pintaba",    "nosotros": "pintábamos",    "vosotros": "pintabais",    "ellos/ellas": "pintaban"},
        "future":    {"yo": "pintaré",    "tú": "pintarás",    "él/ella": "pintará",    "nosotros": "pintaremos",    "vosotros": "pintaréis",    "ellos/ellas": "pintarán"},
    },
    "presentar": {
        "english": "to present",
        "sentence": "{presentar} el espectáculo en el teatro.",
        "present":   {"yo": "presento",   "tú": "presentas",   "él/ella": "presenta",   "nosotros": "presentamos",   "vosotros": "presentáis",   "ellos/ellas": "presentan"},
        "preterite": {"yo": "presenté",   "tú": "presentaste", "él/ella": "presentó",   "nosotros": "presentamos",   "vosotros": "presentasteis","ellos/ellas": "presentaron"},
        "imperfect": {"yo": "presentaba", "tú": "presentabas", "él/ella": "presentaba", "nosotros": "presentábamos", "vosotros": "presentabais", "ellos/ellas": "presentaban"},
        "future":    {"yo": "presentaré", "tú": "presentarás", "él/ella": "presentará", "nosotros": "presentaremos", "vosotros": "presentaréis", "ellos/ellas": "presentarán"},
    },
    "apreciar": {
        "english": "to appreciate",
        "sentence": "{apreciar} la música clásica de la orquesta.",
        "present":   {"yo": "aprecio",    "tú": "aprecias",    "él/ella": "aprecia",    "nosotros": "apreciamos",    "vosotros": "apreciáis",    "ellos/ellas": "aprecian"},
        "preterite": {"yo": "aprecié",    "tú": "apreciaste",  "él/ella": "apreció",    "nosotros": "apreciamos",    "vosotros": "apreciasteis", "ellos/ellas": "apreciaron"},
        "imperfect": {"yo": "apreciaba",  "tú": "apreciabas",  "él/ella": "apreciaba",  "nosotros": "apreciábamos",  "vosotros": "apreciabais",  "ellos/ellas": "apreciaban"},
        "future":    {"yo": "apreciaré",  "tú": "apreciarás",  "él/ella": "apreciará",  "nosotros": "apreciaremos",  "vosotros": "apreciaréis",  "ellos/ellas": "apreciarán"},
    },
    "declamar": {
        "english": "to recite / declaim",
        "sentence": "{declamar} un poema en el festival de arte.",
        "present":   {"yo": "declamo",    "tú": "declamas",    "él/ella": "declama",    "nosotros": "declamamos",    "vosotros": "declamáis",    "ellos/ellas": "declaman"},
        "preterite": {"yo": "declamé",    "tú": "declamaste",  "él/ella": "declamó",    "nosotros": "declamamos",    "vosotros": "declamasteis", "ellos/ellas": "declamaron"},
        "imperfect": {"yo": "declamaba",  "tú": "declamabas",  "él/ella": "declamaba",  "nosotros": "declamábamos",  "vosotros": "declamabais",  "ellos/ellas": "declamaban"},
        "future":    {"yo": "declamaré",  "tú": "declamarás",  "él/ella": "declamará",  "nosotros": "declamaremos",  "vosotros": "declamaréis",  "ellos/ellas": "declamarán"},
    },
    "interpretar": {
        "english": "to perform / interpret",
        "sentence": "{interpretar} el papel del protagonista en la obra.",
        "present":   {"yo": "interpreto",    "tú": "interpretas",    "él/ella": "interpreta",    "nosotros": "interpretamos",    "vosotros": "interpretáis",    "ellos/ellas": "interpretan"},
        "preterite": {"yo": "interpreté",    "tú": "interpretaste",  "él/ella": "interpretó",    "nosotros": "interpretamos",    "vosotros": "interpretasteis", "ellos/ellas": "interpretaron"},
        "imperfect": {"yo": "interpretaba",  "tú": "interpretabas",  "él/ella": "interpretaba",  "nosotros": "interpretábamos",  "vosotros": "interpretabais",  "ellos/ellas": "interpretaban"},
        "future":    {"yo": "interpretaré",  "tú": "interpretarás",  "él/ella": "interpretará",  "nosotros": "interpretaremos",  "vosotros": "interpretaréis",  "ellos/ellas": "interpretarán"},
    },
    # ── Spelling-change -AR ───────────────────────────────────────────────────
    # tocar  (c → qu before e — affects yo preterite)
    "tocar": {
        "english": "to play (instrument)",
        "sentence": "{tocar} la guitarra en la orquesta.",
        "present":   {"yo": "toco",       "tú": "tocas",       "él/ella": "toca",       "nosotros": "tocamos",       "vosotros": "tocáis",       "ellos/ellas": "tocan"},
        "preterite": {"yo": "toqué",      "tú": "tocaste",     "él/ella": "tocó",       "nosotros": "tocamos",       "vosotros": "tocasteis",    "ellos/ellas": "tocaron"},
        "imperfect": {"yo": "tocaba",     "tú": "tocabas",     "él/ella": "tocaba",     "nosotros": "tocábamos",     "vosotros": "tocabais",     "ellos/ellas": "tocaban"},
        "future":    {"yo": "tocaré",     "tú": "tocarás",     "él/ella": "tocará",     "nosotros": "tocaremos",     "vosotros": "tocaréis",     "ellos/ellas": "tocarán"},
    },
    # criticar  (c → qu before e)
    "criticar": {
        "english": "to criticize",
        "sentence": "{criticar} la obra maestra expuesta en el museo.",
        "present":   {"yo": "critico",    "tú": "criticas",    "él/ella": "critica",    "nosotros": "criticamos",    "vosotros": "criticáis",    "ellos/ellas": "critican"},
        "preterite": {"yo": "critiqué",   "tú": "criticaste",  "él/ella": "criticó",    "nosotros": "criticamos",    "vosotros": "criticasteis", "ellos/ellas": "criticaron"},
        "imperfect": {"yo": "criticaba",  "tú": "criticabas",  "él/ella": "criticaba",  "nosotros": "criticábamos",  "vosotros": "criticabais",  "ellos/ellas": "criticaban"},
        "future":    {"yo": "criticaré",  "tú": "criticarás",  "él/ella": "criticará",  "nosotros": "criticaremos",  "vosotros": "criticaréis",  "ellos/ellas": "criticarán"},
    },
    # publicar  (c → qu before e)
    "publicar": {
        "english": "to publish",
        "sentence": "{publicar} un libro de poesía este año.",
        "present":   {"yo": "publico",    "tú": "publicas",    "él/ella": "publica",    "nosotros": "publicamos",    "vosotros": "publicáis",    "ellos/ellas": "publican"},
        "preterite": {"yo": "publiqué",   "tú": "publicaste",  "él/ella": "publicó",    "nosotros": "publicamos",    "vosotros": "publicasteis", "ellos/ellas": "publicaron"},
        "imperfect": {"yo": "publicaba",  "tú": "publicabas",  "él/ella": "publicaba",  "nosotros": "publicábamos",  "vosotros": "publicabais",  "ellos/ellas": "publicaban"},
        "future":    {"yo": "publicaré",  "tú": "publicarás",  "él/ella": "publicará",  "nosotros": "publicaremos",  "vosotros": "publicaréis",  "ellos/ellas": "publicarán"},
    },
    # dramatizar  (z → c before e — affects yo preterite)
    "dramatizar": {
        "english": "to dramatize",
        "sentence": "{dramatizar} la historia de la telenovela en el escenario.",
        "present":   {"yo": "dramatizo",   "tú": "dramatizas",   "él/ella": "dramatiza",   "nosotros": "dramatizamos",   "vosotros": "dramatizáis",   "ellos/ellas": "dramatizan"},
        "preterite": {"yo": "dramaticé",   "tú": "dramatizaste", "él/ella": "dramatizó",   "nosotros": "dramatizamos",   "vosotros": "dramatizasteis","ellos/ellas": "dramatizaron"},
        "imperfect": {"yo": "dramatizaba", "tú": "dramatizabas", "él/ella": "dramatizaba", "nosotros": "dramatizábamos", "vosotros": "dramatizabais", "ellos/ellas": "dramatizaban"},
        "future":    {"yo": "dramatizaré", "tú": "dramatizarás", "él/ella": "dramatizará", "nosotros": "dramatizaremos", "vosotros": "dramatizaréis", "ellos/ellas": "dramatizarán"},
    },
    # actuar  (u → ú when stressed: yo/tú/él/ellos in present)
    "actuar": {
        "english": "to act",
        "sentence": "{actuar} en la telenovela más popular del canal.",
        "present":   {"yo": "actúo",      "tú": "actúas",      "él/ella": "actúa",      "nosotros": "actuamos",      "vosotros": "actuáis",      "ellos/ellas": "actúan"},
        "preterite": {"yo": "actué",      "tú": "actuaste",    "él/ella": "actuó",      "nosotros": "actuamos",      "vosotros": "actuasteis",   "ellos/ellas": "actuaron"},
        "imperfect": {"yo": "actuaba",    "tú": "actuabas",    "él/ella": "actuaba",    "nosotros": "actuábamos",    "vosotros": "actuabais",    "ellos/ellas": "actuaban"},
        "future":    {"yo": "actuaré",    "tú": "actuarás",    "él/ella": "actuará",    "nosotros": "actuaremos",    "vosotros": "actuaréis",    "ellos/ellas": "actuarán"},
    },
    # ── Regular -IR ───────────────────────────────────────────────────────────
    "escribir": {
        "english": "to write",
        "sentence": "{escribir} un cuento para el festival literario.",
        "present":   {"yo": "escribo",    "tú": "escribes",    "él/ella": "escribe",    "nosotros": "escribimos",    "vosotros": "escribís",     "ellos/ellas": "escriben"},
        "preterite": {"yo": "escribí",    "tú": "escribiste",  "él/ella": "escribió",   "nosotros": "escribimos",    "vosotros": "escribisteis", "ellos/ellas": "escribieron"},
        "imperfect": {"yo": "escribía",   "tú": "escribías",   "él/ella": "escribía",   "nosotros": "escribíamos",   "vosotros": "escribíais",   "ellos/ellas": "escribían"},
        "future":    {"yo": "escribiré",  "tú": "escribirás",  "él/ella": "escribirá",  "nosotros": "escribiremos",  "vosotros": "escribiréis",  "ellos/ellas": "escribirán"},
    },
    "aplaudir": {
        "english": "to applaud",
        "sentence": "{aplaudir} al actor al final del espectáculo.",
        "present":   {"yo": "aplaudo",    "tú": "aplaudes",    "él/ella": "aplaude",    "nosotros": "aplaudimos",    "vosotros": "aplaudís",     "ellos/ellas": "aplauden"},
        "preterite": {"yo": "aplaudí",    "tú": "aplaudiste",  "él/ella": "aplaudió",   "nosotros": "aplaudimos",    "vosotros": "aplaudisteis", "ellos/ellas": "aplaudieron"},
        "imperfect": {"yo": "aplaudía",   "tú": "aplaudías",   "él/ella": "aplaudía",   "nosotros": "aplaudíamos",   "vosotros": "aplaudíais",   "ellos/ellas": "aplaudían"},
        "future":    {"yo": "aplaudiré",  "tú": "aplaudirás",  "él/ella": "aplaudirá",  "nosotros": "aplaudiremos",  "vosotros": "aplaudiréis",  "ellos/ellas": "aplaudirán"},
    },
    "esculpir": {
        "english": "to sculpt",
        "sentence": "{esculpir} una estatua de mármol para la exposición.",
        "present":   {"yo": "esculpo",    "tú": "esculpes",    "él/ella": "esculpe",    "nosotros": "esculpimos",    "vosotros": "esculpís",     "ellos/ellas": "esculpen"},
        "preterite": {"yo": "esculpí",    "tú": "esculpiste",  "él/ella": "esculpió",   "nosotros": "esculpimos",    "vosotros": "esculpisteis", "ellos/ellas": "esculpieron"},
        "imperfect": {"yo": "esculpía",   "tú": "esculpías",   "él/ella": "esculpía",   "nosotros": "esculpíamos",   "vosotros": "esculpíais",   "ellos/ellas": "esculpían"},
        "future":    {"yo": "esculpiré",  "tú": "esculpirás",  "él/ella": "esculpirá",  "nosotros": "esculpiremos",  "vosotros": "esculpiréis",  "ellos/ellas": "esculpirán"},
    },
    # dirigir  (g → j before o/a — affects yo present)
    "dirigir": {
        "english": "to direct",
        "sentence": "{dirigir} la orquesta con mucho talento.",
        "present":   {"yo": "dirijo",     "tú": "diriges",     "él/ella": "dirige",     "nosotros": "dirigimos",     "vosotros": "dirigís",      "ellos/ellas": "dirigen"},
        "preterite": {"yo": "dirigí",     "tú": "dirigiste",   "él/ella": "dirigió",    "nosotros": "dirigimos",     "vosotros": "dirigisteis",  "ellos/ellas": "dirigieron"},
        "imperfect": {"yo": "dirigía",    "tú": "dirigías",    "él/ella": "dirigía",    "nosotros": "dirigíamos",    "vosotros": "dirigíais",    "ellos/ellas": "dirigían"},
        "future":    {"yo": "dirigiré",   "tú": "dirigirás",   "él/ella": "dirigirá",   "nosotros": "dirigiremos",   "vosotros": "dirigiréis",   "ellos/ellas": "dirigirán"},
    },
    # ── Regular -ER ───────────────────────────────────────────────────────────
    "tejer": {
        "english": "to knit / weave",
        "sentence": "{tejer} una manta colorida para el invierno.",
        "present":   {"yo": "tejo",       "tú": "tejes",       "él/ella": "teje",       "nosotros": "tejemos",       "vosotros": "tejéis",       "ellos/ellas": "tejen"},
        "preterite": {"yo": "tejí",       "tú": "tejiste",     "él/ella": "tejió",      "nosotros": "tejimos",       "vosotros": "tejisteis",    "ellos/ellas": "tejieron"},
        "imperfect": {"yo": "tejía",      "tú": "tejías",      "él/ella": "tejía",      "nosotros": "tejíamos",      "vosotros": "tejíais",      "ellos/ellas": "tejían"},
        "future":    {"yo": "teje ré",    "tú": "tejerás",     "él/ella": "tejerá",     "nosotros": "tejeremos",     "vosotros": "tejeréis",     "ellos/ellas": "tejerán"},
    },
    # ── Irregular ─────────────────────────────────────────────────────────────
    # componer  (like poner: pongo/compongo; preterite puse → compuse)
    "componer": {
        "english": "to compose",
        "sentence": "{componer} una ópera famosa para el teatro nacional.",
        "present":   {"yo": "compongo",   "tú": "compones",    "él/ella": "compone",    "nosotros": "componemos",    "vosotros": "componéis",    "ellos/ellas": "componen"},
        "preterite": {"yo": "compuse",    "tú": "compusiste",  "él/ella": "compuso",    "nosotros": "compusimos",    "vosotros": "compusisteis", "ellos/ellas": "compusieron"},
        "imperfect": {"yo": "componía",   "tú": "componías",   "él/ella": "componía",   "nosotros": "componíamos",   "vosotros": "componíais",   "ellos/ellas": "componían"},
        "future":    {"yo": "compondré",  "tú": "compondrás",  "él/ella": "compondrá",  "nosotros": "compondremos",  "vosotros": "compondréis",  "ellos/ellas": "compondrán"},
    },
    # ── Reflexive -IR ─────────────────────────────────────────────────────────
    # aburrirse  (regular -ir, reflexive)
    "aburrirse": {
        "english": "to get bored",
        "sentence": "{aburrirse} durante el documental muy largo.",
        "present":   {"yo": "me aburro",     "tú": "te aburres",     "él/ella": "se aburre",     "nosotros": "nos aburrimos",     "vosotros": "os aburrís",      "ellos/ellas": "se aburren"},
        "preterite": {"yo": "me aburrí",     "tú": "te aburriste",   "él/ella": "se aburrió",    "nosotros": "nos aburrimos",     "vosotros": "os aburrísteis",  "ellos/ellas": "se aburrieron"},
        "imperfect": {"yo": "me aburría",    "tú": "te aburrías",    "él/ella": "se aburría",    "nosotros": "nos aburríamos",    "vosotros": "os aburríais",    "ellos/ellas": "se aburrían"},
        "future":    {"yo": "me aburriré",   "tú": "te aburrirás",   "él/ella": "se aburrirá",   "nosotros": "nos aburriremos",   "vosotros": "os aburriréis",   "ellos/ellas": "se aburrirán"},
    },
    # divertirse  (e → ie stem change in present: yo/tú/él/ellos;
    #              e → i in preterite: él/ellos;  reflexive)
    "divertirse": {
        "english": "to have fun / enjoy oneself",
        "sentence": "{divertirse} mucho en el festival de arte.",
        "present":   {"yo": "me divierto",   "tú": "te diviertes",   "él/ella": "se divierte",   "nosotros": "nos divertimos",    "vosotros": "os divertís",     "ellos/ellas": "se divierten"},
        "preterite": {"yo": "me divertí",    "tú": "te divertiste",  "él/ella": "se divirtió",   "nosotros": "nos divertimos",    "vosotros": "os divertisteis", "ellos/ellas": "se divirtieron"},
        "imperfect": {"yo": "me divertía",   "tú": "te divertías",   "él/ella": "se divertía",   "nosotros": "nos divertíamos",   "vosotros": "os divertíais",   "ellos/ellas": "se divertían"},
        "future":    {"yo": "me divertiré",  "tú": "te divertirás",  "él/ella": "se divertirá",  "nosotros": "nos divertiremos",  "vosotros": "os divertiréis",  "ellos/ellas": "se divertirán"},
    },
}
# fmt: on

# Fix typo in tejer future yo form
VERBS["tejer"]["future"]["yo"] = "tejeré"


def strip_accents(text: str) -> str:
    """Normalize text for accent-insensitive comparison."""
    return "".join(
        c for c in unicodedata.normalize("NFD", text.lower().strip())
        if unicodedata.category(c) != "Mn"
    )


def check_answer(user: str, correct: str) -> bool:
    return strip_accents(user) == strip_accents(correct)


def print_score(correct: int, total: int) -> None:
    if total == 0:
        return
    pct = correct / total * 100
    bar_len = 24
    filled = round(bar_len * correct / total)
    bar = "█" * filled + "░" * (bar_len - filled)
    print(f"\n  Score: {correct}/{total}  [{bar}]  {pct:.0f}%")


def select_tenses() -> list[str]:
    tense_list = list(TENSE_NAMES.keys())
    print("\nSelect tenses to practice:")
    for i, t in enumerate(tense_list, 1):
        print(f"  {i}. {TENSE_NAMES[t]}")
    print(f"  {len(tense_list) + 1}. All tenses")

    while True:
        try:
            raw = input("\nYour choice (e.g. 1 3  or  5 for all): ").strip()
        except (KeyboardInterrupt, EOFError):
            sys.exit(0)
        if not raw:
            return tense_list
        try:
            indices = [int(x) for x in raw.split()]
            if len(tense_list) + 1 in indices or not indices:
                return tense_list
            selected = [tense_list[i - 1] for i in indices if 1 <= i <= len(tense_list)]
            if selected:
                return selected
        except (ValueError, IndexError):
            pass
        print("  Invalid input, try again.")


def select_verbs() -> list[str]:
    verb_list = list(VERBS.keys())
    print("\nSelect verbs to practice:")
    for i, v in enumerate(verb_list, 1):
        print(f"  {i:2}. {v:15}  ({VERBS[v]['english']})")
    print(f"  {len(verb_list) + 1:2}. All verbs")

    while True:
        try:
            raw = input("\nYour choice (e.g. 1 3 5  or press Enter for all): ").strip()
        except (KeyboardInterrupt, EOFError):
            sys.exit(0)
        if not raw:
            return verb_list
        try:
            indices = [int(x) for x in raw.split()]
            if len(verb_list) + 1 in indices:
                return verb_list
            selected = [verb_list[i - 1] for i in indices if 1 <= i <= len(verb_list)]
            if selected:
                return selected
        except (ValueError, IndexError):
            pass
        print("  Invalid input, try again.")


def load_combos(path: str) -> list[dict]:
    file = Path(path)
    if not file.exists():
        print(f"Error: input file '{path}' not found.")
        sys.exit(1)
    with file.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        print("Error: input file must be a JSON array.")
        sys.exit(1)
    valid = [
        c for c in data
        if c.get("verb") in VERBS
        and c.get("tense") in TENSE_NAMES
        and c.get("pronoun") in PRONOUNS
    ]
    return valid


def save_combos(combos: list[dict], path: str) -> None:
    with Path(path).open("w", encoding="utf-8") as f:
        json.dump(combos, f, ensure_ascii=False, indent=2)
    print(f"  Saved to '{path}'")


def run_quiz(input_file: str | None, output_file: str | None) -> None:
    if input_file:
        combos = load_combos(input_file)
        if not combos:
            print("No valid combinations in input file.")
            return
        tenses_used = sorted(set(c["tense"] for c in combos), key=list(TENSE_NAMES).index)
        tense_label = " + ".join(TENSE_NAMES[t] for t in tenses_used)
        print(f"\n  Loaded {len(combos)} combos from '{input_file}'.")
    else:
        selected_verbs = select_verbs()
        selected_tenses = select_tenses()
        combos = [
            {"verb": v, "tense": t, "pronoun": p}
            for v in selected_verbs
            for t in selected_tenses
            for p in PRONOUNS
        ]
        tense_label = " + ".join(TENSE_NAMES[t] for t in selected_tenses)
        random.shuffle(combos)

    print("\n" + "=" * 58)
    print(f"   Spanish Conjugation Quiz — {tense_label}")
    print("=" * 58)
    print(f"  {len(combos)} conjugations to practice.")
    print("  Accents are not required.")
    print("  Commands:  'skip' — skip word   'quit' — exit\n")

    correct_count = 0
    total = 0
    wrong: list[dict] = []
    wrong_keys: set[tuple] = set()

    for combo in combos:
        verb    = combo["verb"]
        tense   = combo["tense"]
        pronoun = combo["pronoun"]
        key     = (verb, tense, pronoun)

        total += 1
        correct_form = VERBS[verb][tense][pronoun]
        english      = VERBS[verb]["english"]
        tense_name   = TENSE_NAMES[tense]

        # Build example sentence: prepend pronoun as subject, verb stays in {braces}
        raw_sentence = VERBS[verb].get("sentence", f"{{verb}} ...")
        sentence = pronoun.capitalize() + " " + raw_sentence

        print(f"[{total}/{len(combos)}]  {verb} ({english})")
        print(f"         {tense_name}  —  {pronoun}")
        print(f"         {sentence}")
        try:
            answer = input("  ➜  ").strip()
        except (KeyboardInterrupt, EOFError):
            total -= 1
            break

        cmd = answer.lower()
        if cmd == "quit":
            total -= 1
            break
        if cmd == "skip":
            print(f"  Skipped. Correct: {correct_form}\n")
            total -= 1
            continue

        if check_answer(answer, correct_form):
            correct_count += 1
            print("  Correct!\n")
        else:
            print(f"  Wrong.   Correct: {correct_form}\n")
            if key not in wrong_keys:
                wrong.append(combo)
                wrong_keys.add(key)

    print("\n" + "=" * 58)
    print("  Final Results")
    print("=" * 58)
    print_score(correct_count, total)

    if total > 0:
        pct = correct_count / total
        if pct == 1.0:
            print("  Perfect! Excellent work!")
        elif pct >= 0.8:
            print("  Great job!")
        elif pct >= 0.5:
            print("  Keep practicing!")
        else:
            print("  Keep studying, you'll get there!")

    if wrong:
        print(f"\n  Conjugations to review ({len(wrong)}):")
        for c in wrong[:12]:
            v, t, p = c["verb"], c["tense"], c["pronoun"]
            ans = VERBS[v][t][p]
            print(f"    {v:15} {TENSE_NAMES[t]:12} {p:14} → {ans}")
        if len(wrong) > 12:
            print(f"    ... and {len(wrong) - 12} more")

    if output_file:
        print()
        if wrong:
            save_combos(wrong, output_file)
            print(f"  {len(wrong)} incorrect conjugations saved for next practice.")
        else:
            save_combos([], output_file)
            print(f"  No mistakes — '{output_file}' cleared.")

    print("=" * 58 + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Spanish verb conjugation quiz — Lección 5",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  # Interactive tense/verb selection, save mistakes\n"
            "  python3 conjugation_quiz.py -o wrong.json\n\n"
            "  # Re-quiz only previous mistakes, update the file\n"
            "  python3 conjugation_quiz.py -i wrong.json -o wrong.json"
        ),
    )
    parser.add_argument("-i", "--input",  metavar="FILE",
                        help="JSON file with verb/tense/pronoun combos to re-quiz")
    parser.add_argument("-o", "--output", metavar="FILE",
                        help="JSON file to save incorrectly answered conjugations to")
    args = parser.parse_args()

    run_quiz(input_file=args.input, output_file=args.output)
