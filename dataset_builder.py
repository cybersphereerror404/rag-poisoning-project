from datasets import load_dataset

dataset = load_dataset("deepset/prompt-injections")

documents = []
labels = []

for item in dataset["train"]:
    text = item["text"]

    documents.append(text)

    if item["label"] == "injection":
        labels.append(1)
    else:
        labels.append(0)

print("Total documents:", len(documents))