from smbus import SMBus
import time

def MPL3115_setup():
    # Special Chars
    deg = u'\N{DEGREE SIGN}'

    # I2C Constants
    global ADDR
    ADDR = 0x60
    CTRL_REG1 = 0x26
    PT_DATA_CFG = 0x13
    global bus
    bus = SMBus(1)

    who_am_i = bus.read_byte_data(ADDR, 0x0C)
    #print hex(who_am_i)
    if who_am_i != 0xc4:
        print "Device not active."
        exit(1)

    # Set oversample rate to 128
    setting = bus.read_byte_data(ADDR, CTRL_REG1)
    newSetting = setting | 0x38
    bus.write_byte_data(ADDR, CTRL_REG1, newSetting)

    # Enable event flags
    bus.write_byte_data(ADDR, PT_DATA_CFG, 0x07)

    # Toggel One Shot
    setting = bus.read_byte_data(ADDR, CTRL_REG1)
    if (setting & 0x02) == 0:
        bus.write_byte_data(ADDR, CTRL_REG1, (setting | 0x02))
    return

def MPL3115_read_temp():
    # Read sensor data

    t_data = bus.read_i2c_block_data(ADDR,0x04,2)

    t_msb = t_data[0]
    t_lsb = t_data[1]

    celsius = t_msb + (t_lsb >> 4)/16.0
   
    return celsius

def MPL3115_read_pressure():
    # Read sensor data

    status = bus.read_byte_data(ADDR,0x00)

    p_data = bus.read_i2c_block_data(ADDR,0x01,3)

    p_msb = p_data[0]
    p_csb = p_data[1]
    p_lsb = p_data[2]

    pressure = (p_msb << 10) | (p_csb << 2) | (p_lsb >> 6)
    p_decimal = ((p_lsb & 0x30) >> 4)/4.0

    return pressure + p_decimal
   


