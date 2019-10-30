import itertools
import math
import json
import requests
import re
import time
def  register(account,password):
    url='http://api.revth.com/register'
    form_data = {
        "username": account,
         "password": password

    }

    headers = {}

    response = requests.post(url=url, headers=headers,data=form_data)

    print(response.text)
def rank():#排行榜

    url=' http://api.revth.com/rank'
    headers={}
    soup=requests.get(url,headers).text
    soup=json.loads(soup)
    #print(soup)
    return  soup
def history(token,id1):#历史战绩
    url='http://api.revth.com/history'
    headers={'X-Auth-Token':token}
    data= {"page": 1, "limit": 28, "player_id": id1}
    #x=json.dumps(data, ensure_ascii=False)
    soup=requests.request("GET",url,headers=headers,params=data).text
    soup = json.loads(soup)
    #print(soup)
    return soup

def gameend(token,id2):
    url='http://api.revth.com/history/'+str(id2)
    headers = {"X-Auth-Token": token}
    soup = requests.request("GET",url,headers=headers).text
    soup = json.loads(soup)
    #print(soup)
    return soup


def regiseterAndBind(username,password,student_number,student_password):#注册绑定

    url = 'http://api.revth.com/auth/register2'
    form_data = {

    "username":username,

    "password": password,

    "student_number": student_number,

    "student_password": student_password
   }

    headers = {

    "Content-Type": 'application/json',
    }

    response = requests.post(url=url, headers=headers, data=json.dumps(form_data))

    #print(response.text)
    p=re.compile('status":(.+?),')
    pid=p.findall(str(response.text))[0]
    return pid


def login(username,password):
    url = " http://api.revth.com/auth/login"
    data={
        'username':username,
        'password':password
    }
    json_data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json_data, headers=headers)
    #print(response.text)
    p1=re.compile('status":(.+?),')
    pid=p1.findall(response.text)[0]
    try:
        p=re.compile('token":"(.+?)"')
        token=p.findall(response.text)[0]
        p2 = re.compile('user_id":(.+?),')
        user_id = p2.findall(response.text)[0]
        return pid,token,user_id
    except IndexError:
       return pid

def gameopen(token):
    url = "http://api.revth.com/game/open"
    headers = {'x-auth-token': token}
    response = requests.request("POST", url, headers=headers)
    #print(response.text)
    dict_data = str(json.loads(response.text))
    #print(dict_data)
    p=re.compile("'id': (.+?),")
    id4=p.findall(dict_data)
    #print(id4)
    p=re.compile("card': '(.+?)'")
    card=p.findall(dict_data)[0]
    #print(card)
    id4.append(card)
    return id4
def PlayGame(data,token):
    card=['$2','$3','$4','$5','$6','$7','$8','$9','$10','$J','$Q','$K','$A','&2','&3','&4','&5','&6','&7','&8','&9','&10','&J','&Q','&K','&A','*2','*3','*4','*5','*6','*7','*8','*9','*10','*J','*Q','*K','*A','#2','#3','#4','#5','#6','#7','#8','#9','#10','#J','#Q','#K','#A']
    mycard = data[1].split(' ')
    id3 = int(data[0])
    othercard = list(set(card) - set(mycard))
    string = getjson(id3, getcard(mycard, othercard))
    submit(str(token), id3, string['card'])
    print(string)
    return string
