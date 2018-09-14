import tensorflow as tf

a = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
x = tf.Variable(tf.zeros([784, 10]))
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    b = sess.run(a)
    y = sess.run(x)
    print(b)
    print(x)