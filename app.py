import streamlit as st
import pandas as pd
import sys
import base64
import numpy as np
from sklearn.cluster import KMeans
import os
import socket

st.title('欢迎使用基于数据挖掘技术的学生成绩分析系统')
st.header('负责人：南昌航空大学18208144-羊绍平')
st.write('联系qq：1046901023')
file = st.file_uploader("点击下方上传南昌航空大学(xxxx级成绩列表.csv)文件")
jishu = ''
if file is not None:
    jishu = file.name[0:5]

def DataProcess(file):
    data = pd.read_csv(file,encoding='gbk')
    data.to_csv(jishu+'成绩列表.csv', index=False, encoding='gbk')
    # print(data.isnull().sum().sort_values(ascending=True))  # 统计空值
    # print(data[data['总成绩'].isnull()]['课程编号'])# 经查看只有两个科目因为系统原因重修没有录分数
    data.fillna(0,inplace=True)#用0填充空值
    # print(data['总成绩'].unique())#经查看，成绩里有优良中差等级。
    for i in range(len(data['总成绩'])):  # 将优、中、良、及格、差转换化为90、75、65、60、45
        if data['总成绩'].values[i] == '良':
            data['总成绩'].values[i] = 65
        elif data['总成绩'].values[i] == '及格':
            data['总成绩'].values[i] = 60
        elif data['总成绩'].values[i] == '中':
            data['总成绩'].values[i] = 75
        elif data['总成绩'].values[i] == '差':
            data['总成绩'].values[i] = 45
        elif data['总成绩'].values[i] == '优':
            data['总成绩'].values[i] = 90
    # c = pd.merge(a,b,on='课程编号')
    # print(data.isnull().sum().sort_values(ascending=True))
    a = pd.DataFrame(data,columns=['学号','课程编号','总成绩'])
    # print(a.dtypes)
    a['学号'] = a['学号'].astype(str)
    # print(a.dtypes)
    a.to_csv(jishu+'大表.csv', index=False, encoding='gbk')
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data6 = []
    data7 = []
    data8 = []
    data9 = []
    for i in range(len(a.index)):
        # print(a['学号'][i][4]=='1')
        if a['学号'][i][4]=='1':
            data1.append(a.loc[i])
        elif a['学号'][i][4]=='2':
            data2.append(a.loc[i])
        elif a['学号'][i][4]=='3':
            data3.append(a.loc[i])
        elif a['学号'][i][4]=='4':
            data4.append(a.loc[i])
        elif a['学号'][i][4]=='5':
            data5.append(a.loc[i])
        elif a['学号'][i][4]=='6':
            data6.append(a.loc[i])
        elif a['学号'][i][4]=='7':
            data7.append(a.loc[i])
        elif a['学号'][i][4]=='8':
            data8.append(a.loc[i])
        elif a['学号'][i][4]=='9':
            data9.append(a.loc[i])
    data1 = pd.DataFrame(data1)
    data2 = pd.DataFrame(data2)
    data3 = pd.DataFrame(data3)
    data4 = pd.DataFrame(data4)
    data5 = pd.DataFrame(data5)
    data6 = pd.DataFrame(data6)
    data7 = pd.DataFrame(data7)
    data8 = pd.DataFrame(data8)
    data9 = pd.DataFrame(data9)
    data1.to_csv(jishu+'1方向表.csv', index=False, encoding='gbk')
    data2.to_csv(jishu+'2方向表.csv', index=False, encoding='gbk')
    data3.to_csv(jishu+'3方向表.csv', index=False, encoding='gbk')
    data4.to_csv(jishu+'4方向表.csv', index=False, encoding='gbk')
    data5.to_csv(jishu+'5方向表.csv', index=False, encoding='gbk')
    data6.to_csv(jishu+'6方向表.csv', index=False, encoding='gbk')
    data7.to_csv(jishu+'7方向表.csv', index=False, encoding='gbk')
    data8.to_csv(jishu+'8方向表.csv', index=False, encoding='gbk')
    data9.to_csv(jishu+'9方向表.csv', index=False, encoding='gbk')
    st.success('已完成数据加工1，进度：12.5%')

