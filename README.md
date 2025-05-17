# Smart-Home-Assistant
![GitHub License](https://img.shields.io/github/license/ZhuchenZhong/Smart-Home-Assistant)![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2FZhuchenZhong%2FSmart-Home-Assistant%2Frefs%2Fheads%2Fmain%2Fpyproject.toml)



## Run

```bash
$ cd Smart-Home-Assistant/
$ pdm init
$ pdm install

; Start Backend
$ pdm run uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

> In cases where PDM is not used (e.g., with conda, pipx, or venv), all dependencies have been specified in the `requirements.txt` file.

