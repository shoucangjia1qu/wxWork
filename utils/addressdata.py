__all__ =['Employee', 'Department', 'Tag']

# 员工类
class Employee(object):
    def __init__(self, token, userid, session):
        self.userid = -99
        self.get_employee(token, userid, session)

    def get_employee(self, token, userid, session):
        """
        保存员工userid, name, mobile, department, position, gender信息
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}"
        res = session.get(url)
        jsonres = res.json()
        self.errcode = jsonres['errcode']
        self.errmsg = jsonres['errmsg']
        # 调用失败的处理，只有成功了才保存userid
        if self.errcode != 0:
            print("Failed To Get Employee INFO !")
        else:
            self.userid = jsonres['userid']
            self.name = jsonres['name']
            self.mobile = jsonres['mobile']
            self.department = jsonres['department']
            self.position = jsonres['position']
            self.gender = jsonres['gender']
            print("Get Employee INFO Successed !")
        return


# 部门类
class Department(object):
    """
    保存部门ID的信息（包括下面的子部门信息）
    保存部门ID里面的员工信息（包括下面的子部门的员工），可选择是否详情数据（默认详情）
    """
    def __init__(self, token, departmentid, session, detail=True):
        self.departmentid = -99
        self.departmentList = self.get_departmentList(token, departmentid, session)
        self.employeeList = self.get_employeeList(token, self.departmentid, session, detail)

    def get_departmentList(self, token, departmentid, session):
        """
        保存部门的id, name, parentid, order信息
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={token}&id={departmentid}"
        res = session.get(url)
        jsonres = res.json()
        self.errcode_dpt = jsonres['errcode']
        self.errmsg_dpt = jsonres['errmsg']
        departmentList = jsonres['department']
        # 调用失败的处理，只有成功了才保存departmengid
        if self.errcode_dpt != 0:
            print("Failed To Get Department List !")
        else:
            self.departmentid = departmentid if departmentid != "" else 1
            print("Get Department List Successed !")
        return departmentList

    def get_employeeList(self, token, departmentid, session, detail=True):
        """
        保存部门的员工信息，有详情和非详情两种模式。
        详情：userid, name, mobile, department, position, gender, email, is_leader_in_dept等等信息
        非详情：userid, name, department, open_userid
        """
        if detail == True:
            url = f"https://qyapi.weixin.qq.com/cgi-bin/user/list?access_token={token}&department_id={departmentid}&fetch_child=1"
        else:
            url = f"https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token={token}&department_id={departmentid}&fetch_child=1"
        res = session.get(url)
        jsonres = res.json()
        self.errcode_user = jsonres['errcode']
        self.errmsg_user = jsonres['errmsg']
        userList = jsonres['userlist']
        # 调用失败的处理
        if self.errcode_user != 0:
            print("Failed To Get Department Employee !")
        else:
            print("Get Department Employee Successed !")
        return userList


#标签类
class Tag(object):
    """
    保存标签ID的标签信息、员工信息等
    """
    def __init__(self, token, tagid, session):
        self.tagid = -99
        self.employeeList = self.get_employeeList(token, tagid, session)

    def get_employeeList(self, token, tagid, session):
        """
        保存标签信息：tagname
        保存部门的员工信息：userid, name, department, open_userid
        保存标签中的部门信息：partylist
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token={token}&tagid={tagid}"
        res = session.get(url)
        jsonres = res.json()
        self.errcode = jsonres['errcode']
        self.errmsg = jsonres['errmsg']
        self.partylist = jsonres['partylist']
        userList = jsonres['userlist']
        # 调用失败的处理，只有成功了才保存tagid
        if self.errcode != 0:
            print("Failed To Get Tag Employee !")
        else:
            self.tagid = tagid
            print("Get Tag Employee Successed !")
        return userList






