import torch.nn as nn
from core.model.blocks.resnet import ResNet, Bottleneck


class ResNet152(ResNet):
    def __init__(self, num_channels=1, num_classes=10):
        super(ResNet152, self).__init__(Bottleneck, [
            3, 8, 36, 3], num_channels, num_classes)
