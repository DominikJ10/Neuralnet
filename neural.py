from keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, MaxPool2D, Activation, Flatten
from keras.utils.np_utils import to_categorical
from extra_keras_datasets import emnist
from tensorflow.keras.optimizers import Adam


import tensorflow
import keras

net = tensorflow.keras.Sequential()

input_shape = (28, 28, 1)
kernel_size = (3, 3)

net.add(Conv2D(64, kernel_size, input_shape=input_shape)) 
net.add(MaxPool2D(pool_size=(2, 2)))
net.add(Activation('relu'))
net.add(Flatten())

net.add(Dense(128, activation='relu')) #warstwa ukryta - 128
net.add(Dense(27, activation='softmax')) #warstwa wyjściowa


(X_train, y_train), (X_test, y_test) = emnist.load_data(type='letters') #załaduj emnist 'letters'
X_train = X_train.reshape(-1, 28, 28, 1) 
X_test = X_test.reshape(-1, 28, 28, 1) #matryca obrazka
y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train = X_train/255.0
X_test = X_test/255.0

tensorboard = tensorflow.keras.callbacks.TensorBoard(
    log_dir=r"C:\Users\Dominik\Desktop\logs",
    histogram_freq=0,
    write_graph=True,
    write_images=False,
    update_freq="batch",
    profile_batch=2,
    embeddings_freq=0,
    embeddings_metadata=None,
)

net.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])
net.fit(X_train, y_train_cat, batch_size=9, epochs=5, verbose=1, validation_split=0.3, callbacks=[tensorboard])
net.evaluate(X_test, y_test_cat)

net.save('neuralnet\model')