#def submit()
def num(List):#将卡牌根据数字进行分类
    numlist=[[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for x in List :
        if x[1]=='J':
            numlist[9].append(x)
        elif x[1]=='Q':
            numlist[10].append(x)
        elif x[1]=='K':
            numlist[11].append(x)
        elif x[1] == 'A':
            numlist[12].append(x)
        else:
            numlist[int(x[1:])-2].append(x)
    return numlist
def color(List):#将卡牌根据花色进行分类
    colorlist=[[],[],[],[]]
    for x in List:
        if x[0]=='$':
            colorlist[0].append(x)
        elif x[0]=='&':
            colorlist[1].append(x)
        elif x[0]=='*':
            colorlist[2].append(x)
        elif x[0]=='#':
            colorlist[3].append(x)
    return colorlist
def com(list1):#组合
    z=[]
    for i in range(0,len(list1)-1):
        for j in range(i+1,len(list1)):
            x=[]
            x.append(list1[i])
            x.append(list1[j])
            z.append(x)
            del x
    return z
def f(list2):#排序
    x=num(list2)
    z=[]
    for y in x:
        z.extend(y)
    return z
def No1(list3):#连对
    x=num(list3)
    z=[]
    for i in range(0,12):
        if (len(x[i])>=2)and(len(x[i+1])>=2):
            for a in com(x[i]):
                A=a
                for b in com(x[i+1]):
                    B=b
                    c=[]
                    c.extend(A)
                    c.extend(B)
                    z.append(c)
                    del c
    return z
def No2(list4):#一对
    z=[]
    x=num(list4)
    for y in x:
        if len(y)==2:
            z.append(y)
    return z
def No3(list5):#三条
    z=[]
    x=num(list5)
    for y in x:
        if len(y)==3:
            z.append(y)
    return z
def No4(list6): #顺子
    z=[]
    x=num(list6)
    for i in range(0,9):
        y=[]
        if len(x[i])>0:
            for j in range(i,i+5):
                if len(x[j])==0:
                    i=j
                    break;
                else:
                    y.append(x[j])
            if len(y)==5:
                z.append(y)
        del y
    return z
def No5(list7):#同花
    x=color(list7)
    z=[]
    for y in x:
        if len(y)>=5:
           z.append(y)
    return z
def No6(list8):#炸弹
    x=num(list8)
    z=[]
    for y in x:
        if len(y)==4:
            z.append(y)
    return z
def No7(list9):#同花顺
    z=[]
    k=[]
    x=No5(list9)
    if x!=None:
        for y in x:
            k=No4(y)
            if(k!=None):
                for h in k:
                    z.append(h)
    return z
def func(n):#阶乘
    if n == 0 or n == 1:
        return 1
    else:
        return (n * func(n - 1))
def comb(x,y):#求组合数
    if(x>=y):
        return int(func(x)/(func(y)*func(x-y)))
    return 0;
def value0(list16):#后墩计算权值
 
    x=No7(list16)
    n9=len(x)#同花顺
    x=No6(list16)
    n8=len(x)*35#炸弹
    x=No3(list16)
    y=No2(list16)
    z=No6(list16)
    n7=(len(z)*comb(4,3)+len(x))*(len(y)+len(x)*comb(3,2)+len(z)*comb(4,2)-4)#葫芦
    x=No5(list16)
    n6=0
    for y in x:
        n6=n6+comb(len(y),5)
    n6=n6-n9#同花
    x=No4(list16)
    n5=0
    for y in x:
        i=1
        for z in y:
            i=i*len(z)
        n5=n5+i
    n5=n5-n9#顺子
    x=No3(list16)
    y=No6(list16)
    n4=len(x)*comb(36,2)+len(y)*comb(4,3)*comb(36,2)-n8-n7#三条
    x=No1(list16)
    n3_2=len(x)*comb(35,1)#连对
    x=No2(list16)
    y=No3(list16)
    z=No6(list16)
    n3_1=comb(len(x),2)+len(x)*len(y)*3+len(x)*len(z)*6+comb(len(y),2)*9+len(y)*len(z)*18+comb(len(z),2)*36
    n3_1=n3_1*35-n7-n3_2#两对
    n2=len(x)+len(y)*3+len(z)*6
    n2=0
    del z
    s=(n2+n3_1+n3_2+n4+n5+n6+n7+n8+n9)/1000
    z=[0/s,n2/s,(n3_1+n2)/s ,(n3_2+n3_1+n2)/s,(n4+n3_1+n3_2+n2)/s,(n5+n4+n3_2+n3_1+n2)/s,(n6+n5+n4+n3_1+n3_2+n2)/s,(n7+n6+n5+n4+n3_2+n3_1+n2)/s,(n8+n7+n6+n5+n4+n3_1+n3_2+n2)/s,(n9+n7+n6+n5+n4+n3_2+n3_1+n2)/s]#散牌、对子、两对、连对、三条、顺子、同花、葫芦、炸弹、同花顺
    return z
def value1(list10):#中墩计算权值
    x=No7(list10)
    n9=len(x)#同花顺
    n9=math.sqrt(n9)
    x=No6(list)
    n8=len(x)*35#炸弹
    n8=math.sqrt(n8)
    x=No3(list10)
    y=No2(list10)
    z=No6(list10)
    n7=(len(z)*comb(4,3)+len(x))*(len(y)+len(x)*comb(3,2)+len(z)*comb(4,2)-4)#葫芦
    n7=math.sqrt(n7)
    x=No5(list10)
    n6=0
    for y in x:
        n6=n6+comb(len(y),5)
    n6=n6-n9#同花
    n6=math.sqrt(n6)
    x=No4(list10)
    n5=0
    for y in x:
        i=1
        for z in y:
            i=i*len(z)
        n5=n5+i
    n5=n5-n9#顺子
    n5=math.sqrt(n5)
    x=No3(list10)
    y=No6(list10)
    n4=len(x)*comb(36,2)+len(y)*comb(4,3)*comb(36,2)-n8-n7#三条
    n4=math.sqrt(n4)
    x=No1(list10)
    n3_2=len(x)*comb(35,1)#连对
    n3_2=math.sqrt(n3_2)
    x=No2(list10)
    y=No3(list10)
    z=No6(list10)
    n3_1=comb(len(x),2)+len(x)*len(y)*3+len(x)*len(z)*6+comb(len(y),2)*9+len(y)*len(z)*18+comb(len(z),2)*36
    n3_1=n3_1*35-n7-n3_2#两对
    n3_1=math.sqrt(n3_1)
    n2=len(x)+len(y)*3+len(z)*6
    n2=n2*comb(37,3)-n3_2-n3_1-n4-n7-n8
    n2=math.sqrt(n2)
    del z
    s=(n2+n3_1+n3_2+n4+n5+n6+n7+n8+n9)/1000
    z=[0/s,n2/s,(n3_1+n2)/s ,(n3_2+n3_1+n2)/s,(n4+n3_1+n3_2+n2)/s,(n5+n4+n3_2+n3_1+n2)/s,(n6+n5+n4+n3_1+n3_2+n2)/s,(n7+n6+n5+n4+n3_2+n3_1+n2)/s,(n8+n7+n6+n5+n4+n3_1+n3_2+n2)/s,(n9+n7+n6+n5+n4+n3_2+n3_1+n2)/s]#散牌、对子、两对、连对、三条、顺子、同花、葫芦、炸弹、同花顺
    return z
def value2(list11):#前墩权值
    x=No3(list11)
    y=No6(list11)
    z=No2(list11)
    n3=len(x)+len(y)*4#三条
    n2=(len(z)+len(x)*3+len(y)*6)*37-n3#一对
    n1=comb(39,3)-n2-n3#散牌
    s=comb(39,3)/1000
    del z
    z=[n1/s,(n2+n1)/s,(n3+n2+n1)/s]
    return z
def max1(list12,n):#判断牌的大小
    x=num(list12)
    d=0
    len3=len(x)
    for i in range(0,len3):
        if len(x[i])==n:
            d=i+1
    return d
def grade(list13):#牌型分级
    if len(list13)==5:#中墩和后墩
        if(len(No7(list13))>0):
            return [9,max1(list13,1)]#同花顺
        elif len(No6(list13))>0:
            return [8,max1(list13,4)]#炸弹
        elif (len(No3(list13))==1)and (len(No2(list13))==1):
            return [7,max1(list13,3)]#葫芦
        elif (len(No5(list13))==1):
            return[6,max1(list13,1)]#同花
        elif (len(No4(list13))==1):
            return [5,max1(list13,1)]#顺子
        elif len(No3(list13))==1:
            return [4,max1(list13,3)]#三条
        elif len(No1(list13))==1:
            return [3,max1(list13,2)]#连对
        elif len(No2(list13))==2:
            return [2,max1(list13,2)]#两对
        elif len(No2(list13))==1:
            return [1,max1(list13,2)]#一对
        else:
            return [0,max1(list13,1)]#散牌
    elif len(list13)==3:#前墩
        if len(No3(list13))==1:
            return[4,max1(list13,3)]#三条
        elif len(No2(list13))==1:
            return[1,max1(list13,2)]#对子
        else:
            return[0,max1(list13,1)]#散牌
def sanshunzi(x,n,ok):
    l=x
    for i in range(0, 13-n):
        if (l[i] > 0 and ok == 1):
            for j in range(0, n):
                if (l[i + j] > 0):
                    l[i + j] -= 1
                else:
                    ok = 0
            break
    return [ok,l]
def special(card):
    x=num(card)
    y=color(card)
    ok=1
    for i in x:
        if len(i)!=1:
            ok=0
    if(ok==1):
        return card
    ok=0
    for i in range(9,len(x)):
        ok+=len(x[i])
    if(ok>=12):
        return card
    ok=1
    j=[5,5,3]
    k=0
    l=[]
    for i in y:
        l.append(len(i))
    del i
    len4=len(l)
    for i in range(0, len4):
        if ((k < 3) and (l[i] >= j[k])):
            l[i] -= j[k]
            k += 1
            if ((k < 3) and (l[i] >= j[k])):
                l[i] -= j[k]
                k += 1
    if(k==3):
        return card
    elif(k==2):
        len2=len(l)
        for i in range(0, len2):
            if ((k < 3) and (l[i] >= j[k])):
                l[i] -= j[k]
                k += 1
                if ((k < 3) and (l[i] >= j[k])):
                    l[i] -= j[k]
                    k += 1
    if (k==3):
        return card
    if(len(No6(card))==3):
        return card
    ok=1
    for i in range(0,7):
        if len(x[i])!=0:
            ok=0
    if(ok==1):
        return card
    ok =1
    for i in range(6,13):
        if(len(x[i])!=0):
            ok=0
    if(ok==1):
        return card
    if (len(y[0])+len(y[1])==13)or(len(y[2])+len(y[3])==13):
        return card
    i=len(No3(card))
    if(i==2):
        j=len(No2(card))+len(No6(card))*2
        if(j==3):
            return card
    elif(i==1):
        if(len(No6(card))>0):
            j=len(No2(card))+(len(No6(card))-1)*2
            if(j==3):
                return card
    if(len(No3(card))+len(No6(card))==4):
        return card
    if len(No2(card))+len(No3(card))+len(No6(card))*2==6:
        return card
    del l
    l=[]
    for i in x:
        l.append(len(i))
    ok1=1
    ok2=1
    ok3=1
    l1=sanshunzi(l,5,ok1)
    l1=sanshunzi(l1[1],5,l1[0])
    l1=sanshunzi(l1[1],3,l1[0])
    l2 = sanshunzi(l, 3, ok2)
    l2 = sanshunzi(l2[1], 5, l1[0])
    l2 = sanshunzi(l2[1], 5, l1[0])
    l3 = sanshunzi(l, 5, ok3)
    l3 = sanshunzi(l3[1], 3, l1[0])
    l3 = sanshunzi(l3[1], 5, l1[0])
    if(l1[0]or l2[0] or l3[0]):
        return card
    return 0
def value(list1,list2,n):#墩的权值
    if len(list1)==3:
        if(list2[0]==0):
            x= list1[0]*list2[1]/13
        elif(list2[0]==1):
            x= (list1[1]-list1[0])*list2[1]/13+list1[0]
        else:
            x= (list1[2]-list1[2])*list2[1]/13+list1[1]
    else:
        if(list2[0]==0):
            x= list1[0]*list2[1]/13
        else:
            x= (list1[list2[0]]-list1[list2[0]-1])*list2[1]/13+list1[list2[0]-1]
    if n==2:
        if(list2[0]==7):
            x=x*2
        elif list2[0]==8:
            x=x*8
        elif list2[0]==9:
            x=x*9
    elif n==3:
        if list2[0]==8:
            x=x*4
        elif list2[0]==9:
            x=x*5
    return x
def getcard(list1,list2):#出牌
    x1=tuple(list1)
    d=0
    v1=value0(list2)
    v2=value1(list2)
    v3=value2(list2)
    #print(v1,v2,v3)
    ca1=[]
    ca2=[]
    ca3=[]
    for i in itertools.combinations(x1, 5):#选后墩
        c1=list(i)
        vc1=grade(c1)
        x2=tuple(set(list1)-set(c1))
        if(vc1[0]>1):
            for j in itertools.combinations(x2,5):#选中墩前墩
                c2=list(j)
                vc2=grade(c2)
                c3=list(set(x2)-set(j))
                vc3=grade(c3)
                if((vc1[0]>vc2[0])and (vc2[0]>vc3[0]))or((vc1[0]==vc2[0])and( vc2[0]>vc3[0])and (vc1[1]>vc2[1]))or((vc1[0]>vc2[0])and (vc2[0]==vc3[0])and( vc2[1]>vc3[1]))or((vc1[0]==vc2[0])and (vc2[0]==vc3[0])and( vc1[1]>vc2[1])and (vc2[1]>vc3[1])):
                    m=value(v3,vc3,0)+value(v2,vc2,2)+value(v1,vc1,3)
                    a1=value(v3, vc3, 0)
                    a2=value(v2, vc2, 2)
                    a3=value(v1, vc1, 3)
                    if((a1>910)and (a2>880 )and(a3>980)):
                        m*=2
                    if ((a1>910)or (a2>880 )or(a3>980))and((value(v3,vc3,0)-910)*(value(v2,vc2,2)-880)*(value(v1,vc1,3)-975)<0):#放一水赢两水
                        m=m+650
                    elif((a1>910)or (a2>880 )or(a3>980))and((a1-820)*(a2-720)*(a3-940)<0):#不能赢时尽量不被打枪
                        m+=300
                        #print(m)
                    if m>d:
                        d=m
                        ca1=c1
                        ca2=c2
                        ca3=c3
    ca3=f(ca3)
    ca2=f(ca2)
    ca1=f(ca1)
    #print(grade(['*K', '*10', '#J', '$Q', '*9']))
    #print(value(v3, grade(['&3', '$4', '&8']), 0), value(v2, grade(['*K', '*10', '#J', '$Q', '*A']), 2), value(v1, grade(['$2', '#2', '*2', '*6', '$6']), 3))
    #print(value(v3,grade(ca3),0),value(v2,grade(ca2),2),value(v1,grade(ca1),3))
    return [ca3,ca2,ca1]
def getjson(id5,list14):#转化json格式
    z=['','','']
    len1=len(list14)
    for i in range(0,len1):
        for j in range(0,len1):
            z[i]=z[i]+list14[i][j]
            if(j!=len(list14[i])-1):
                z[i]=z[i]+' '
    data = {'id': id5, 'card':z}
    #string = json.dumps(data, ensure_ascii=False)
    return data
def submit(token,gid, mycard):
    header={
        'X-Auth-Token': token,
        'Content-Type':'application/json'
    }
    url = 'http://api.revth.com/game/submit'
    data = {
        'id':gid,
        'card':mycard
    }
    x = json.dumps(data, ensure_ascii=False)
    print(x)
    response = requests.request('POST', url,headers=header , data=x).text
    print(response)
card=['$2','$3','$4','$5','$6','$7','$8','$9','$10','$J','$Q','$K','$A','&2','&3','&4','&5','&6','&7','&8','&9','&10','&J','&Q','&K','&A','*2','*3','*4','*5','*6','*7','*8','*9','*10','*J','*Q','*K','*A','#2','#3','#4','#5','#6','#7','#8','#9','#10','#J','#Q','#K','#A']
if __name__ == '__main__':
    #t1=time.time()
    t=28
    '''
    try:
        pid,token = login('x', 'xxx')
    except ValueError:
        pid= login('x', 'xxx')
        exit()
    gameend(token, t)
    '''
    rank()
    while(1):
        rank()
        pid,token,user_id = login('xxx', 'xxx')
        data = gameend(token,t)
        print(data)
        #print(token)
        data = gameopen(token)
        #print(data)
        mycard = data[1].split(' ')
        id0 = int(data[0])
        # print(mycard)
        #mycard=random.sample(card,13)
        # mycard=['*6', '$2', '*10', '#2', '&8', '$Q', '$6', '*2', '$4', '*A', '&3', '*K', '#J']
        othercard = list(set(card) - set(mycard))
        x=special(mycard)
        if(x!=0):
            string=x[0]
            for i in range(1,13):
                string=string+' '+x[i]
            submit(str(token),id0,string)
        else:
            string = getjson(id0, getcard(mycard, othercard))
            #print(token,id,string['card'])
            submit(str(token),id0,string['card'])
        # print(mycard)
        #t2 = time.time()
        #print(t2 - t1)
        with open('历史对局.txt','a+')as a:
            a.write(str(id0))
            a.write('\n')
        gameend(token,t)
        t = id
        history(token,9)
        #print(string)
        time.sleep(15)