def DataProcess1():
    for w in range(1,10):
        size = os.path.getsize(jishu + str(w)+'方向表.csv')
        if size >10:
            data1 = pd.read_csv(jishu + str(w) + '方向表.csv', encoding='gbk')
            a = pd.DataFrame(data1['学号'].unique())
            b = data1['课程编号'].unique()
            # print(d)
            columns = ['学号']
            for i in range(len(b)):
                a.loc[0, i + 1] = ''
                columns.append(b[i])
            a.columns = columns
            a.index = [a['学号']]
            # a.to_csv('test.csv', index=False, encoding='gbk')
            x = data1['学号'].unique()
            # df=data1[data1['学号']==11201106]
            # print(len(df))
            # print(len(df['课程编号'].unique()))
            # print(x)
            for id in x:
                df = data1[data1['学号'] == id]
                # print(df)
                # print(df['课程编号'])
                for cid in b:
                    # print(cid,pd.DataFrame(df['课程编号']))
                    if (cid in df['课程编号'].values):
                        df1 = df[df['课程编号'] == cid]
                        a.loc[id, cid] = df1['总成绩'].values[0]
                a.to_csv('test' + str(w) + '.csv', index=False, encoding='gbk')

    st.success('已完成数据加工2，进度：25%')

def DataProcess2():
    for w in range(1,10):
        if os.path.exists('test'+str(w)+'.csv'):
            data = pd.read_csv('test' + str(w) + '.csv', encoding='gbk')
            # print(data.isnull().sum().sort_values(ascending=True))  # 统计空值
            # print(data.isnull().sum()>len(data)/3)
            for i in data.columns:
                if data[i].isnull().sum() > len(data) / 2:
                    # print(i)
                    del data[i]  # 删除大于一半学生都没有的课
            for i in data.columns:
                data[i].fillna(data[i].mean(), inplace=True)  # 用均值填充缺失值
            data['平均分'] = 0  # 新增平均分列
            for i in range(len(data['学号'].values)):
                data1 = data.drop(['学号'], axis=1)
                data['平均分'][i] = data1.loc[i].mean()
                # print(data1.loc[i].mean())
            data.to_csv(jishu + str(w) + '方向数据分析.csv', encoding='gbk', index=False)
            data1 = pd.DataFrame(data.corr())
            data1.to_csv(jishu + str(w) + '方向各科相关程度.csv', encoding='gbk')

    st.success('已完成数据加工3，给出每方向学科相关程度，进度：37.5%')

def FailRate():
    data = pd.read_csv(jishu+'大表.csv', encoding='gbk')
    data1 = pd.read_csv(jishu+'成绩列表.csv', encoding='gbk')
    a = data['课程编号'].unique()
    oldPrint = sys.stdout
    f = open(jishu+'挂科率.txt', "w+",encoding='gbk')
    sys.stdout = f
    for i in a:
        df = data[data['课程编号'] == i]['学号']
        df2 = data1[data1['课程编号'] == i]['课程名称'].values[0]
        # print(df2)
        df1 = df.unique()
        rate = (len(df) - len(df1)) / len(df)
        print('科目编号：' + i + ' 课程名称: ' + df2 + ' 该科的挂科率为' + str(rate))
    sys.stdout = oldPrint
    f.close()
    st.success('已完成挂科率计算，进度：50%')

def FailWarning():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('max_colwidth', 1000)
    np.set_printoptions(threshold=np.inf)
    for w in range(1,10):
        df = pd.read_csv(jishu + '成绩列表.csv', encoding='gbk')
        if os.path.exists(jishu + str(w) +'方向各科相关程度.csv'):
            oldPrint = sys.stdout
            f = open(jishu + str(w) + '方向挂科预警.txt', "w+", encoding='gbk')
            sys.stdout = f
            data1 = pd.read_csv(jishu + str(w) + '方向各科相关程度.csv', encoding='gbk')
            data1.index = data1.iloc[:, 0]
            list1 = ['']
            for v in data1.iloc[:, 0][1:-1]:
                list1.append(df[df['课程编号']==v]['课程名称'].values[0])
            list1.append('')
            col_name = data1.columns.tolist()
            col_name.insert(1,'课程名称')
            data1 = data1.reindex(columns=col_name)
            data1['课程名称'] = list1
            data = pd.read_csv(jishu + str(w) + '方向数据分析.csv', encoding='gbk')
            print('以下同学你的平均分小于等于65分,具有很大的挂科风险，请继续努力！！')
            for e in data[data['平均分'] <= 65]['学号'].values:
                b = df[df['学号']==e]['姓名'].values[0]
                print(e,b)
            print('\n')
            for i in data.columns[1:-1]:
                print('以下学生，你们的该科目分数小于等于65,课程编号:' + i + ' 课程名称:' + df[df['课程编号'] == i]['课程名称'].values[0])
                for g in data[data[i] <= 65]['学号'].values:
                    h = df[df['学号']==g]['姓名'].values[0]
                    print(g,h)
                print('预警人数：',data[data[i] <= 65]['学号'].count())
                print('该科目与其他科目的相关程度为：')
                print(pd.DataFrame(data1,columns=['课程名称',i])[1:-1])
                print('请继续努力！！')
                print('\n')
            sys.stdout = oldPrint
            f.close()

    st.success('已完成每方向挂科预警，进度：62.5%')

