# app実行コマンド設定
APP_CMD := poetry run streamlit run app.py --server.port 8080

# 環境変数 & 実行コマンド設定
# OS: Windows
ifeq ($(OS),Windows_NT)
    OS_TYPE := windows
    ENV_CMD := $$env:PYTHONPATH = '../';
    RUN_CMD := powershell -Command "$(ENV_CMD) $(APP_CMD)"
# OS: UNIX
else
    OS_TYPE := unix
    ENV_CMD := PYTHONPATH="../"
    RUN_CMD := $(ENV_CMD) $(APP_CMD)
endif


run:
	@echo "Running on $(OS_TYPE)"
	@echo "command: [ $(RUN_CMD) ]"
	@$(RUN_CMD)
