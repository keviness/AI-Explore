# 深度学习实战8-生活照片转化漫画照片应用

**文章目录**

**一、论文介绍**

**二、漫画图片生成原理**

**三、代码部分**

**四、生成效果**

### **一、论文介绍**

![](https://fjjwhjwd3p.feishu.cn/space/api/box/stream/download/asynccode/?code=YjA3NDZkZGYwNzJjNGU0MTM5Yjc2NjFkZTBiZmRmYzlfV2g2RjI0TER5cVhWR1lpdlM3YTVpTFpOcmY3c3JpQkRfVG9rZW46RFhyQmJIbVk4bzBEVHV4ZjJkamNpVUc2bmpLXzE3MDM5NDA1MjQ6MTcwMzk0NDEyNF9WNA)

![](https://fjjwhjwd3p.feishu.cn/space/api/box/stream/download/asynccode/?code=YzQzY2M1ZmExM2JmZWQzZTkzMzg0NWJmMGRiY2QzMDlfQlRack5MQzRNMEltTjJ5OFRDRGNKOU5pblpvVWZpR05fVG9rZW46SFlkNGJSYXhGbzFDdEV4d1RNSGN4RVpVbnVlXzE3MDM5NDA1MjQ6MTcwMzk0NDEyNF9WNA)

### 二、漫画图片生成原理

主要方法是构建一下生成模型框架，其中 xp 表示输入照片， xc 表示输入的卡通图像，图像通过Modeling网络层后，经过多个S-AdaIN层，输出 xp′ 和 xc′ ，其中 xp′和 xc′表示重建结果， y 表示漫画化的目标结果。

![](https://fjjwhjwd3p.feishu.cn/space/api/box/stream/download/asynccode/?code=OGM2MWI0ZjkwYjgwZTgyZjM0NTYxY2Q1NmJmNGMzN2NfQzlJVVEyekhIS0RIZ2tNbFI5aE5zNkJ3OEhIZTlLRjNfVG9rZW46VEszb2JCUGt1b1BidWh4S0ZoTmNZa09rblNlXzE3MDM5NDA1MjQ6MTcwMzk0NDEyNF9WNA)

图像生成的过程就是利用对抗神经网络原理构建。本模型是利用CartonRenderer自动编码器，模型网络将输入图像映射到特征空间。与Adain 6和MUNIT 7中使用的传统编码器不同，我们的建模网络将输入图像映射到多尺度特征空间，是单个固定比例要素空间的。CartonRenderer的参数优化部分是由四个S-AdaIN块组成，对应于特征模型。每个S-AdaIN块用于对齐相应的刻度。其过程还是相对复杂的。

![](https://fjjwhjwd3p.feishu.cn/space/api/box/stream/download/asynccode/?code=MWUzNGY3NDk1NzMwYWFhYWNmMGMyM2NkZjY2YTU0ODhfMzBFdG0xMzZTOE9POXBwTnlqQWlkcDBDRExOWFRIc2tfVG9rZW46S1lBYmJkTXMyb3dPOTF4eE81dWNURmNEbkFnXzE3MDM5NDA1MjQ6MTcwMzk0NDEyNF9WNA)

### 三，代码部分

快速开始：安装

pip install "modelscope[cv]" -f https://modelscope.oss-cn-beijing.aliyuncs.com/releases/repo.html

代码部分：

```COBOL
import cv2
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
 
img_cartoon = pipeline(Tasks.image_portrait_stylization,
                       model='damo/cv_unet_person-image-cartoon_compound-models',
                       device='cpu')
# 图像本地路径
img_path = 'input.png'
 
result = img_cartoon(img_path)
cv2.imwrite('result.png', result[OutputKeys.OUTPUT_IMG])
print('完成!')
```

### 四、生成效果

以下是风景图的漫画风格生成效果：

![](https://fjjwhjwd3p.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTM2Y2JjYjc2NWRhMGY1YTY1ZjcyYTk5NDAwMmFhMTlfcFphUUpIRkI1Qno2MnZjd0owaENwa0tqUXpoUncxQkVfVG9rZW46SXRqSmJNczhwb0ZRMWV4bGZORWNDVmx0blBnXzE3MDM5NDA1MjQ6MTcwMzk0NDEyNF9WNA)

![](https://fjjwhjwd3p.feishu.cn/space/api/box/stream/download/asynccode/?code=ODc3NWE5ZjZiZTZiMmNhOGY5MmIxZTZhYWM3YWQzMzBfVEZ1dGYxcEVMQmdVUVpjM01WNVI4dDJvZjd5VVp3UmhfVG9rZW46WWlzMWJ3czJTbzgzOXh4aEFJZ2NpV1pQbkQ5XzE3MDM5NDA1MjQ6MTcwMzk0NDEyNF9WNA)

以下是人物的漫画风格生成效果：效果还是挺好的

![](https://fjjwhjwd3p.feishu.cn/space/api/box/stream/download/asynccode/?code=OTVhZWM0MDFmOTgwYTUwMzAyYjcyNWM2NzVkZGM1YWNfaGU3RVJMRHRaclVCZ3RobVAxNk5uNlV5OVllcjN6RFlfVG9rZW46V1FJRmJuelB1b1hXSlF4VVFtQmNoRXA0bm1mXzE3MDM5NDA1MjQ6MTcwMzk0NDEyNF9WNA)
