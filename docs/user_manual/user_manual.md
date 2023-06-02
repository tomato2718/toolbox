# toolbox
## 概要
- 此文件介紹此工具包的使用方法。

## 環境需求
### 系統
- `python >= 3.10`

### Python 套件
- `pyyaml >= 6.0`

## 使用方式
### 啟動
- 導入 package 後即可使用
```py
from toolbox import LogTool
from toolbox import Global
from toolbox import Handle
from toolbox import Style
from toolbox import metaclasses
from toolbox import utils
```

## 各模組的介紹
### LogTool
#### 說明
logging 快速設定工具。

- `set_logger()`：由 yaml 檔設定 logger
- `get_logger()`：取得指定 logger
    - `logging.getLogger()` wrapper 方法
- `colorful_logger()`：依照傳入參數設定 logger 顏色

#### 範例
- 使用範例
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
- 設定檔範例
```yml
version: 1

formatters:
  standard:
    class: logging.Formatter
    format: '[%(levelname)-5s %(asctime)s] : %(message)s'
    datefmt: '%Y-%m-%d %H:%M:%S'

handlers:
  console:
    class: logging.StreamHandler
    formatter: standard
    level: DEBUG
    stream: ext://sys.stdout
  errlog:
    class: logging.handlers.RotatingFileHandler
    formatter: standard
    level: ERROR
    filename: log/error.log
    mode: a
    encoding: utf-8

loggers:
  __main__:
    level: INFO
    handlers:
      - console
      - errlog
```

### Global
#### 說明
> **注意:** 不建議在正式環境使用，僅供開發測試用。

指派全域變數工具，在需要的模組 import 此類別即可取得。
- `set_global()`：指派全域變數
- `get_global()`：取得全域變數

#### 範例
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
#### 說明
> **注意:** 目前不支援 coroutine 方法。

例外處理工具，簡化 try...except 為裝飾器。

- `Log()`：遇到例外時進行記錄
- `Return()`：遇到例外時回傳
- `Raise()`：遇到例外時丟出
- `Ignore()`：遇到例外時忽略

#### 範例
```py
from lib.toolbox import Handle

# 直接裝飾於函式上即可進行例外處理
@Handle.Log(ZeroDivisionError, logger = __name__)
def foo():
    2/0
```

### Style
#### 說明
stdout 格式工具，使用 SGR。

- `RESET_ALL`：重置所有格式
- `RESET_FG`：重置前景 (文字) 顏色
- `RESET_BG`：重置背景顏色
- `Style()`：產生複雜格式 (同時包含字形、文字、背景)
- `Font`：取得字型
- `FG`：取得前景 (文字) 顏色
- `BG`：取得背景顏色

#### 範例
```py
from lib.toolbox import Style

# 於字串前後加入即可
print(Style.FG.RED + 'tomato' + Style.RESET_ALL)
```

### metaclasses
#### 說明
> **注意:** 此方法可能影響類別下所有成員。

一些常用的 metaclass

- `PathMeta`：該類別底下的路徑會被轉換為絕對路徑

#### 範例
```py
from lib.toolbox.metaclasses import PathMeta

# 使用 metaclass 方式繼承
class Path(metaclass = PathMeta):
    TEST = 'conf/something.conf'

# 會被轉換為絕對路徑
print(Path.TEST) 
```

### utils
#### 說明
一些常用但未歸類的小工具。
- `ReadFile()`：讀取檔案
- `get_abs_path()`：取得絕對路徑
- `parse_unknown_args()`：用以解析 `ArgumentParser.parse_known_args()` 回傳的未知參數

#### 範例
```py
from lib.toolbox.utils import (ReadFile,
                               get_abs_path,
                               parse_unknown_args)

# 取得該路徑的絕對路徑
path = get_abs_path('foo/bar/file.yml')
# 讀取 yml 檔
data = ReadFile.yml(path)
# 解析參數為字典
args = ["test",
        "--foo",
        "bar",
        "-buz",
        "1",
        "2",
        "3",
        "--sys",
        "xyz"
        ]
args = parse_unknown_args(args)
```