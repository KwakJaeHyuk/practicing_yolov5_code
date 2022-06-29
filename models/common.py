import torch.nn as nn
import torch

def autopad(k, p=None): # kernel, padding 자동으로 패딩을 진행해주는 함수
    if p is None:
        if isinstance(k, int): 
            p = k // 2 
        else:
            [x // 2 for x in k]
    return p



class Conv(nn.Module):
    def __init__(self, c1, c2, k=1, s=1,p=None, g=1, act=True):
        super().__init__() # 이전에 가지고 있던 class의 정보를 얻는다.(class의 상속, 따라서 계속 새로운 convolution layer를 업데이트 한다.)
        self.conv = nn.Conv2d(c1, c2, k, s, autopad(k, p), groups=g, bias=False)
        self.bn = nn.BatchNorm2d(c2)
        self.act = nn.SiLU() if act is True else (act if isinstance(act, nn.Module) else nn.Identity())

    def forward(self, x):
        return self.act(self.bn(self.conv(x)))

    def forward_fuse(self, x):
        return self.act(self.conv(x))


class DetectMultiBackend(nn.Module): # 306
    def __init__(self, weights='yolov5s.pt', device=torch.device('cpu'), dnn=False, data=None, fp16=False):
        from models.experimental # models에서 작성중
