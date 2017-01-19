import tensorflow as tf
import numpy as np

count = tf.Variable(0, name='count')
x = tf.Variable(0, name='x')

model = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(model)
    for i in range(5):
        count = count + 1
        data = np.random.randint(1000)
        y = np.average(data)
        x = x + y
        print(session.run(x/count))
