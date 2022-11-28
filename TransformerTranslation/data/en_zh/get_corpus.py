import json

if __name__ == "__main__":
    files = ['train', 'dev', 'test']
    ch_path = 'corpus.ch'
    en_path = 'corpus.en'
    ch_lines = []
    en_lines = []

    corpus = json.load(open('ch2en_align_result.json', 'r', encoding="utf-8"))
    for item in corpus:
        ch_lines.append(item['chinese_content'] + "\n")
        en_lines.append(item['english_content'] + "\n")
    for file in files:
        with open(f"{file}.ch", "w+", encoding="utf-8") as fch:
            if file == "train":
                ch_lines = ch_lines[:int(len(ch_lines) * 0.8)]
                fch.writelines(ch_lines)
            elif file == "dev":
                ch_lines = ch_lines[int(len(ch_lines) * 0.8):]
                fch.writelines(ch_lines)
            else:
                ch_lines = ch_lines[int(len(ch_lines) * 0.8):]
                fch.writelines(ch_lines)

        with open(f"{file}.en", "w+", encoding="utf-8") as fen:
            if file == "train":
                en_lines = en_lines[:int(len(en_lines) * 0.8)]
                fen.writelines(en_lines)
            elif file == "dev":
                en_lines = en_lines[int(len(en_lines) * 0.8):]
                fen.writelines(en_lines)
            else:
                en_lines = en_lines[int(len(en_lines) * 0.8):]
                fen.writelines(en_lines)
