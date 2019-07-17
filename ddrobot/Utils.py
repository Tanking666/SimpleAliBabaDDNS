from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


class CommonRequestSing:  # 私有类变量
    __request = None

    # 该修饰符将实例方法变成类方法
    # #,因为类方法无法操作私有的类变量，所以使用实例方法进行操作，再进行转换为类方法
    @classmethod
    def getInstance(self):
        if self.__request is None:
            self.__request = CommonRequest()
            return self.__request


class AcsClientSing:
    __client = None

    @classmethod
    def getInstance(self):
        if self.client is None:
            self.__client = AcsClient('LTAIc8YWfR2ROU2t', '7MXSBNpJxqqJHfLGmEUYbTZukswZEv', 'cn-hangzhou')
            return self.__client
