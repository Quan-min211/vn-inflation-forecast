import json

with open("c:\\HCMUTE\\nam3ki2_2\\da\\vn-inflation-forecast\\src\\Project1_DAAN.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

with open("c:\\HCMUTE\\nam3ki2_2\\da\\vn-inflation-forecast\\scratch_nb_content.txt", "w", encoding="utf-8") as out:
    for cell in nb.get("cells", []):
        if cell.get("cell_type") in ["markdown", "code"]:
            out.write(f"--- {cell['cell_type'].upper()} ---\n")
            source = cell.get("source", [])
            if isinstance(source, list):
                out.write("".join(source))
            else:
                out.write(source)
            out.write("\n\n")
