from selenium import webdriver as wd
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as DC
dcap = dict(DC.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87"
)
class MyPhantomJS(wd.PhantomJS):
    def __init__(self,**args):
        wd.PhantomJS.__init__(self,desired_capabilities=dcap,**args)
        self.set_window_size(1024,768)

    