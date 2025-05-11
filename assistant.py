


class Assistant:
    def __init__(self, show=False, tell=False):
        self.showing = show
        self.telling = tell
        if tell: 
            mixer.init()
        self.traffic_light_status = None
        
        
    def show(file,results, analyze):
        img = Analyzer.img
        cv2.imshow('driver', img)
    
    def tell(self, analyzed_results):
        analyzed_results = analyzed_results[0]
        if self.traffic_light_status == analyzed_results:
            return
        mixer.music.load(f'traffic_light_{analyzed_results}_alarm.mp3')
        mixer.music.play ()  
        self.traffic_light_status = analyzed_results
        return
    
    def help(self, results, analyzed_results):
        if self.telling:
            Assistant.tell(self,analyzed_results)
        if self.showing:
            Assistant.show(self,results, analyzed_results)