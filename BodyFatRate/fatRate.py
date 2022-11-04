# BMI = 体重（kg） / (身高（米） * 身高（米）)
# 体脂率 = （1.2 * BMI + 0.23 * 年龄 - 5.4 - 10.8 * 性别（男：1，女：0））/ 100
# 体脂率范围： 男 15% - 18% ，女 25% - 28%

class Persion :

    def get_body_fat_rate(name,sex,age,height,weight):
        # 计算 处理数据
        BMI = weight / (height * height)
        Body_fat = (1.2 * BMI + 0.23 * age - 5.4 - 10.8 * sex) / 100
        Body_fat = round(Body_fat,2)
        # 输出数据
        normal_body_fat = ((0.25,0.28),(0.15,0.18))
        min_body_fat,max_body_fat = normal_body_fat[sex]

        result = "正常"
        if Body_fat > max_body_fat:
            result = "偏重"
        elif Body_fat < min_body_fat:
            result = "偏瘦"
        result_notice = "{}你好，你的体脂率结果是:{}, 体脂率正常范围是{}-{},测量结果:{}".format(name,Body_fat,min_body_fat,max_body_fat,result)
        return result_notice

        # 输入数据
    name = input("请输入你的姓名: ")
    sex  = input("请输入你的性别(男/女): ")
    sex = 1 if sex == "男" else 0
    age  = int(input("请输入你的年龄: "))
    height = float(input("请输入你的身高(m): "))
    weight = float(input("请输入你的体重(kg): "))

    result = get_body_fat_rate(name,sex,age,height,weight)
    print(result)