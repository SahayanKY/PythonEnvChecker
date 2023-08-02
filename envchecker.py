def check():
    """
    実行環境をチェック
    """
    import socket
    import platform
    import datetime


    # コンピュータ名を取得
    print('hostname:{}'.format(socket.gethostname()))
    # pythonや各ライブラリのバージョンを確認
    print('python:{}'.format(platform.python_version()))
    # 実行日時を取得
    print('current time:{}'.format(datetime.datetime.now()))

    print('library version:')

    libdict = {}
    # numpy
    try:
        import numpy as np
        libdict['numpy'] = np.__version__
    except ModuleNotFoundError:
        pass

    # pandas
    try:
        import pandas as pd
        libdict['pandas'] = pd.__version__
    except ModuleNotFoundError:
        pass

    # matplotlib
    try:
        import matplotlib
        libdict['matplotlib'] = matplotlib.__version__
    except ModuleNotFoundError:
        pass

    # seaborn
    try:
        import seaborn as sns
        libdict['seaborn'] = sns.__version__
    except ModuleNotFoundError:
        pass

    # scipy
    try:
        import scipy
        libdict['scipy'] = scipy.__version__
    except ModuleNotFoundError:
        pass

    # sklearn
    try:
        import sklearn
        libdict['sklearn'] = sklearn.__version__
    except ModuleNotFoundError:
        pass

    # pytorch
    try:
        import torch
        libdict['torch'] = torch.__version__
        libdict['torch-cuda'] = torch.cuda_version
        libdict['torch-cuda is available'] = torch.cuda.is_available()
    except ModuleNotFoundError:
        pass
    except OSError:
        pass

    # plotly
    try:
        import plotly
        libdict['plotly'] = plotly.__version__
    except ModuleNotFoundError:
        pass

    # rdkit
    try:
        import rdkit
        libdict['rdkit'] = rdkit.__version__
    except ModuleNotFoundError:
        pass

    for name, value in libdict.items():
        print('\t{}:{}'.format(name, value))

    #

