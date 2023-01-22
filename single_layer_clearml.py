import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


from clearml import Task


task=Task.init(project_name="workshop_clearml_example",task_name="scikit-learn_example")



training_data = np.array([[1, 1, 1], [2, 3, 1], [0, -1, 4], [0, 3, 0], [10, -6, 8], [-3, -12, 4]])
testing_data = np.array([6, 11, 1, 9, 10, -38])

training_data.shape

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units = 1, activation = tf.keras.activations.relu, input_shape = (3,)))
model.compile(optimizer = tf.keras.optimizers.RMSprop(0.001), loss = tf.keras.losses.mean_squared_error, metrics = [tf.keras.metrics.mean_squared_error])
model.summary()


model.fit(training_data, testing_data, epochs = 1, verbose = 'True')
print("Traning completed.")


a=model.predict(np.array([[1, 2, 1]]))
print(a) 