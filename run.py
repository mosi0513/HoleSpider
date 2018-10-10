from newcuet import NewCuteInput
from hotcuet import HotCuteInput
from jsl import  Input
import time





fscute = 'https://www.kashen.com/f-71.html'# 放水口子
newcute = 'https://www.kashen.com/f-2.html'# 最新口子



print('-'*50)
print('欢迎使用金时利爬虫程序   v1.00版')

time.sleep(6)
print('-'*50)

# 填入数据
print('更新文章首页-放水口子')
inputo1 = Input(fscute)
inputo1.login()
inputo1.close()

time.sleep(3)

print('更新文章首页-最新口子')
inputo2 = Input(newcute)
inputo2.login()
inputo2.close()

time.sleep(3)

print('更新最新口子')
newcu = NewCuteInput()
newcu.login()
newcu.close()

time.sleep(3)

print('更新热门口子')
hotcu = HotCuteInput()
hotcu.login()
hotcu.close()

time.sleep(3)

for x in range(100):
	print('已完成更新， 请关闭终端')
	time.sleep(1)


exit()