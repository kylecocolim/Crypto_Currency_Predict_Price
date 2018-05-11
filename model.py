import tensorflow as tf
import pandas as pd
import numpy as np
from build_data import *

def model(minutes,coinName,date):
    tf.set_random_seed(2018)
    tf.reset_default_graph()

    testX,testY = build_data.build_data(minutes,coinName,date)
    trainX ,trainY = build_data.build_data(minutes,coinName,"2018-04-03")
    trainX_2 ,trainY_2 = build_data.build_data(minutes,coinName,"2018-05-03")
    trainX_3 ,trainY_3 = build_data.build_data(minutes,coinName,"2018-02-03")

    # Hyper Parameter 21/02/18
    input_dim = 4  # input 4 , open, high , low , trade
    output_dim = 1  # output 1 , Close Price
    seq_length = 6  # sequence Length _ 10 min = 6, 1h - 6 = 6h , 1d - 15 = 15days
    hidden_dim = 20
    iterations = 10
    learning_rate = 0.01

    # input place holder
    X = tf.placeholder(tf.float32, [None, seq_length, input_dim])
    Y = tf.placeholder(tf.float32, [None, 1])

    cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_dim, state_is_tuple=True, activation=tf.nn.softsign)
    outputs, _states = tf.nn.dynamic_rnn(cell, X, dtype=tf.float32)
    Y_pred = tf.contrib.layers.fully_connected(outputs[:, -1], output_dim, activation_fn=tf.identity)
    # Fully Connect / Xavier , Relu Activation w : 20 b : 1 , output : 1

    optimizer = tf.train.AdamOptimizer(learning_rate)
    loss = tf.reduce_sum(tf.square(Y_pred - Y))
    train = optimizer.minimize(loss)

    # RMSE
    targets = tf.placeholder(tf.float32, [None, 1])
    predictions = tf.placeholder(tf.float32, [None, 1])
    rmse = tf.sqrt(tf.reduce_mean(tf.square(targets - predictions)))

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for i in range(iterations):
        if i % 3 == 0:
            _, step_loss = sess.run([train, loss], feed_dict={X: trainX, Y: trainY})
            print("[step: {}] loss: {}".format(i, step_loss))
        elif i % 3 == 1:
            _, step_loss = sess.run([train, loss], feed_dict={X: trainX_2, Y: trainY_2})
            print("[step: {}] loss: {}".format(i, step_loss))
        else:
            _, step_loss = sess.run([train, loss], feed_dict={X: trainX_3, Y: trainY_3})
            print("[step: {}] loss: {}".format(i, step_loss))

            # Test step
    test_predict = sess.run(Y_pred, feed_dict={X: testX, Y: testY})
    rmse_val = sess.run(rmse, feed_dict={targets: testY, predictions: test_predict})
    print("RMSE: {}".format(rmse_val))

    # inverse_transform

    test_Y = scaler_Y_test.inverse_transform(testY)
    test_predict = scaler_Y_test.inverse_transform(test_predict)
