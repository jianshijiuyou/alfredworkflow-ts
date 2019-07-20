#encoding: utf-8
import sys
from datetime import datetime
import time

from workflow import Workflow3

log = None

def ts2date(ts):
    try:
        dt = datetime.fromtimestamp(float(ts))
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        pass
    return ""

def date2ts(date):
    try:
        date = str(date).replace("\\","")
        datetime_object = datetime.strptime(date, '%Y-%m-%d %H:%M')
        return date_obj_ts(datetime_object)
    except Exception as e:
        pass
    return ""

def date_obj_ts(dt):
    return str(int(time.mktime(dt.timetuple())))

def default_data(wf):
    today = datetime.now()
    today_ts = date_obj_ts(today)
    wf.add_item(title=today_ts,
                    subtitle="当前时间戳",
                    arg=today_ts, 
                    valid=True)
    today_date = ts2date(today_ts)
    wf.add_item(title=today_date,
                    subtitle="当前日期",
                    arg=today_date, 
                    valid=True)
    # Send output to Alfred
    wf.send_feedback()

def main(wf):


    query = None
    title = ""
    subtitle = "回车复制内容"
    if len(wf.args):
        query = str(wf.args[0])

    if query == "-":
        default_data(wf)
        return
    elif len(query)==10:
        title = ts2date(query)
    else:
        title = date2ts(query)

    if title == "":
        title = "请输入正确的日期或时间戳格式"
        subtitle = "例: 2019-01-01 12:05 或者 1563604190"

    wf.add_item(title=title,
                    subtitle=subtitle,
                    arg=title, 
                    valid=True)
    # Send output to Alfred
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    # Assign Workflow logger to a global variable for convenience
    log = wf.logger
    sys.exit(wf.run(main))
