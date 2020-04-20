def make_readable(seconds):    
    return ("{:02d}:{:02d}:{:02d}".format(seconds//3600, (seconds%3600)//60, (seconds%3600)%60))