def DegreeAndRepeaterWarning():
    data = pd.read_csv(jishu+'成绩列表.csv', encoding='gbk')
#     print(data[data['总成绩'].isnull()]['课程编号'])  # 经查看只有两个科目因为系统原因重修没有录分数
    data.fillna(0, inplace=True)  # 用0填充空值
    print(data['总成绩'].unique())  # 经查看，成绩里有优良中差等级。
    for i in range(len(data['总成绩'])):  # 将优、中、良、及格、差转换化为90、75、65、60、45
        if data['总成绩'].values[i] == '良':
            data['总成绩'].values[i] = 65
        elif data['总成绩'].values[i] == '及格':
            data['总成绩'].values[i] = 60
        elif data['总成绩'].values[i] == '中':
            data['总成绩'].values[i] = 75
        elif data['总成绩'].values[i] == '差':
            data['总成绩'].values[i] = 45
        elif data['总成绩'].values[i] == '优':
            data['总成绩'].values[i] = 90
    data['总成绩'] = data['总成绩'].astype(float)
    data1 = data[data['总成绩'].values < 60]
    # data1.to_csv('xxx1.csv',encoding='gbk')
    df = data1['学号'].unique()
    # print(df)
    oldPrint = sys.stdout
    f = open(jishu+'学位与留级预警.txt',"w+", encoding='gbk')
    sys.stdout = f
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('max_colwidth', 1000)
    np.set_printoptions(threshold=np.inf)
    for i in df:
        a = pd.DataFrame(columns=data.columns)
        df1 = data1[data1['学号'] == i]
        df1 = df1[df1['课程属性'] != '选修']
        df2 = df1.drop_duplicates(subset=['课程编号'])
        df3 = df1['课程编号'].unique()
        print('学号：' + str(i) + '你的挂科科目有：')
        dd = pd.DataFrame(df1, columns=['学号', '姓名', '课程编号', '课程名称', '学分', '总成绩','考试性质'])
        dd = pd.DataFrame(df1, columns=['学号', '姓名', '课程编号', '课程名称', '学分', '总成绩','考试性质'])
        dd[dd['考试性质'] == '正常考试']['考试性质'] = 0
        dd[dd['考试性质'] == '补考一']['考试性质'] = 1
        dd[dd['考试性质'] == '重修一']['考试性质'] = 2
        dd[dd['考试性质'] == '重修二']['考试性质'] = 3
        dd[dd['考试性质'] == '重修三']['考试性质'] = 4
        dd[dd['考试性质'] == '重修四']['考试性质'] = 5
        dd = dd.sort_values(by=['课程编号','考试性质'])
        dd[dd['考试性质'] == 0]['考试性质'] = '正常考试'
        dd[dd['考试性质'] == 1]['考试性质'] = '补考一'
        dd[dd['考试性质'] == 2]['考试性质'] = '重修一'
        dd[dd['考试性质'] == 3]['考试性质'] = '重修二'
        dd[dd['考试性质'] == 4]['考试性质'] = '重修三'
        dd[dd['考试性质'] == 5]['考试性质'] = '重修四'
        print(dd)
        x = sum(df2['学分'].values)
        print('累计所挂学分：' + str(x))
        for j in df3:
            df4 = data[data['学号'] == i]
            df5 = df4[df4['课程编号'] == j]
            df6 = df5[df5['总成绩'].values >= 60]
            a = a.append(df6)

        print('已过科目：')
        dd1 = pd.DataFrame(a, columns=['学号', '姓名', '课程编号', '课程名称', '学分', '总成绩','考试性质'])
        print(dd1.sort_values(by='课程编号'))
        print('累计已过学分：' + str(sum(a['学分'].values)))
        print('未过科目：')
        dd2 = dd
        for k in dd1['课程编号'].values:
            dd2 = dd2[dd2['课程编号']!=k]
        print(dd2.sort_values(by='课程编号'))
        print('未过学分：' + str(x - sum(a['学分'].values)))
        print('\n')

    sys.stdout = oldPrint
    f.close()
    st.success('已完成学位与留级预警，进度：75%')

