import cv2
import os


def Picture_Taken(input_text):
    # 待提取视频的路径

    path = r'C:\01_AllDownloads\05_Projects\005_PyCharm\03_KeystoneForTest_2\attempt1\images'
    for i in os.listdir(path):
        path_file = os.path.join(path, i)
        if os.path.isfile(path_file):
            os.remove(path_file)



    input_text = str(input_text)
    # video_path = r"/Users/tianfenhua123/Desktop/1.mp4"
    video_path = r"C:\01_AllDownloads\05_Projects\005_PyCharm\03_KeystoneForTest_2\attempt1\videos/" + input_text + '.mp4'

    # 生成图片的路径
    img_path = r'C:\01_AllDownloads\05_Projects\005_PyCharm\03_KeystoneForTest_2\attempt1\images'

    # 生成img_path文件夹
    if not os.path.isdir(img_path):
        os.mkdir(img_path)

    # cv2.VideoCapture可以提取视频的第一帧，返回两个值：
    # 第一个是bool值，表示有没有提取到；第二个是对应的帧
    vidcap = cv2.VideoCapture(video_path)
    (cap, frame) = vidcap.read()

    if cap == False:
        result = 'cannot open video file'
        print('cannot open video file')
        return result
    count = 0

    result = ''

    # 将读取的帧对应的图片按顺序重命名为000000.jpg六位整数的格式，并写入img_path路径
    # 因为相邻帧可能过于相似，可以每隔几帧取一帧，由for循环完成
    # while cap and count<100:
    while cap:
        cv2.imwrite(os.path.join(img_path, '%.6d.jpg' % count), frame)
        print('%.6d.jpg' % count)
        result = result + str('%.6d.jpg' % count) + '\n'
        count += 1
        for i in range(5):
            (cap, frame) = vidcap.read()

    #result = 'Success!'

    return result
