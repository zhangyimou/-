from selenium import webdriver
import time
from userdate import get_webinfo

def openBrowser():
    webdriver_handle = webdriver.Chrome()
    #webdriver_handle = webdriver.Firefox()
    return webdriver_handle

def openUrl(handle,url):
    handle.get(url)
    browser.maximize_window()
    time.sleep(2)
    #alter = handle.switch_to_alert()
    #alter.accept()

def findElement(d,arg):
    useEle = d.find_element_by_name(arg['userid'])
    pwdEle = d.find_element_by_name(arg['pwdid'])
    loginEle = d.find_element_by_class_name(arg['loginid'])
    return useEle,pwdEle,loginEle

def sendVals(eletuple,arg):
    listkey1 = ['uname','pwd']
    eletuple[0].send_keys('')
    eletuple[0].clear()
    time.sleep(1)
    eletuple[0].send_keys(arg[listkey1[0]])
    time.sleep(1)
    eletuple[1].clear()
    time.sleep(1)
    eletuple[1].send_keys(arg[listkey1[1]])
    eletuple[2].click()

def login_test(ele_dict):
    #browser = openBrowser()
    openUrl(browser,ele_dict['url'])
    ele_tuple = findElement(browser,ele_dict)
    sendVals(ele_tuple,ele_dict)

def inquire_task(d):
    ele_tasklist = d.find_element_by_xpath('//*[@id="layoutAll"]/div[2]/section/div/div/div[1]/div[1]/ul/a[4]').click()
    ele_new_task = d.find_elements_by_class_name('listTableCont.el-row')
    a = ele_new_task[0].text
    text = a.split( )
    i = 0
    for line in text:
        i = i+1
    dict = {'ID':text[0],'任务名':text[1],'创建时间':[text[2],text[3]],'工艺模板':text[4],'任务状态':text[i-3]}
    print (dict)
    return dict

if __name__=='__main__':
    url = 'http://192.168.1.76:2020/operate/index.html#/login'
    account = 'admin'
    pwd = 'admin'
    ele_dict = {'url':url,'userid': 'username', 'pwdid': 'password', 'loginid': 'el-button',\
                'uname': account, 'pwd': pwd}
    ele_dict1 = get_webinfo(r'E:\zidonghua\webinfo.txt')
    browser = openBrowser()
    login_test(ele_dict)
    time.sleep(1)
    inquire_task(browser)






