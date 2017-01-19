import tensorflow as tf

x = tf.constant([35, 40, 45], name='x')
y = tf.Variable(x + 5, name='y')

model = tf.global_variables_initializer()

session = tf.Session()

session.run(model)
print(session.run(y))
