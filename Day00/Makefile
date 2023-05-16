FILES :=  ./ex0*/*.py





all: $(FILES) 
	@echo "processeing ex07"
	@make -C ./ex07
	@echo "processeing ex06"
	@make -C ./ex06

$(FILES):
	@echo "processeing $@"
	@python3 $@
	@echo "--------------"


.PHONY: all $(FILES)

