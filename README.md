# toolbox
## Summary
- 個人專案常用工具包
- 目前僅於 python 3.10.5 測試
- 功能持續更新，若有想法歡迎提出

## Requirements
### System
- `Python>=3.10`

### Python
- `PyYAML>=6.0`

## Setup
### Installation
- 使用 pip 安裝
```sh
>>> pip install ./toolbox-0.4.5-py3-none-any.whl -t .
```

- 或是直接複製資料夾至目標位置
```sh
>>> cp toolbox /path/to/dest
```

### Configuration
- 無需進行設定


## Usage
- 導入 package 後即可使用
```py
from toolbox import LogTool
from toolbox import Global
from toolbox import Handle
from toolbox import Style
from toolbox import metaclasses
from toolbox import utils
```

## Run the tests
- 直接執行專案內 tests package 即可。
```sh
>>> python -m tests
```

## Known Bugs
- Handle 類無法處理非同步函式

## Support
### Author
- `yveschen2718@gmail.com`

### Maintainer
- `yveschen2718@gmail.com`