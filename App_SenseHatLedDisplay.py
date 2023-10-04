from SenseHatLedDisplay import Class_SenseHatLedDisplay as SHLD

if __name__ == "__main__":
    display = SHLD.LedDisplay(dyn=True, alias=2, duration=10, low_light=False)
    display.run()
