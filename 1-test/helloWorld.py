"""
helloWorld

A hello world sample using TensorFlow library.

"""

from __future__ import print_function

import tensorflow as tf

# Simple hello world using TensorFlow

# Create a Constant operator as a node to the default graph.
hello = tf.constant('Hello from TensorFlow!')

# Start a Tensorflow session
sess = tf.Session()

# Run the operator
print(sess.run(hello))

'''
End of file
'''