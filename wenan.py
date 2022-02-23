# -*- coding:utf-8 -*-

studyTextList = """
支路电流分析法\n节点电压分析法\n网孔电流分析法\n回路电流分析法\n叠加定理\n替代定理\n戴维南定理\n诺顿定理\n电容元件\n电感元件\n零输入与零状态响应\n全响应\n三要素法\n正弦量三要素\n同频率正弦量的相位差\n正弦电压和正弦电流的有效值\n同频率正弦量的向量表示\n基尔霍夫定律的向量形式\n电阻、电感和电容的电压向量与电流向量的关系\n阻抗和导纳\n正弦稳态电路分析、向量分析\n正弦稳态电路的功率\n最大功率传输定理\n谐振电路\n半导体基本知识\nPN结形成及其特性\n半导体二极管\n半导体二极管应用电路分析方法\n特殊二极管\n基本共射放大电路\nBJT放大电路分析方法\nBJT放大电路静态工作点稳定\n共基和共集放大电路\nBJT多级放大电路\n集成运算放大器\n理想运算放大器\n基本线性运算\n同相输入和反相输入放大电路的其它应用\n加法运算电路与减法运算电路\n单门限比较器\n逻辑代数运算\n逻辑代数定理\n逻辑函数的表示方法及化简\n二极管、三极管和MOS管的开关条件\n基本逻辑门的功能和符号\n正逻辑和负逻辑\nTTL反相器（非门）的电路结构和工作原理\nTTL逻辑门电路的各种技术参数\nOC门及线与\nCMOS反相器的电路结构和传输特性\nCMOS与非门、CMOS或非门的电路结构\nCMOS传输门的电路结构和工作原理\n组合逻辑电路的分析和设计流程\n组合逻辑电路的设计\n分析给定逻辑图的逻辑功能\nRS触发器\nJK触发器\nD触发器\n触发器转换\n时序电路的输出方程、驱动房产和状态方程\n同步时序逻辑电路的分析\n同步二进制计数器\n同步十进制计数器\nR-2R倒T网络构成的D/A转换的原理电路\n权电流电阻网络构成的D/A转换的原理电路\nD/A转换器的主要技术指标\nA/D转换过程中的取样、保持、量化与编码\n并行比较器、逐次比较型和双积分型A/D转换器工作原理\nA/D转换器的主要技术指标"""

#处理内容
studyList = studyTextList.split("\n") #分割 studyList
studyListlen = len(studyList)# 求 studyList 的长

# 随机数生成器
import random
randNumList = list()
randomNum = random.randint(7,13)

for randomLine in range(randomNum):
    key = True
    while(key):
        randNumListNum = random.randint(0,studyListlen)
        randNumListNum
        if not randNumListNum in randNumList:
            randNumList.append(randNumListNum)
        key = False

# 打印答案模式
countNum = 0
print("今天我学习如下内容：")
for printText in randNumList:
    countNum += 1
    print("{}、{}".format(countNum,studyList[printText]))

while True:
    a=1
