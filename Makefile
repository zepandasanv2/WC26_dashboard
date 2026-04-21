DATA_DIR=data/raw
WC_URL=https://raw.githubusercontent.com/openfootball/worldcup.json/master/2026/worldcup.json
WC_FILE=$(DATA_DIR)/worldcup_2026.json

.PHONY: extract clean

extract:
	mkdir -p $(DATA_DIR)
	curl -f -o $(WC_FILE) $(WC_URL)
	@echo "[INFO] Extraction completed: $(WC_FILE)"

clean:
	rm -rf data/raw/*
	@echo "[INFO] Cleanup done"