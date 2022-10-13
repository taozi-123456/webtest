"""
一条用例涉及的数据有url。data，check_sql

"""
import json
import re


from Common.handle_config import conf
class ENVData:
    """
    存储用例所需要的数据
    """
    pass

def clear_data():
    """
    清理数据
    :return:
    """
    values = dict(ENVData.__dict__.items())
    for key, value in values.items():
        if key.startswith("__"):
                pass
        else:
            delattr(ENVData, key)

def replace_case_by_regular(case):
    """
    对excle中，读取出来的整条测试用例做全部替换
    包括url data，prerwquests，check_sql
    :param case:
        :return:
        """
    # #把case字典（从excleu取出来的一条用力）转换成字符串
    case_str=json.dumps(case)
    # #替换
    new_case=replace_by_regular(case_str)
    # #把替换后的字符串，转化成字典
    case_dict=json.loads(new_case)
    return case_dict
    # for key,value in case.items():
    #     if value is not None and isinstance(value,str):#确保是个字符串
    #         case[key]=replace_by_regular(value)
    # return case


def replace_by_regular(data):
  """
  将字符串中，匹配#（。*？）# 部分，替换成真实的数据
  真实数据只从2个地方去获取#标识夫对应的是，来自于1.环境变量 2.配置文件
  :param data: 字符串
  :return: 返货的是替换之后的字符串
  """
  res = re.findall("#(.*?)#", data)

  # #标识夫对应的是，来自于1.环境变量的EvnData的类属性 2.配置文件的data区域
  if res:
    for item in res:
      # 得到标识符对应的值
       try:
         value = conf.get("data", item)
       except:
          try:
             value = getattr(ENVData, item)
          except AttributeError:
             continue
    # 再去替换原字符
       data = data.replace("#{}#".format(item),value)

    return data


def replace_markdata(case,mark,real_data):
    """
    遍历一个http请求用例设计道德所有数据，如果说每一个数据需要替换，都会替换
    :param case: excle当中读取处理啊一条数据，是个字典
    :param mark: 数据当中的占位符，
    :param real_data: 要替换mark的真实数据
    :return:
    """
    for key,value in case.items():
        if value is not None and isinstance(value,str):#确保是个字符串
            if value.find(mark) !=-1: #找到标识符
                case[key] =value.replace(mark,real_data)

    return case

if __name__ =='__main__':
    case = {
        "method": "POST",
        "url": "http://api.lemonban.com/futureloan/member/register",
        "data": '{"mobile_phone": "#phone#", "pwd": "12345678", "type": 0, "reg_name": "小yaoyao"}'
    }
    if case["data"].find("#phone#"):
        new_phone = get_new_phone()
        #    case["data"]=case["data"].repalce("#phone#",new_phone)
        #    case["check_sql"]=case["check_sql"].replace("#phone#",new_phone)
        case = replace_markdata(case, "#phone#", new_phone)

