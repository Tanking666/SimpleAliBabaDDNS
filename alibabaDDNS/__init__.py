from aliyunsdkcore.request import CommonRequest
from aliyunsdkcore.client import AcsClient


def DDNS(ip):
    # 更改www解析
    client = AcsClient('LTAIc8YWfR2ROU2t', '7MXSBNpJxqqJHfLGmEUYbTZukswZEv', 'cn-hangzhou')
    request = CommonRequest()
    recordId = "your recordId"
    request.set_domain('alidns.aliyuncs.com')
    request.set_version('2015-01-09')
    request.set_action_name('UpdateDomainRecord')
    request.add_query_param('RecordId', recordId)
    request.add_query_param('RR', 'www')
    request.add_query_param('Type', 'A')
    request.add_query_param('Value', ip)
    client.do_action_with_exception(request)

    # 更改@解析
    request = CommonRequest()
    recordId = "17833809750340608"
    request.set_domain('alidns.aliyuncs.com')
    request.set_version('2015-01-09')
    request.set_action_name('UpdateDomainRecord')
    request.add_query_param('RecordId', recordId)
    request.add_query_param('RR', '@')
    request.add_query_param('Type', 'A')
    request.add_query_param('Value', ip)
    response = client.do_action_with_exception(request)
    return response
