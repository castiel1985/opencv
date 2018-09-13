# IPython log file

get_ipython().run_line_magic('logstart', '')
import tensorflow as tf
x = tf.Variable(3, name='x')
y = x * 5
sess = tf.IndexedSlices()
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())
sess.run(y)
print(x)
print(y)
sess.run(y)
a = tf.constant([1,2,3,4])
b = tf.square(a)
print(b)
with tf.Session as sess:
    ptint(sess.run(a))
    print(sess.run(b))
    
with tf.Session as sess:
    print(sess.run(a))
    print(sess.run(b))

        
print(a)
print(b)
with tf.Session() as sess:
    print(sess.run(a))
    print(sess.run(b))
    
with tf.Session() as sess:
    print(sess.run(a))
    print(sess.run(15))
    
    
v= tf.Variable(3, name="v")
print(v)
p= tf.Variable(3, name="k")
print(p)
w = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
print(w)
sess.run(w)
with tf.Session() as sess:
    print(sess.run(a))
    print(sess.run(w))
    
    
    
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(w)
    
    
    
    
w = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(w)
    
    
    
    
