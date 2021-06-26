import utils as ut
import requests

corpid = ""
AgentId = 1000002
secret = ""


# 创建会话
session = requests.session()
# 获取该应用的Token类
Token = ut.Token(corpid, secret, session)
# 获取IP段
Apiip = ut.ApiIp(Token.access_token, session)
# 获取企业的信息
Cor = ut.Corporation(Token.access_token, session)



if __name__ == '__main__':
    print_hi('PyCharm')

