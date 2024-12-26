PICO_DEVICE=/mnt/picow
BINARY_PATH=./build/main.uf2

flash:
	cp $(BINARY_PATH) $(PICO_DEVICE)
