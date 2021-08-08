import os
import datetime

class Logger:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        cwd = os.getcwd()
        path = os.path.abspath(os.path.join(cwd, 'board' ,'text', 'logger.txt'))
        if not os.path.exists(path):
            with open(path, encoding='utf-8', mode='w') as file:
                pass
        date = datetime.datetime.now().timetuple()
        time = ''.join([' time: ', str(date[3]), ':', str(date[4]), ':', str(date[5])])
        date = ''.join(['date: ', str(date[0]), '.', str(date[1]), '.', str(date[2])])
        method = ''.join([' method: ', request.method])
        url = ''.join([' url: ', ''.join([request.get_host(), request.get_full_path()])])
        data = ['\n', date, time, method, url]
        with open(path, encoding='utf-8', mode='a') as file:
            file.write(''.join([data[0], data[1], data[2], data[3], data[4]]))
        response = self.get_response(request)
        return response
