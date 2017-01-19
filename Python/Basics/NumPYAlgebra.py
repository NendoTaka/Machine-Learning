import tensorflow as tf
import numpy as np

x = np.random.randint(1000, size=10000)
y = tf.Variable(5*x**2 + 3*x + 15, name='y')

model = tf.global_variables_initializer()

session = tf.Session()

session.run(model)
print(session.run(y))
