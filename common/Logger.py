#coding:utf-8
import logging,os,time
#log_path 是存放日志的路径
current_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(current_path),'logs')
print(log_path)
#如果不存在这个logs文件夹就创建一个
if not os.path.exists(log_path):os.mkdir(log_path)

class Log():
    def __init__(self):
        '''文件命名'''
        self.logname = os.path.join(log_path,'%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        '''日志输出格式'''
        self.formatter = logging.Formatter('[%(asctime)s]- %(filename)s] - %(levelname)s: %(message)s')
    def __console(self,level,message):
        '''创建一个FileHandler，用于写到本地'''
        fh = logging.FileHandler(self.logname,'a',encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        # 创建一个 StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level== 'info':
            self.logger.info(message)
        elif level=='debug':
            self.logger.debug(message)
        elif level=='warning':
            self.logger.warning(message)
        elif level=='error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        #关闭打开的文件
        fh.close()
    def debug(self,message):
        self.__console('debug',message)
    def info(self,message):
        self.__console('info',message)
    def warning(self,message):
        self.__console('warning',message)
    def error(self,message):
        self.__console('error',message)



class   LogOutput():
    def logOutput(self,logpath):
        '''
        para log_dir 日志路径
        para name_Project
        '''
        now = time.strftime("%Y_%m_%d %H_%M_%S")
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=logpath + now + '.log',
                            filemode='w')
        logger = logging.getLogger()
        logger.info(self)


if __name__ == '__main__':
    log = Log()
    log.info('测试开始')
    log.info('操作步骤1 2 3')
    log.warning('测试结束')
