from SenseHatLedDisplay import Class_SenseHatLedDisplay as SHLD

if __name__ == "__main__":
    display = SHLD.LedDisplay(dyn=False, alias=4, duration=10, low_light=False)
    display.run()
