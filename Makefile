DATA_DIR=data/raw
WC_URL=https://raw.githubusercontent.com/openfootball/worldcup.json/master/2026/worldcup.json
WC_FILE=$(DATA_DIR)/baseLvl1.json

.PHONY: extract clean

extract:
	@echo "[INFO] Starting data extraction..."
	@mkdir -p $(DATA_DIR)

	@echo "[INFO] Downloading data..."
	@curl -f -s -S -o $(WC_FILE) $(WC_URL) || (echo "[ERROR] Download failed" && exit 1)

	@if [ ! -s $(WC_FILE) ]; then \
		echo "[ERROR] File is empty or not created"; \
		exit 1; \
	fi

	@echo "[INFO] Validating JSON..."
	@python -c "import json,sys; json.load(open('$(WC_FILE)'))" \
		|| (echo "[ERROR] Invalid JSON file" && exit 1)

	@echo "[SUCCESS] JSON is valid: $(WC_FILE)"

clean:
	@echo "[INFO] Cleaning raw data..."
	@rm -rf $(DATA_DIR)/*
	@echo "[CLEAN] Raw data removed"