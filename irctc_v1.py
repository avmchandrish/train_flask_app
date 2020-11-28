#!/usr/bin/env python
# coding: utf-8

# In[1]:

def run_crawls(fr, to, dt):
    import time
    st=time.time()
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.keys import Keys
    #from selenium.webdriver.support import expected_conditions as EC
    #from selenium.webdriver.support.ui import WebDriverWait
    import pandas as pd
    import time
    import datetime
    import json
    import os
    import warnings
    warnings.filterwarnings('ignore')        

    # In[2]:


    #os.chdir('C:\\Users\\hp\\Desktop\\My Projects\\IRCTC Availability')

    if os.path.exists('test4.csv'): 
        os.remove('test4.csv')

    # In[3]:


    
    chrome_options = Options()
    if os.environ.get("GOOGLE_CHROME_BIN"):
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.headless=True
    if os.environ.get("CHROMEDRIVER_PATH"):
        driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options) 
    else:
        driver=webdriver.Chrome(options=chrome_options)
    #wait=WebDriverWait
    # In[4]:


    #inputs
    #fr='VISAKHAPATNAM - VSKP'
    #to='BHUBANESWAR - BBS'
    #dt='14-11-2020'


    # In[5]:

    driver.get('https://rail-api-1809.herokuapp.com/')
    txt = driver.find_element_by_tag_name('h1').text
    return txt


    # driver.get('https://www.irctc.co.in/nget/train-search')
    # #click ok of popup
    # driver.find_element_by_css_selector('button.btn').click()
    # #time.sleep(2)

    # #clear the fields 
    # driver.find_element_by_id('origin').find_element_by_tag_name('input').clear()
    # driver.find_element_by_id('destination').find_element_by_tag_name('input').clear()

    # #time.sleep(0.5)
    # #input origin and destination
    # driver.find_element_by_id('origin').find_element_by_tag_name('input').send_keys(fr)
    # driver.find_element_by_id('destination').find_element_by_tag_name('input').send_keys(to)

    # driver.find_element_by_tag_name('p-calendar').find_element_by_tag_name('input').send_keys(dt)
    # driver.find_element_by_tag_name('p-calendar').find_element_by_tag_name('input').clear()
    # driver.find_element_by_tag_name('p-calendar').find_element_by_tag_name('input').send_keys(dt)
    # driver.find_element_by_css_selector('button.ui-datepicker-trigger').click()

    # #click ok of popup
    # driver.find_elements_by_css_selector('label.css-label_c')[0].click()
    # driver.find_elements_by_css_selector('button.search_btn')[1].click()


    # # In[6]:


    # def extract_info(i, k, cls):
    #     #driver.implicitly_wait(1)
    #     #getting the common attributes
    #     #print(trains[i].text)
    #     route=trains[i].text.split('\n')[1]
    #     t_name=trains[i].text.split('\n')[0]
    #     t_dep=trains[i].text.split('\n')[4]
    #     t_arr=trains[i].text.split('\n')[6]
    #     com_arr=[route, t_name, t_dep, t_arr, cls]
        
    #     #scroll to the end
    #     html = driver.find_element_by_tag_name('html')
    #     html.send_keys(Keys.END)
        
    #     #getting the prices for different days shown in the panel
    #     #wait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ui-panel-' + str(k) + '-content')))       
    #     re=0
    #     while re<5: 
    #         try:
    #             av_text=driver.find_element_by_id('ui-panel-' + str(k) + '-content').text
    #             break
    #         except:
    #             driver.implicitly_wait(0.7)
    #         re=re+1
    #     k=k+1
    #     av_split=av_text.split('\n')
        
    #     #code for handling "regret"
    #     l=len(av_split)
    #     ind=0
    #     while ind<l:
    #         if av_split[ind]=='REGRET':
    #             av_split.insert(ind, '')
    #             ind=ind+2
    #             l=len(av_split)
    #         else:
    #             ind=ind+1
        
    #     #removing cnf_probablity
    #     av_split=[val for val in av_split if val!='CNF Probability']
    #     res=[[av_split[j], av_split[j+1], av_split[j+2]] for j in range(0,len(av_split),3)]
        
    #     #merge common and this
    #     for r in range(len(res)):
    #         res[r]=com_arr +res[r]
        
    #     #creating a dataframe
    #     df_avail=pd.DataFrame(res, columns=['route', 't_name', 't_dep', 't_arr', 'cls', 'dt', 'status', 'col1'])
        
    #     #writing the dataframe into a csv
    #     df_avail.to_csv('test4.csv', mode='a')


    # # In[7]:


    # #trains
    # trains=driver.find_elements_by_class_name('train_avl_enq_box')
    # while len(trains)==0:
    #     time.sleep(1)
    #     trains=driver.find_elements_by_class_name('train_avl_enq_box')
    # #blue clikable price boxes
    # chk_price=driver.find_elements_by_id('check-availability')


    # # In[8]:


    # k=0
    # for i in range(len(trains)):
    #     html = driver.find_element_by_tag_name('html')
    #     html.send_keys(Keys.END)
    #     cls=trains[i].find_element_by_css_selector('select.form-control').find_elements_by_tag_name('option')
    #     for cli in range(len(cls)):
    #         cls[cli].click()
    #         cls_name=cls[cli].text
    #         chk_price=driver.find_elements_by_id('check-availability')
    #         s=0
    #         while s<5:
    #             try:
    #                 chk_price[i].click()
    #                 break
    #             except:
    #                 time.sleep(2)
    #                 s=s+1
    #         #if len(driver.find_elements_by_id('corover-close-cb-btn'))>0:
    #         #driver.find_elements_by_id('corover-close-cb-btn')
    #         driver.implicitly_wait(1)
    #         extract_info(i,k,cls_name)
    #         k=k+1
    # driver.quit()


    # # In[9]:


    # df_train=pd.read_csv('test4.csv')
    # today=datetime.datetime.strptime(dt, '%d-%m-%Y')
    # req_dt=today.strftime('%d %b %Y ')+ today.strftime('(%a)').upper()

    # df_train1=df_train[df_train.dt==req_dt]
    # df_train1.drop(['Unnamed: 0'], axis=1, inplace=True)
    # df_train1=df_train1.drop_duplicates().reset_index(drop=True)
    # df_base=df_train1[['t_name', 't_dep', 't_arr']].drop_duplicates().reset_index(drop=True)

    # df_base['2S']=''
    # df_base['SL']=''
    # df_base['3A']=''
    # df_base['2A']=''
    # df_base['1A']=''


    # for (i, row) in df_base.iterrows():
    #     for (j, r) in df_train1.iterrows():
    #         if r.t_name==row.t_name and r.cls=='Second Sitting (2S)':
    #             row['2S']=r.status
    #         if r.t_name==row.t_name and r.cls=='Sleeper (SL)':
    #             row['SL']=r.status
    #         if r.t_name==row.t_name and r.cls=='AC 3 Tier (3A)':
    #             row['3A']=r.status
    #         if r.t_name==row.t_name and r.cls=='AC 2 Tier (2A)':
    #             row['2A']=r.status
    #         if r.t_name==row.t_name and r.cls=='AC First Class (1A)':
    #             row['1A']=r.status

    # jsn=json.loads(df_base.to_json(orient='records'))
    # return jsn

# In[10]:


# In[11]:


#import irctc_v1 as c


# In[12]:


#c.run_crawls('BHUBANESWAR - BBS', 'VISAKHAPATNAM - VSKP', '23-11-2020')

