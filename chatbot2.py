import json
import random
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.feature_extraction.text import CountVectorizer

# Training Data
training_data = [
    ("hello", "greeting"),
    ("hi", "greeting"),
    ("how are you", "greeting"),
    ("bye", "goodbye"),
    ("see you later", "goodbye"),
    ("what is ai", "ai_question"),
    ("tell me about machine learning", "ai_question")
]

responses = {
    "greeting": [
        "Hello!",
        "Hi there!",
        "Nice to meet you."
    ],
    "goodbye": [
        "Goodbye!",
        "See you later!"
    ],
    "ai_question": [
        "AI is the simulation of human intelligence by machines."
    ]
}

texts = [x[0] for x in training_data]
labels = [x[1] for x in training_data]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts).toarray()

unique_labels = list(set(labels))
label_map = {label: i for i, label in enumerate(unique_labels)}

y = torch.tensor(
    [label_map[label] for label in labels],
    dtype=torch.long
)

X = torch.tensor(X, dtype=torch.float32)

class ChatNet(nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()

        self.model = nn.Sequential(
            nn.Linear(input_size, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, output_size)
        )

    def forward(self, x):
        return self.model(x)

model = ChatNet(
    X.shape[1],
    len(unique_labels)
)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

for epoch in range(500):
    optimizer.zero_grad()

    outputs = model(X)

    loss = criterion(outputs, y)

    loss.backward()

    optimizer.step()

print("Training Complete")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        break

    vector = vectorizer.transform(
        [user_input]
    ).toarray()

    vector = torch.tensor(
        vector,
        dtype=torch.float32
    )

    prediction = model(vector)

    tag = unique_labels[
        torch.argmax(prediction).item()
    ]

    print(
        "Bot:",
        random.choice(responses[tag])
    )