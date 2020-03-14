```mysql
    GRANT ALL PRIVILEGES ON marriage.* TO tianjin@"%" IDENTIFIED BY "TJ307440205";
```

### 接口文档
#### 首页接口


|接口名称| url | methods |描述|参数说明|
|--------|-----|-------|----|-----|
|导航栏根据id收搜|http://192.168.3.11:5000/front/wechat/search_id?uid=2| GET ||返回收搜的用户信息|
|根据性别进行收搜|http://192.168.3.11:5000/front/wechat/search_sex?sex=女|GET||返回同性别用户信息|



#### 详情页接口
|接口名称| url | methods |描述|参数说明|
|--------|-----|-------|----|-----|
|个人详情页|http://192.168.3.11:5000/front/personal/personal_details?uid=1|GET|返回个人详情信息|用户id|
|收藏|http://192.168.3.11:5000/front/personal/collect?id=5&cid=6|GET|收藏用户|用户id以及被收藏的用户cid|
|查看号码|http://192.168.3.11:5000/front/personal/search_phone?id=1&uid=4|GET|查看电话号码|用户id以及被收藏的用户cid|
|查看QQ|http://192.168.3.11:5000/front/personal/search_qq?id=1&uid=4|GET|查看qq号码|用户id以及被收藏的用户cid|
|查看微信|http://192.168.3.11:5000/front/personal/search_wx?id=1&uid=4|GET|查看微信号码|用户id以及被收藏的用户cid|


#### 个人中心接口文档
|接口名称| url | methods |描述|参数说明|
|--------|-----|-------|----|-----|
|查看过我电话的人|http://192.168.3.11:5000/front/personal/phone_list?id=7|GET|查看电话|用户id|
|查看过我微信的人|http://192.168.3.11:5000/front/personal/wx_list?id=7|GET|查看微信|用户id|
|查看过我QQ的人|http://192.168.3.11:5000/front/personal/qq_list?id=7|GET|查看QQ|用户id|