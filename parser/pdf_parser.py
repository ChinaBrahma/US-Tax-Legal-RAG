import fitz
import os
import json

# Dataset folder
DATASET_FOLDER = "dataset"

all_documents = []

# Har category (Acts, Court Judgements, etc.)
for category in os.listdir(DATASET_FOLDER):

    category_path = os.path.join(DATASET_FOLDER, category)

    if not os.path.isdir(category_path):
        continue

    print(f"\nProcessing Folder: {category}")

    # Har PDF
    for filename in os.listdir(category_path):

        if not filename.endswith(".pdf"):
            continue

        pdf_path = os.path.join(category_path, filename)

        print(f"Reading: {filename}")

        try:
            doc = fitz.open(pdf_path)

            for page_number in range(len(doc)):

                page = doc.load_page(page_number)

                text = page.get_text()

                all_documents.append({
                    "document": filename,
                    "category": category,
                    "page": page_number + 1,
                    "text": text
                })

        except Exception as e:
            print("Error:", filename, e)

# output folder
os.makedirs("output", exist_ok=True)

with open("output/legal_documents.json", "w", encoding="utf-8") as f:
    json.dump(all_documents, f, indent=4, ensure_ascii=False)

print("\nDone!")
print("Total Pages:", len(all_documents))