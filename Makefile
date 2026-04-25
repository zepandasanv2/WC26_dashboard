DATA_DIR=data/raw
ARCHIVE_DIR=data/archive

TODAY=$(shell date +%Y%m%d)
WC_URL=https://raw.githubusercontent.com/openfootball/worldcup.json/master/2026/worldcup.json
WC_FILE=$(DATA_DIR)/baseWC_$(TODAY).json

.PHONY: extract clean

extract:
	@echo "[INFO] Starting data extraction..."
	@mkdir -p $(DATA_DIR)
	@mkdir -p $(ARCHIVE_DIR)

	@echo "[INFO] Archiving old files..."
	@for f in $(DATA_DIR)/baseWC_*.json; do \
		if [ -f "$$f" ] && [[ "$$f" != *$(TODAY)* ]]; then \
			mv "$$f" $(ARCHIVE_DIR)/; \
		fi; \
	done

	@echo "[INFO] Downloading data..."
	@curl -f -s -S -o $(WC_FILE) $(WC_URL) || (echo "[ERROR] Download failed" && exit 1)

	@if [ ! -s $(WC_FILE) ]; then \
		echo "[ERROR] File is empty or not created"; \
		exit 1; \
	fi

	@echo "[INFO] Validating JSON..."
	@python -c "import json; json.load(open('$(WC_FILE)'))" \
		|| (echo "[ERROR] Invalid JSON file" && exit 1)

	@echo "[SUCCESS] JSON is valid: $(WC_FILE)"

clean:
	@echo "[INFO] Cleaning raw data..."
	@rm -rf $(DATA_DIR)/*
	@echo "[CLEAN] Raw data removed"