import argparse
import json
import random
import sys
from pathlib import Path

VOCABULARY = {
    # Las Bellas Artes
    "el baile": ["dance"],
    "la danza": ["dance"],
    "el boleto": ["ticket"],
    "la canción": ["song"],
    "el concierto": ["concert"],
    "la comedia": ["comedy"],
    "el cuento": ["story", "short story"],
    "la cultura": ["culture"],
    "el drama": ["drama"],
    "la tragedia": ["tragedy"],
    "la escultura": ["sculpture"],
    "el espectáculo": ["show", "spectacle", "performance"],
    "la estatua": ["statue"],
    "el festival": ["festival"],
    "la historia": ["history", "story"],
    "la música": ["music"],
    "la obra": ["work", "play"],
    "el crítico": ["critic"],
    "la crítica": ["criticism", "critique", "review"],
    "la obra maestra": ["masterpiece"],
    "la ópera": ["opera"],
    "la zarzuela": ["musical", "spanish musical"],
    "la orquesta": ["orchestra"],
    "el personaje": ["character"],
    "el protagonista": ["protagonist", "main character"],
    "la pintura": ["painting"],
    "la poesía": ["poetry"],
    "el público": ["audience", "public"],
    "el teatro": ["theater", "theatre"],
    "la taquilla": ["ticket booth", "box office"],
    "el papel": ["role", "paper"],
    "los instrumentos": ["instruments"],
    "artístico": ["artistic"],
    "clásico": ["classic", "classical"],
    "dramático": ["dramatic"],
    "extranjero": ["foreign"],
    "folclórico": ["folkloric", "folk"],
    "moderno": ["modern"],
    "romántico": ["romantic"],
    "talentoso": ["talented"],
    # Otras artes
    "la cerámica": ["ceramics", "pottery"],
    "el tejido": ["knitting", "weaving", "fabric"],
    "la fotografía": ["photography"],
    # Los Artistas
    "el bailarín": ["dancer", "male dancer"],
    "la bailarina": ["dancer", "female dancer", "ballerina"],
    "el/la cantante": ["singer"],
    "el/la compositor/a": ["composer"],
    "el/la director/a": ["director"],
    "el/la dramaturgo/a": ["playwright"],
    "el/la escritor/a": ["writer", "author"],
    "la estrella de cine": ["movie star", "film star"],
    "el músico": ["musician"],
    "el poeta": ["poet"],
    "la poetisa": ["poetess", "poet"],
    "el/la artesano/a": ["artisan", "craftsperson"],
    "el actor / la actriz": ["actor", "actress"],
    # El Cine y la Televisión
    "el canal": ["channel"],
    "el concurso": ["competition", "contest", "game show"],
    "los dibujos animados": ["cartoons", "animations"],
    "el documental": ["documentary"],
    "el premio": ["award", "prize"],
    "la realidad": ["reality"],
    "el programa de entrevistas": ["talk show", "interview show"],
    "la telenovela": ["soap opera"],
    "de acción": ["action"],
    "de aventuras": ["adventure"],
    "de terror": ["horror", "terror"],
    "de horror": ["horror"],
    "de ciencia ficción": ["science fiction", "sci-fi"],
    "de vaqueros": ["western", "cowboy"],
    "romántica": ["romantic"],
    "histórica": ["historical", "historic"],
    "basada en un hecho real": ["based on a true story"],
    # Verbos
    "dibujar": ["to draw"],
    "bailar": ["to dance"],
    "cantar": ["to sing"],
    "escribir": ["to write"],
    "declamar": ["to recite", "to declaim"],
    "pintar": ["to paint"],
    "esculpir": ["to sculpt"],
    "aburrirse": ["to get bored", "to be bored"],
    "divertirse": ["to have fun", "to enjoy oneself"],
    "aplaudir": ["to applaud", "to clap"],
    "apreciar": ["to appreciate"],
    "criticar": ["to criticize"],
    "dirigir": ["to direct"],
    "hacer el papel de": ["to play the role of"],
    "interpretar": ["to perform", "to interpret"],
    "presentar": ["to present"],
    "publicar": ["to publish"],
    "tocar": ["to play (instrument)", "to touch"],
    "dramatizar": ["to dramatize"],
    "actuar": ["to act"],
    "componer": ["to compose"],
    "tejer": ["to knit", "to weave"],
}


def normalize(text: str) -> str:
    return text.strip().lower()


