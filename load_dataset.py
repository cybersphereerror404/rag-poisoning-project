from datasets import load_dataset

# load dataset
dataset = load_dataset("deepset/prompt-injections")

print(dataset)

# show a few examples
for i in range(5):
    print(dataset["train"][i])