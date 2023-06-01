# toolbox
## Summary
> **重要:** 有點久沒整理內容了，近期會重新整理相關文件

- 提供專案常用工具
- 目前僅於 python 3.10.5 測試
- 功能持續更新，若有其他想法歡迎提出

## Setup
- 直接加入專案後即可調用
- 各層級工具皆會提供說明文件
- 以使用有文件的功能為主
- 有前置底線 _ 檔案或類別為原始檔案，盡量避免調用

## Usage

### LogTool
logging 快速設定工具
- set_logger()：由 yaml 檔設定 logger
- get_logger()：取得指定 logger
    - 與 logging.getLogger() 相同
- colorful_logger()：依照傳入參數設定 logger 顏色

```py
from lib.toolbox import LogTool
from lib.toolbox import Style

# logger 的顏色建議以 dict 方式設定並傳入
# 使用 SGR 參數設定，詳細參考 Style
LOGGER_COLOR = {'debug': Style.FG.BLUE,
                'info':'',
                'warning': Style.FG.YELLOW,
                'error': Style.FG.RED,
                'critical': Style(['BOLD'], 'RED'),
                }

# 設定 logger
LogTool.set_logger('path/to/logger.yml')
# 設定 logger 顏色
LogTool.colorful_logger(__name__, **LOGGER_COLOR)
# 取得 logger
logger = LogTool.get_logger(__name__)
```

### Global
指派全域變數工具，在需要的模組 import 此類別即可取得
- set_global()：指派全域變數
- get_global()：取得全域變數

```py
from lib.toolbox import Global

# 兩種方法皆可指派
Global.set_global('apple', 20)
Global.banana = 30

# 兩種方法皆可取得
Global.get_global('apple')
Global.banana
```

### Handle
例外處理工具，簡化 try...except 為裝飾器
- Log()：遇到例外時進行記錄
- Return()：遇到例外時回傳
- Raise()：遇到例外時丟出
- Ignore()：遇到例外時忽略
```py
from lib.toolbox import Handle

# 直接裝飾於函式上即可進行例外處理
@Handle.Log(ZeroDivisionError, logger = __name__)
def foo():
    2/0
```

### Style
stdout 格式工具，使用 SGR
- RESET_ALL：重置所有格式
- RESET_FG：重置前景 (文字) 顏色
- RESET_BG：重置背景顏色
- Style()：產生複雜格式 (同時包含字形、文字、背景)
- Font：取得字型
- FG：取得前景 (文字) 顏色
- BG：取得背景顏色

```py
from lib.toolbox import Style

# 於字串前後加入即可
print(Style.FG.RED + 'tomato' + Style.RESET_ALL)
```

### metaclasses
一些常用的 metaclass
**注意**：此方法可能影響類別下所有成員
- PathMeta：該類別底下的路徑會被轉換為絕對路徑

```py
from lib.toolbox.metaclasses import PathMeta

# 使用 metaclass 方式繼承
class Path(metaclass = PathMeta):
    TEST = 'conf/something.conf'

# 會被轉換為絕對路徑
print(Path.TEST) 
```

### utils
一些常用的小工具
- ReadFile()：讀取檔案
- get_abs_path()：取得絕對路徑
```py
from lib.toolbox.utils import ReadFile, get_abs_path

path = get_abs_path('foo/bar/file.yml')
data = ReadFile.yml(path)
```


## Project structure
```sh
toolbox
├── __about__.py
├── __init__.py
├── _global.py
├── _handle
│   ├── __init__.py
│   └── _exception_handler.py
├── _logtool
│   ├── __init__.py
│   ├── _formatter.py
│   ├── _logging.py
│   └── _utils.py
├── _style
│   ├── __init__.py
│   └── _style.py
├── metaclass
│   ├── __init__.py
│   └── _meta.py
└── utils
    ├── __init__.py
    ├── _path_helper.py
    └── _reader.py
```