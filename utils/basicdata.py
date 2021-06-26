import time
from .addressdata import Department

__all__ =['Token', 'ApiIp', 'Corporation']

# access_token的类
class Token(object):
    """
    根据企业id和应用密钥获取token，以及其他信息，统一放到Token类里面。
    """
    def __init__(self, corpid, secret, session):
        self.session = session
        self.corpid = corpid
        self.secret = secret
        self.starttime = time.time()
        self.access_token, self.expires_in = self.get_token(corpid, secret, session)

    def get_token(self, corpid, secret, session):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={secret}"
        # session = requests.session()
        res = session.get(url)
        jsonres = res.json()
        self.errmsg = jsonres['errmsg']
        self.errcode = jsonres['errcode']
        # 调用失败的处理
        if jsonres['errcode'] != 0:
            token, expires_in = -99, -99
            print("Failed To Get Token !")
        else:
            token, expires_in = res.json()['access_token'], res.json()['expires_in']
            print("Get Token Successed !")
        return token, expires_in


# ApiIp类
class ApiIp(object):
    """
    根据有效token获取当前API的IP段
    """
    def __init__(self, token, session):
        self.session = session
        self.ipList = self.get_apiip(token, session)

    def get_apiip(self, token, session):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/get_api_domain_ip?access_token={token}"
        # session = requests.session()
        res = session.get(url)
        jsonres = res.json()
        self.errcode = jsonres['errcode']
        self.errmsg = jsonres['errmsg']
        # 调用失败的处理
        apiip = jsonres['ip_list']
        if self.errcode != 0:
            print("Failed To Get ApiIp !")
        else:
            print("Get Token Successed !")
        return apiip


#获取企业的整体信息，包括全部门信息、全标签信息、全员信息、全部群聊信息
class Corporation(Department):
    """
    储存公司全部门信息、全标签信息、[全员信息]。
    """
    def __init__(self, token, session):
        # 获取全部门信息、全员简单信息
        super(Corporation, self).__init__(token=token, departmentid="", session=session, detail=False)
        # 获取全部门信息
        # self.departmentListsimple = self.get_departmentList(token=token, departmentid="", session=session)
        # 获取全标签信息
        self.tagList = self.get_taglist(token=token, session=session)
        # 获取全部应用信息
        self.agentList = self.get_agentlist(token=token, session=session)

    def get_taglist(self, token, session):
        """
        获取全部的标签列表，包括id，name
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={token}"
        res = session.get(url)
        jsonres = res.json()
        self.errcode_tag = jsonres['errcode']
        self.errmsg_tag = jsonres['errmsg']
        tagList = jsonres['taglist']
        # 调用失败的处理
        if self.errcode_tag != 0:
            print("Failed To Get Tag List !")
        else:
            print("Get Tag List Successed !")
        return tagList

    def get_agentlist(self, token, session):
        """
        获取全部的应用列表，包括agentid, name, square_logo_url
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/agent/list?access_token={token}"
        res = session.get(url)
        jsonres = res.json()
        self.errcode_app = jsonres['errcode']
        self.errmsg_app = jsonres['errmsg']
        agentList = jsonres['agentlist']
        # 调用失败的处理
        if self.errcode_tag != 0:
            print("Failed To Get Agent List !")
        else:
            print("Get Agent List Successed !")
        return agentList


