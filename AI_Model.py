import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# 1. Load dataset (MNIST digits)
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# 2. Normalize
x_train, x_test = x_train / 255.0, x_test / 255.0

# 3. Build model
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')
])

# 4. Compile
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 5. Train
model.fit(x_train, y_train, epochs=5)

# 6. Evaluate
model.evaluate(x_test, y_test)
