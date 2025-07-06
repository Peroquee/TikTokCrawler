import whisper
import argparse

def main():
    parser = argparse.ArgumentParser(
        description= "Audiodatei transcribieren mit whisper"
    )
    parser.add_argument(
        "-i", "--input", required=False,
        default= "input.mp4",
        help="Pfad zur EingabeAudiodatei"
    )
    parser.add_argument(
        "-o", "--output", required=False,
        default= "output\\output.txt",
        help="Pfad zur Ausgabgedatei"
    )
    parser.add_argument(
        "-m", "--model",
        default="medium",
        help="Whisper-modellgröße (tiny,base,small,medium,large)"
    )
    args = parser.parse_args()
    #model laden
    model = whisper.load_model(args.model)
    #Transkription
    result = model.transcribe(args.input)

    #in Datei schreiben

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(result["text"])

    print(f"Transcription output written to {output_path}")

if __name__ == "__main__":
    main()