def Kmeans():
    df = pd.read_csv(jishu + '成绩列表.csv', encoding='gbk')
    pd.reset_option('display.max_columns')
    # pd.reset_option('display.max_rows')
    # pd.reset_option('max_colwidth')
   
    for w in range(1,10):
        if os.path.exists(jishu + str(w) +'方向数据分析.csv'):
            data = pd.read_csv(jishu + str(w) + '方向数据分析.csv', encoding='gbk')
            center = 5
            if len(data)<5:
                center = len(data)
            myKmeans = KMeans(algorithm='auto', n_clusters=center, n_init=10)
            data1 = data.drop(['学号'], axis=1)
            # print(data1.head(6))
            myKmeans.fit(data1)
            y_Kmeans = myKmeans.predict(data1)
            # print(y_Kmeans)
            dataKmeans = pd.DataFrame(y_Kmeans)
            # print(dataKmeans.values)
            data.index = range(len(data))
            list2 = []
            for x in data['学号'].values:
                list2.append(df[df['学号']==x]['姓名'].values[0])
            col_name = data.columns.tolist()
            col_name.insert(1,'姓名')
            data.reindex(columns = col_name)
            data['姓名'] = list2
            oldPrint = sys.stdout
            f = open(jishu + str(w) + '方向聚类.txt', "w+", encoding='gbk')
            sys.stdout = f
            for i in range(center):
                ls = []
                ls.append(dataKmeans[dataKmeans.values == i].index)
                print('聚类', i)
                for j in ls:
                    print(data.loc[j])
            sys.stdout = oldPrint
            f.close()

    st.success('已完成每方向聚类，进度：87.5%')

def delete():
    for w in range(1,10):
        if os.path.exists(jishu+'大表.csv'):
            os.remove(jishu+'大表.csv')
        if os.path.exists(jishu+str(w)+'方向表.csv'):
            os.remove(jishu+str(w)+'方向表.csv')
        if os.path.exists(jishu+str(w)+'方向数据分析.csv'):
            os.remove(jishu+str(w)+'方向数据分析.csv')
        if os.path.exists('test'+str(w)+'.csv'):
            os.remove('test'+str(w)+'.csv')
    st.success('已完成中间过渡文件删除，进度100%')

def printfile():
    o = pd.read_table(jishu + '学位与留级预警.txt',encoding='gbk',index_col=False)
    st.write(jishu + '学位与留级预警',o)
    t = pd.read_table(jishu + '挂科率.txt',encoding='gbk')
    st.write(jishu + '挂科率',t)
    for w in range(1, 10):
        if os.path.exists(jishu + str(w) + '方向各科相关程度.csv'):
            l = pd.read_csv(jishu + str(w) + '方向各科相关程度.csv', encoding='gbk')
            st.write(jishu + str(w) + '方向各科相关程度',l)
        if os.path.exists(jishu + str(w) + '方向聚类.txt'):
            k = pd.read_table(jishu + str(w) + '方向聚类.txt', encoding='gbk',index_col=False)
            st.write( jishu + str(w) + '方向聚类',k)
        if os.path.exists(jishu + str(w) + '方向挂科预警.txt'):
            h = pd.read_table(jishu + str(w) + '方向挂科预警.txt', encoding='gbk')
            st.write(jishu + str(w) + '方向挂科预警',h)
#     l = pd.read_table(jishu + '学位与留级预警.txt',encoding='gbk')
#     st.write(jishu + '学位与留级预警',l)
#     k = pd.read_table(jishu + '挂科率.txt',encoding='gbk')
#     st.write(jishu + '挂科率',k)

def get_table_download_link(df,file_name):
    csv = df.to_csv(index=False,encoding='gbk')
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    return f'<a href="data:file/csv;base64,{b64}" download="{file_name}.csv">Download {file_name} file</a>'

if file is None:
    st.write('目前文件为空，请上传您需要处理的南昌航空大学(xxxx级成绩列表.csv)文件')
    st.write('© 2021南昌航空大学18208144-羊绍平')
if file is not None:
    DataProcess(file)
    DataProcess1()
    DataProcess2()
    FailRate()
    FailWarning()
    DegreeAndRepeaterWarning()
    Kmeans()
    delete()
    st.write('© 2021南昌航空大学18208144-羊绍平')
    printfile()
    for w in range(1,10):
        if os.path.exists(jishu + str(w) + '方向各科相关程度.csv'):
            data = pd.read_csv(jishu + str(w) + '方向各科相关程度.csv',encoding='gbk')
            st.markdown(get_table_download_link(data,jishu + str(w) + '方向各科相关程度'),unsafe_allow_html=True)

    
