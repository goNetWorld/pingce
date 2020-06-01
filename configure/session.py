import hashlib,time
class Session:
    """自定义session"""

    info_container = {
        # session_id: {'user': info} --> 通过session保存用户信息，权限等
    }

    def __init__(self, handler):
        """
        初始化时传入RequestHandler对象，通过它进行cookie操作
        self.handler.set_cookie()
        self.handler.get_cookie()
        :param handler: 
        """
        self.handler = handler

        # 从 cookie 中获取作为 session_id 的随机字符串，如果没有或不匹配则生成 session_id
        random_str = self.handler.get_cookie('session_id')
        if (not random_str) or (random_str not in self.info_container):
            md = hashlib.md5("mySaltCode".encode("utf-8"))  # bytes
            md.update(str(time.time()).encode("utf-8"))  # encode
            re = md.hexdigest()
            random_str = re
            self.info_container[random_str] = {}
        self.random_str = random_str

        # 每次请求进来都会执行set_cookie，保证每次重置过期时间为当前时间以后xx秒以后
        self.handler.set_cookie('session_id', random_str, max_age=60)

    def __getitem__(self, item):
        return self.info_container[self.random_str].get(item)

    def __setitem__(self, key, value):
        self.info_container[self.random_str][key] = value

    def __delitem__(self, key):
        if self.info_container[self.random_str].get(key):
            del self.info_container[self.random_str][key]

    def delete(self):
        """从大字典删除session_id"""
        del self.info_container[self.random_str]