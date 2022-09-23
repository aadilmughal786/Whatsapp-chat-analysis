import re
import pandas as pd


def preprocess(data):
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': messages, 'dates': dates})

    # convert message_date type to datetype object
    df['dates'] = pd.to_datetime(
        df['dates'], format='%m/%d/%y, %H:%M - ')

    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:  # user name
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df = df[df['user'] != 'group_notification']
    df.drop(columns=['user_message'], inplace=True)
    df.loc[df["message"] == "<Media omitted>\n", "message"] = "Share Media"

    df['date'] = df['dates'].dt.date
    df['year'] = df['dates'].dt.year
    df['month_num'] = df['dates'].dt.month
    df['month'] = df['dates'].dt.month_name()
    df['day'] = df['dates'].dt.day
    df['day_name'] = df['dates'].dt.day_name()
    df['hour'] = df['dates'].dt.hour
    df['minute'] = df['dates'].dt.minute
    df.drop(columns=['dates'], inplace=True)

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))
    df['period'] = period

    return df
