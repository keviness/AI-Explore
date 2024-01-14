from gtts import gTTS
import os

# 函数功能: 用gtts库阅读文本,保存为.mp3文件后, 用系统内置的浏览器阅读出来, 打开mp3文件, 函数执行结束(播放方式为os库)
def gtts_os_debug(text,mp3_filepath,language):#参数说明:参数1是朗读的文字,参数2是保存路径,参数3是数字{0英文,1中文,2日语}
    #大成功,可惜的是os调用自带播放器, 实际上只执行了"打开mp3"的操作, 它并不会在音频播报完后再进行下一条语句

    # 已知zh-tw版本违和感较高,所以我们用zh-CN来进行后续工作
    if int(language) ==0 :
        s = gTTS(text=text, lang='en', tld='com')
        # s = gTTS(text=text, lang='en', tld='co.uk')#我比较喜欢美音,但是如果你喜欢英国口音可以尝试这个
    elif int(language) ==1 :
        s = gTTS(text=text, lang='zh-CN')
    elif int(language) ==2 :
        s = gTTS(text=text, lang='ja')
    try:
        s.save(mp3_filepath)
    except:
        os.remove(mp3_filepath)
        print(mp3_filepath,"文件已经存在,但是没有关系!已经删掉了")
        s.save(mp3_filepath)
    print(mp3_filepath,"保存成功")
    os.system(mp3_filepath)#调用系统自带的播放器播放MP3
gtts_os_debug(text="I'm gtts library,from google Artificial Intelligence & Google Translate.",mp3_filepath="gtts英文测试.mp3",language=0)
gtts_os_debug(text="我是gtts库, 你想听听我的声音吗",mp3_filepath="gtts中文测试.mp3",language=1)
gtts_os_debug(text="真実はいつもひとつ" ,mp3_filepath="gtts日语测试.mp3",language=2)
