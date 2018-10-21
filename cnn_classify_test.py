from skimage import io,transform
import tensorflow as tf
import numpy as np

#the path of pictures you want to recognize
path1 = ''
path2 = ''
path3 = ''
path4 = ''
path5 = ''

flower_dict = {0:'dasiy',1:'dandelion',2:'roses',3:'sunflowers',4:'tulips'}

w=100
h=100
c=3

def read_one_image(path):
    img = io.imread(path)
    img = transform.resize(img,(w,h))
    return np.asarray(img)

with tf.Session() as sess:
    data = []
    data1 = read_one_image(path1)
    data2 = read_one_image(path2)
    data3 = read_one_image(path3)
    data4 = read_one_image(path4)
    data5 = read_one_image(path5)
    data.append(data1)
    data.append(data2)
    data.append(data3)
    data.append(data4)
    data.append(data5)

    saver = tf.train.import_meta_graph('Users/duqinmei/flowers/model.ckpt.meta')
    saver.restore(sess,tf.train.latest_checkpoint('Users/duqinmei/flowers/'))

    graph = tf.get_default_graph()
    x = graph.get_tensor_by_name("x:0")
    feed_dict = {x:data}

    logits = graph.get_tensor_by_name("logits_eval:0")

    classification_result = sess.run(logits,feed_dict)

    print(classification_result)
    print(tf.argmax(classification_result,1).eval())
    output = []
    output = tf.argmax(classification_result,1).eval()
    for i in range(len(output)):
        print(i+1,"prediction:"+flower_dict[output[i]])