def check_answer(user_answer: str, correct_answers: list[str]) -> bool:
    user = normalize(user_answer)
    return any(user == normalize(ans) for ans in correct_answers)


def print_score(correct: int, total: int) -> None:
    if total == 0:
        return
    pct = correct / total * 100
    bar_len = 20
    filled = round(bar_len * correct / total)
    bar = "█" * filled + "░" * (bar_len - filled)
    print(f"\n  Score: {correct}/{total}  [{bar}]  {pct:.0f}%")


def load_vocabulary(path: str) -> dict[str, list[str]]:
    file = Path(path)
    if not file.exists():
        print(f"Error: input file '{path}' not found.")
        sys.exit(1)
    with file.open(encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        print("Error: input file must be a JSON object.")
        sys.exit(1)
    # Normalize values: accept both strings and lists
    return {k: ([v] if isinstance(v, str) else v) for k, v in data.items()}


def save_vocabulary(vocab: dict[str, list[str]], path: str) -> None:
    with Path(path).open("w", encoding="utf-8") as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)
    print(f"  Incorrect words saved to '{path}'")


def run_quiz(input_file: str | None, output_file: str | None) -> None:
    vocab = load_vocabulary(input_file) if input_file else VOCABULARY

    if not vocab:
        print("No words to quiz. The input file is empty.")
        return

    words = list(vocab.keys())
    random.shuffle(words)

    correct = 0
    total = 0
    asked: set[str] = set()
    wrong: dict[str, list[str]] = {}

    source_label = f"from '{input_file}'" if input_file else "— Lección 5"
    print("\n" + "=" * 50)
    print(f"   Spanish Vocabulary Quiz {source_label}")
    print("=" * 50)
    print(f"  {len(words)} words loaded.")
    print("Type your English translation and press Enter.")
    print("Type  'skip'  to skip,  'quit'  to exit.\n")

    while True:
        remaining = [w for w in words if w not in asked]
        if not remaining:
            print("\nYou've gone through all the words!")
            break

        word = random.choice(remaining)
        asked.add(word)
        total += 1

        print(f"[{total}/{len(words)}]  {word}")
        try:
            answer = input("  Your answer: ").strip()
        except (KeyboardInterrupt, EOFError):
            total -= 1
            break

        if normalize(answer) == "quit":
            total -= 1
            break

        if normalize(answer) == "skip":
            correct_list = " / ".join(vocab[word])
            print(f"  Skipped. Correct: {correct_list}\n")
            total -= 1
            asked.discard(word)
            continue

        correct_answers = vocab[word]
        if check_answer(answer, correct_answers):
            correct += 1
            print("  Correct!\n")
        else:
            correct_str = " / ".join(correct_answers)
            print(f"  Wrong. Correct answer: {correct_str}\n")
            wrong[word] = correct_answers

    print("\n" + "=" * 50)
    print("  Final Results")
    print("=" * 50)
    print_score(correct, total)
    if total > 0:
        if correct == total:
            print("  Perfect score! Excellent work!")
        elif correct / total >= 0.8:
            print("  Great job!")
        elif correct / total >= 0.5:
            print("  Keep practicing!")
        else:
            print("  Keep studying, you'll get there!")

    if wrong:
        print(f"\n  Words to review: {len(wrong)}")
        for w, answers in wrong.items():
            print(f"    {w}  →  {' / '.join(answers)}")

    if output_file:
        print()
        if wrong:
            save_vocabulary(wrong, output_file)
        else:
            # All correct — clear the file so next run won't re-quiz old mistakes
            save_vocabulary({}, output_file)
            print(f"  No mistakes — '{output_file}' cleared.")

    print("=" * 50 + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Spanish vocabulary quiz",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  # Quiz all words, save mistakes\n"
            "  python3 spanish_quiz.py -o wrong.json\n\n"
            "  # Re-quiz only previous mistakes, update the file\n"
            "  python3 spanish_quiz.py -i wrong.json -o wrong.json\n\n"
            "  # Load custom word list, save mistakes elsewhere\n"
            "  python3 spanish_quiz.py -i my_words.json -o mistakes.json"
        ),
    )
    parser.add_argument("-i", "--input", metavar="FILE",
                        help="JSON file to load words from (default: built-in vocabulary)")
    parser.add_argument("-o", "--output", metavar="FILE",
                        help="JSON file to save incorrectly answered words to")
    args = parser.parse_args()

    run_quiz(input_file=args.input, output_file=args.output)
