# MIT License

# Copyright (c) 2023 Juan L. Gamella

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import torch
import torch.nn as nn
from datetime import datetime


class CNNLinearHead(nn.Module):
    def __init__(self, out_size, device="cpu"):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(3, 64, 3, 2, dilation=1),
            nn.ReLU(),
            nn.Conv2d(64, 128, 3, 2, dilation=1),
            nn.ReLU(),
            nn.MaxPool2d(3),
            nn.Conv2d(128, 128, 3, 2, dilation=1),
            nn.ReLU(),
            nn.Conv2d(128, 64, 1, 1, dilation=1),
            nn.ReLU(),
            nn.Conv2d(64, 3, 1, 1, dilation=1),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(27, 100),
            nn.ReLU(),
            nn.Linear(100, out_size),
        )
        self.device = device
        self.to(device)

    def forward(self, x):
        return self.net(x.to(self.device))

    def save(self, directory=None, path=None):
        if directory is not None:
            timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
            path = directory + f"model_{timestamp}.pkl"
        elif path is None:
            raise ValueError("Must provide either directory or path")
        torch.save(self.state_dict(), path)
        print(f'Saved model {model} to "{path}"')

    def load(self, path):
        self.load_state_dict(torch.load(path))


class MLP(nn.Module):
    def __init__(self, in_size, out_size, layer_sizes=[], device="cpu"):
        super().__init__()
        # Construct layers
        if len(layer_sizes) == 0:
            layers = [nn.Linear(in_size, out_size)]
        else:
            layers = []
            for i, s in enumerate(layer_sizes):
                if i == 0:
                    layers.append(nn.Linear(in_size, layer_sizes[0]))
                else:
                    layers.append(nn.Linear(layer_sizes[i - 1], s))
                layers.append(nn.ReLU())
            # Add output layer
            layers.append(nn.Linear(s, out_size))
        # Compose
        self.net = nn.Sequential(*layers)
        self.device = device
        self.to(device)

    def forward(self, x):
        return self.net(x.to(self.device))

    def save(self, directory=None, path=None):
        if directory is not None:
            timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
            path = directory + f"model_{timestamp}.pkl"
        elif path is None:
            raise ValueError("Must provide either directory or path")
        torch.save(self.state_dict(), path)
        print(f'Saved model {model} to "{path}"')

    def load(self, path):
        self.load_state_dict(torch.load(path))
