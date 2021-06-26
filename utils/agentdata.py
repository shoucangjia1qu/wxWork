class Agent(object):
    def __init__(self, token, agentid, session):
        self.agentid = -99
        self.get_agent(token, agentid, session)

    def get_agent(self, token, agentid, session):
        """
        保存应用agentid, name, square_logo_url, description等等信息
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/agent/get?access_token={token}&agentid={agentid}"
        res = session.get(url)
        jsonres = res.json()
        self.errcode = jsonres['errcode']
        self.errmsg = jsonres['errmsg']
        # 调用失败的处理，只有成功了才保存userid
        if self.errcode != 0:
            print("Failed To Get Agent INFO !")
        else:
            self.agentid = jsonres['agentid']
            self.name = jsonres['name']
            self.square_logo_url = jsonres['square_logo_url']
            self.description = jsonres['description']
            self.allow_userinfos = jsonres['allow_userinfos']
            self.allow_partys = jsonres['allow_partys']
            self.allow_tags = jsonres['allow_tags']
            self.close = jsonres['close']
            self.redirect_domain = jsonres['redirect_domain']
            self.report_location_flag = jsonres['report_location_flag']
            self.isreportenter = jsonres['isreportenter']
            self.home_url = jsonres['home_url']
            print("Get Agent INFO Successed !")
        return
