DATA_DIR=data/raw
ARCHIVE_DIR=data/archive

TODAY=$(shell date +%Y%m%d)
WC_URL=https://raw.githubusercontent.com/openfootball/worldcup.json/master/2026/worldcup.json
WC_FILE=$(DATA_DIR)/baseWC_$(TODAY).json

.PHONY: extract clean pipeline transform clean-all

extract:
	@echo "[INFO] Starting data extraction..."
	@mkdir -p $(DATA_DIR)
	@mkdir -p $(ARCHIVE_DIR)

	@echo "[INFO] Archiving old files..."
	@for f in $(DATA_DIR)/baseWC_*.json; do \
		if [ -f "$$f" ]; then \
			case "$$f" in \
				*$(TODAY)*) ;; \
				*) mv "$$f" $(ARCHIVE_DIR)/ ;; \
			esac \
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


transform:
	@echo "[INFO] Transforming data..."
	@python scripts/transform.py || (echo "[ERROR] Transformation failed" && exit 1)
	@echo "[SUCCESS] Transformation completed"

pipeline: extract transform
	@echo "[DONE] Full pipeline executed"

clean:
	@echo "[INFO] Cleaning processed data..."
	@rm -rf data/processed/*
	@echo "[CLEAN] Processed data removed"

clean-all:
	@echo "[WARNING] Removing ALL data (raw + processed)..."
	@rm -rf data/raw/*
	@rm -rf data/processed/*
	@rm -rf data/archive/*
	@echo "[CLEAN] All data removed"
