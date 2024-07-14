from app.config import *


def authenticate(username, password):
    """
    根据用户名和密码进行认证验证
    返回值：(认证成功的用户ID, None) 或 (None, 错误消息)
    """
    with open(USER_FILE, 'r') as f:
        for line in f:
            user_data = line.strip().split(',')
            if len(user_data) == 3:
                user_id, stored_username, stored_password = user_data
                if stored_username == username and stored_password == password:
                    return user_id, None
    
    return None, '验证失败'