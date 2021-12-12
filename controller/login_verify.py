from Dao.AdminMapper import login

def login_verify(username, password):
    errMessage = ""
    result = False
    if len(username) == 0:
        errMessage = errMessage + "用户名不能为空！"
    elif len(password) == 0:
        errMessage = errMessage + "密码不能为空！"
    else:
        result = login(username, password)

    if result == True:
        errMessage = errMessage + "登录成功"
    else:
        errMessage = errMessage + "用户名或密码错误"
    return errMessage