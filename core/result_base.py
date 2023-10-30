class ResultBase():

    def __init__(self, res) -> None:
        super().__init__()
        self.code = res.json()['code']
        if 'msg' in res.json():   # jiaqi: returned variable contain msg
            self.msg = res.json()['msg']
        self.time = res.elapsed.total_seconds()
        self.response = res
