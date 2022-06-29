import argparse
import os # 운영체제 상에서 제공되는 기능들을 파이썬에서 사용하기 위해 사용
import sys # 
from pathlib import Path

import torch
import torch.backends.cudnn as cudnn

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))

from models.common import DetectMultiBackend # yolov5에 만들어져있는 models 모듈
from utils.dataloaders import IMG_FORMAT, VID_FORMATS, LoadImages, LoadStreams
from utils.general import (Logger, check_file, check_img_size, check_imshow)