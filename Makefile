.PHONY: validate language-analysis-record-validate

validate: language-analysis-record-validate

language-analysis-record-validate:
	python3 tools/validate_language_analysis_record.py
