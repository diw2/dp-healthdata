from faker import Faker
import random
import csv
import codecs

##############
# first batch of Prenatal fake data: personal information
# 年龄，志愿者中心，民族，居住地，文化程度，职业，家庭人均月收入，医疗费用支付方式
# 所有elements取自国自科调查表
##############
def generateprenatalata(record):
    fake = Faker( locale='zh_CN' )
    headers = ["年龄", "志愿者中心","民族","居住地","文化程度","职业","家庭人均月收入","医疗费用支付方式"]
    with codecs.open("Prenatal_Data.csv", "w+", 'utf_8_sig') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for _ in range( record ):
            writer.writerow({
                "年龄": random.randint( 18, 40 ),
                "志愿者中心": fake.random_elements( elements=('渝北区妇幼保健院', '江津区妇幼保健院', '云阳县妇幼保健院', '黔江区妇幼保健院'), length=1, unique=False ),
                "民族": fake.random_elements( elements=('汉族', '回族', '土家族', '苗族', '藏族', '其他'), length=1, unique=False ),
                "居住地": fake.random_elements( elements=('城市', '农村'), length=1, unique=False ),
                "文化程度": fake.random_elements( elements=('小学及以下', '初中', '高中/职高/中专', '大专/本科', '硕士及以上'), length=1, unique=False ),
                "职业": fake.random_elements( elements=('机关、事业单位职工', '企业职员', '餐饮、销售等服务行业', '个体经营者', '农民', '家庭主妇', '无业或待业', '其他'),length=1, unique=False ),
                "家庭人均月收入":fake.random_elements(elements=('1000元以下', '1001～3000', '3001～5000', '5001～10000', '10001～15000', '15001以上'),length=1, unique=False ),
                "医疗费用支付方式": fake.random_elements( elements=('自费', '城镇职工基本医疗保险（含生育保险）', '城镇居民基本医疗保险（含民政救助）', '新型农村合作医疗（含民政救助）', '商业医疗保险', '其他'),length=1, unique=False )
            })


if __name__ == '__main__':
    #the amount of records going to be generated
    records = 50
    generateprenatalata( records )
    print( "CSV generated" )
