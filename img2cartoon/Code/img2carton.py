import cv2
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
 
img_cartoon = pipeline(Tasks.image_portrait_stylization,
                       model='damo/cv_unet_person-image-cartoon_compound-models',
                       device='cpu')
# 图像本地路径
'''
img_path = 'input.png'
 
result = img_cartoon(img_path)
cv2.imwrite('result.png', result[OutputKeys.OUTPUT_IMG])
print('完成!')
'''