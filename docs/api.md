# Python 常用工具包 API v1.0.0

## (class) toolbox.LogTool
快速設定 logging.Logger 的類別

### (method) LogTool.set_logger
```py
LogTool.set_logger(path: str) -> None
```
依照設定檔設定 logger，設定檔的編寫格式參考內部 KB
- path <str>：設定檔路徑

### (method) LogTool.get_logger
```py
LogTool.get_logger(target: str) -> logging.Logger
```
與 logging.getLogger 相同

- target <str>：目標 Logger 的名字
- return <logging.Logger>：取得的 Logger，若目標不存在則創建空 Logger

### (method) LogTool.colorful_logger
```py
LogTool.colorful_logger(target: str,
                        debug: str = '', info: str = '',
                        warning: str = '', error: str = '', 
                        critical: str = '', **kwargs) -> None
```
指定 logger 的顏色，是透過在 logger 的 stdout 前方加上 SGR 參數運作，建議配合 Style 使用

- target <str>：目標 Logger 的名字
- debug <str>：debug 層級顏色的 SGR 參數
- info <str>：info 層級的顏色的 SGR 參數
- warning <str>：warning 層級的顏色的 SGR 參數
- error <str>：error 層級的顏色的 SGR 參數
- critical <str>：critical 層級的顏色的 SGR 參數
- **kwarg：其他自訂層級的顏色的 SGR 參數

## (class) toolbox.Style
快速產生 SGR 參數的類別

### (method) Style.\_\_new__
```py
Style(font: list = [], fg: str = None, bg: str = None) -> str
```
重寫 `__new__` 方法，Style 類別無法被實體化，取而代之的是會回傳複雜格式的 SGR。
允許的字串參考類別內成員名稱 (BOLD, RED 等)

- font <list>：字體的名字，以 list<str> 方式填寫
- fg <str>：文字前景色
- bg <str>：文字背景色
- return <str>：產生的 SGR

### (constant) Style.RESET_ALL
常數，重置所有格式

### (constant) Style.RESET_FG
常數，重置前景格式

### (constant) Style.RESET_BG
常數，重置背景格式

### (class) Style.Font
儲存字體的類別，重寫了 `__getattribute__` 方法，取得成員時會以 `\033[<編號>m` 格式回傳

- (constant) Font.BOLD：粗體
- (constant) Font.DIM：暗色
- (constant) Font.ITALIC：斜體
- (constant) Font.UNDERLINE：底線
- (constant) Font.STRIKE：刪除線
- (constant) Font.NORMAL：正常
- (constant) Font.DOUBLE_UNDERLINE：雙底線

### (class) Style.FG
儲存前景色的類別，重寫了 `__getattribute__` 方法，取得成員時會以 `\033[<編號>m` 格式回傳

- (constant) Font.BLACK：黑色
- (constant) Font.RED：紅色
- (constant) Font.GREEN：綠色
- (constant) Font.YELLOW：黃色
- (constant) Font.BLUE：藍色
- (constant) Font.MAGENTA：洋紅色
- (constant) Font.CYAN：青色
- (constant) Font.WHITE：白色
- (constant) Font.BRIGHT_BLACK：亮黑色
- (constant) Font.BRIGHT_RED：亮紅色
- (constant) Font.BRIGHT_GREEN：亮綠色
- (constant) Font.BRIGHT_YELLOW：亮黃色
- (constant) Font.BRIGHT_BLUE：亮藍色
- (constant) Font.BRIGHT_MAGENTA：亮洋紅色
- (constant) Font.BRIGHT_CYAN：亮青色
- (constant) Font.BRIGHT_WHITE：亮白色

### (class) Style.BG
儲存背景色的類別，重寫了 `__getattribute__` 方法，取得成員時會以 `\033[<編號>m` 格式回傳

- (constant) Font.BLACK：黑色
- (constant) Font.RED：紅色
- (constant) Font.GREEN：綠色
- (constant) Font.YELLOW：黃色
- (constant) Font.BLUE：藍色
- (constant) Font.MAGENTA：洋紅色
- (constant) Font.CYAN：青色
- (constant) Font.WHITE：白色
- (constant) Font.BRIGHT_BLACK：亮黑色
- (constant) Font.BRIGHT_RED：亮紅色
- (constant) Font.BRIGHT_GREEN：亮綠色
- (constant) Font.BRIGHT_YELLOW：亮黃色
- (constant) Font.BRIGHT_BLUE：亮藍色
- (constant) Font.BRIGHT_MAGENTA：亮洋紅色
- (constant) Font.BRIGHT_CYAN：亮青色
- (constant) Font.BRIGHT_WHITE：亮白色

## (class) toolbox.Global
註冊全域變數的類別，單純將參數加入 Global 的成員中

### (method) Global.set_global
```py
Global.set_global(container: str, content: Any) → None
```
註冊成員至 Global，也可以透過 `Global.foo = bar` 的方式註冊

- container <str>：成員名稱
- content <Any>：成員之值

### (method) Global.get_global
```py
get_global(container: str) -> Any:
```
取得 Global 成員，也可以透過 Global.foo 的方式取得

- container <str>：成員名稱
- return <Any>：取得成員之值

## (class) toolbox.Handle
簡易例外處理類別，改寫了 `__call__` 方法，以裝飾器 `@` 的方式使用

### (class) Handle.Log
```py
Handle.Log(exceptions: tuple = Exception, logger: str = '') ->None
```
遇到指定例外時，由 logger 輸出

- exceptions <Exception | tuple>：目標偵測的例外，預設為偵測 Exception
- logger <str>：用來輸出的 logger 名稱，會以 error 層級輸出

### (class) Handle.Raise
```py
Handle.Raise(exceptions: tuple = Exception,
             raise_: Exception = None,
             trace: bool = False) -> None
```
遇到指定例外時，由 raise 往外層拋出

- exceptions <Exception | tuple>：目標偵測的例外，預設為偵測 Exception
- raise_ <Exception>：要拋出的例外，預設為拋出當前例外
- trace <bool>：是否要追蹤原始例外，預設為 False

### (class) Handle.Return
```py
Handle.Return(exceptions: tuple = Exception,
              return_: Any = None) -> Any
```
遇到指定例外時，回傳指定內容

- exceptions <Exception | tuple>：目標偵測的例外，預設為偵測 Exception
- return_ <Any>：要回傳的內容
- return <Any>：return_ 指定的內容

### (class) Handle.Ignore
```py
Handle.Ignore(exceptions: tuple = Exception) -> None
```
遇到指定例外時，直接忽略

- exceptions <Exception | tuple>：目標偵測的例外，預設為偵測 Exception

## (package) toolbox.metaclasses
提供簡易 metaclasses 類別，此方法可能影響類別下所有成員

### (class) metaclasses.PathMeta
建立路徑類別的元類別，改寫 `__getattribute__` 方法，回傳成員時會將相對路徑轉為絕對路徑

## (package) toolbox.utils
提供簡易工具類別

### (class) utils.ReadFile
讀取檔案工具
#### (method) ReadFile.yml
```py
ReadFile.yml(path: str) -> Any
```
讀取 yaml 檔案

- path <str>：檔案路徑
- return <dict | list>：yaml 讀取結果

### (function) utils.get_abs_path
```py
utils.get_abs_path(path: str) -> str
```
將相對路徑轉換為絕對路徑

- path <str>：相對路徑
- return <str>：轉換後絕對路徑